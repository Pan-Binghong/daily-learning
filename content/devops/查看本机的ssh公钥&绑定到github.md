---
title: 查看本机的SSH公钥&绑定到Github
date: '2026-02-03T02:14:00.000Z'
lastmod: '2026-02-03T03:32:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 配置Git使用SSH方式, 本文环境：windows + powershell + git guissh 

---

## 查看

```json
ls  ~/.ssh
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUUWRQZG%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDJ%2FdXtsDZUUylg6NgJdsdF%2FxacXhKny7%2FKEU8csrN99wIgVf02BAaVSSvHmo%2FlHiwYNA7du0NF70QCy%2BCTLEQH7DEqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJSehMhLBemGG%2FvbLircA66vobPuvXmnzLQQ3IjAJ18GirNaCG3R%2Bn1lrCZr4reTWQiQ924uEYjTZJTqjKZGz8Zp1Xlr5jSZxvT7hdslS4xzJ5yjpDedj5ojJLBvaZNIIcvRVU3V%2FI6p4Mu5upMxuJUNGByW8J0YXPgwpYuWLej3cTb3mzTowXICkZ2E7eV2QGEmc62OMpWSXQmUkc1XjKvmG0frR8c0vDfvdKSQzL5TU4J6Qy%2FkTFbYXiWeG64Xa8MUyrWJnnAGKlbugH14lo2uFDenvgGTFSLGIV3YlD3vCrEe32aHx3gX7Dymu605RDmPZU3nN%2FTMQl84Rzh0GXF4VPCAX33l8ZVLxVOUjzQjgJubxP%2Fv2gVlEoktwVM88521W4y46z4LnjfhERwV%2Fb4VU0fD%2FE%2BdvChlYmgUejULrfiFacI95ZbYmdnVZcOzhA6sd6X3MuhfxIgJ98w6aUwzCIyIgV651JZJiTe94uWS3GL0zww1k0D7dnXF3fASdJ29qwNxP%2Fdb8BxwIIVlixvwC4F3KCmAc%2BQFmdJYuHARSrv95QO1eEAcR22autxBUUzncW77OXtF62RYzz6tGoAxStDDpRXE9hRt3nMlS9oO3AY8XGqRxBrNvElJljtgInv29bhP%2B6lVQvsoMP%2FuwM8GOqUBEKNARFrP76cVCz7uKoqbP2C1LuZBIE%2BuevM9mCpRItxUcumxGzfQCSIrfrvPJi56D28HzAGhXE2asqoe7DuPk28zQWINOdanIA0kNe3Yv8SEAwuUMHzFquSBFkPdPmP0bwGTP7l9gt365zyNDmHAzmlaHS0xhTL3jSpYBNyPKh8O%2FWBEYp%2FRwfUE3JufEJx%2Bcy5sWnMEP3R%2FniDlqAIRm2fRqMFK&X-Amz-Signature=fafc5bb348eb476ab694b94b42789ad2d8cf3604069791976dba6f15fff7e8d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 创建

```json
# 推荐使用Ed25519算法
ssh-keygen -t ed25519 -C "your_email@example.com"

# 备选
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

---

## 配置

```json
# 将ssh密钥添加到ssh-agent
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add .\.ssh\id_ed25519

# 查看是否添加成功
ssh-add -l
```

### 安装gh（github cli）

```json
# 打开powershell
choco install gh

# 登录
gh auth login
```

## 打开GIT/提交

```json
gh ssh-key add ~/.ssh/id_ed25519.pub --title "公司主机"
```

## 验证

```json
ssh -T git@github.com
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUUWRQZG%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDJ%2FdXtsDZUUylg6NgJdsdF%2FxacXhKny7%2FKEU8csrN99wIgVf02BAaVSSvHmo%2FlHiwYNA7du0NF70QCy%2BCTLEQH7DEqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJSehMhLBemGG%2FvbLircA66vobPuvXmnzLQQ3IjAJ18GirNaCG3R%2Bn1lrCZr4reTWQiQ924uEYjTZJTqjKZGz8Zp1Xlr5jSZxvT7hdslS4xzJ5yjpDedj5ojJLBvaZNIIcvRVU3V%2FI6p4Mu5upMxuJUNGByW8J0YXPgwpYuWLej3cTb3mzTowXICkZ2E7eV2QGEmc62OMpWSXQmUkc1XjKvmG0frR8c0vDfvdKSQzL5TU4J6Qy%2FkTFbYXiWeG64Xa8MUyrWJnnAGKlbugH14lo2uFDenvgGTFSLGIV3YlD3vCrEe32aHx3gX7Dymu605RDmPZU3nN%2FTMQl84Rzh0GXF4VPCAX33l8ZVLxVOUjzQjgJubxP%2Fv2gVlEoktwVM88521W4y46z4LnjfhERwV%2Fb4VU0fD%2FE%2BdvChlYmgUejULrfiFacI95ZbYmdnVZcOzhA6sd6X3MuhfxIgJ98w6aUwzCIyIgV651JZJiTe94uWS3GL0zww1k0D7dnXF3fASdJ29qwNxP%2Fdb8BxwIIVlixvwC4F3KCmAc%2BQFmdJYuHARSrv95QO1eEAcR22autxBUUzncW77OXtF62RYzz6tGoAxStDDpRXE9hRt3nMlS9oO3AY8XGqRxBrNvElJljtgInv29bhP%2B6lVQvsoMP%2FuwM8GOqUBEKNARFrP76cVCz7uKoqbP2C1LuZBIE%2BuevM9mCpRItxUcumxGzfQCSIrfrvPJi56D28HzAGhXE2asqoe7DuPk28zQWINOdanIA0kNe3Yv8SEAwuUMHzFquSBFkPdPmP0bwGTP7l9gt365zyNDmHAzmlaHS0xhTL3jSpYBNyPKh8O%2FWBEYp%2FRwfUE3JufEJx%2Bcy5sWnMEP3R%2FniDlqAIRm2fRqMFK&X-Amz-Signature=391e195d96a6a85a9521c444e23355a5200b02f5ad4ba7d2b11164621e8afed6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


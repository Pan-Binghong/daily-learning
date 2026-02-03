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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VINJFRE%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDJe8tqMVP0S8NaMg%2F7I4X41ASF6xVK5Tx33OayfLTQdgIgNcEeQQH40V7IHV7ZF178QrQ88BAA3WMXADTXvsOhM4gqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8PEyb3%2FokUpq9q1ircAzElPxF26WK6TZociKvgLrcQ2KFEqr%2F9qKamsRkRURdBnSX46CNv63TBcGZ3wrSViw1eX4AFFa5X0ptbrO%2BflhUkLTsIgFZBkEai2hhNUSwRAHm1GmlhPlY%2FJpiDNcj8tRLElo5kwg546PlROrgkj6tFUAdV%2Biua5%2FLRNlVDWxN12l5jpuR7rG6TEQUYK6ueInzjlPaYiG1onho3mjgnWcGOn%2BRxSqzjyoQnPxxLokyZdPHbxoLLbHfLkE1uMuyMEWmIovGNf61uOJdGJD%2BFWsyfiJgsKikQkQqX0aX9oDCE02fohFn9DvrjscvTk%2F2vYdAjANQMmemC%2FiUepCxKJfIQaQf3uCh8yemMUkT7rwx1r8ZniQg1S%2BPmrP671zsCkyMk3bRa%2Fr8KEZEbumalmbaBznRo3KoVOrSA3knRrZ45LDjVnoJe5cJ%2BqLnKPvPB%2BKFTP5Z1uEqloBEL8Dz5k7lqtoFpQQelM5Q3jQmzFQkbesAekk%2BwxYTUMf2y3RUgbrusb6z%2FfDdUSjeAL5xNKR5pdXc05ivoufjzhqPeHs40vazXNGcQgcOuh6PKq%2FxDHXl%2FsmDlrH9P2iZkKmaLuONMXh9WgU6pxSpOikRFijwrZbVoZz8yZmmDFiQTMLvYhcwGOqUBJtlBIzRWRlmP0NvoxD6rZ6TfKO2bhPk2oCR5VCgwDBXfhpOcjfzWi7EB1CrYU1a%2BayQz17jrCTFGoD9yM686hvzlbKMNR9BYSfWZ6Jnp8mKHxgxfnRwY1pi5yfjU%2BpT%2FxvNnx08FM%2BgO9FCsXKDnQTlegIqkcP1nzpf9rROrC%2BhVDcq%2FWrvdXFwbfbKeDDqEC%2F%2BjhoCt1CQOq%2BZjoJZNE6utw1YJ&X-Amz-Signature=054545f8bf19900850028fcf5b59ec6379ab95958822631b735d115a990a0ca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VINJFRE%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDJe8tqMVP0S8NaMg%2F7I4X41ASF6xVK5Tx33OayfLTQdgIgNcEeQQH40V7IHV7ZF178QrQ88BAA3WMXADTXvsOhM4gqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8PEyb3%2FokUpq9q1ircAzElPxF26WK6TZociKvgLrcQ2KFEqr%2F9qKamsRkRURdBnSX46CNv63TBcGZ3wrSViw1eX4AFFa5X0ptbrO%2BflhUkLTsIgFZBkEai2hhNUSwRAHm1GmlhPlY%2FJpiDNcj8tRLElo5kwg546PlROrgkj6tFUAdV%2Biua5%2FLRNlVDWxN12l5jpuR7rG6TEQUYK6ueInzjlPaYiG1onho3mjgnWcGOn%2BRxSqzjyoQnPxxLokyZdPHbxoLLbHfLkE1uMuyMEWmIovGNf61uOJdGJD%2BFWsyfiJgsKikQkQqX0aX9oDCE02fohFn9DvrjscvTk%2F2vYdAjANQMmemC%2FiUepCxKJfIQaQf3uCh8yemMUkT7rwx1r8ZniQg1S%2BPmrP671zsCkyMk3bRa%2Fr8KEZEbumalmbaBznRo3KoVOrSA3knRrZ45LDjVnoJe5cJ%2BqLnKPvPB%2BKFTP5Z1uEqloBEL8Dz5k7lqtoFpQQelM5Q3jQmzFQkbesAekk%2BwxYTUMf2y3RUgbrusb6z%2FfDdUSjeAL5xNKR5pdXc05ivoufjzhqPeHs40vazXNGcQgcOuh6PKq%2FxDHXl%2FsmDlrH9P2iZkKmaLuONMXh9WgU6pxSpOikRFijwrZbVoZz8yZmmDFiQTMLvYhcwGOqUBJtlBIzRWRlmP0NvoxD6rZ6TfKO2bhPk2oCR5VCgwDBXfhpOcjfzWi7EB1CrYU1a%2BayQz17jrCTFGoD9yM686hvzlbKMNR9BYSfWZ6Jnp8mKHxgxfnRwY1pi5yfjU%2BpT%2FxvNnx08FM%2BgO9FCsXKDnQTlegIqkcP1nzpf9rROrC%2BhVDcq%2FWrvdXFwbfbKeDDqEC%2F%2BjhoCt1CQOq%2BZjoJZNE6utw1YJ&X-Amz-Signature=2928f10dcbcf4681ac74dbdf5ca7a3543d0ff2c9920683d5ec61dd5903292678&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


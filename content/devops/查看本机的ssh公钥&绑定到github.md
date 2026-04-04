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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OTZLAK5%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICulk9hKYQbibL1meKNCpHtNpp6dJuJ733Oi8m7EbopCAiEAzRui2CNSUIpjPWdPDbyePxxX6Woz92iz6KeN4oPid%2BkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF53qBnpbw%2FG2M6jyrcA4tceOF5m4EuOpuAB4VYV8d%2FHhsc9UuM%2FVH%2Fw8xiCuMVax4jzKB9arM45yowW6BrUzNeqNO0k0%2Bsl%2BWVT5gf%2Bsq2cLzAs5I15%2F0SDh%2FmEgHpOC4MwJx1Amn3xbFXPelhFgI9ZhKKThGGsGIXsHu3P29u2io0yMbOu9US%2FvFB8cWrO1NC5v4CO0Q%2Frv1YfehCxR53mrNRQWCWkAy0bWw4dFmpiYgIauoqrPTqh3wwNud64EDSFGD0hznKukRtsWCoKB%2FcADzAWfXwsQI37lWu1mo3QQlWoCAXAn5kKdS2oYTvJ8pEbuJFZUyjja8zrMIz3QlnOrv0uXYYF5cQ2X0GBbi512SAaBd3n65RNt1LBexFjxdLPKHn551fgdh0%2BqH%2B8qJGXzWgE1OwscCyvpTyJnPTRS6Fv7z3GIZIquWfqc9s0b6Vq2RlkRV3B4CLI8L1d24znzanxAGblZCqRCBXpThDgOa8yZ9Adll%2BBkZDvo%2BkDb8%2FWOh11TUAG0wQg2EfJbNgK6Sk7Kl5IRYYTLHFI%2FYtwkCIYTgke9ZAEqNuZiURPMbKXvmQVyGgFqg4sluwfvjkLBtdBx6E7M441X9vuwmJE%2BXQodYQBf%2BaDLCn9Z71KIYUeOV0XqQjkVB3MKeOws4GOqUBT6uXoBepDwZ1lqNbyP0in%2FyjD8pt6nck0gK5ap2bp5mjIKB81kpKAgs0%2Bd1lsAd6zbOukYxruQep4m%2FS7zQ025lkdSBdDxWEs9L5j1SWqZqsc77dJsn7NICWvvPdBwgE0%2FAr2Rm%2BpBY6ltqIO6RAjJQNCjyB2TvR84sfVeMuhcepSidjiqkx3n3ZPPLebQ5Xoa7yzZQSXZmoYx3ovNveSATFEuhC&X-Amz-Signature=5ee0b122a2d504d2a2b2eadad10f8a7baa594dd7d0c4f7aadd93d5609a6f811e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OTZLAK5%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICulk9hKYQbibL1meKNCpHtNpp6dJuJ733Oi8m7EbopCAiEAzRui2CNSUIpjPWdPDbyePxxX6Woz92iz6KeN4oPid%2BkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF53qBnpbw%2FG2M6jyrcA4tceOF5m4EuOpuAB4VYV8d%2FHhsc9UuM%2FVH%2Fw8xiCuMVax4jzKB9arM45yowW6BrUzNeqNO0k0%2Bsl%2BWVT5gf%2Bsq2cLzAs5I15%2F0SDh%2FmEgHpOC4MwJx1Amn3xbFXPelhFgI9ZhKKThGGsGIXsHu3P29u2io0yMbOu9US%2FvFB8cWrO1NC5v4CO0Q%2Frv1YfehCxR53mrNRQWCWkAy0bWw4dFmpiYgIauoqrPTqh3wwNud64EDSFGD0hznKukRtsWCoKB%2FcADzAWfXwsQI37lWu1mo3QQlWoCAXAn5kKdS2oYTvJ8pEbuJFZUyjja8zrMIz3QlnOrv0uXYYF5cQ2X0GBbi512SAaBd3n65RNt1LBexFjxdLPKHn551fgdh0%2BqH%2B8qJGXzWgE1OwscCyvpTyJnPTRS6Fv7z3GIZIquWfqc9s0b6Vq2RlkRV3B4CLI8L1d24znzanxAGblZCqRCBXpThDgOa8yZ9Adll%2BBkZDvo%2BkDb8%2FWOh11TUAG0wQg2EfJbNgK6Sk7Kl5IRYYTLHFI%2FYtwkCIYTgke9ZAEqNuZiURPMbKXvmQVyGgFqg4sluwfvjkLBtdBx6E7M441X9vuwmJE%2BXQodYQBf%2BaDLCn9Z71KIYUeOV0XqQjkVB3MKeOws4GOqUBT6uXoBepDwZ1lqNbyP0in%2FyjD8pt6nck0gK5ap2bp5mjIKB81kpKAgs0%2Bd1lsAd6zbOukYxruQep4m%2FS7zQ025lkdSBdDxWEs9L5j1SWqZqsc77dJsn7NICWvvPdBwgE0%2FAr2Rm%2BpBY6ltqIO6RAjJQNCjyB2TvR84sfVeMuhcepSidjiqkx3n3ZPPLebQ5Xoa7yzZQSXZmoYx3ovNveSATFEuhC&X-Amz-Signature=8e843e33fa83dd7db0659b78213674886ea64722bad57423db678cbd630b11ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


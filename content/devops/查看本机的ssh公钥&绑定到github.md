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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJWNJETH%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICDtcrNZabidT8AkolMznnKFbr5rrOijMuzmrQIDT%2B3%2FAiEAqnyuORLtDepUDLVZJXEYxm4BfByIgmWoQvcfVwUrY8Aq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAZdEKXRzILQcuwcZircAwhsNEAwQhWatQiPfe%2FNOhIJ4wbTJ71dUV7X0UYxmklOp7Q2FzPb%2FuhUEMO3YqPFg56HGxkMuGfXV6sKhDwpGaZA8rjI3EYYJP%2FtskwGnoWXKjIUjbQOXwGZidHSVeT2UKEuV7Y7LVdwB4GHuLBd%2BJXnq9ZCsQg1ONNVdgRCNUI6aAh%2BC0cBK2G%2FVTD7QzDrU0XrRYJgwxAae4APzOIPdWir%2FowNFMlBzxKVL%2B8uIgSdqqtTRfv0tjqOZ908xIDbxI0Vrif32BgmXl0lshuHWuUcU1G9VU7A8wiBJE16x5%2Bf0vk2q2xnV%2F0RxMaFDO0mgQUBMMT1S1lOdvHqkzX7uveD5gxooYckJ1woSgPfrctG4KR7VOFS1s7hJg%2B5zS%2FomWn3pYL67ewxiIQ2c1WpyB1rL%2Fdrhd3SikIBp9HQls67h%2BILmLHQIH9y3mwyeblvz14Z%2FLhsKKDup5xK9yTcBretRNpFKzQNbtkezlT%2FNPdz%2Bs%2FLJYNA7KQBA6dxDsmdqMbh%2FSrbxgpUOvwAnTPkNadEN9Qqcwp6O77PgPKFzm6mSOipyoxtSDG6Fnx4FjJIm2KRe8bPL%2B%2F0IIZ5FalHT1ycs3XXuVhCyy5dIombSkGmS%2FXeWAyU6uhEi1sHMN2MoMwGOqUBg4RZ4hfaL7HrtK%2B5WfL2k5ikya%2Bg%2BffgdnfdfuzohnieFaPaQgFo94Lxjh1ljlezTba5EnrTJEqwEtc1RS8nyoVu1r%2FsQQNK20QAheg%2FoW0%2BSrdDti1YE29zrFTG43jRPvXv7mpXsxXbwr7VM0YXQoqY0fm5dNaN3xTeTaNJAYjLoo5mMoiAkOKwHB8KsqnhSCsxAm3j%2BOX4jIrap%2B5qilPSdJ5u&X-Amz-Signature=b7a0297f9e62a6fc466f10d2fa3e918f71c333696add065474198955d7b91e8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJWNJETH%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICDtcrNZabidT8AkolMznnKFbr5rrOijMuzmrQIDT%2B3%2FAiEAqnyuORLtDepUDLVZJXEYxm4BfByIgmWoQvcfVwUrY8Aq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAZdEKXRzILQcuwcZircAwhsNEAwQhWatQiPfe%2FNOhIJ4wbTJ71dUV7X0UYxmklOp7Q2FzPb%2FuhUEMO3YqPFg56HGxkMuGfXV6sKhDwpGaZA8rjI3EYYJP%2FtskwGnoWXKjIUjbQOXwGZidHSVeT2UKEuV7Y7LVdwB4GHuLBd%2BJXnq9ZCsQg1ONNVdgRCNUI6aAh%2BC0cBK2G%2FVTD7QzDrU0XrRYJgwxAae4APzOIPdWir%2FowNFMlBzxKVL%2B8uIgSdqqtTRfv0tjqOZ908xIDbxI0Vrif32BgmXl0lshuHWuUcU1G9VU7A8wiBJE16x5%2Bf0vk2q2xnV%2F0RxMaFDO0mgQUBMMT1S1lOdvHqkzX7uveD5gxooYckJ1woSgPfrctG4KR7VOFS1s7hJg%2B5zS%2FomWn3pYL67ewxiIQ2c1WpyB1rL%2Fdrhd3SikIBp9HQls67h%2BILmLHQIH9y3mwyeblvz14Z%2FLhsKKDup5xK9yTcBretRNpFKzQNbtkezlT%2FNPdz%2Bs%2FLJYNA7KQBA6dxDsmdqMbh%2FSrbxgpUOvwAnTPkNadEN9Qqcwp6O77PgPKFzm6mSOipyoxtSDG6Fnx4FjJIm2KRe8bPL%2B%2F0IIZ5FalHT1ycs3XXuVhCyy5dIombSkGmS%2FXeWAyU6uhEi1sHMN2MoMwGOqUBg4RZ4hfaL7HrtK%2B5WfL2k5ikya%2Bg%2BffgdnfdfuzohnieFaPaQgFo94Lxjh1ljlezTba5EnrTJEqwEtc1RS8nyoVu1r%2FsQQNK20QAheg%2FoW0%2BSrdDti1YE29zrFTG43jRPvXv7mpXsxXbwr7VM0YXQoqY0fm5dNaN3xTeTaNJAYjLoo5mMoiAkOKwHB8KsqnhSCsxAm3j%2BOX4jIrap%2B5qilPSdJ5u&X-Amz-Signature=253ff92d63044b0cf6aece6d2b89f07ab6f525658317919845b367350fd4009f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


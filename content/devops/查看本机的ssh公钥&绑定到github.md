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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQCEIE4%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwmQ0oL62EnPx%2FOIrCcrNNHi%2BvtnXOpQDMqPoZfoEhpwIgFxXCLnr21dhOb0vkWY7SAk0HRFRw26sMY4BP1Eu9dBkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP88%2BgHcfq1o%2F8%2BPQCrcA%2F7e%2Fil9XOqqiLPzWqF9FYZkziB31xFXvOQsfngQ1l3VL7u0k7NCcm7AwTPQvorYJlA0X1R1B2y2QRhlTOz8rfwVqLIcxlDpRsHTzDqx2wV4wF3Ze7fZEoEyYYJN%2BIcDEVW%2FYwvzth09sPhBaj7rvBfUPvwikTrPJxGkvvlD8M4OU%2Fes%2B4YyjY%2BJVLmo56ul6XLSmS64wjEvum2QNXmbeCK0Ljk7JyvOD9ZLfj0joXZhzu2TPUJkf8cv%2BWEGxqZXbRCZ8U4GpPvc3GLCh1lDYKccYUCMHEOyVvBov7xbzaJ98BPJpUDAn8v06NUxZf3pyavxmTBOIYuTnpJ5yAkPfsEdiyUFlIgjoN8MEu48tBYJB75SvGp0csIJ1RRABohKuYoZBdm9wswsdzda1b4T9az7ytejGSU4bf1eZzT8Wixm%2BfF6SFCLbqYuQC6pquf5qpOnsK1EreyLSxN4SsgTapdkM8WZY2rM%2BFgOyQ5U%2BNGWsFMM%2BkP%2ByB5LJ0bk0wjT7vbu2OcaDAa2TxJ%2BLrbWnTP9VeZYwxtZ3nZHApHBDvyZTCehgW4BPvq8DmOB82G8CTD5i0yNLgTRjOQhMHKkjXxAXrHzc9TU83VO6%2B8JclRlX5yTV3uP2PyIZMr9MKHxsM8GOqUB1Fd6z%2Bo1Y%2FAmlWEmv7ePMjOTi9a%2FvcaPPnnctc7YywxU2lduI0%2FgRneNtHbJk%2B75K2mdSGuA6KiOWNkDnI3ITKJ92JU9pM6mEe3aQ%2FgWTao3HRx7QKEOpVd4ivqI1DOIX9nf4ifroV3J%2BS82UJdhEhelN2hnvoaqPNLzkL892%2B12t3fY%2BBaXNtxif36lSzpHOKDsoZXvkNYa2IXcjjGAXJpEiu7W&X-Amz-Signature=d46f05789b4d876fd777947f81065dfb9fdf803de3820f6922d841e5136a2fd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQCEIE4%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwmQ0oL62EnPx%2FOIrCcrNNHi%2BvtnXOpQDMqPoZfoEhpwIgFxXCLnr21dhOb0vkWY7SAk0HRFRw26sMY4BP1Eu9dBkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP88%2BgHcfq1o%2F8%2BPQCrcA%2F7e%2Fil9XOqqiLPzWqF9FYZkziB31xFXvOQsfngQ1l3VL7u0k7NCcm7AwTPQvorYJlA0X1R1B2y2QRhlTOz8rfwVqLIcxlDpRsHTzDqx2wV4wF3Ze7fZEoEyYYJN%2BIcDEVW%2FYwvzth09sPhBaj7rvBfUPvwikTrPJxGkvvlD8M4OU%2Fes%2B4YyjY%2BJVLmo56ul6XLSmS64wjEvum2QNXmbeCK0Ljk7JyvOD9ZLfj0joXZhzu2TPUJkf8cv%2BWEGxqZXbRCZ8U4GpPvc3GLCh1lDYKccYUCMHEOyVvBov7xbzaJ98BPJpUDAn8v06NUxZf3pyavxmTBOIYuTnpJ5yAkPfsEdiyUFlIgjoN8MEu48tBYJB75SvGp0csIJ1RRABohKuYoZBdm9wswsdzda1b4T9az7ytejGSU4bf1eZzT8Wixm%2BfF6SFCLbqYuQC6pquf5qpOnsK1EreyLSxN4SsgTapdkM8WZY2rM%2BFgOyQ5U%2BNGWsFMM%2BkP%2ByB5LJ0bk0wjT7vbu2OcaDAa2TxJ%2BLrbWnTP9VeZYwxtZ3nZHApHBDvyZTCehgW4BPvq8DmOB82G8CTD5i0yNLgTRjOQhMHKkjXxAXrHzc9TU83VO6%2B8JclRlX5yTV3uP2PyIZMr9MKHxsM8GOqUB1Fd6z%2Bo1Y%2FAmlWEmv7ePMjOTi9a%2FvcaPPnnctc7YywxU2lduI0%2FgRneNtHbJk%2B75K2mdSGuA6KiOWNkDnI3ITKJ92JU9pM6mEe3aQ%2FgWTao3HRx7QKEOpVd4ivqI1DOIX9nf4ifroV3J%2BS82UJdhEhelN2hnvoaqPNLzkL892%2B12t3fY%2BBaXNtxif36lSzpHOKDsoZXvkNYa2IXcjjGAXJpEiu7W&X-Amz-Signature=8e0a1210437b4e16c428321886424ecaeafb1204c166ca3fa4bdf7009d7991c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


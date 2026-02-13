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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AQRM7PI%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIG341Ub0dytQ%2BmU7oXKZtUV8zcv3xWIMiY%2FWThwAQlOmAiAZB7ylQuKR%2FYWeBd7MMQmA9zEnVZQq4jaY%2Fg1%2BuTeqMiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLeeJnwDLd6ptQczSKtwDi4v7VDFMAXqT6gFPZMFNmpjYm5fEs1XvHc29nKPkxWFVjqRj%2F6viJZ%2Fwy5tPqJMjBGjIiJEj%2Fz9wP8%2BD4cktxZzklWwbgIyRHGIIwIcSMRIKSijlBu1%2FxNHEw54ljLgUbp2QaLAspquhLb%2F9kPbpQlcMNW8Q%2B9xP2WAnp3Bcu2yf9j5ZTp7CEXtM%2Bw1G4T8CZZD%2BJOF4M4TONjRx5uCaniFMxY4RpNMbottmdRwHOhG2FsJ3cnHAtiMT9zkWSNZBdvG8PFfRvFKaVxal8cksbwo%2BOdT6z9XLnwxiLWTQXUnVeMnnwdhc0ywICibi%2FFyd%2FOh0k2STnRUcWk03VdyNI6Jw4Yw7hTgN6xGL8iqAe51%2FDYVmK5u2FUlgN9KRn4P9tbXKcdKYY3vOsA6vfRlwOoQt9nyc%2FYk%2FqApRAWwUWv08pV0FtpZUbj8MjnxfKKeIOlYoYrHHYNwoEuXz7qqbDYw1bpYnFJzrRw4La8KckeCPNiUigM%2Biy%2BWLxxUgMKq8fNxzLuORUMXe48yX1Q5WXucVsFYoBopwSu1%2BMcpV9ZbH7u9yi%2FA%2FoucozrWZMhT4qmhJacYsYRfFLOpgkM4DLV8AGQolnbVRG8LTUadWoqU64Cfq5%2F7HD1l%2FTX0wiLq6zAY6pgFuWimQDLfuNCIq0DQ%2BcdTHHlR75LA6YX9%2FiP2dJ2L3mojbGWJ%2FV8as1Hfmc6AHTvKf%2Be4Bbh8VHrotASToSHxcKydwtuON9P4aVcCfj1OVq8Wb2z%2BFzZlG2AqEPbsqENjSAfsTtetVUPx60POCY7vF8DkutxnynlQtKcEVwZ%2FOXHqJYA7UTqc3sqqAN5PpujoGnu%2B1v9ZvnGIZ%2BOjp3ewD2fwyFADj&X-Amz-Signature=805dfa09d771a5842c579d9c1a5f93cc1c17d6b2bac27870bd6638e2b5894fb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AQRM7PI%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIG341Ub0dytQ%2BmU7oXKZtUV8zcv3xWIMiY%2FWThwAQlOmAiAZB7ylQuKR%2FYWeBd7MMQmA9zEnVZQq4jaY%2Fg1%2BuTeqMiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLeeJnwDLd6ptQczSKtwDi4v7VDFMAXqT6gFPZMFNmpjYm5fEs1XvHc29nKPkxWFVjqRj%2F6viJZ%2Fwy5tPqJMjBGjIiJEj%2Fz9wP8%2BD4cktxZzklWwbgIyRHGIIwIcSMRIKSijlBu1%2FxNHEw54ljLgUbp2QaLAspquhLb%2F9kPbpQlcMNW8Q%2B9xP2WAnp3Bcu2yf9j5ZTp7CEXtM%2Bw1G4T8CZZD%2BJOF4M4TONjRx5uCaniFMxY4RpNMbottmdRwHOhG2FsJ3cnHAtiMT9zkWSNZBdvG8PFfRvFKaVxal8cksbwo%2BOdT6z9XLnwxiLWTQXUnVeMnnwdhc0ywICibi%2FFyd%2FOh0k2STnRUcWk03VdyNI6Jw4Yw7hTgN6xGL8iqAe51%2FDYVmK5u2FUlgN9KRn4P9tbXKcdKYY3vOsA6vfRlwOoQt9nyc%2FYk%2FqApRAWwUWv08pV0FtpZUbj8MjnxfKKeIOlYoYrHHYNwoEuXz7qqbDYw1bpYnFJzrRw4La8KckeCPNiUigM%2Biy%2BWLxxUgMKq8fNxzLuORUMXe48yX1Q5WXucVsFYoBopwSu1%2BMcpV9ZbH7u9yi%2FA%2FoucozrWZMhT4qmhJacYsYRfFLOpgkM4DLV8AGQolnbVRG8LTUadWoqU64Cfq5%2F7HD1l%2FTX0wiLq6zAY6pgFuWimQDLfuNCIq0DQ%2BcdTHHlR75LA6YX9%2FiP2dJ2L3mojbGWJ%2FV8as1Hfmc6AHTvKf%2Be4Bbh8VHrotASToSHxcKydwtuON9P4aVcCfj1OVq8Wb2z%2BFzZlG2AqEPbsqENjSAfsTtetVUPx60POCY7vF8DkutxnynlQtKcEVwZ%2FOXHqJYA7UTqc3sqqAN5PpujoGnu%2B1v9ZvnGIZ%2BOjp3ewD2fwyFADj&X-Amz-Signature=beb46625c3f7cb0641c5d6bf8c29b26afa87af70f4bc1a97f635e92a545b03ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


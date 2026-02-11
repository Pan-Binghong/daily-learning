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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J6XXKJJ%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxI7JwfD%2FPYiZMpv%2Fi9zlOfdWk%2BF9D5zWXi85LvdTTdAIgeBQXO4Ei4dYKi2rrMstNLUZN2jRAdC%2FgaPmzc9kkGc4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDzx7DOE0FhINEf4TircAxOlvQG6ZpFwt9DLfzuXFP9WiIIZ2WWgDUmtaOTDfRsnCD5t5CnG%2FuqncmZmx645aKU8Ajdre39cMVxhaBdi56li1oS2gXcgUcSkYcRbrCsrZvr3lSW6beoxdccNLDgaT5esvscFGXZidG6g%2FoL2qBNo4Y%2BKgf03VixLevNWDqEuH%2FW1wdI9x3yddZ5GE9LMLZhHDdfpUBbe6NOCGTAs1VrHbX1jLxcvmle4ouNMSPdaHuLLJDXeMFGN6FolsltdY3DtAhOwdi6E%2FEPcKy9YN6nM4TIEbGGqIf%2FJQ%2BEEnpDPC3ViP6y9zBNn4%2FHnnDQAbT1nt6nlE0YibwIzhjfj9LpiTQZJhQ%2FqQk2Pt%2BRO3Xo1uHAGoKI9qUNjjpPr%2B0CTSNn3UBsDhN%2BGaG7P4c09byOSH%2By0%2BUYfZKjWDKFFlSaOvUcbG5tvW%2FvsPtpKttCIzeGSarkvEYSBhmNHH4P3qFiKo9wFxt%2FVO1Il174g12sak4iRL59HHJoM3vvSOLdL4oQgnantzLRben0ciFtO4AIkmmengfB0HmCESot%2B56XQCzrc8QAgOJZKLnN7NkKzwKS%2FQok6C8CbBTGRw0zQZ6hMwPGvCnLfKDLyiOiXrTPSeI8TE%2B8oqoHnHHrCMIPLr8wGOqUBQE%2BaYPcP4trLmbPSCrvN2a4sBDrO1%2BI83YUMi6XC4Nkh7i6dtv61RHUWnaXaVySyIT8LA4PPGJhtqULJKVWcvU4OzgGYfovtNVAsSI7aX%2BXdwLhDr8uIFrIWcRJ3pSly8RtxCP%2FOg6yWSWaYW6sgrV0TsNGrDFzpjylKCXU2hgZEAidIKJmUOiTIexdB8s4bOluoTDZ%2BBkbfqmq0N2x10SE0QYKA&X-Amz-Signature=4fd2b00a79b1967cb86ce186a2fba748fc3ff4ab859736d7d01ea62ce2e7f567&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J6XXKJJ%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxI7JwfD%2FPYiZMpv%2Fi9zlOfdWk%2BF9D5zWXi85LvdTTdAIgeBQXO4Ei4dYKi2rrMstNLUZN2jRAdC%2FgaPmzc9kkGc4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDzx7DOE0FhINEf4TircAxOlvQG6ZpFwt9DLfzuXFP9WiIIZ2WWgDUmtaOTDfRsnCD5t5CnG%2FuqncmZmx645aKU8Ajdre39cMVxhaBdi56li1oS2gXcgUcSkYcRbrCsrZvr3lSW6beoxdccNLDgaT5esvscFGXZidG6g%2FoL2qBNo4Y%2BKgf03VixLevNWDqEuH%2FW1wdI9x3yddZ5GE9LMLZhHDdfpUBbe6NOCGTAs1VrHbX1jLxcvmle4ouNMSPdaHuLLJDXeMFGN6FolsltdY3DtAhOwdi6E%2FEPcKy9YN6nM4TIEbGGqIf%2FJQ%2BEEnpDPC3ViP6y9zBNn4%2FHnnDQAbT1nt6nlE0YibwIzhjfj9LpiTQZJhQ%2FqQk2Pt%2BRO3Xo1uHAGoKI9qUNjjpPr%2B0CTSNn3UBsDhN%2BGaG7P4c09byOSH%2By0%2BUYfZKjWDKFFlSaOvUcbG5tvW%2FvsPtpKttCIzeGSarkvEYSBhmNHH4P3qFiKo9wFxt%2FVO1Il174g12sak4iRL59HHJoM3vvSOLdL4oQgnantzLRben0ciFtO4AIkmmengfB0HmCESot%2B56XQCzrc8QAgOJZKLnN7NkKzwKS%2FQok6C8CbBTGRw0zQZ6hMwPGvCnLfKDLyiOiXrTPSeI8TE%2B8oqoHnHHrCMIPLr8wGOqUBQE%2BaYPcP4trLmbPSCrvN2a4sBDrO1%2BI83YUMi6XC4Nkh7i6dtv61RHUWnaXaVySyIT8LA4PPGJhtqULJKVWcvU4OzgGYfovtNVAsSI7aX%2BXdwLhDr8uIFrIWcRJ3pSly8RtxCP%2FOg6yWSWaYW6sgrV0TsNGrDFzpjylKCXU2hgZEAidIKJmUOiTIexdB8s4bOluoTDZ%2BBkbfqmq0N2x10SE0QYKA&X-Amz-Signature=e5d1e972f089064b8f9a74429ffe5137bb230e455c3c7ff8b588e8e75ef00228&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


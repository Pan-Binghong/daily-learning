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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMFVK4T%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFUD0LtbNlZAyW%2Brc7zT%2Bcb3TOiAx36OdJ71FkIr9pbEAiEAi76gMbu8PAhg2D5hhMUX%2B39pjsja0TZ2PNyoZf9YAdMq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDMRx951JYl8VFtdYdCrcA%2F4SeMTcDexfVrnpPGFRKlA9qELp%2FtiHFVecAA5VVzB1y12ZMqtdkG08SG7abUQcGIQpu1QUpRE%2F2PHgMv5WDLrXWmeO9x%2BMEh8btnw90jM7f7SLqycZGgHlZ1N2uTWdVSw5zv9pg3dpNtDxHTq0WNu2l9BzsS4bAlRJX3GmpeCUoXXHSCulYiVpjrJs9UBgy%2F%2FAEv4zOuCoryn0tcjmOh0WHFmDITZ3VSUgdAyCLvL9RRBcDlg5pC6EN1%2FYSVTJgcTVU61HgjnhHisoSigp4BuFB2HbsyjZrhmipTn4b%2B%2B32lTokfNaERecmFsoIkwGslOoridlG5Nq%2BzjkIskL4YzqNcze6884Nm%2BuJzDqBVujH1mgMJqvrbVKTlNk8ThzFAJ6z6WDA%2FjeWFgpX9Sip%2FdcoypKipCsAmQFkMYLd5aQBOyCXkTLG3gLIFpVHYHeVurGTd%2F4Wz3jPLdQTd5qVpZ3lEH6E5RRCOzn18l2%2FK8RRcX18joXFVmOLnLl4KpuADu7nvJ4tztxZbGGalE2T1%2Fidjslw0CHNFGudsaCt3fzqlcBP5Xl8opkOM2CdCHNXIXBb7eCCYFbEUtYXH4xAAuynShTtsCaK0nJ1EFmtO0c%2B1luRNAK9wSHF45%2FMObCs80GOqUBpQfMKf%2BLcl%2BU218E%2FqrYfCpEdEcME0hjuKiKUZF1oeYmQkI8dklqcxir2j4ACJXEuaiFX9qPMnO8abJSS6oHZeobe5hAQV26fuZ5N%2B%2Bskl%2FkVYUJHLrdvgyh5kPP9gUqZbdCjCqOdIWoTB5KjMLw3wtVYKR8Hc9dyOJPSD6hku7rL9PAkISh3F2LrxIMzmRNfBbRB9rwC55t6iv2ftntgKkerTq7&X-Amz-Signature=215d7d813b157caa233a6d926a34e6172b33e79cf710c0dcc6708abf8481224f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMFVK4T%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFUD0LtbNlZAyW%2Brc7zT%2Bcb3TOiAx36OdJ71FkIr9pbEAiEAi76gMbu8PAhg2D5hhMUX%2B39pjsja0TZ2PNyoZf9YAdMq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDMRx951JYl8VFtdYdCrcA%2F4SeMTcDexfVrnpPGFRKlA9qELp%2FtiHFVecAA5VVzB1y12ZMqtdkG08SG7abUQcGIQpu1QUpRE%2F2PHgMv5WDLrXWmeO9x%2BMEh8btnw90jM7f7SLqycZGgHlZ1N2uTWdVSw5zv9pg3dpNtDxHTq0WNu2l9BzsS4bAlRJX3GmpeCUoXXHSCulYiVpjrJs9UBgy%2F%2FAEv4zOuCoryn0tcjmOh0WHFmDITZ3VSUgdAyCLvL9RRBcDlg5pC6EN1%2FYSVTJgcTVU61HgjnhHisoSigp4BuFB2HbsyjZrhmipTn4b%2B%2B32lTokfNaERecmFsoIkwGslOoridlG5Nq%2BzjkIskL4YzqNcze6884Nm%2BuJzDqBVujH1mgMJqvrbVKTlNk8ThzFAJ6z6WDA%2FjeWFgpX9Sip%2FdcoypKipCsAmQFkMYLd5aQBOyCXkTLG3gLIFpVHYHeVurGTd%2F4Wz3jPLdQTd5qVpZ3lEH6E5RRCOzn18l2%2FK8RRcX18joXFVmOLnLl4KpuADu7nvJ4tztxZbGGalE2T1%2Fidjslw0CHNFGudsaCt3fzqlcBP5Xl8opkOM2CdCHNXIXBb7eCCYFbEUtYXH4xAAuynShTtsCaK0nJ1EFmtO0c%2B1luRNAK9wSHF45%2FMObCs80GOqUBpQfMKf%2BLcl%2BU218E%2FqrYfCpEdEcME0hjuKiKUZF1oeYmQkI8dklqcxir2j4ACJXEuaiFX9qPMnO8abJSS6oHZeobe5hAQV26fuZ5N%2B%2Bskl%2FkVYUJHLrdvgyh5kPP9gUqZbdCjCqOdIWoTB5KjMLw3wtVYKR8Hc9dyOJPSD6hku7rL9PAkISh3F2LrxIMzmRNfBbRB9rwC55t6iv2ftntgKkerTq7&X-Amz-Signature=fd083c369830c12a1c42569e48ad742925589f69850751557296442d344b4682&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


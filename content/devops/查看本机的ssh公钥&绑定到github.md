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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QQULSDB%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQCE6JyZJU5bT7QEngywfP%2Brgy%2F6WcFxFcfv%2F%2BZ6cVXrBQIgKLvKcUmBC9mUeVTdO4PPxEx4NXWZ6c%2Bt0Nhb2AYBtmEqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIHAso%2FaUbS0lZqRTCrcAxXZevjeNLemWKbRQyrjZK4dUDwlLfHRSg%2FhJduWk1QVwJLiT62CeCW9xqJIDCeIGNiQN%2FTixoy%2FeKLez6%2FSTQvsJ6ULOoKZlS61oL9KPMY0Es7BjOfqpo02w2AzIr%2BWeONzcCeT%2Fm70hcr6JffEldCOtm%2FEPxY1xWKwnUqzkp3zFxucjq9BB5q5o5wmC2X%2BibgzMEl8JvEnjp4ktrbcxqs8rDzOi9nou11VytZzp0LG%2FGe1Dy2lmo2Teq2YguGyz7%2FghBFoZ3ZVErv6ONyKpxtgwZxYFGp4y5bl%2FNDeNq5uG38Ufz3VnDkH0pFeCnS8mHFRawC6AUdnMMD18kO7C7EV32yn6D5aGVEHP9fZiq4KVnc70QXC3QSN5hCsztM01cLDRFu93qUwCyzGaslyyMYELCxTh4xeeBurQUSdf4yAzOcG2DrXbOuzYIJ4t7xTAVjaWlYXt9QoGsYt2d5%2Br7uV0cSFQ%2BmKqNtPgUmaY17SnZRgj1UAoaxhq2756LssUWwrgHHggfFDNE2mYbUVUsFdKQRJPp1DKTlDhquWG%2BRX%2Fqw95B%2FjJWdQ35bHIiSqjMWPKSu1hqGs7GA88wKrYu4ziIwZZwmursYLMovP4yprfQ%2FnfI6Pm52RVcLqMOiRtcwGOqUBCfynGSGYsF%2FoBiCyri0mnNmdU4FOjl1VJC3Cnmj8dY8Ru3ju%2BUghqNQGqctHx4e8MMn8JfrlcatRx6%2FPSuCpbGzBNRZS7jltPz7zgn2bGpsH5xB3L8nMHYnEqJ%2FMGS39uWR3B02lKdwR%2BuQWE1YT1FbPqqzJYmSZf2ZeTnGpxV9j0zfnOo0UnMHn2gM04soUOurPExekvv3sGZ6d8hUWItCs69XX&X-Amz-Signature=8697f566e9187985b756236141a1191dcd6d5443b90b2f67a89f01babad96952&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QQULSDB%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQCE6JyZJU5bT7QEngywfP%2Brgy%2F6WcFxFcfv%2F%2BZ6cVXrBQIgKLvKcUmBC9mUeVTdO4PPxEx4NXWZ6c%2Bt0Nhb2AYBtmEqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIHAso%2FaUbS0lZqRTCrcAxXZevjeNLemWKbRQyrjZK4dUDwlLfHRSg%2FhJduWk1QVwJLiT62CeCW9xqJIDCeIGNiQN%2FTixoy%2FeKLez6%2FSTQvsJ6ULOoKZlS61oL9KPMY0Es7BjOfqpo02w2AzIr%2BWeONzcCeT%2Fm70hcr6JffEldCOtm%2FEPxY1xWKwnUqzkp3zFxucjq9BB5q5o5wmC2X%2BibgzMEl8JvEnjp4ktrbcxqs8rDzOi9nou11VytZzp0LG%2FGe1Dy2lmo2Teq2YguGyz7%2FghBFoZ3ZVErv6ONyKpxtgwZxYFGp4y5bl%2FNDeNq5uG38Ufz3VnDkH0pFeCnS8mHFRawC6AUdnMMD18kO7C7EV32yn6D5aGVEHP9fZiq4KVnc70QXC3QSN5hCsztM01cLDRFu93qUwCyzGaslyyMYELCxTh4xeeBurQUSdf4yAzOcG2DrXbOuzYIJ4t7xTAVjaWlYXt9QoGsYt2d5%2Br7uV0cSFQ%2BmKqNtPgUmaY17SnZRgj1UAoaxhq2756LssUWwrgHHggfFDNE2mYbUVUsFdKQRJPp1DKTlDhquWG%2BRX%2Fqw95B%2FjJWdQ35bHIiSqjMWPKSu1hqGs7GA88wKrYu4ziIwZZwmursYLMovP4yprfQ%2FnfI6Pm52RVcLqMOiRtcwGOqUBCfynGSGYsF%2FoBiCyri0mnNmdU4FOjl1VJC3Cnmj8dY8Ru3ju%2BUghqNQGqctHx4e8MMn8JfrlcatRx6%2FPSuCpbGzBNRZS7jltPz7zgn2bGpsH5xB3L8nMHYnEqJ%2FMGS39uWR3B02lKdwR%2BuQWE1YT1FbPqqzJYmSZf2ZeTnGpxV9j0zfnOo0UnMHn2gM04soUOurPExekvv3sGZ6d8hUWItCs69XX&X-Amz-Signature=42adce5ecf8c8a19dfebdfe5f9faec0c4352e6291231d66e234dc03d0b8b5564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


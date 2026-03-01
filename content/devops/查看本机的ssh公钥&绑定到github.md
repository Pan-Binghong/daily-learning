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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LJGEF5X%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9YRsz0jYVFGsbwU0akzr91lLZZGSzbobgfqYgDF6a5wIgfBlf4krzmGSgla%2FR8ORzDx%2FvsvPQ2sc9i31jjhW%2FC0Yq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDGngmzoJs%2BCzynF3PCrcA0Zl1oqBnWcUMOOlsQwddLfPMFOsSL%2BEjkpywVMpAVB5XDJ5JtxDS587CbIlK2AuTlVEbp%2F7GqESeyAeuwzZ7qjPva%2FLWRdiwqCez%2BQ1aeyFTbJFAUoDjGhX7PhzpdnL7ciTQbjucwOJXzUe2sti0OLGGNDE80JLdgfkOyDmZk6HDk2v%2Fv6AIG8jcDTNuqIKSBIjkVQXJJnNT3eD%2B4YB7LP27vlD1Wg39ROMN8B2D6HLE1BMqfNcQ6EBbkPXQEG0wdWjP6io0ClZfP2jl0qO65ViH34JWfKxnSfjZgOfEShPAbxiC%2FHhOYI5CR2MP8Fo%2FhIQJjEHXcLBydXCOqIY0nOzY5SZvGpjJg9iB%2FjZP4QK3Pvl95hLC5%2B8JjACdWJlWrmYVJlpQ2MQ36fsESAkDlYyDA5oBITNos9TgbDoHHo%2FF6aMmnHRILh8eBJE2%2FrTCZBG3hJSb5rXn0x8HZmNVbEnieBQOXF%2B4i3MGyE0eKXVz1mRaAmjhmfdIG88FJkmc3H2jVo38AFV4mRDXzgu7TFOfWftaGbaVz8e%2Bs0vMOZonR5JX2bDwRwXHE1jZDIlIDM%2FQj8Q%2BEeQI9%2BytWy09sjcCXGAaGiMaUShBrFCKIp1vzlg5aXqo8zM3YrVMJPOjs0GOqUBzcAW7aZ6b%2F%2FS20ikWoU6d%2FOdCyF77hrmiWl3jH54%2Bc7f6WdJQ69FqyOEHdmrc4UTLsNtfB%2Fo4vk8KEE6u434cnC%2BZ6bnzYesXMMTgtuSxzvbqq7MKAS6otbgGfd5GV0tuzNxFojSJ7Juy0br50S2dLZiNPWzdYnahFbiyEgcAW9zsAUUNrWCqdQdtMF%2F8MOUIQDpJUgmXAdYRuGhIJW1CtoJDD1Q&X-Amz-Signature=5d38704ac0b928ecdd83c76a46c1aa5684b9b103d97f65227e02a03759156e1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LJGEF5X%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9YRsz0jYVFGsbwU0akzr91lLZZGSzbobgfqYgDF6a5wIgfBlf4krzmGSgla%2FR8ORzDx%2FvsvPQ2sc9i31jjhW%2FC0Yq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDGngmzoJs%2BCzynF3PCrcA0Zl1oqBnWcUMOOlsQwddLfPMFOsSL%2BEjkpywVMpAVB5XDJ5JtxDS587CbIlK2AuTlVEbp%2F7GqESeyAeuwzZ7qjPva%2FLWRdiwqCez%2BQ1aeyFTbJFAUoDjGhX7PhzpdnL7ciTQbjucwOJXzUe2sti0OLGGNDE80JLdgfkOyDmZk6HDk2v%2Fv6AIG8jcDTNuqIKSBIjkVQXJJnNT3eD%2B4YB7LP27vlD1Wg39ROMN8B2D6HLE1BMqfNcQ6EBbkPXQEG0wdWjP6io0ClZfP2jl0qO65ViH34JWfKxnSfjZgOfEShPAbxiC%2FHhOYI5CR2MP8Fo%2FhIQJjEHXcLBydXCOqIY0nOzY5SZvGpjJg9iB%2FjZP4QK3Pvl95hLC5%2B8JjACdWJlWrmYVJlpQ2MQ36fsESAkDlYyDA5oBITNos9TgbDoHHo%2FF6aMmnHRILh8eBJE2%2FrTCZBG3hJSb5rXn0x8HZmNVbEnieBQOXF%2B4i3MGyE0eKXVz1mRaAmjhmfdIG88FJkmc3H2jVo38AFV4mRDXzgu7TFOfWftaGbaVz8e%2Bs0vMOZonR5JX2bDwRwXHE1jZDIlIDM%2FQj8Q%2BEeQI9%2BytWy09sjcCXGAaGiMaUShBrFCKIp1vzlg5aXqo8zM3YrVMJPOjs0GOqUBzcAW7aZ6b%2F%2FS20ikWoU6d%2FOdCyF77hrmiWl3jH54%2Bc7f6WdJQ69FqyOEHdmrc4UTLsNtfB%2Fo4vk8KEE6u434cnC%2BZ6bnzYesXMMTgtuSxzvbqq7MKAS6otbgGfd5GV0tuzNxFojSJ7Juy0br50S2dLZiNPWzdYnahFbiyEgcAW9zsAUUNrWCqdQdtMF%2F8MOUIQDpJUgmXAdYRuGhIJW1CtoJDD1Q&X-Amz-Signature=75c37a85c110966d0333fe14a25b2ba14ef8e556e4b5fe0cd2d8ab5e00ae88c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


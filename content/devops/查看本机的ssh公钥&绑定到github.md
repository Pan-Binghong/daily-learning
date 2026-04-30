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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NZERINI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIC9p6KLjKTAxCc1GtqbC3t%2B%2F7gf6iVjQ8EamL2BNkUVAAiAjZqWaSr3FgFv6GK4gvI0bbePNMKfNUWqPGAuRHgpwMSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMLQ13vUQnXDJORURlKtwDeLNyFOcPMNXru%2FLUKU612ZZsQTbBXRXhzKku0HcKIeQl8MZNkbD3PFEEEIAP7dDmut4zicWCRkht5gXTClgHMjzgH1czbgPMaSLGJRIBwAV1D1994MtSDivkcEH%2BWXxJnuhQp3LhDWFfx9HeZISZgvwxSLEIQau%2Bg66ftsjW%2Bs6MMJWFf5hzqHLwII22JgLhWw5BpqxMOYvVglepNyPfls69LvkkJ1lL1knCBc6lirEHIQO%2FfGg9HjhXPTKFq%2B2Jf6kHrmdkWI5JafsJ0uZJJkfIw66nm8OaDDZR4lPhM2GgG8h1kQaQFbEks2gqvsWuKLp%2BULJBN2LJ4kw2lFKqS8s0Kjn0Gh75hGB87j8BqFsszbvcEL94vYcMfoniHXBOBTCg7pU6SvO1E9ULs7%2BbLhvdhkBRJW2g3OETB4DUFKho8Uz7E%2BTkqGT3zwMyAwDIc12X%2Fc1%2BqbvuuMbJvSbFBiN7FO6sm2W00txGItwLcCqbrP1OITVD9he8m1dstIhyzqaygSpGTGCjexLgZoHS8L4tR%2BdM4bZFURRTT5q5%2BMiCLh1aTmzy1uNKCP90FoA1UzP5q1RnBXZiJFkV3NagYroZCofAQMRiMAOTVE2kH5eKGzt0BlofEahkLRYwp57MzwY6pgFrSQQnfSxGt9UDctT6726wL7TQo52X6AdxomppKSl%2FucJTuoq17Ig2rhcxEyONvYXqPwhoxA3kDDVGcheNXSdqhL4FG4ak3n8UZBdcpk8oi5UWrZds5UpNIrjE%2FryqpU5q%2B8a4krg8e7uk%2FyutTyeeSPOw7nIZIdqIIXt%2F2pKgTWfKRyBwdvfr6fPi0DKGZpUwU0Is66abJ%2FCWpRS90%2BBC4IYLb5iY&X-Amz-Signature=fc0f074697cd7aa93aca663b270fa5df389923bcee8419f82c9b4c239c16b01d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NZERINI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIC9p6KLjKTAxCc1GtqbC3t%2B%2F7gf6iVjQ8EamL2BNkUVAAiAjZqWaSr3FgFv6GK4gvI0bbePNMKfNUWqPGAuRHgpwMSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMLQ13vUQnXDJORURlKtwDeLNyFOcPMNXru%2FLUKU612ZZsQTbBXRXhzKku0HcKIeQl8MZNkbD3PFEEEIAP7dDmut4zicWCRkht5gXTClgHMjzgH1czbgPMaSLGJRIBwAV1D1994MtSDivkcEH%2BWXxJnuhQp3LhDWFfx9HeZISZgvwxSLEIQau%2Bg66ftsjW%2Bs6MMJWFf5hzqHLwII22JgLhWw5BpqxMOYvVglepNyPfls69LvkkJ1lL1knCBc6lirEHIQO%2FfGg9HjhXPTKFq%2B2Jf6kHrmdkWI5JafsJ0uZJJkfIw66nm8OaDDZR4lPhM2GgG8h1kQaQFbEks2gqvsWuKLp%2BULJBN2LJ4kw2lFKqS8s0Kjn0Gh75hGB87j8BqFsszbvcEL94vYcMfoniHXBOBTCg7pU6SvO1E9ULs7%2BbLhvdhkBRJW2g3OETB4DUFKho8Uz7E%2BTkqGT3zwMyAwDIc12X%2Fc1%2BqbvuuMbJvSbFBiN7FO6sm2W00txGItwLcCqbrP1OITVD9he8m1dstIhyzqaygSpGTGCjexLgZoHS8L4tR%2BdM4bZFURRTT5q5%2BMiCLh1aTmzy1uNKCP90FoA1UzP5q1RnBXZiJFkV3NagYroZCofAQMRiMAOTVE2kH5eKGzt0BlofEahkLRYwp57MzwY6pgFrSQQnfSxGt9UDctT6726wL7TQo52X6AdxomppKSl%2FucJTuoq17Ig2rhcxEyONvYXqPwhoxA3kDDVGcheNXSdqhL4FG4ak3n8UZBdcpk8oi5UWrZds5UpNIrjE%2FryqpU5q%2B8a4krg8e7uk%2FyutTyeeSPOw7nIZIdqIIXt%2F2pKgTWfKRyBwdvfr6fPi0DKGZpUwU0Is66abJ%2FCWpRS90%2BBC4IYLb5iY&X-Amz-Signature=f7a30472d55eed9c8e96e456fef0a35fb97f5189ce5728d8fd365aa3d79e044e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


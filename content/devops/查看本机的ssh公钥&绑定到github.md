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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663FLTGUR%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHGkiaHG64QH5tzlmfOv%2BaVNc7gunP2EOfKNVusV6bjXAiEA9QH0yd3Jpvm8HdIqaP8B2Wvdz7ySRtZTzRJgfvuRETwq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDKz8fD5AKAb1CcW%2FdyrcAx3lMvdHOQWAWpolwp%2BXeCL4E8wzWDEE1u6Slv1i5JSW7LrT9g1ou%2FxRpS6IRbtjLgbZsWpkBX4qyXbHP%2FMbUJYVF8mHRMmfZF%2BG4WJFlkWLKXMzBVD4UKoQwTL1thKcSKBhHgfzihcbinr016syP%2FlcOekUQEygIVDO7WChjcqYAv9yA8Xdr9IpnEd3FVQgRXL5OuSTwWrevYC%2BzZ5uUm4v6C47%2BAewof%2FMS3Oae6hIR%2FxFdFKTSvp3j%2FKXZdtRmgvMtVG9ycoxGEaWvOwAMbgfEeCL0agnt7ngRyXAPO6K2fXA%2FnWuUkvcclVPm%2FjM0tjqRGVYa0juxfx93layTobDdYj%2FTzXPpYFIDIijx41VHsJ4eJWgLG%2FuPsjYUopz1euvd7K5OSsknyQ4ft04BQ9GbTgjSPJKvDpWf8zzKJN9BDYCvPwdUigvwZ0mHO5LDY14YdQWkTH9F0AwPhpU3aJKsLhi%2BgQyXtYJdFFsJdL5r3sXjhuhxwX%2BuVoZ9ns22OqbjveXpINNpQG0cxGK0m%2FrXTEcYWpwAyf6xriEzBwQwNdtJTQVwWs415QURMskMAVKD%2FpP%2FmlwgFKw6JHdgYH5DzLLABv%2BRkN494dCAq1bu0Ipmac0ojR2eXwbMPO9os4GOqUBB6sOtwi%2BE14KesWOb76bSQtTx6l6djahXOosa1pVnK3SHVI%2FiIUGuh%2BAkNi9wEmitjoAej9etRW5OshtpZ8y8jRDTNnuccZZNaOpP1JmxgmLGRzqyzM3eDvrum%2BPRu7y5Iq16gdOAiZB6K7FRjynFdQNP8%2BXYPBwGKW5%2Fi7TtoI%2Bhd1Ii7owpT1KG8jOfMdeoCnwtwBtGgnqsrd90SHhWWsRSK%2B%2B&X-Amz-Signature=63fee877caf8b0fde8d728825d0e2484ed87eb7058343e134cc5728e2645417d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663FLTGUR%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHGkiaHG64QH5tzlmfOv%2BaVNc7gunP2EOfKNVusV6bjXAiEA9QH0yd3Jpvm8HdIqaP8B2Wvdz7ySRtZTzRJgfvuRETwq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDKz8fD5AKAb1CcW%2FdyrcAx3lMvdHOQWAWpolwp%2BXeCL4E8wzWDEE1u6Slv1i5JSW7LrT9g1ou%2FxRpS6IRbtjLgbZsWpkBX4qyXbHP%2FMbUJYVF8mHRMmfZF%2BG4WJFlkWLKXMzBVD4UKoQwTL1thKcSKBhHgfzihcbinr016syP%2FlcOekUQEygIVDO7WChjcqYAv9yA8Xdr9IpnEd3FVQgRXL5OuSTwWrevYC%2BzZ5uUm4v6C47%2BAewof%2FMS3Oae6hIR%2FxFdFKTSvp3j%2FKXZdtRmgvMtVG9ycoxGEaWvOwAMbgfEeCL0agnt7ngRyXAPO6K2fXA%2FnWuUkvcclVPm%2FjM0tjqRGVYa0juxfx93layTobDdYj%2FTzXPpYFIDIijx41VHsJ4eJWgLG%2FuPsjYUopz1euvd7K5OSsknyQ4ft04BQ9GbTgjSPJKvDpWf8zzKJN9BDYCvPwdUigvwZ0mHO5LDY14YdQWkTH9F0AwPhpU3aJKsLhi%2BgQyXtYJdFFsJdL5r3sXjhuhxwX%2BuVoZ9ns22OqbjveXpINNpQG0cxGK0m%2FrXTEcYWpwAyf6xriEzBwQwNdtJTQVwWs415QURMskMAVKD%2FpP%2FmlwgFKw6JHdgYH5DzLLABv%2BRkN494dCAq1bu0Ipmac0ojR2eXwbMPO9os4GOqUBB6sOtwi%2BE14KesWOb76bSQtTx6l6djahXOosa1pVnK3SHVI%2FiIUGuh%2BAkNi9wEmitjoAej9etRW5OshtpZ8y8jRDTNnuccZZNaOpP1JmxgmLGRzqyzM3eDvrum%2BPRu7y5Iq16gdOAiZB6K7FRjynFdQNP8%2BXYPBwGKW5%2Fi7TtoI%2Bhd1Ii7owpT1KG8jOfMdeoCnwtwBtGgnqsrd90SHhWWsRSK%2B%2B&X-Amz-Signature=e5c0881f1c0485f8b10969db224101f89f798d2ec3d92063a15bd5e3ee1907f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


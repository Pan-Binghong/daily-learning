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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGK7K5NB%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIBWog9EgAFKo63O%2BMyyAk7vqyd%2BudXEmjUSXDfExm0ZAAiEAqUp%2B%2BzjGXxMckDMiaihrobZBbuO%2BlY1nNz7RJ5%2F%2FA1cqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2FVSnGJoagIhCyUXircA9slkrH%2FVRkKFphV86gCCTS42Hlr1rvKIBGagScTTyExqqI0Kr9Nl%2FO52a3%2Blriq%2FBblW%2Fim7kcpjWatrXBMYEUek1DxBidA1RqDpDcmvd1%2BFuLaAWa60JwBuxmEkOKkFLi6tgyWFI2pg7NWkmUz6tj5cbUUwf14W4ExVmSxCbXWqPI9wQL6OArQeY94bbE8ypSId2qA0f7e73p5uz9XAyRcXJOsFk9E6RQgEcsmmj%2BTjFcImZmSX9qKD5tcEPgZpBwkA82R583jsYnSURQfG4VrK%2BKKUWSoRAcc8VLHIXQLtB5hpp9TG4Eg%2FRfqc9v8UNTeF7VNxxfvk2BsP3aUkju0irH5QXmeCBItIgpD7z%2FSnx%2Fc2sq0mQ8zOUcE3FDN3ZDRnNca68gWPRmLMZ1ue%2FU0FflHc92FnckX%2FrQBODipiPtUWzJjbgO08C5%2FelNx%2BDIBq5L4ncg5KjJyRbDMO3NzaSk1Z1wGhFOzCwdzJId6mJ4flKfPDo%2FaMwfcobQ2voHVnJhIv5LSlePdFPfFMdEweYCXbRb3ZzMArvlPyazRQEnlEd6L0AaWF3%2FKKg40O4zHp7Jy1WDobiUwffHZFhXjO%2Bt4QEdQtPoTABhLKK4cRaNmWrgNsh07y4TKMLWT78wGOqUByP6Vai0koHWKxSFnsxBh2ntZDmhKjlJdyDZucgpVthls6HDib9%2FPWTpAMLOWL67%2BRiETeF6Dsv6K7bYToVOwUDEeNWEhizGZYTzgEZQEPpIEhpW2Q7NtUps%2BT8BAXTYxqnuGuDDQRD5QDRyyR9TgLAVV0gsYgfxPyrDkoQd%2BcuE9%2BEteNIgqdIiM1YfPPAVuEZy5FCs%2FMkZcX%2BsxzhGrLNjQk0S3&X-Amz-Signature=bb4adfe0cc2151c6ade3e475e32d9fbbb1866d2e0efe50aca1c9105458ca38f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGK7K5NB%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIBWog9EgAFKo63O%2BMyyAk7vqyd%2BudXEmjUSXDfExm0ZAAiEAqUp%2B%2BzjGXxMckDMiaihrobZBbuO%2BlY1nNz7RJ5%2F%2FA1cqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2FVSnGJoagIhCyUXircA9slkrH%2FVRkKFphV86gCCTS42Hlr1rvKIBGagScTTyExqqI0Kr9Nl%2FO52a3%2Blriq%2FBblW%2Fim7kcpjWatrXBMYEUek1DxBidA1RqDpDcmvd1%2BFuLaAWa60JwBuxmEkOKkFLi6tgyWFI2pg7NWkmUz6tj5cbUUwf14W4ExVmSxCbXWqPI9wQL6OArQeY94bbE8ypSId2qA0f7e73p5uz9XAyRcXJOsFk9E6RQgEcsmmj%2BTjFcImZmSX9qKD5tcEPgZpBwkA82R583jsYnSURQfG4VrK%2BKKUWSoRAcc8VLHIXQLtB5hpp9TG4Eg%2FRfqc9v8UNTeF7VNxxfvk2BsP3aUkju0irH5QXmeCBItIgpD7z%2FSnx%2Fc2sq0mQ8zOUcE3FDN3ZDRnNca68gWPRmLMZ1ue%2FU0FflHc92FnckX%2FrQBODipiPtUWzJjbgO08C5%2FelNx%2BDIBq5L4ncg5KjJyRbDMO3NzaSk1Z1wGhFOzCwdzJId6mJ4flKfPDo%2FaMwfcobQ2voHVnJhIv5LSlePdFPfFMdEweYCXbRb3ZzMArvlPyazRQEnlEd6L0AaWF3%2FKKg40O4zHp7Jy1WDobiUwffHZFhXjO%2Bt4QEdQtPoTABhLKK4cRaNmWrgNsh07y4TKMLWT78wGOqUByP6Vai0koHWKxSFnsxBh2ntZDmhKjlJdyDZucgpVthls6HDib9%2FPWTpAMLOWL67%2BRiETeF6Dsv6K7bYToVOwUDEeNWEhizGZYTzgEZQEPpIEhpW2Q7NtUps%2BT8BAXTYxqnuGuDDQRD5QDRyyR9TgLAVV0gsYgfxPyrDkoQd%2BcuE9%2BEteNIgqdIiM1YfPPAVuEZy5FCs%2FMkZcX%2BsxzhGrLNjQk0S3&X-Amz-Signature=527dab9e0efa7dda6aeb49331408557212090bfec9a74657197659adac6fe354&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


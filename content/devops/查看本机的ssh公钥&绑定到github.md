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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWX7TQ3R%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIEj5npUk073985sDEoSUmydL%2BlX%2FX8U8R%2B3lch3DJvFHAiEAr5qr2CzO98oLK2UakmEf0DcribbSzVy7v25muhAKb0Qq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDCnW7yrRhGghXWaPJCrcA2vIt3Nv1%2BqgIXfisOchCY4RXIkfri%2F0Cfq86kcwfSdPPdgRuANiEWw%2FXIeXwoTXMu4gPp0DrZwC64%2BLS9AO73agHamkXKomFgfEPjoh9cOz8Xrko3HlLrZbmmGv29%2FjGzj4xKHinhsvtp8gZiZUXnVObSC350b3DvQJ%2FV3TL5c5%2B8%2B83WXlsDiIJSrh1vuLU69ADmqYQH4wtN0YKMb4Q470fwLA98iZI2oJDuDBchj6%2BuU3mgdLj%2FRxqZnE7t0JSRed1SiynQ6r4F8Ne%2FYV8qI%2FSpYt7RfvTnxEkE8C1jS3R8Q%2Bk8G8jqzhRP2Qj%2BBRjYbvWqthwcxbZ2HBQve9dkhF%2FqoQK0fItHvBxUo2dWATqu4g4pN2%2BXKmi5K0vy3FGjGIuhFQwsbZwuS9rY%2BY1l8jlOjOQbahNtFN7SRQt%2Fs5wDLgDmcatqKjWC0ENdSbpEgWwfPl2gaVlu%2FVxJas9WmKsYGQl%2BZzdFUNwyMABAlARmhcTx1er8texdXdWMYhhbZV2Q%2BJvoyKK2uYYm518OIfrpg%2FBubic4ieX2nQPr9I2A%2FUfmcnp84xGoQ3%2FUpFxyxZ0zoYReWk8P4bnyzRVPPk5woEuIkWfhzPUi6w4fHwgVtr%2BhwpRm8b%2Fy1HMJ%2Bz3M4GOqUBY8w%2F8%2BJjVXmFload8MqINr9ddoBc49sIiRvlBWQmPiApk2Vy%2BdFIE1HRf0YeAr9lbsay%2FMJiDCBaYIniUWV0THytB7mPUDLxizzFyfZihKQ2%2BbHtz82zCWDrNCVcU82mbq655fy4XUNseMJhlSTVL%2Fynn94D73EGYFwNlLaYGQ28PQWNkQ96tKSYeHZ9oEy9XVLgkWT5PzNOaOICrbQu7vFWPOvh&X-Amz-Signature=52dfafa76ae677f6c59d7fc66ee0fd1d0046f3b7888b9aedb00e8c51b050dcdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWX7TQ3R%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIEj5npUk073985sDEoSUmydL%2BlX%2FX8U8R%2B3lch3DJvFHAiEAr5qr2CzO98oLK2UakmEf0DcribbSzVy7v25muhAKb0Qq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDCnW7yrRhGghXWaPJCrcA2vIt3Nv1%2BqgIXfisOchCY4RXIkfri%2F0Cfq86kcwfSdPPdgRuANiEWw%2FXIeXwoTXMu4gPp0DrZwC64%2BLS9AO73agHamkXKomFgfEPjoh9cOz8Xrko3HlLrZbmmGv29%2FjGzj4xKHinhsvtp8gZiZUXnVObSC350b3DvQJ%2FV3TL5c5%2B8%2B83WXlsDiIJSrh1vuLU69ADmqYQH4wtN0YKMb4Q470fwLA98iZI2oJDuDBchj6%2BuU3mgdLj%2FRxqZnE7t0JSRed1SiynQ6r4F8Ne%2FYV8qI%2FSpYt7RfvTnxEkE8C1jS3R8Q%2Bk8G8jqzhRP2Qj%2BBRjYbvWqthwcxbZ2HBQve9dkhF%2FqoQK0fItHvBxUo2dWATqu4g4pN2%2BXKmi5K0vy3FGjGIuhFQwsbZwuS9rY%2BY1l8jlOjOQbahNtFN7SRQt%2Fs5wDLgDmcatqKjWC0ENdSbpEgWwfPl2gaVlu%2FVxJas9WmKsYGQl%2BZzdFUNwyMABAlARmhcTx1er8texdXdWMYhhbZV2Q%2BJvoyKK2uYYm518OIfrpg%2FBubic4ieX2nQPr9I2A%2FUfmcnp84xGoQ3%2FUpFxyxZ0zoYReWk8P4bnyzRVPPk5woEuIkWfhzPUi6w4fHwgVtr%2BhwpRm8b%2Fy1HMJ%2Bz3M4GOqUBY8w%2F8%2BJjVXmFload8MqINr9ddoBc49sIiRvlBWQmPiApk2Vy%2BdFIE1HRf0YeAr9lbsay%2FMJiDCBaYIniUWV0THytB7mPUDLxizzFyfZihKQ2%2BbHtz82zCWDrNCVcU82mbq655fy4XUNseMJhlSTVL%2Fynn94D73EGYFwNlLaYGQ28PQWNkQ96tKSYeHZ9oEy9XVLgkWT5PzNOaOICrbQu7vFWPOvh&X-Amz-Signature=8a2621966d26a36d5611a08d4d34ccf4303b6d76c858a809672ba00b8a615246&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


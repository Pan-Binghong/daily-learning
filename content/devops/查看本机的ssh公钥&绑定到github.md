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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OEJYKXU%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCq3tNEM%2F1Wb6pSKEqGVY69P0i7C0U3kV4%2BncqFeWzcHAIhAJSmddoyFrvXK6o3gnVHIUMCzLnYdq8Dhr27QHzkGpGUKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgb1omjwqutd4QPtsq3AMNFTMWTDvMufAl2wmHLafG8I7bHD4CtbblstYx3Q8YtxZPv5u51y5D9doE6dzMR2DlkQFSo0fgGASKtyrYIvrGUvhyzR%2B4Y2H3%2F7GfPwZsengk%2FiS5EVbm8WThqufCgM0be%2FGWgIE9B3Emed6SD72uGrEHwphxX9wuj15IRpERmBwz%2F%2BMgU7etZ00eCVoffBbTvJSjzjini6%2BFZOT0juORgAFWasCHAByciTyDRA55N3IQo5Axnx30Q8cVASDkcrWUhGSmSa4VTwvYSccKMeR19hk5QDcK9l1gcrwZzdaAuHZJURPBmVOVOgsqoRS2tujit1WNDWiMqHsm%2BXe5YXoeOJtd8UVKqHULCKUoV1UvMWzmCzGiyhJpLXHHok7XwaZpEmCZnUqlePjMj8NTimh5AfjicGWB9t48o2FFaxWKJMTGs2npBBf9S4hVwts65MZuN9o3duA58UipLynnGe5kyl9FGMGTLz6ZbbzWhkaiK6NivHttN99tMj4VcwX7s5z3fhrnAXL6nwwx6f263%2BciUin4YrshpgbE70uEQ7ds8Ajq9VoQ5c7Akxnb1OWgQ%2F9ClUv1ZRkr%2B4VrQrL3d2KMVKD1UJuS1x2f%2FiqYoBYRkmYfC8VePQ0vvUlr2zDp5%2BLNBjqkAXyl2RK3VskT6KEdQYth7VhNTTYSFVzgZot%2BN6TUHTKtfvNkTtDYyqRGzCbH9YySuXlf8GmXbDw%2B55Mhw1D%2F6WCqX1pKDwOtZL5BRGOHnX8zoX%2BlVK3ywi%2BmrdfTkNON8nVJRRsutZ3jOcz3qxDiXIWyti1o%2FHSECHTuyjyj4KwUVbyJLXyFWwl9XfR2z1s31OzgCk8VGqbO8ENA1NafdFOo%2FqzK&X-Amz-Signature=5fea0b59df163ba949156745d2b1521618b3775dc59cf9d9b12ef3a789934f43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OEJYKXU%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCq3tNEM%2F1Wb6pSKEqGVY69P0i7C0U3kV4%2BncqFeWzcHAIhAJSmddoyFrvXK6o3gnVHIUMCzLnYdq8Dhr27QHzkGpGUKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgb1omjwqutd4QPtsq3AMNFTMWTDvMufAl2wmHLafG8I7bHD4CtbblstYx3Q8YtxZPv5u51y5D9doE6dzMR2DlkQFSo0fgGASKtyrYIvrGUvhyzR%2B4Y2H3%2F7GfPwZsengk%2FiS5EVbm8WThqufCgM0be%2FGWgIE9B3Emed6SD72uGrEHwphxX9wuj15IRpERmBwz%2F%2BMgU7etZ00eCVoffBbTvJSjzjini6%2BFZOT0juORgAFWasCHAByciTyDRA55N3IQo5Axnx30Q8cVASDkcrWUhGSmSa4VTwvYSccKMeR19hk5QDcK9l1gcrwZzdaAuHZJURPBmVOVOgsqoRS2tujit1WNDWiMqHsm%2BXe5YXoeOJtd8UVKqHULCKUoV1UvMWzmCzGiyhJpLXHHok7XwaZpEmCZnUqlePjMj8NTimh5AfjicGWB9t48o2FFaxWKJMTGs2npBBf9S4hVwts65MZuN9o3duA58UipLynnGe5kyl9FGMGTLz6ZbbzWhkaiK6NivHttN99tMj4VcwX7s5z3fhrnAXL6nwwx6f263%2BciUin4YrshpgbE70uEQ7ds8Ajq9VoQ5c7Akxnb1OWgQ%2F9ClUv1ZRkr%2B4VrQrL3d2KMVKD1UJuS1x2f%2FiqYoBYRkmYfC8VePQ0vvUlr2zDp5%2BLNBjqkAXyl2RK3VskT6KEdQYth7VhNTTYSFVzgZot%2BN6TUHTKtfvNkTtDYyqRGzCbH9YySuXlf8GmXbDw%2B55Mhw1D%2F6WCqX1pKDwOtZL5BRGOHnX8zoX%2BlVK3ywi%2BmrdfTkNON8nVJRRsutZ3jOcz3qxDiXIWyti1o%2FHSECHTuyjyj4KwUVbyJLXyFWwl9XfR2z1s31OzgCk8VGqbO8ENA1NafdFOo%2FqzK&X-Amz-Signature=adb82d3ea1aa50db77cc04e2422e0cce29549720292dbf55c9e41bb6e5eab61f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


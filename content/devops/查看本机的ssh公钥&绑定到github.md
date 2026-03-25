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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHPMS5HW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGlsD5OX5yikWkMO9Q7Hdd0Zw2v2R26l%2Bn%2F9BrFWJ0RdAiBu0bYSF4D1xvQRsCcHFDj8c4F9Wkky4VkY7H9KI3SUSCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2%2FLwM4pMubYB9uoDKtwD8%2Fi4eLQWACUgKZ%2FNQTkD0Guwqa%2FA%2Borviw%2Bjhc2OGsq6yUt7BXDYJpcRO1CsUqyJMwi83WM2aXG%2FfmwHVjgRxKnqGml2e8gF5RofbPNmOtyNPIUrt7qe9dH8f0XDY8ck59Waik4imSwvZEOJreEwqEf0zjBJyl5NuGzQQIRqm%2BtOVLUXShLbIxSssVP4eJI2irvDziyt8Xi37y6nz%2Bt8QV8QAxF3kuL7wKQVU32HyByMR4UB52%2BVQ5DxQOQREGs8RQWyexh%2B7jy91qTdlBxWFJ6mhC5B%2BECeXBJKBOxtlazT5fZ066GEtzvcKgVSIiNmMJOghyxJAjGDxQQLAR%2Bi0QEEAvQFurKWEcVO4sG345XOiwmFFx%2B%2FU6FdMTjE%2BAgUFKkgFJ60dfK619zLETQhbXvfO2Vv433GYJ2820RBGUtvH59E1OVZwicF3WsU14Xtdh6X4mmFkNfuvPmlSqxmBt8L29%2FXFyx9VM%2BH6J9oqFeYxiV1ee5%2BRQLVv0v7iqtQrR1Cm4RLBAJsU9BFckVR5qd5v%2FVWvg8SeIqGFFpO%2BXuamUoxSeM69LS1odwLoEXmhKBtNzVXV9mya47BlFYsWA6RdviWxudCSomTdoV%2B5BDzwyoHJzoP5wI5%2Fk8wy6SNzgY6pgHwwf7%2FpTM%2BUMKj6S13CxOz0F9zZHjpKIp9tFWOVGCZkNHB9eRozky97AP16vmF9KjH182ON%2FFTnIrQzdHz8aHJIcFMbURZJtdUoKntWkFrkOiwGAseeue9QceaPnJfYpuDYDpRmOaDBqQewOfCNQsAV%2F0zEHysM0uKBmaAMofuKFloefjXp5T7mrDwtRAeRpy1WLw9W2X1PHneZ%2BLXilz6fOCQ7W5K&X-Amz-Signature=1feb1013baa37f4a190cd29388e9d7cb3c187e29175c0e6d7b1d12262513f5d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHPMS5HW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGlsD5OX5yikWkMO9Q7Hdd0Zw2v2R26l%2Bn%2F9BrFWJ0RdAiBu0bYSF4D1xvQRsCcHFDj8c4F9Wkky4VkY7H9KI3SUSCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2%2FLwM4pMubYB9uoDKtwD8%2Fi4eLQWACUgKZ%2FNQTkD0Guwqa%2FA%2Borviw%2Bjhc2OGsq6yUt7BXDYJpcRO1CsUqyJMwi83WM2aXG%2FfmwHVjgRxKnqGml2e8gF5RofbPNmOtyNPIUrt7qe9dH8f0XDY8ck59Waik4imSwvZEOJreEwqEf0zjBJyl5NuGzQQIRqm%2BtOVLUXShLbIxSssVP4eJI2irvDziyt8Xi37y6nz%2Bt8QV8QAxF3kuL7wKQVU32HyByMR4UB52%2BVQ5DxQOQREGs8RQWyexh%2B7jy91qTdlBxWFJ6mhC5B%2BECeXBJKBOxtlazT5fZ066GEtzvcKgVSIiNmMJOghyxJAjGDxQQLAR%2Bi0QEEAvQFurKWEcVO4sG345XOiwmFFx%2B%2FU6FdMTjE%2BAgUFKkgFJ60dfK619zLETQhbXvfO2Vv433GYJ2820RBGUtvH59E1OVZwicF3WsU14Xtdh6X4mmFkNfuvPmlSqxmBt8L29%2FXFyx9VM%2BH6J9oqFeYxiV1ee5%2BRQLVv0v7iqtQrR1Cm4RLBAJsU9BFckVR5qd5v%2FVWvg8SeIqGFFpO%2BXuamUoxSeM69LS1odwLoEXmhKBtNzVXV9mya47BlFYsWA6RdviWxudCSomTdoV%2B5BDzwyoHJzoP5wI5%2Fk8wy6SNzgY6pgHwwf7%2FpTM%2BUMKj6S13CxOz0F9zZHjpKIp9tFWOVGCZkNHB9eRozky97AP16vmF9KjH182ON%2FFTnIrQzdHz8aHJIcFMbURZJtdUoKntWkFrkOiwGAseeue9QceaPnJfYpuDYDpRmOaDBqQewOfCNQsAV%2F0zEHysM0uKBmaAMofuKFloefjXp5T7mrDwtRAeRpy1WLw9W2X1PHneZ%2BLXilz6fOCQ7W5K&X-Amz-Signature=856a0cf20b46a5c0c6ddfe92bd88cb238fe8de388798152888411c1f43ead2af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


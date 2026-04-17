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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ILNUWC2%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDRjD029N%2Fx7nzX033i6%2FuIUvWr45RCcq2I9%2FagL%2BnLqgIgQCOtyCN%2B1uKqVnReQ4l%2B9zV83yavroqiaCfusk%2FXEaMqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFH%2B4a6QQtsKcfPCIircAz769%2BXTZA3ro45zg9kcnmigFxyMSqhL1eiILRlKX%2BGeOTpQRDPPxLVc0XgYmqBllQPdnY05VGNweXE3jMmyBKjPfNPeLnbWnp1ePrvEaj6OhAmYAQKMQRUW61A3NX9Yi4w7QjVnT07KVDGxUV%2FLXdqUPEUyi3VNDkZosgQLQoBBoA%2BX2%2BxI9arkpVupoS4jY6uQy%2Bi%2FJvmEfG7LwEMxHqwVRBXrliYKjF%2Bzy9eflVSUHXbYxsMO56hYwM9kAzsDNfEusXj1RJyKd2RUGoiBAjxOngNQLv0NsWCCMRPzpmy0XWfpqo57czDI7ajNHsh%2FQx0f%2FlZE4hlHcf%2B%2BDqfXMr%2F56Sf3x2et19fJsJu8dRgbgSpIVQ2d4udDII%2FL2rQqcKHtXG0wwvS1%2B85yL6NITXRHsuh256vK450ACJskvGY5shnH7xFLnMni1MOTdkXNnmqEtrYqnnlBDgwbkJFFPLW0%2F7MppOt3vDu7TARh%2FYC14Eq6Jn7X96vYcckjg%2BhALTf7FBS9%2FbIGlJI7fBMpElShuGum%2BKr02vRWUF1f72eONFHK9k6%2ByYVRtkftcnIdKd%2F8iNYG3M9FKvAsA43Q%2BZGVhT73D4kvMt1i8r6uI87pwY1M87MiwN63JWrnMJi9hs8GOqUBERovqFYV1qZFCMnJRXeVSKPPN8CaHuwevNRWGgUrpFIfvqs3HDG0ZeVF3OKXbUikyLtu340E5c5ZDaBNaz1TFsplQqj7QKw6FmGQvQ0sxyO2A6dyz%2B6VEih13BAScbTbVVcSi3O7LuveUgSMTSH9xPClyQLYgMpz6FJdZk654mm5vcC1hH%2F9TZ9FMDgQvGlBZFrm8G%2BhPap2SY%2Bmu5VhPTpu%2F5JZ&X-Amz-Signature=1603217ed8e9f9b690b73e29c4078b2e6d47c239e17e159b7e99505216ddb5f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ILNUWC2%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDRjD029N%2Fx7nzX033i6%2FuIUvWr45RCcq2I9%2FagL%2BnLqgIgQCOtyCN%2B1uKqVnReQ4l%2B9zV83yavroqiaCfusk%2FXEaMqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFH%2B4a6QQtsKcfPCIircAz769%2BXTZA3ro45zg9kcnmigFxyMSqhL1eiILRlKX%2BGeOTpQRDPPxLVc0XgYmqBllQPdnY05VGNweXE3jMmyBKjPfNPeLnbWnp1ePrvEaj6OhAmYAQKMQRUW61A3NX9Yi4w7QjVnT07KVDGxUV%2FLXdqUPEUyi3VNDkZosgQLQoBBoA%2BX2%2BxI9arkpVupoS4jY6uQy%2Bi%2FJvmEfG7LwEMxHqwVRBXrliYKjF%2Bzy9eflVSUHXbYxsMO56hYwM9kAzsDNfEusXj1RJyKd2RUGoiBAjxOngNQLv0NsWCCMRPzpmy0XWfpqo57czDI7ajNHsh%2FQx0f%2FlZE4hlHcf%2B%2BDqfXMr%2F56Sf3x2et19fJsJu8dRgbgSpIVQ2d4udDII%2FL2rQqcKHtXG0wwvS1%2B85yL6NITXRHsuh256vK450ACJskvGY5shnH7xFLnMni1MOTdkXNnmqEtrYqnnlBDgwbkJFFPLW0%2F7MppOt3vDu7TARh%2FYC14Eq6Jn7X96vYcckjg%2BhALTf7FBS9%2FbIGlJI7fBMpElShuGum%2BKr02vRWUF1f72eONFHK9k6%2ByYVRtkftcnIdKd%2F8iNYG3M9FKvAsA43Q%2BZGVhT73D4kvMt1i8r6uI87pwY1M87MiwN63JWrnMJi9hs8GOqUBERovqFYV1qZFCMnJRXeVSKPPN8CaHuwevNRWGgUrpFIfvqs3HDG0ZeVF3OKXbUikyLtu340E5c5ZDaBNaz1TFsplQqj7QKw6FmGQvQ0sxyO2A6dyz%2B6VEih13BAScbTbVVcSi3O7LuveUgSMTSH9xPClyQLYgMpz6FJdZk654mm5vcC1hH%2F9TZ9FMDgQvGlBZFrm8G%2BhPap2SY%2Bmu5VhPTpu%2F5JZ&X-Amz-Signature=8ce5ae17d6aad9526a62d3be9217a5eac340cd8c09ca5dcb5cc1d16995dec39c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


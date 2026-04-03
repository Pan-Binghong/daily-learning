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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LCTCAWM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4tlsNGNsgju2zRPlDiaAxyIYVTBtFvqzwHLU9x5gnzAIgFzyu7NdqvFWr1I3DGmLqV%2B9FtSJGQDBNVCVS7msHMxEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDL8apzRT8uZXvV5OsCrcA8MJO2RfQc7psV6VuD0FmmAWyrzDhOhc7GTzQS7Cv%2FXvR7IP8hzyJnLWG%2FFhGsER8mikNnOTT7NQKMLZncWrVWhn1TOasV9kPyQMP%2F3QmxDTi2VgvgZRdWJEYO33eczn3yGzokY8zIj8yVgSYnYUcDHXk3ViyWIdC6RY6PUq84ViXbUk4XpPItStUuiIR4sQWx0eaSxmQuRQTBnw4AXCdQhSp3TDSPGineVAQzWgP6MnGdmTJxhgn3%2FEMjV7hVrf9RORXcM%2BqoyNGk9hKS7tZ6YkVDZqimNPeMsrT65JcU3YkSk%2BObbKt15UaqE%2BA9QgV%2F1dPtEpz5TJwaBdb6HoHdZ7uf11j1elfe1vF04Xne30a%2FBJWgaRsIzjfSp0%2FHahC81ie1saVNW5qHNYp1%2B3zAy9Fki%2Bl67yrbgJsrTayagoEc8rHRKzo7us%2BxsTrYcr9SEpmCbUmCXrfK%2BFWU9aV5MURduCwO%2BYKIh3h3ltSy5zQMDIkjP2ex%2BcpccxDQ%2Flvp%2B17im%2FDA2foj1%2FNOKPIJAgmdGUb3ycNIVuN7xZCbufxUCQMJOSLZ46Vraadn4YWm9MLoUnmfbqzjamMmzi%2FsRjiI57cXW30594zF10CA5yBWeJN7jOC1aUotnmMKavvc4GOqUBEC9y4U4NKg6XjmSB1DojxnDu1L3vdqTZIIJjil3NVQ0asUUL6MXuylh45usolgQ1ZBoJAEa854Ty97xGYN0UItNBbfiLwjXK3dB3SX%2Bj44FeMdX18UqkPlGLHrTQHc%2BrDgcE%2BuYtK6qaobrEAeVU8CuhZv7vst84LBBYXlqpQ5oPpETF5ITdV7B%2FLat9AV1sCIlqsZ9oCZWn6noWTq9dkT3Vj8J5&X-Amz-Signature=49313529d222ecca027a644299859b07d4ff49d1834a7198d3059a8c65182d17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LCTCAWM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4tlsNGNsgju2zRPlDiaAxyIYVTBtFvqzwHLU9x5gnzAIgFzyu7NdqvFWr1I3DGmLqV%2B9FtSJGQDBNVCVS7msHMxEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDL8apzRT8uZXvV5OsCrcA8MJO2RfQc7psV6VuD0FmmAWyrzDhOhc7GTzQS7Cv%2FXvR7IP8hzyJnLWG%2FFhGsER8mikNnOTT7NQKMLZncWrVWhn1TOasV9kPyQMP%2F3QmxDTi2VgvgZRdWJEYO33eczn3yGzokY8zIj8yVgSYnYUcDHXk3ViyWIdC6RY6PUq84ViXbUk4XpPItStUuiIR4sQWx0eaSxmQuRQTBnw4AXCdQhSp3TDSPGineVAQzWgP6MnGdmTJxhgn3%2FEMjV7hVrf9RORXcM%2BqoyNGk9hKS7tZ6YkVDZqimNPeMsrT65JcU3YkSk%2BObbKt15UaqE%2BA9QgV%2F1dPtEpz5TJwaBdb6HoHdZ7uf11j1elfe1vF04Xne30a%2FBJWgaRsIzjfSp0%2FHahC81ie1saVNW5qHNYp1%2B3zAy9Fki%2Bl67yrbgJsrTayagoEc8rHRKzo7us%2BxsTrYcr9SEpmCbUmCXrfK%2BFWU9aV5MURduCwO%2BYKIh3h3ltSy5zQMDIkjP2ex%2BcpccxDQ%2Flvp%2B17im%2FDA2foj1%2FNOKPIJAgmdGUb3ycNIVuN7xZCbufxUCQMJOSLZ46Vraadn4YWm9MLoUnmfbqzjamMmzi%2FsRjiI57cXW30594zF10CA5yBWeJN7jOC1aUotnmMKavvc4GOqUBEC9y4U4NKg6XjmSB1DojxnDu1L3vdqTZIIJjil3NVQ0asUUL6MXuylh45usolgQ1ZBoJAEa854Ty97xGYN0UItNBbfiLwjXK3dB3SX%2Bj44FeMdX18UqkPlGLHrTQHc%2BrDgcE%2BuYtK6qaobrEAeVU8CuhZv7vst84LBBYXlqpQ5oPpETF5ITdV7B%2FLat9AV1sCIlqsZ9oCZWn6noWTq9dkT3Vj8J5&X-Amz-Signature=fb582f0a0edd6eff9094f80266c492f09a46f4276de51e2a273661ae84902125&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


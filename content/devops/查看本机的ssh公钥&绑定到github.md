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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMAMR45N%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9ru7MvGPWdZ%2FEgZypSognryc0xKlS%2BVD0u%2B275xB%2F8wIhAKegDYMQKLVdVBtLG%2FVhdY4Ckv8AXYAG7td6eTkQK%2B3zKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fm2%2BJ1E%2FVDyA0unwq3APGZWafctVS7rT7re9YdkfxK7BZ0X3ZFovuJVwPmLbT7r%2FYTZcwskUvBuMV6tFsGsHg04G24bs%2FQKhYf50UG5usMg3QUrffeEw%2F46TPVSUFSnerDHuEmbSGG5BoyYxeynLzi7JAdoKeWND0hK37XxYh%2BlhK3zOFmxkaGnI9%2FWGx2lIstEYGEP6qZ3Ch7XhBC1SlnzM2YtPR14Iui3EYH2X4PtnwsICcjU5nTZITKvjDslgYRLRpv8gnQSq6ghQt04XRPWNVMVLSgjvtxFaG%2B5%2FADXDgQNMGqgkvCSzE5ezPCEPPc2RA1M%2BA5nxNbttTX%2FWI%2BkZsU6Q8u7DhY8DcTBUjRUpzUpjvXQAgOR2PSWPZIwQ05eJY7vwrmbHdobcrcZ%2BxKLjX%2B%2BV4EeOYOB8Q9ywQQq657KE4EPEDz6vIyiRdJD%2FUui3bQm2kSDW617%2BWXsvqSjCBetKmiMu2YuC4NQ699qE08GQdnkx%2BmKwpAWguf6m4imD5nh0EOjeNl5vmIvUPBBJMwHa4YLPe1kRTy%2B0SDtKRBDqmlq92Jlh69VA4SY24k2t9EfaKiDteMQnJ5wl0b6k6j8vlIU782ZiWC71uaInXWn7JVgqiyC2BXtL6i5IxDNIS4rPWpyR51TCb1o7OBjqkAQxQcqRuZatnlUnZ6lWSqanaz1Q%2B9zKcNl17RaFS%2F32qSuLNawBgQZCs0d2SXvDyf44Q2U%2Bdtd3Ih21NHRPPERLS%2BwXgjXJlnK49%2FUwtW79pdn1tGEEMKZXEQWgMStVfYKyxYDDm2AjJE3AyeI5EbVrrAGLX1WJKxskDqZxXudns5GWkgUjds29L1ilD7UgZvphCHtSEydEkuiNGRo55RQPmb36M&X-Amz-Signature=b1a3504c0fc85046b1b17017fa5f8ab38f6b481b4e160a98ec8e2d5d0e3f4bbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMAMR45N%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9ru7MvGPWdZ%2FEgZypSognryc0xKlS%2BVD0u%2B275xB%2F8wIhAKegDYMQKLVdVBtLG%2FVhdY4Ckv8AXYAG7td6eTkQK%2B3zKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fm2%2BJ1E%2FVDyA0unwq3APGZWafctVS7rT7re9YdkfxK7BZ0X3ZFovuJVwPmLbT7r%2FYTZcwskUvBuMV6tFsGsHg04G24bs%2FQKhYf50UG5usMg3QUrffeEw%2F46TPVSUFSnerDHuEmbSGG5BoyYxeynLzi7JAdoKeWND0hK37XxYh%2BlhK3zOFmxkaGnI9%2FWGx2lIstEYGEP6qZ3Ch7XhBC1SlnzM2YtPR14Iui3EYH2X4PtnwsICcjU5nTZITKvjDslgYRLRpv8gnQSq6ghQt04XRPWNVMVLSgjvtxFaG%2B5%2FADXDgQNMGqgkvCSzE5ezPCEPPc2RA1M%2BA5nxNbttTX%2FWI%2BkZsU6Q8u7DhY8DcTBUjRUpzUpjvXQAgOR2PSWPZIwQ05eJY7vwrmbHdobcrcZ%2BxKLjX%2B%2BV4EeOYOB8Q9ywQQq657KE4EPEDz6vIyiRdJD%2FUui3bQm2kSDW617%2BWXsvqSjCBetKmiMu2YuC4NQ699qE08GQdnkx%2BmKwpAWguf6m4imD5nh0EOjeNl5vmIvUPBBJMwHa4YLPe1kRTy%2B0SDtKRBDqmlq92Jlh69VA4SY24k2t9EfaKiDteMQnJ5wl0b6k6j8vlIU782ZiWC71uaInXWn7JVgqiyC2BXtL6i5IxDNIS4rPWpyR51TCb1o7OBjqkAQxQcqRuZatnlUnZ6lWSqanaz1Q%2B9zKcNl17RaFS%2F32qSuLNawBgQZCs0d2SXvDyf44Q2U%2Bdtd3Ih21NHRPPERLS%2BwXgjXJlnK49%2FUwtW79pdn1tGEEMKZXEQWgMStVfYKyxYDDm2AjJE3AyeI5EbVrrAGLX1WJKxskDqZxXudns5GWkgUjds29L1ilD7UgZvphCHtSEydEkuiNGRo55RQPmb36M&X-Amz-Signature=be036091cd54a054293578e4db6c1fa4a9ccee82e2e4fd3d18dc1d0dab7f82ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


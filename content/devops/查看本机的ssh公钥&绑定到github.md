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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZHYJKTJ%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNOlfbtv13EXAts0CxiGm5apwA2feSCefgx4CglMPOXwIhANCO797L9ncw7gBDZwSDDkld9XtlbXrg3wwqGU3GEg%2FzKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1VyYwcePv158IAEIq3AM%2BZ0qDcye7Ge8XHlwMd1PKCwj0IdC9XNFVEBSl3FSCRPKMd2fkhSxhwXije08thVdLAthil1%2FRkOL1j3cKhD%2F1iAuNYHhPMwb1%2B5nB9%2BoQrSAr%2Br%2FQPb%2FfQROOtIYZe5GfehGmakzyx%2FRuWPnKELuE9sF38sjNNavrCv4383DFB%2FLczMsnU48fhsOqkjXvVll3CW7QVP9uBwNPHnYpBLxMJfKlABRXUJSS%2BNV4jZOem0fzUv%2FgBLJiPZJMNDsZdR4v62hUStCXmqSE4fAPhRtm9kzqnAsNI73UF0thpluof7%2FlKotlyeiJcbAlxlQuwpTFiclzY2LBXBTXhzWclFWSEZsUEMFyMzm5DzWqa3JszkV9vzlGk8JFYQLweMS0iI0QLzkHumdRyU9Iq9U%2FrNitDSd7OT%2F9IMnEDLz%2BFimw%2F4zkZegXljuO3Gik3RB8n96qnGIxC3%2BPz%2BE6tLj4YxHuab7MAGDu1AzEv%2B9NDA3BNB2pyEiYJs3gOVyEUbA4wPoafUeGdzAviGrMO6Sdqks67UWkjBRsypTTjDIuKDhPbOg%2BSqzhCtpnsYcyyE4Jtz4ak%2BLy61QIUNx4FJaDxzcsDnG1%2BO25Gcd%2FPY9TLCmmqu0UmwzEY8S22G3EyzDe3vbOBjqkAdsLwDyEkVyIEp6QBsNmiKAIa27GYLyRVue8HwQXv5hmHudRal0%2FDhb4sUr238G%2FyOpbmUOd6zLSOrb%2F0c8jnhxGRsW%2FYL7%2FvUynmoVEeI0PEKFuTsFcaobEPPYUwXXiK3ryfhvQ7IU70kk3Ng3vM8pxlJ8c2J3My%2FpW7Hqm9lW%2FB50hMWLu0EYco9ZYxFk%2F2DtrYLu6KnJEIP5%2BtXnIJhk9xQvJ&X-Amz-Signature=e4e1a8ac1852cf4a970bd0af82500a2397c43e2ec0311ed4f3c7ecf5d870ee9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZHYJKTJ%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNOlfbtv13EXAts0CxiGm5apwA2feSCefgx4CglMPOXwIhANCO797L9ncw7gBDZwSDDkld9XtlbXrg3wwqGU3GEg%2FzKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1VyYwcePv158IAEIq3AM%2BZ0qDcye7Ge8XHlwMd1PKCwj0IdC9XNFVEBSl3FSCRPKMd2fkhSxhwXije08thVdLAthil1%2FRkOL1j3cKhD%2F1iAuNYHhPMwb1%2B5nB9%2BoQrSAr%2Br%2FQPb%2FfQROOtIYZe5GfehGmakzyx%2FRuWPnKELuE9sF38sjNNavrCv4383DFB%2FLczMsnU48fhsOqkjXvVll3CW7QVP9uBwNPHnYpBLxMJfKlABRXUJSS%2BNV4jZOem0fzUv%2FgBLJiPZJMNDsZdR4v62hUStCXmqSE4fAPhRtm9kzqnAsNI73UF0thpluof7%2FlKotlyeiJcbAlxlQuwpTFiclzY2LBXBTXhzWclFWSEZsUEMFyMzm5DzWqa3JszkV9vzlGk8JFYQLweMS0iI0QLzkHumdRyU9Iq9U%2FrNitDSd7OT%2F9IMnEDLz%2BFimw%2F4zkZegXljuO3Gik3RB8n96qnGIxC3%2BPz%2BE6tLj4YxHuab7MAGDu1AzEv%2B9NDA3BNB2pyEiYJs3gOVyEUbA4wPoafUeGdzAviGrMO6Sdqks67UWkjBRsypTTjDIuKDhPbOg%2BSqzhCtpnsYcyyE4Jtz4ak%2BLy61QIUNx4FJaDxzcsDnG1%2BO25Gcd%2FPY9TLCmmqu0UmwzEY8S22G3EyzDe3vbOBjqkAdsLwDyEkVyIEp6QBsNmiKAIa27GYLyRVue8HwQXv5hmHudRal0%2FDhb4sUr238G%2FyOpbmUOd6zLSOrb%2F0c8jnhxGRsW%2FYL7%2FvUynmoVEeI0PEKFuTsFcaobEPPYUwXXiK3ryfhvQ7IU70kk3Ng3vM8pxlJ8c2J3My%2FpW7Hqm9lW%2FB50hMWLu0EYco9ZYxFk%2F2DtrYLu6KnJEIP5%2BtXnIJhk9xQvJ&X-Amz-Signature=3ce9702f14b1ac8cbba6f20fbd4853e8284f06c122775387b18a5e4f0d2af428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


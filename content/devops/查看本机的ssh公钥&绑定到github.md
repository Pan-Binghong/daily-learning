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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVFGIHO%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCqdEkr17HxkfWHbEjid2Z%2B6dckOlSK2SZ56fwv2MTUAiABJyjdPV0iWKrDGnbCjmRA0BqiGSzL3v7ThxqjQsXpGyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMmSpOSpJiyblwuI0PKtwDl42FZFHLcQNN9Bukca51zeCIiUyloVR0AOn6hhLnEfyVJjZ9aKyYKgp17wo42HWbtfRU6MXmlR77GqBSE1v5VqLqoequeWRfu0WiIa4Y1tf7rLcYnJO87EVvMevB%2FYIW2kSDy8xvkI%2FedPe6ntfHvTx1U93RXEKBytY6bkstJZAdDVFFStWxi6Qq8BKEJiPb4Cd2DAUD%2BAw9zAi0J254Ml8rLd3Wq6F17XFYOq0098TzE0lzSGRKDYhQsw1YrXC3YXiVaXFpP%2ByeToCvOPq9wR17IVvvMP1l2jaHi6pXUgrnKibw2cmD6p%2BVyt52Poch0qNALffBAGnp5D2kmOaYm0qgP%2FPEAGS%2FWFrAPXqHuVgU%2BO3evSRik5V%2BpQiqUYn8oeUik1wmgRy4KMthbCB6uC6n1Z24P8EffgH1inIbcVsMS9sw%2BHPAPfsMcoOuySsjMEXAouAt1Bswz%2BPWapRiH9Kv%2B1pa%2FU3y7uCO92xBLexsVdq5ufvlsUkstFN5u2UYQFDDcRsjAQ0oqUUS05aR5ZmtgQGNodio8xtXMgTEshclILZSZH34unhGq3zBfWGoiGG5Rzq87juMcOhXZVlyG8f0yg2Kif28CxD6nrfGrNL%2BP0PMowipuoDrZCowzLLxzgY6pgEbO43mEMikPXTLuYai17r59MDSGpXXFmFH6A0OXpt9xEsGF7Kghmn02oUJ%2FBxt0ksXIqMAjGIzQi3eRkeSjpJwukeJo3Pm53d3qSIHSLnO%2F4nmpzRfi9aLoEW5JL8qQFMhBFBRB4LM6UAGYZja%2F6gFNNzH0j0o%2BwMZJk9XEFjd32FWc7eBBaGpCsCv9mUEja2lpXFVIoC4fthSEL962gQYaTLQ%2B7wk&X-Amz-Signature=fd446ec36a2119938c4676deb08a36c33344df85e5407329d20af6c245af57e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVVFGIHO%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCqdEkr17HxkfWHbEjid2Z%2B6dckOlSK2SZ56fwv2MTUAiABJyjdPV0iWKrDGnbCjmRA0BqiGSzL3v7ThxqjQsXpGyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMmSpOSpJiyblwuI0PKtwDl42FZFHLcQNN9Bukca51zeCIiUyloVR0AOn6hhLnEfyVJjZ9aKyYKgp17wo42HWbtfRU6MXmlR77GqBSE1v5VqLqoequeWRfu0WiIa4Y1tf7rLcYnJO87EVvMevB%2FYIW2kSDy8xvkI%2FedPe6ntfHvTx1U93RXEKBytY6bkstJZAdDVFFStWxi6Qq8BKEJiPb4Cd2DAUD%2BAw9zAi0J254Ml8rLd3Wq6F17XFYOq0098TzE0lzSGRKDYhQsw1YrXC3YXiVaXFpP%2ByeToCvOPq9wR17IVvvMP1l2jaHi6pXUgrnKibw2cmD6p%2BVyt52Poch0qNALffBAGnp5D2kmOaYm0qgP%2FPEAGS%2FWFrAPXqHuVgU%2BO3evSRik5V%2BpQiqUYn8oeUik1wmgRy4KMthbCB6uC6n1Z24P8EffgH1inIbcVsMS9sw%2BHPAPfsMcoOuySsjMEXAouAt1Bswz%2BPWapRiH9Kv%2B1pa%2FU3y7uCO92xBLexsVdq5ufvlsUkstFN5u2UYQFDDcRsjAQ0oqUUS05aR5ZmtgQGNodio8xtXMgTEshclILZSZH34unhGq3zBfWGoiGG5Rzq87juMcOhXZVlyG8f0yg2Kif28CxD6nrfGrNL%2BP0PMowipuoDrZCowzLLxzgY6pgEbO43mEMikPXTLuYai17r59MDSGpXXFmFH6A0OXpt9xEsGF7Kghmn02oUJ%2FBxt0ksXIqMAjGIzQi3eRkeSjpJwukeJo3Pm53d3qSIHSLnO%2F4nmpzRfi9aLoEW5JL8qQFMhBFBRB4LM6UAGYZja%2F6gFNNzH0j0o%2BwMZJk9XEFjd32FWc7eBBaGpCsCv9mUEja2lpXFVIoC4fthSEL962gQYaTLQ%2B7wk&X-Amz-Signature=cfd18e9143d2e136b66da25ad943e26f1ffb8cfbb4794ef8a5b0c0e5a774266c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZPHJDWE%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDf%2Fc%2BxYDQPZChuW6ncRyUIYNlH6QCKxqXiXOUo3HHN8QIgGnl%2F%2F%2BmPLIsDjcMdm9x8jQwXRoPgtykWIu6TiGI%2BjiUqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG0tAL3kZzZABR2VMircA8m%2BwdHTkPHChgo3HNAbiniFFYqtz6PmxOYqC53WkZjqTawv0KfyVDdUK5tNkikbFVT2ZnX0hxk92UocKmWrdPBN0PU7Xt5RChZS5cYjveKI5cm51%2Bb24ALWdIKt1%2Brq2sRB6o6sG87anQElq72Ta1VbuXZzu%2BeojmgPl8Sfyr20cshcv4yi6O849ckgkCrXwjyMYLpfx0mwQsF%2Fd%2BdryoDhK4OBca4%2Bb%2FvtyFjpZEZVWH4afp5ghpu0dKCz4QXLovx8AnvfT5m7Q1e6KehL9dJrIu71jG7L%2FUHe01Uws2j%2BmTd3Ud%2BO2kO1DzrnA7wEk4Eg65%2FF%2BH9qO66w8zIHkiHA0kZDGv7OqPU5fa%2BJEpm3ooJSzVtjy6yllqhZ6R9TBYGM78VgMAuKs4K4jTwix%2FREsBp3rzwYnxQcbTFSZkPIaJLBhX5CaCEtGKBejsBtDSvF0MEPKM1yRISTMrxnz7YMH4j%2B8a5eFNBUCBXJjtsGHBPRNLgCBMJmYblLmPuS4lAh620oD%2BdSTBZql6QVAcTsHc%2Bl8CSLwjFuKm59fg3%2F4QmFUWt86navIg5vozhBQhlfDk4AdNtDgzU6iFP%2BB3A5V1f5hoXE6jbyyGOO2UC3HP9QNUKBSREQ95nWMJG1u88GOqUBQ43NmejkUkUrBNxZg6n9uAJZvhutLL6%2BLpnnrLXFKAdl%2FoHs1jt2Qxmynnhthg%2FE7d6EkHCMEOr6RgGqvHgWKVzewIhgoNcNNDoYLPFV6gyd3JETEo%2BgHLpQ4cLohYfalLfIFTMMqfGB8hzEN0moJAC%2FlYSKgICtyndEFCwgpKplQCvW8spLgZJmW3PjjDPhcfDkVk%2FNPxU9UwSCIxnyzgbL0L6F&X-Amz-Signature=42f0f1f600a42b3bfbc92c96d79198b49dca21b6ec7b90cbe4a080a6a0267919&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZPHJDWE%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDf%2Fc%2BxYDQPZChuW6ncRyUIYNlH6QCKxqXiXOUo3HHN8QIgGnl%2F%2F%2BmPLIsDjcMdm9x8jQwXRoPgtykWIu6TiGI%2BjiUqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG0tAL3kZzZABR2VMircA8m%2BwdHTkPHChgo3HNAbiniFFYqtz6PmxOYqC53WkZjqTawv0KfyVDdUK5tNkikbFVT2ZnX0hxk92UocKmWrdPBN0PU7Xt5RChZS5cYjveKI5cm51%2Bb24ALWdIKt1%2Brq2sRB6o6sG87anQElq72Ta1VbuXZzu%2BeojmgPl8Sfyr20cshcv4yi6O849ckgkCrXwjyMYLpfx0mwQsF%2Fd%2BdryoDhK4OBca4%2Bb%2FvtyFjpZEZVWH4afp5ghpu0dKCz4QXLovx8AnvfT5m7Q1e6KehL9dJrIu71jG7L%2FUHe01Uws2j%2BmTd3Ud%2BO2kO1DzrnA7wEk4Eg65%2FF%2BH9qO66w8zIHkiHA0kZDGv7OqPU5fa%2BJEpm3ooJSzVtjy6yllqhZ6R9TBYGM78VgMAuKs4K4jTwix%2FREsBp3rzwYnxQcbTFSZkPIaJLBhX5CaCEtGKBejsBtDSvF0MEPKM1yRISTMrxnz7YMH4j%2B8a5eFNBUCBXJjtsGHBPRNLgCBMJmYblLmPuS4lAh620oD%2BdSTBZql6QVAcTsHc%2Bl8CSLwjFuKm59fg3%2F4QmFUWt86navIg5vozhBQhlfDk4AdNtDgzU6iFP%2BB3A5V1f5hoXE6jbyyGOO2UC3HP9QNUKBSREQ95nWMJG1u88GOqUBQ43NmejkUkUrBNxZg6n9uAJZvhutLL6%2BLpnnrLXFKAdl%2FoHs1jt2Qxmynnhthg%2FE7d6EkHCMEOr6RgGqvHgWKVzewIhgoNcNNDoYLPFV6gyd3JETEo%2BgHLpQ4cLohYfalLfIFTMMqfGB8hzEN0moJAC%2FlYSKgICtyndEFCwgpKplQCvW8spLgZJmW3PjjDPhcfDkVk%2FNPxU9UwSCIxnyzgbL0L6F&X-Amz-Signature=4420e014529f2dc8d95e7e32f86544e41cd7e8a80d6e5c9a658bafaafab0efbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVHSECF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhrlg%2FFTcI8eQKuG3mktLJ533aOirFbfxbmK2aO8tBXAiEAwPxyBIUnKOei2UUMioahVPg2LfHdk33VlBnQed4lbhgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDG6akQHTkGE1e%2FsUWCrcAxVywjZLbxBA7o%2FJ06bRl%2F0fmPQw4CkrHiMWJNQNpLf0cOooZisw4zys%2FGa5G2fgQZBhP42%2BX3QCArERHj1bLNnLIXCskpKRsvxSOMWUZs1dMxg9LpuLepxj5AGOcqG1Gy%2FaHacxtGPXe7wvV2kj43KDy%2BzQDoxbhJShOHvCj%2FjXK0Zs7JRPZ%2B33NCRqyS7KlKaGKj9efc%2Fwws7gt9GIKXfYDaQKsnMC9YmKxWeqpKlgwtQxlNaY85I3Nga3qcuy2O54dpiwwz2hVz6JVTgORD6h3bCCKgU0MOdAu5LQ4DkhQ0r%2FQOot0cNxdV3wIc9FmJS7v0AI98eyjZAwImERa%2BghTQrf6NMDZKgc57W1CsZGn6wtdgOHDEVVquqeq0ReGthhtBNMrDYYgmcsjIJvds5F6OPkzoYC3Gc7cn6vXYY88Ge6Fv6WB7O8C3TVAWnlk28I%2BGtlR0tGFafwaWxlt6f%2BOFfbiTjqlMRkhCkGwWpUW1ZiTa8vY2Z73ZRQQVN8%2FiugYoTCtiWRddU2fzRyBIM4FrlXp4uW4W7zSpn2awiU%2FCZ0Ha7ytuLkgD8eFIf%2Fol16KUl8brn1s9Af0gfCvknJeZgzwpLUGA1kY1Pfx9YC1qe4qircThGaQpO%2BMNurvc4GOqUBw70pnbNFzFYacpQyki1DjbYWXhNrLT1btm0ov6%2BfNtEhcHDKd0n%2Be8TyrABkY8Dl2eAjRuhmQhRhZL%2Fh%2FmHjB0k1SKRCLPwUk2oSqXNo0Er8kElEkqI5UaZx%2BrYmmsMdzvNf1DzKWjnBrlkbq0lSB3O96rUT7OmvDEBeVsyFeqEQHK0KCN%2FUBLGTioGWnTNbldzJwUO151OzrvvIgop4Mm8sozlP&X-Amz-Signature=37b6d010d794aa9588aefb163c0948c38c3006ec054ff36e9e8b0f8760ab0fb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVHSECF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhrlg%2FFTcI8eQKuG3mktLJ533aOirFbfxbmK2aO8tBXAiEAwPxyBIUnKOei2UUMioahVPg2LfHdk33VlBnQed4lbhgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDG6akQHTkGE1e%2FsUWCrcAxVywjZLbxBA7o%2FJ06bRl%2F0fmPQw4CkrHiMWJNQNpLf0cOooZisw4zys%2FGa5G2fgQZBhP42%2BX3QCArERHj1bLNnLIXCskpKRsvxSOMWUZs1dMxg9LpuLepxj5AGOcqG1Gy%2FaHacxtGPXe7wvV2kj43KDy%2BzQDoxbhJShOHvCj%2FjXK0Zs7JRPZ%2B33NCRqyS7KlKaGKj9efc%2Fwws7gt9GIKXfYDaQKsnMC9YmKxWeqpKlgwtQxlNaY85I3Nga3qcuy2O54dpiwwz2hVz6JVTgORD6h3bCCKgU0MOdAu5LQ4DkhQ0r%2FQOot0cNxdV3wIc9FmJS7v0AI98eyjZAwImERa%2BghTQrf6NMDZKgc57W1CsZGn6wtdgOHDEVVquqeq0ReGthhtBNMrDYYgmcsjIJvds5F6OPkzoYC3Gc7cn6vXYY88Ge6Fv6WB7O8C3TVAWnlk28I%2BGtlR0tGFafwaWxlt6f%2BOFfbiTjqlMRkhCkGwWpUW1ZiTa8vY2Z73ZRQQVN8%2FiugYoTCtiWRddU2fzRyBIM4FrlXp4uW4W7zSpn2awiU%2FCZ0Ha7ytuLkgD8eFIf%2Fol16KUl8brn1s9Af0gfCvknJeZgzwpLUGA1kY1Pfx9YC1qe4qircThGaQpO%2BMNurvc4GOqUBw70pnbNFzFYacpQyki1DjbYWXhNrLT1btm0ov6%2BfNtEhcHDKd0n%2Be8TyrABkY8Dl2eAjRuhmQhRhZL%2Fh%2FmHjB0k1SKRCLPwUk2oSqXNo0Er8kElEkqI5UaZx%2BrYmmsMdzvNf1DzKWjnBrlkbq0lSB3O96rUT7OmvDEBeVsyFeqEQHK0KCN%2FUBLGTioGWnTNbldzJwUO151OzrvvIgop4Mm8sozlP&X-Amz-Signature=8fca0cc70b38ffcdbe31744faca3cb0ba502ff5696b8665383cc46a1a650a072&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


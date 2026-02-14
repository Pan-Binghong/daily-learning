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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466526ZHUAG%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICv9SsD97S0EPbEDDoY%2BvL13DSO5CwYMDEyGWHZiUc%2FZAiBtuzYE6C3pxdaM49UXA6SOmLwuWTyiZabgu8EkWUxrOiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZzbQ1ak2rhFxUvpbKtwDQTh3Ol9%2ByW8vW%2BMHAPTySQXUsKmIuIhEPMbgWb%2F1C2oAz4k6753JeEKbkpO74Faj0jo%2FGbLw5gqB2Jjd%2F%2BYZRuJbhzQdG0O%2FfJGg4sFT18hkTk4BQiunzfoC7pTuEEsifNV4jVnKotHuRoinVJLIB8S9ywAa%2BV5z9zPz8fpv9uzvlF4GjGjjZYxyqIdeyySAwdXAWgh%2BMr3GriLih5RW8xDLWnWkMidi7xMUi9vejqRGdFHap9LbHlLNgQZsM3VPuVJuFMPjdabppskUyhhgY1JKZb8Riwn1XG2Ryy%2F9wQhVkNj59GMnzryZchzLj0YiboH2EoGb2pi2%2BRBAfZxvKsY%2BGOhvUKPwlonEaXTFl3EGqhxz3OWiEOFF2JdgK0wMLOiOzvUXUkJmAdamKTIHMMckNIddbUcSRPzCtBmXQxb4sktisz5x91ng%2B7T6wyvwufuSx%2FjY5EOgOIIuqzvA%2FvfKnQl%2Bp%2FEUEUaeSCg%2BjrgP7sUgqnF%2FQKS87BrU%2F0MYO%2BGBIq0JWz8leg%2BGy%2FL5DDqjeIvvFW8%2Frqb5Suq6C4%2FRywQ8hVS6%2BkY%2Fq%2F9t3R7yPL7UsPfyBu208Wtq5hVTVP1OEzsSq%2B88aGdIaS0%2BiuD%2BYam4mN1sfa4KdvUw6sC%2FzAY6pgGyAg0ONQyntoym6tr402BTtvLqmsGeG9nuhOV0ZzZxUubx1%2F7BC%2F8dni6yiDXp2a8vGAzbqRhlRxQkSlyLhWG8wmhzd9gEy%2FkoyDFsk9gwq56DHSxxtYLdLHAUHxXRjN3gXths5m6MVmJxqz3twKGW0xwM9goBscv%2BoUeMaXivqvnkJxPxz3v7rL0w7wNvQ13OMNd5UPA9Wf9W36BqCNSgObfsBOPv&X-Amz-Signature=bc652df861ed26923cae53666d55d809d94771f37d83b998794e5bac2081c9c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466526ZHUAG%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICv9SsD97S0EPbEDDoY%2BvL13DSO5CwYMDEyGWHZiUc%2FZAiBtuzYE6C3pxdaM49UXA6SOmLwuWTyiZabgu8EkWUxrOiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZzbQ1ak2rhFxUvpbKtwDQTh3Ol9%2ByW8vW%2BMHAPTySQXUsKmIuIhEPMbgWb%2F1C2oAz4k6753JeEKbkpO74Faj0jo%2FGbLw5gqB2Jjd%2F%2BYZRuJbhzQdG0O%2FfJGg4sFT18hkTk4BQiunzfoC7pTuEEsifNV4jVnKotHuRoinVJLIB8S9ywAa%2BV5z9zPz8fpv9uzvlF4GjGjjZYxyqIdeyySAwdXAWgh%2BMr3GriLih5RW8xDLWnWkMidi7xMUi9vejqRGdFHap9LbHlLNgQZsM3VPuVJuFMPjdabppskUyhhgY1JKZb8Riwn1XG2Ryy%2F9wQhVkNj59GMnzryZchzLj0YiboH2EoGb2pi2%2BRBAfZxvKsY%2BGOhvUKPwlonEaXTFl3EGqhxz3OWiEOFF2JdgK0wMLOiOzvUXUkJmAdamKTIHMMckNIddbUcSRPzCtBmXQxb4sktisz5x91ng%2B7T6wyvwufuSx%2FjY5EOgOIIuqzvA%2FvfKnQl%2Bp%2FEUEUaeSCg%2BjrgP7sUgqnF%2FQKS87BrU%2F0MYO%2BGBIq0JWz8leg%2BGy%2FL5DDqjeIvvFW8%2Frqb5Suq6C4%2FRywQ8hVS6%2BkY%2Fq%2F9t3R7yPL7UsPfyBu208Wtq5hVTVP1OEzsSq%2B88aGdIaS0%2BiuD%2BYam4mN1sfa4KdvUw6sC%2FzAY6pgGyAg0ONQyntoym6tr402BTtvLqmsGeG9nuhOV0ZzZxUubx1%2F7BC%2F8dni6yiDXp2a8vGAzbqRhlRxQkSlyLhWG8wmhzd9gEy%2FkoyDFsk9gwq56DHSxxtYLdLHAUHxXRjN3gXths5m6MVmJxqz3twKGW0xwM9goBscv%2BoUeMaXivqvnkJxPxz3v7rL0w7wNvQ13OMNd5UPA9Wf9W36BqCNSgObfsBOPv&X-Amz-Signature=ecc171f86726b0b8eb636cfdf25fb648f982efb57b53eb948228c2e8d45b2090&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KDJNOEG%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBhJO4iBUi9ZtVsciLTUSaIFJbBNX%2Bl2jITQI%2FhNb4RtAiAbIFA027D%2BuzjwyGqlQk16VyimufuYLTCktRthlsdFcSqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM79FXQZ4b8acnZU%2FaKtwDhrwOz6zmd%2FcfHI6CIqTTpdeR5mVchyKm7AhVyqU6ZJ9lVoqvME04SwgxfW2rCmicWtp4KaxT%2FgflUcSNGheuGRSH7pmyhFTt%2FYb8gmk3rwMM9v3VByyuY68UUHoMbKCwOzZ2oK0GI3jhxErdVP%2BDYbd0OlteaHqHCH5D1YOzZfRqBuh7QaZPiBoa8D6HdOQBfBzO9pAbIRgV65cJwIVhR8z0NfC0GofSwa%2FSCJ9hI%2FdOzUf3EJSN7NmeZ%2BnrzMxQQPja39K72UQGK7I%2B85ngKRSmvYGpMUP1EbMuIAB6jMC9LCokrrMEf3qEyTrnDjnVlCD1uqIb96fYNQKdmQqfG8Fuh5qrKocAC5SX2yumN9piDFAZjyBqqj9Ave8tVEWe3tN9lSUq16N3TUYfxsEnM8Uq3tD5qxQeOBmGXToOkyqLAcYRUkfQuPdHrhtvvhgZy3khgw3gesZN8UHAl7xIS8VLZ8XJPcI0QWWRNxCxmKAi6cRNJ8gXq7ADUu05f%2FnC8DKqg4rWCNinRaubVs307et6S595QIYMHrbuJ%2FabdE8uKhCzVD5G6n4oGoaryrIySoZ6WY1PfYaJXnrUUeIiksf8a2RnrKLVPa92u7YpIQsQ%2BjdSb7DDxN3xaJ0wy5X8zgY6pgH5ptzzUdhniBf%2FqwyjCcAlB%2Bkh9VYS7DoKwCn80lo64bve2rx%2B0rGhwu5%2F7LL4yFCIMGEFe1O2702qDeHgly94088F%2BSjqRV7nEKgfugTBxxGQCm7Pq9SzdbVYwSYCY5P1RrTXNxlcd3HXpTakkeuDOVaVipR9cjgrnxVKRd8bARcLvOvcjMPKuOSfGi6R%2BeGonGPaz9AfAQseFuQcR1glOJIZRGbA&X-Amz-Signature=31fbee1c0f001cde7354384bff42d8a537b8ed682fd92a6cdfee7bf5754c1bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KDJNOEG%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBhJO4iBUi9ZtVsciLTUSaIFJbBNX%2Bl2jITQI%2FhNb4RtAiAbIFA027D%2BuzjwyGqlQk16VyimufuYLTCktRthlsdFcSqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM79FXQZ4b8acnZU%2FaKtwDhrwOz6zmd%2FcfHI6CIqTTpdeR5mVchyKm7AhVyqU6ZJ9lVoqvME04SwgxfW2rCmicWtp4KaxT%2FgflUcSNGheuGRSH7pmyhFTt%2FYb8gmk3rwMM9v3VByyuY68UUHoMbKCwOzZ2oK0GI3jhxErdVP%2BDYbd0OlteaHqHCH5D1YOzZfRqBuh7QaZPiBoa8D6HdOQBfBzO9pAbIRgV65cJwIVhR8z0NfC0GofSwa%2FSCJ9hI%2FdOzUf3EJSN7NmeZ%2BnrzMxQQPja39K72UQGK7I%2B85ngKRSmvYGpMUP1EbMuIAB6jMC9LCokrrMEf3qEyTrnDjnVlCD1uqIb96fYNQKdmQqfG8Fuh5qrKocAC5SX2yumN9piDFAZjyBqqj9Ave8tVEWe3tN9lSUq16N3TUYfxsEnM8Uq3tD5qxQeOBmGXToOkyqLAcYRUkfQuPdHrhtvvhgZy3khgw3gesZN8UHAl7xIS8VLZ8XJPcI0QWWRNxCxmKAi6cRNJ8gXq7ADUu05f%2FnC8DKqg4rWCNinRaubVs307et6S595QIYMHrbuJ%2FabdE8uKhCzVD5G6n4oGoaryrIySoZ6WY1PfYaJXnrUUeIiksf8a2RnrKLVPa92u7YpIQsQ%2BjdSb7DDxN3xaJ0wy5X8zgY6pgH5ptzzUdhniBf%2FqwyjCcAlB%2Bkh9VYS7DoKwCn80lo64bve2rx%2B0rGhwu5%2F7LL4yFCIMGEFe1O2702qDeHgly94088F%2BSjqRV7nEKgfugTBxxGQCm7Pq9SzdbVYwSYCY5P1RrTXNxlcd3HXpTakkeuDOVaVipR9cjgrnxVKRd8bARcLvOvcjMPKuOSfGi6R%2BeGonGPaz9AfAQseFuQcR1glOJIZRGbA&X-Amz-Signature=0cfd26b6267c6c2801b96a70d7913b444ae54555040ad9724f1690639c899fab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


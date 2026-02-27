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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HPV6CDN%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCe8%2FA3nVgPGUq0mCReekeiPaiJIsSvA6e5XnM2GMAvjwIhAKN1wOEs96JuAxjWuX9rVQ4%2Be03AjPDLDEYq3Gzzc5a8Kv8DCDQQABoMNjM3NDIzMTgzODA1Igw9nYoo7OfMlnGMQm8q3APVh5MC7lRHsowMeLAbBhq9568ti2jFJ9TxfW2IvQESKYetgeld%2BaFdnu1thUXnxRyycU47QxW7qDewXOIVY7a0Xqf4uNV1fZM7Rbb%2B%2BTw6wh6lhCD55HaLInfM24pnuxkmF%2BEYpxlqWg3yIcY5RuXMnqJbycyc3i44O98X5J7M7VquxgoL6PGNb9Niw2Y%2BQrdRBWyzWtL871YlVJhu5X9hHVIIDNirq2hopAzrIjLTBsFUKojMXpCcv3cACt29kxdUyhlIzW0ZoRvVhx8u91n8o%2FHgK37oU8dEeXT5RosDNVwo7bmtutAjSpDSun7jof06rze1Y106K%2BeJXzBxFGmU%2BESuioFHdRWqxlo2OOiPAdqI25O%2FqA0w5jgfbsK4s0UbG35J2DdKXQlEdF7RyiCXCXghAPz6WFuz7FJIteDPgsCzG0KKXt6W3TDxNj4ixgyQIIUU%2FqH%2BlCjG0Nru4khXtGVkQq1sphZNSF37mnji6Jbk4FWqrNaB2o3AMROACFyZqlvynsWO9O63CGOnFJ7ZM5v8NJdMJN5Wns1UU3xJ44Dt9MhpooBnfuXn22B3muH5B3z6tYlrVWtOVpqcE3wby5Rzp04Aq0neb5k3OVz%2Fz2FL3aAMrP%2BhARrz%2FDCkh4TNBjqkAQCR8z0mjUN%2BOuVfenSpLpa9DdopwFPZzc51RC8uzeZ%2BfrH3581Sj4NSeZ8DWznLyydTli3D8f8iYVAItiY6Hbc8HGx3TSX55nleLB1GRMEPWsf9HurLJ5X4mlnk44FR%2BL2T3pkRvDS9gJwKVRYNvpfaPunlZ4%2BvdEO8ZC%2BH6Rx1S6a72yiCQ89BeJ8hoAU%2FJhrKj3JLIszU9tVsUQz%2FaseEeK0U&X-Amz-Signature=d906da49293822188d59291846c6e07932e211cba9a4e36d793dffa777967dcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HPV6CDN%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCe8%2FA3nVgPGUq0mCReekeiPaiJIsSvA6e5XnM2GMAvjwIhAKN1wOEs96JuAxjWuX9rVQ4%2Be03AjPDLDEYq3Gzzc5a8Kv8DCDQQABoMNjM3NDIzMTgzODA1Igw9nYoo7OfMlnGMQm8q3APVh5MC7lRHsowMeLAbBhq9568ti2jFJ9TxfW2IvQESKYetgeld%2BaFdnu1thUXnxRyycU47QxW7qDewXOIVY7a0Xqf4uNV1fZM7Rbb%2B%2BTw6wh6lhCD55HaLInfM24pnuxkmF%2BEYpxlqWg3yIcY5RuXMnqJbycyc3i44O98X5J7M7VquxgoL6PGNb9Niw2Y%2BQrdRBWyzWtL871YlVJhu5X9hHVIIDNirq2hopAzrIjLTBsFUKojMXpCcv3cACt29kxdUyhlIzW0ZoRvVhx8u91n8o%2FHgK37oU8dEeXT5RosDNVwo7bmtutAjSpDSun7jof06rze1Y106K%2BeJXzBxFGmU%2BESuioFHdRWqxlo2OOiPAdqI25O%2FqA0w5jgfbsK4s0UbG35J2DdKXQlEdF7RyiCXCXghAPz6WFuz7FJIteDPgsCzG0KKXt6W3TDxNj4ixgyQIIUU%2FqH%2BlCjG0Nru4khXtGVkQq1sphZNSF37mnji6Jbk4FWqrNaB2o3AMROACFyZqlvynsWO9O63CGOnFJ7ZM5v8NJdMJN5Wns1UU3xJ44Dt9MhpooBnfuXn22B3muH5B3z6tYlrVWtOVpqcE3wby5Rzp04Aq0neb5k3OVz%2Fz2FL3aAMrP%2BhARrz%2FDCkh4TNBjqkAQCR8z0mjUN%2BOuVfenSpLpa9DdopwFPZzc51RC8uzeZ%2BfrH3581Sj4NSeZ8DWznLyydTli3D8f8iYVAItiY6Hbc8HGx3TSX55nleLB1GRMEPWsf9HurLJ5X4mlnk44FR%2BL2T3pkRvDS9gJwKVRYNvpfaPunlZ4%2BvdEO8ZC%2BH6Rx1S6a72yiCQ89BeJ8hoAU%2FJhrKj3JLIszU9tVsUQz%2FaseEeK0U&X-Amz-Signature=a024b1ae489a30913af24104aee441f7e335ca69a2f6fdad3801cfa952ec1c50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


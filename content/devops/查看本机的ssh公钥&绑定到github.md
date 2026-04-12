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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWH32TT%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtGgTrh3GAxFa2AHbjskGkagVT6VYp9kw7SThYy7dTIgIhAKf5waGjTMjt4Q18rdJJFaSyyIvNe4ftjHmx7OQCmkMlKv8DCFQQABoMNjM3NDIzMTgzODA1IgzcsSPlRZ3ZeF9jtDoq3ANG7RtltH8DpEs1gHTWWaB%2BGdns7BPj0mwjcEa0KeSooFuMuC6XmGECZLdLtTZ7wDR0M%2FL4kLw4z63D7sFrC0aq6wYvKUq8N5hbySIOzK0%2B2bs%2Fz8HwdbqrPXgMu%2BpaszKEhluT%2Bvr6sAu0DwsUrjizZ2rcA%2BuPKs5oJ91skFQw4QA5r5itAg7XZ%2BwWVJZa1q%2FrFe9KUzAsR5R%2BQ%2BB57SUzFviZyfbrjlFUVBviCosZXTpGPEIpgnh60VFJC0qLP2V0qVFN3V6TSsI9qAFkxr7UlE6DS0XTcYV4ibdc3ebCgOFp96HfVXFv%2FcBM5a0NUyWCfCxmf3%2B29nhoL6%2F59W7hF3yY6l4XNZnDF51Brr3hi53qUa%2BeDrCpRiAS%2BRMAaGeCJVwxw715PC6I140jk3fWsTZBbl6oCzHCcJkfzIgNHwo43XeP%2BhSO%2BnwZqCXMs71brayu%2Fc%2FcFhWE4etnhgO1mDppz0mbVPXQwaoKTph%2Fs%2Fz3nm9IOqFwuecxP%2FDnyiFZhQ7m%2BfoApYvidGA7DXc%2FMi2kJkjZrFPez3hEhAAEJ0HI0iu7Owoid7xRgrGgZHd4Fe%2FSWUq9aYUzFHmOHWeZ8Pe40O%2FQSDOy%2FAu7KooQRWwD7YujVQn05ksz%2FTDciOzOBjqkAX%2FSFx6hD%2Bc8g1VhYE%2BQz%2FKsq9JOSi%2B78lEQQWjWBdNlSjUdCIIhYG2FCb0zfmRRxR9jnMNpSyo8MkvcjZU43i1bl7wrAbRvlppA%2FPzS6HAy5VpJP0OPZd7%2BNBz6Y63izkUrNFSBva%2B1hrTJn6PKkpIHfsbqkeCKU5w2pNoXvue1wya6ZOsb1UcpN%2FILhxowxXPWUfiK8CHJQ50k1%2FpHg7qV42tZ&X-Amz-Signature=250a3a359cca90460223fb71977ca1a600b331725d897a1406dc6589cc66ced0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWH32TT%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtGgTrh3GAxFa2AHbjskGkagVT6VYp9kw7SThYy7dTIgIhAKf5waGjTMjt4Q18rdJJFaSyyIvNe4ftjHmx7OQCmkMlKv8DCFQQABoMNjM3NDIzMTgzODA1IgzcsSPlRZ3ZeF9jtDoq3ANG7RtltH8DpEs1gHTWWaB%2BGdns7BPj0mwjcEa0KeSooFuMuC6XmGECZLdLtTZ7wDR0M%2FL4kLw4z63D7sFrC0aq6wYvKUq8N5hbySIOzK0%2B2bs%2Fz8HwdbqrPXgMu%2BpaszKEhluT%2Bvr6sAu0DwsUrjizZ2rcA%2BuPKs5oJ91skFQw4QA5r5itAg7XZ%2BwWVJZa1q%2FrFe9KUzAsR5R%2BQ%2BB57SUzFviZyfbrjlFUVBviCosZXTpGPEIpgnh60VFJC0qLP2V0qVFN3V6TSsI9qAFkxr7UlE6DS0XTcYV4ibdc3ebCgOFp96HfVXFv%2FcBM5a0NUyWCfCxmf3%2B29nhoL6%2F59W7hF3yY6l4XNZnDF51Brr3hi53qUa%2BeDrCpRiAS%2BRMAaGeCJVwxw715PC6I140jk3fWsTZBbl6oCzHCcJkfzIgNHwo43XeP%2BhSO%2BnwZqCXMs71brayu%2Fc%2FcFhWE4etnhgO1mDppz0mbVPXQwaoKTph%2Fs%2Fz3nm9IOqFwuecxP%2FDnyiFZhQ7m%2BfoApYvidGA7DXc%2FMi2kJkjZrFPez3hEhAAEJ0HI0iu7Owoid7xRgrGgZHd4Fe%2FSWUq9aYUzFHmOHWeZ8Pe40O%2FQSDOy%2FAu7KooQRWwD7YujVQn05ksz%2FTDciOzOBjqkAX%2FSFx6hD%2Bc8g1VhYE%2BQz%2FKsq9JOSi%2B78lEQQWjWBdNlSjUdCIIhYG2FCb0zfmRRxR9jnMNpSyo8MkvcjZU43i1bl7wrAbRvlppA%2FPzS6HAy5VpJP0OPZd7%2BNBz6Y63izkUrNFSBva%2B1hrTJn6PKkpIHfsbqkeCKU5w2pNoXvue1wya6ZOsb1UcpN%2FILhxowxXPWUfiK8CHJQ50k1%2FpHg7qV42tZ&X-Amz-Signature=4dd9c37730ef42d610e259762bb57fdee3a0e9e7ac83669d7c1aa2bada30d594&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


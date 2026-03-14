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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666JI5RFB%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDujuJGiLzWzYjeb3H5YFBJNRhXQUl65UxhZV5fJc39SgIgPZ%2Bxw4RhgO8wfrqrdoyWn9AaxmEkuxitVzYXZKAlZ78qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUMWM3RJkKX5A%2BBwyrcA%2FExhOIn5c%2FK4B5l8Adg0snnqEce6c56wQrQ%2FDoJikPaynxD34WCMubujITum6zTXC1gBXrgNFxldbBYYeoR0Bc3M5NO29LAOEy423e9GN3MFpEJOwvUNG3s7cuH5rjDAGsWtimNcfIOtVju7CQvHoYmicrY8I2HWtgXaXmeMDD0iyK1qJSssbChkpzlphvaaKbn%2BXBWbP0kb5mya12pZqMNtS17YPjsrdpJXPrwz3v%2BA918Ev6rAkcK0Xm5oKhXxwzIL%2B%2BIf67vw5vq%2BcoH9%2BE1iL93wIa4cGlRuR0%2Fo7hyaQmJjR0ZVnDbG4aaszompCQTCgM7lUw0RZTPWvMNYe%2FqvUsZGRPwe8UHLj8fyGje2I9vzkB8x3u9EI5EPRG6k81H0yBR50KmgnMFkx10%2FekKbCYuPMboD77oQwA94nX6XeYxR2tDM8FDVuhHa3niUEpAkhnOSLgaxmPcvufwJgVlDYXQNvk0c68kZLb64K%2F8%2F%2FnJL1BcG5xLUNqRP%2BsqICwQoCHhgz%2FwU2sCOP7AUf6ERYnYb%2FxnPko5Pl4ISvqKGn%2FtMrMpVykbKmH3qBS38kH5FlyuRBCSLW1BKmLc0kkJmOL6CJOY4ZZKqjg9%2Bj7pJ8ATmEE%2B5hG3FTw4MPaB080GOqUBtfKfPWOBGVATv2meqIDwyXYEIFR2L8QATHVt59XhkeqOq5iUG8TZI%2FYAR%2BeMp7UPlCLrK2zh97PO0kd8QFPF%2Fn0Y8WH7y7JKPrxuVMzPIxDq8WqRkEUC2fgvOjbup5BBauOuoeVXhxhWBXGHJl5MKt%2FzsszQDKYHbpWYD9F5p5i8aryf0CisRdk3YO65S5IiDwvlZfKFHEu%2B09Ayn%2Bzh9eAQAE%2BC&X-Amz-Signature=6664c190b2c0f1222da135e2eebce2197fd6800faedc9fac95a19fcebfcf65ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666JI5RFB%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDujuJGiLzWzYjeb3H5YFBJNRhXQUl65UxhZV5fJc39SgIgPZ%2Bxw4RhgO8wfrqrdoyWn9AaxmEkuxitVzYXZKAlZ78qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUMWM3RJkKX5A%2BBwyrcA%2FExhOIn5c%2FK4B5l8Adg0snnqEce6c56wQrQ%2FDoJikPaynxD34WCMubujITum6zTXC1gBXrgNFxldbBYYeoR0Bc3M5NO29LAOEy423e9GN3MFpEJOwvUNG3s7cuH5rjDAGsWtimNcfIOtVju7CQvHoYmicrY8I2HWtgXaXmeMDD0iyK1qJSssbChkpzlphvaaKbn%2BXBWbP0kb5mya12pZqMNtS17YPjsrdpJXPrwz3v%2BA918Ev6rAkcK0Xm5oKhXxwzIL%2B%2BIf67vw5vq%2BcoH9%2BE1iL93wIa4cGlRuR0%2Fo7hyaQmJjR0ZVnDbG4aaszompCQTCgM7lUw0RZTPWvMNYe%2FqvUsZGRPwe8UHLj8fyGje2I9vzkB8x3u9EI5EPRG6k81H0yBR50KmgnMFkx10%2FekKbCYuPMboD77oQwA94nX6XeYxR2tDM8FDVuhHa3niUEpAkhnOSLgaxmPcvufwJgVlDYXQNvk0c68kZLb64K%2F8%2F%2FnJL1BcG5xLUNqRP%2BsqICwQoCHhgz%2FwU2sCOP7AUf6ERYnYb%2FxnPko5Pl4ISvqKGn%2FtMrMpVykbKmH3qBS38kH5FlyuRBCSLW1BKmLc0kkJmOL6CJOY4ZZKqjg9%2Bj7pJ8ATmEE%2B5hG3FTw4MPaB080GOqUBtfKfPWOBGVATv2meqIDwyXYEIFR2L8QATHVt59XhkeqOq5iUG8TZI%2FYAR%2BeMp7UPlCLrK2zh97PO0kd8QFPF%2Fn0Y8WH7y7JKPrxuVMzPIxDq8WqRkEUC2fgvOjbup5BBauOuoeVXhxhWBXGHJl5MKt%2FzsszQDKYHbpWYD9F5p5i8aryf0CisRdk3YO65S5IiDwvlZfKFHEu%2B09Ayn%2Bzh9eAQAE%2BC&X-Amz-Signature=6f77131d5bbd08574eed7f80a683108d296721ed5338a9955b8a973859003812&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U22KA3U%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIBXN2DMntvJz3%2BTS4VSwHJYHFX0AJ5AFnbhwiF2K2q4bAiEAvytFRqqpFPnzHlMg06ywHCR2bcvJYgKpAWulB%2FVTDNQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDNokYIlhrtYMgqne9ircA4gFRDX6U28W7cUBUZYnXAYpcK9f2IO7FCurIy485DM6XJiOatAwQp3fUMLpmQ19ohsBzip79bT4vnSaz%2B0%2Ba7C92k6gi5vphUqZzIVwPoZdKRssvpRcQd9LCOg%2B9hayShEvdLsP3AP%2FwFWX9hueJPJn8QgODobLHZg8Ma%2FUxifbtkxYkHvut7TZcKbX1kFATW4AwmezYh%2FfQqgX6VTVFAtXfgVZViQz0SzwACwcLB5fI5FC06NV%2FT72zwxFzsWS3%2FduMWi6K7kr7gK6MD%2FRiBI4EqCp0qBoau456VhU76hxT3nw4bMBx%2FU7VybaTgVRGtls4BBQ9QpSJFvy5CpOig0QAVb2C3nc8GQvG2UoQVgQhSXa03rDacd%2Fxhj%2BSGqPdwMECQzEJHujj4lsRzg%2FTl41guGz%2BwFrhczukZAJ45sw2pjtmz9QEfvg1hdZdCjMdRolHLXKBjcGjtBPk0AQGkDoB%2BcQzRdNw%2FFjbeK5zRUuRCMIe0Xk5TMvek6b2IuduO7QpfzSoaQtDVM6Tmlm%2FrUgEd1SUXa3H2fUTZntvzX8xDTXEgjPPjugcbDIgv7Eez72lW%2Fu1TlatMB6MuA8PnlYJNk8bPJI2G9c%2FHa3UIwBGTaZSR8JadGDfgNfMLyczM8GOqUBc5iKv1Vz4Wa4XoefB65wqppJk1eEfBliHONYp4prQTPCEuSp41DrZr6bkA80kkTednCiALLP8SiL9L%2FPyMbqFCqfPa%2FsDIdrDRvprXjnPgDdZvTPM4aPC586x8f8fRVPxq1t16EnkJtW4%2B5ZPrHbk0ImgBxhPvNmGEy6gcoWeuvSozlHl7br4p0LQICpaV984zTRIyhkUGM1J72E7OdoZ7m6aDo%2F&X-Amz-Signature=2a6be4e1df2bf486cf158464255317d8facbf93518c0189c3bf735f34cb72e53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U22KA3U%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIBXN2DMntvJz3%2BTS4VSwHJYHFX0AJ5AFnbhwiF2K2q4bAiEAvytFRqqpFPnzHlMg06ywHCR2bcvJYgKpAWulB%2FVTDNQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDNokYIlhrtYMgqne9ircA4gFRDX6U28W7cUBUZYnXAYpcK9f2IO7FCurIy485DM6XJiOatAwQp3fUMLpmQ19ohsBzip79bT4vnSaz%2B0%2Ba7C92k6gi5vphUqZzIVwPoZdKRssvpRcQd9LCOg%2B9hayShEvdLsP3AP%2FwFWX9hueJPJn8QgODobLHZg8Ma%2FUxifbtkxYkHvut7TZcKbX1kFATW4AwmezYh%2FfQqgX6VTVFAtXfgVZViQz0SzwACwcLB5fI5FC06NV%2FT72zwxFzsWS3%2FduMWi6K7kr7gK6MD%2FRiBI4EqCp0qBoau456VhU76hxT3nw4bMBx%2FU7VybaTgVRGtls4BBQ9QpSJFvy5CpOig0QAVb2C3nc8GQvG2UoQVgQhSXa03rDacd%2Fxhj%2BSGqPdwMECQzEJHujj4lsRzg%2FTl41guGz%2BwFrhczukZAJ45sw2pjtmz9QEfvg1hdZdCjMdRolHLXKBjcGjtBPk0AQGkDoB%2BcQzRdNw%2FFjbeK5zRUuRCMIe0Xk5TMvek6b2IuduO7QpfzSoaQtDVM6Tmlm%2FrUgEd1SUXa3H2fUTZntvzX8xDTXEgjPPjugcbDIgv7Eez72lW%2Fu1TlatMB6MuA8PnlYJNk8bPJI2G9c%2FHa3UIwBGTaZSR8JadGDfgNfMLyczM8GOqUBc5iKv1Vz4Wa4XoefB65wqppJk1eEfBliHONYp4prQTPCEuSp41DrZr6bkA80kkTednCiALLP8SiL9L%2FPyMbqFCqfPa%2FsDIdrDRvprXjnPgDdZvTPM4aPC586x8f8fRVPxq1t16EnkJtW4%2B5ZPrHbk0ImgBxhPvNmGEy6gcoWeuvSozlHl7br4p0LQICpaV984zTRIyhkUGM1J72E7OdoZ7m6aDo%2F&X-Amz-Signature=7102d7464bcda4833058a31ecb54fdc8b1e3f2c821ec78365a80e336f7c92183&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References


---
title: Git Common commands
date: '2024-11-20T01:22:00.000Z'
lastmod: '2025-04-03T07:41:00.000Z'
draft: false
tags:
- Git
categories:
- DevOps
---

> 💡 Git代码管理规范说明，以及常用命令。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653KTHULN%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQD09UdTWuMFDlRx%2B0ndlhlEPK3f%2B4l5oHJKCGgKPqQMxAIhAKV5gQGaYENfU4VXiJIj3rRhxli8EJ23r1C2rStr3ngJKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNiZbsVPyBI9kmFS8q3AO4lBbn42s9r7q20ea3saBfbggEA%2BRYH9L4Go6bXZonBswnY%2FqVtTAOp7y9oMa6gepdWhCLzmLlFfnTexKTo%2F7v%2B%2F21Akqiy6S4tcTnDFXPxRbKWaFs5Sk9TjxAK%2FnExbkfCkSdK%2FMXimfWuW3Ch3CYTBY1M5M%2BpCZU7o%2BZkeumizzEfN6hq8cqt12QSGejwqFiUmZipqDymWbESGcAzbBig00dbCGl7KGsXNdFHBF69HMEzJnDnUjvwMpTvgYgysZnB44oPXhyl762YWMK0Bp9TfDvx1BxMACYyrRuzqUo%2F3nIwuV4VwO4nZx9GOpMUnmQn6735AUUrZmnrSkLJwDnqehYXfTKEwMKQMzpDW22JWWW1kecewjA1U0N00j0dAOamJawnIJVyoZD8muXO8vxKzz70eYlbkLg7YGL8V4QJwjpve0BCk933u5krJh5%2F8u3%2FN4bMFVdI2FsUmppHTwnvF%2FnXkBiUgYrA2MuPi6Qz4CoeVISXEYH1AyuzztnhQM6fGW0lz6snv7WvvkP0NIcDcW35gFAuTSG23ayoyZPIXFIJ490jvvzRZGfemoTX3wVUvzu3NvP5G2fIibgGuGbPqJVLD8hgbNVRYuwZlaxaySDS8g9JtveWYv42TDV%2BJzKBjqkAS0n4ixqc1iZnkmnssjtZcY%2B9rmtDb2MF3lcisEipmQz%2FV8zpgQbTMjpzIlJEzOxgublQ2dwlpYck2X85p3sO%2FBZHJHf0HTiYOF0BaQB9k4V1F6KjoT1dTptkeWcBvgCSH%2Fv%2Bnwd51szFV7iyqJP%2F5GvDNz7rCMd%2FO6j7OqpmvjxjzHyztcoQ8PjlMhnV2ZpePyUXWv8xTGNigTHuYMHngfUazze&X-Amz-Signature=5b6cbc22f5385938b7f07869b0e353ad3c6958e86fa6fa052c69d0b77785ba14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 分支说明

最常见的三种类型分支，名称与解释。

- main
- develop
- test
开发人员经常创建的两种临时分支。

- featrue（功能）
- bugfix（Bug修复）
---

## 工作环境常用命令

### Git基础常用命令

> 💡 想多看就继续看吧。以下主要涉及：上传并提交，合并，标签等操作。

1. 添加到暂存区
1. 提交到HEAD
1. 提交到服务器内的仓库中
1. 分支操作
1. 拉取以及合并
1. 标签
1. 替换本地改动
---

### Git常用配置

- 解决win和linux换行符格式问题
- 解决旧版本初始化分支名称为master问题
---

### 实战经历

```bash
# 初始化本地仓库
git init

# 创建并切换到 main 分支
git checkout -b main

# 添加文件
git add .

# 初始提交
git commit -m "Initial commit"

# 推送代码到远程仓库
git push -u origin main
```

> References


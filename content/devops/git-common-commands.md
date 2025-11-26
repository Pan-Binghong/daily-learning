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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U62RIWHY%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICVDg6%2BJG7amFQrPM17cKHRp5QUbIq2x45HXABbR5TSaAiANGV6TYYFeR6fKhBP%2BwWIF5T6eHF7pGygV9JWpXqrTLyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMp9wgANv9VtSUxBAJKtwD7yc7l1sgBUdWZI0P2R9gnjSiB4iXR281mOsZr43WGzofbAb%2B6P9ufsllTHN0o49Z%2F4s07dfX1AcE3Gm7zOF5Ln5fyOcx4RyHI%2BRDgN77KbJPMPy2s1%2FK%2BrGlI6hbLPmJN8z2T2muH9CHT04ESJIv3jS3NjAdnPhSK2OdrO4%2FJuU%2F%2FBNAvG02AsDOGdwJShi0J38OTEjJ3Q1hmD3GCDaIP3uOafG06XkCoNT4hHI9dSx6EQK1pfVaglPwduYLz4Bpp8meXqj1QNGIRCDtC8G4k9jEJxzz3wyp9kUjbNqe7flejyEVto9p9twAwNi2Y%2BH8zIIfhQZWVnFahOqp3zdDRv6snf4s6xUHqRWJ94wDBImQWy4V7BcjbeP%2BNJoWpEhOw%2F6SNa8OKG1%2B0ZLZmiblWYAP5efYc1c8XsNxYnP0pj9SHeD%2FIqw%2B0BIOhOPshCtlIu0YY%2FRGpcUU7Fd9BdI8TINyvLywC5oiCpadfZGW%2BYzEz1gFEZyoB4qKeGaKDpCrsGj%2F7HaTZlcqaK6Wqt51A5YE5OZLMwAqfVwTkFJNrYXgdKP7fwR2Ax5ODIMDly%2BQt5GUyLHBLX3knhmZGg01j5Qr%2BCMmSdWvguaOgGBNAbUp75%2F0nBwfdFfNhRww0bCZyQY6pgGlskHtef%2BAVPz%2FnvJ5jtFkNlAlRzOCBsDKAdDSppdejimGLEQ%2FJ1gAnTXwVooRbYByuAJBlWU4uQmOCJW%2BWfVvS5%2BZptOgI5GXPB9eUKs65jLIFtXU3M4HrAN0ZGZ2PqBajxN5Cl704C4NwlJ8za0LtTz6j1%2BMDbdpGgbXLfjqClZl%2FfC4kk5fyTNfCuBAY14oACiGfuElMMTk0nt%2FVgtwjFAfC%2BJG&X-Amz-Signature=949b0b226ca9dad9bab439cdf3b37af315c60bdf8e2824f55c29148d7c680ba1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


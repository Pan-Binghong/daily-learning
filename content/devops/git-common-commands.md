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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URY67FIF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqqvJrKv9f5thnK3aJWJjSe5X3pdPJamuP3LvXmGIaeAIhAJld9W0G9AE9TfTCmFLmZDrqEXoC7aVTpT9%2FbyYyWeOOKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6GNIzxKNS8FeWQb8q3ANJD9WGrxXMshmq%2F%2F3J9SF3QsN%2FNpvlqsYms%2BofPzxrEFRyjbRDOf3QJzbuAOkEuJ2xYf1MH3%2Bg0Getmo5r%2Frw%2BCiuVmpC%2FjhZc8JNJ7KB3iqYSbObjT98%2F0OlxfgG6%2BZYu6eBDo70s3BkCR77lJ7mvIhehh2NFkuKsaz1%2FqB7i2qglyXuvVkEpMmbi%2BkJNN44ufoGMWHxwPv%2FOFGt0TtvA7QkOqxkT48bCCnHKG202EVE7vy4Rxsxs7N5KFzyI2879hXBTUoTdwl%2B2UcodH7%2FA%2FvibvHWFEfmesqg4N0Rp4tBqc67WtppmXv0Hizavs0avQXcV89%2FYHDUNjjqhp6gFHIsKmdxpjl12LtdrDw1Kxt8KZoXdQbQquQ22BXl9Q%2BzsN6iWHlgnqGOzpi7t1a6CQ6nXdgzB6ynlPu22oSOo0ofIjMqqGYFWAUg7Lw1C7PfyCoJGjMY8MgpMMGf3snM6u1ILjhhB1aaFfXCAxKaYitQa%2FjHYR2UGdmUlmXtWuhoY1h%2FDsceIVKuhbPhMxzv5MverG6h94UoMiAVo8PlWl%2B3URl13NiF3jd5KoWUf23nFGbex%2FS51vupGfLpahLONMYhbZV6hQJYEr3%2FSfqMbLG6saLpPIDip3U%2BRLjDF8K%2FIBjqkAWoqUZIt8b761%2Fs0O8mGIXIYGRGCvs44QwkO2qAYSjC9yeFJ2%2BlCQNtSy81JwYqmLUbXxOUKPZF9AhSyOspOapAQMXulb%2B5ZsmY4V4a2GHpdzd5c5tiU1cWjfA%2BXRCNmR1UfTtRE04aHrDWG%2FJgdrYSWYGmp%2BXGanDbzW5KTJxTSIPi7fB9bnxIDK5hwBPopwREUgMXHqYM8Sa3rGc5ShJmW%2B9oy&X-Amz-Signature=b3a1ebfb6a12ac00db013d525b261389f8af86f8e43c9a400c5d3a3255d76c48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


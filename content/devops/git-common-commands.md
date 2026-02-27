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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY75XPQU%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHZC8IHnk9eRvpqmQCsEPtwIiMAyBsbhT4ubSQ0bsy92AiBsRY3q%2BoWr3acp9R4ohZS8vpicE7GIIJKz8GvYM0cL1Cr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzsNUnyqrRT39s8mUKtwDt8v79GDdyRPb2CTFnhs0cYEONybo8px5gbjj9Si5QvPKoNdqq7v7v1dA3EudmrvUnVgcpsMLooQvH5%2BlPevlPdvXbHj5hVDKAzWTi5Z5gSuqwOsvz8deQd2c06%2BqCU4y8YOVdbsfZO1T4EVFaj1gqVbrbRv9CDLsFf83DOupm%2F9fy%2FmayPIYonQkAMK7OisiT%2BzxmagoogrcN9DJlyrO1z1PNy2I7GRbOofbxnOXYdoQ7mOCpNjZcKoKNJ9zUSLvstcMy57MNcLsGLvUidsBhTxykHiomlx%2B0mO4YaLO46B%2FFTKWQ7bLMbt7wuoclyt43EZYf1WaCIwSyOYbaRnBd0oliTuAXk6%2B62PbwI6RWxDFwyt4mFtRG6ybctqDxrqPKsmpaL07p14p72ldSTFB2Q6VLJJTo5Oa%2B3kN%2Fmm4d71zSHC8oZG%2Bq%2FSvbr3zu8JneaMC4YRlk7eTIz8tQgiIfLi7IPkxiEqGp9qtW%2B%2FISxxglbzGYebKmd0E3XVpOgMoA6r%2BOaVznijNwWgSQM587pnUNrJkJNK%2Fdo2TY4UA0mOMi6ZW0iBmbqSiYVMQz9xvmiBa9IXf4Df6lsNpqyV1GgNX5IckzEbQw9qguH2eBSgSlEhG6QGl04sERtMwy4aEzQY6pgHqszc2EcaT1pBMG42WI6ghET0lIE0PkIlstbR2F71128eOP671WuDuYSv4KLboWmB21vUZk7HKsYmeGLAze4pvUTCqO7rYKuet5vf62Bu7XNSYDa8dCSXI3LH5RuSVzKcTonEsdoyBh%2FpkvB1hQI%2FfpryE7Yp0mW5xX5q2O%2FTkLbbrFeM9b4gCwsBqRE%2BrSDBuojkNbUU5Tw6Trh%2FHXa7uKSzMr5Lp&X-Amz-Signature=e4464d22ab1be0c2ae40f5799c58615a5b635952a57544153fb63c04d6ad37f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


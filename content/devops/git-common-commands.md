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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHEMYCTK%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwZCexn19D8PU9liRWOIL2eaCyzRUZRNEnBxZks3AOXAIhAMKtYIeVdIrajvbFol%2B%2BsWjE3xUPF9%2Fw1gsLpBqRadUoKv8DCH0QABoMNjM3NDIzMTgzODA1IgwVpCdTcI9zEFrGTZoq3AN75qDbJ2cUkC0H3psCv37aij1ylOrVz5tbIjGTSLf8bJt30lmmwJzpG4U4Y5tWjYdLkzBEEunhDLLLZmPuQIkejbyudbhT5GJ%2Fje32Rmh5WfG3eolDXsp5wAKdI9qDNcsU6N%2FGXjVUAdqd3Qjmu%2F4y0DvCiOaWhqqfDkZG2Xi%2FqfpJbtQTX7V7CQwbn2r65HQbcb%2FMaEdaPRPGbOQQynMBJxKfg7dL2EyYkMSVEkDSHqdBKCDNg1g4pbSXl9uUk2A7WCck87fBJbIp%2BGFGRYnHmT6yJWPAtftsW2SIOFQ1p3t59GHVpZHUcpzvf%2FcEbkRAb7EvekG%2BAaryyOq5AIyEuM8zZt98%2BzSK%2FcJ87zYZVVtfG2t%2BBqhwsQ1reULt5G6bEZAbkkorUxf4NZ2Sne%2BvZChcYDHiES3Q7DsPRxj5ZafY0tfQ3nycPwDoAIFGDoRJfNQ40Dac%2FlcnVilW6q2sdkI41pei5DqM6VjpNDFiWKBeYNh%2Bq1W4f1xKWPDe5tOAoWDKK4JEENFH8FQFRrB%2FVI83QDONTvGpABNUKn9X5sh7iJ6uFr8mRyWnhOIguCHMYnM9SvP7OZN3G1PvuY%2B3ZDt69abQbT%2BsLDEbo8dsD2gIfpwWXX9bfrE2RzCs5bzOBjqkAVqxuT1rprRrg7OA65hBmcm8%2BOG0hXmRVFHlbVFjKwRx0eaSkqq20F3hcZH28Y7tX01k4c7O3eo3kKdEN4LzCSNHQUu4OyioCled%2FMLNglPA%2F%2FJjl2JKa0h00Wo61kI5DUKBRIpkqT3%2BsDd%2Bpy9ItVdoaYTt5LMMGW1tjvzha%2BMWpWVTnXLSx9oZusrXr5v8vzo4EyRatdVZu61pBR%2FJT0CVLsyZ&X-Amz-Signature=8ab18bc519f745ba70b9ad013583d8a075ee34ec473a2b35b04a81600d326f29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


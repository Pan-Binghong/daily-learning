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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SV5WTBUM%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGl32Q2TPeXdu9jHScprEibTSJ%2BVMbLrfkh0EPMN3K1SAiAyeljlfsObIdb5CBViDFY2k%2BRUdZ5%2BKcUkvGgwusPdvSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMS9QUwQZEsTRKPrufKtwDLQG0jXDc0gr%2FKjbLXKr7%2BYH2W1vEpzoNHq%2FIiW4aE2YvPthMEOL4xA1z%2FOA37gQK3rny7G%2F9V7Okj3mUN25M88yTysuFobqgxOOfYWJG6P8KhFuF7wdymv9%2BLrhbNyYZY3teb4QOcVfEpEGV0dDl01hgCEp63Ft887bboxt5JG4926CFQMYyVAPWl%2BjcApY5ip6esefD3%2BE3nMsDZR3ZnGpdH8PuN8tXfeyGmcVLMvcvLY59pkXcHu1OMl9X%2BFQXO7i6Lv6r4lDhwfwGz7KzuE3OJlUlgMGdnWtE0Xy92Tk3%2FoPWTzawgt%2F9Jc%2BMfHjtSZmRQVRn7RXcn7yjKiUy8ZfEN7mbmMbQ6g8tqgQlKdymHVSYNRjCAvrKO8RBVhm6KD%2BYAA3UpOos7onfv6zEdMZbug%2FFLWQS5SMnnD5aflVGwkJa8%2BMBy5laXd7bVW%2FdMGvphxT30JY6GILT9F2ZdVJDVHFJyS0D9a1laLgHHuLaob8NKwbrjPj6bMc353e2%2BLvs8tJSYFUv8%2FrFiNjqidHX9JDRnXI08AJV0XcImBC%2F36O8DYnv%2BtqOKmq%2ByNOz7nYblu9BdiPT8sl6YvJqbcPBNElXlIbHzN2J%2BUQ9%2FZEGjTGtryTHv%2FH8jRgw1IGxywY6pgGQnXR0mx1rXEOhb5hGL%2BNtL1h%2B9kUnvNAtVU0KLyq4LLO8TOE4AJQOcDDOjFx%2F6HJ%2BckdlIUGaUW7B1CE8RoqMbEilCeKCTeHV%2FTQXc9PpcmTLsYMoPG%2Fl775wEjPIu2sIReTwsoK6DsUkmpa5Wmf%2BlI2C4CooKj7zoU4lqiTwihW0jLTYhxUYPE2dwSftY1877LFprBOeEuEEUFC1FSEloF269Kg1&X-Amz-Signature=47ace79f197c3e8738b24554ae6d72d83a2f2100a3941953e26c99f53ffc9e9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


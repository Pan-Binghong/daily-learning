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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAUV6WY%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDx9s25%2Bynrogaray2We%2BdNpAF7vR0vuHfgz%2BRDy4mhdgIgcw12Qe6xTTvgoAcAPjHjYIzKTIXE%2F9OuqGlLt5DpN48q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDDsDthsXYX6HtjJs3yrcA3ZNoKGEUhfhcF8xuYTc6FzuiGoQBSbY%2FGfw0YbmayQ%2FkerQU38LHo4tTsI%2BYon2n%2F%2BgMl9rGrz8ELomfIEvYj43rrpMZyLqj6ylJ2R0TMkjmNL7dyMAZQh8AfGexUyJ6HzY%2BEmenEYeWhdBPWV7%2F9kEWjGZdtjmawOOY8Y7K9UUZMKw%2FwptxVdxg%2Ff8VY9GIHP%2FuCWy09AZvdxiWoRzpdVFqYek%2BpwcaTmN4Ws9NPGGJV8%2FYZ0Cr%2BVLkFKZv%2FtRGSqBUrRLkcljzMMAq1DjKU0Ux6UuRZZKd1wce3NzPubutj8V97wDfJDEo2Y872nRb16ToPFmo%2FSrnTbt7CKAntYIbwf7vFyUEBSNF58W8HL049GDCY1h1WpSc8zBdkNf%2BBbaFlnoPq3Gq0Biu8umhFdUUNf77Qkc3BnKyzkgRAp%2Fs2vW1f%2F%2F4pWGyq4S10Qldiybn9o%2B2l3ft6IewjxZvAs0PZEOFWRcJLyRaFqcEU8%2FUw7ID3q1RIOKkQXp6tz%2B8C1oJRmdRkOII%2BEIaIjCjvqrBJnsXSXiT7GzOkEfdqW3BYVoJjvWE1kN5TXpjCfVMKlMa5prf7wrqvFt4REjmLIryl2p7v%2BVgbOI5o%2BwAmWfH5GJ9xh%2B6N%2BlcwGtMInpiswGOqUBJenSW5q%2BPd2FuEPhjoHmmMN57RGiTTXzsg3hdvm1MQ5FI0fWUDu6GRmK1VpDfEmNN4N5XdJ1KJqDUnwTF2DHj86jUVPMZiDVJ72bEpk7LMv9V3aOsroezUslmpNpR3ZbCxdO3T46s%2FXMZlqOn6YXrbSxYuz2avzx8SEhrCTUxJrNk6rssvpwWTCnHouf%2B4%2FQpPjyKr%2BQ34OwYA6g3ficA%2BnkkMWT&X-Amz-Signature=d037a3d0cb2088d4a226ded2fb8022a222b57ee0221cb3daf36b818627259005&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652KEA23X%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIF9fYVZ1oI3SRuFFs6fxJxMDJ8qXsKwIinDZ%2F6pTxlKEAiBcYQYXQ0KvzK%2BnKKhpUxtf2d0gRBfTAAy4%2Bwi2FxwnJSqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0V1AXYDRCxM4LUUYKtwDuBQQoWoWjQDU6hBFxkoLoineRiIkshMk7CzIPAXt1Hw5OwegVq5DYIAgq7xcaz000eAFLQQAq9OtISIe%2BDK5BXhFtI46lWA%2FaTn2GLEuqdBv1DwYVcsG%2B4NjJ66y2bpdSqdFPdDGNSqR6y6oGHo%2FZt7B6m2Ax%2FEC7%2FaM121iLAA9xMpXCms55XbwH7JdgS3%2FYRbGJG5vTsvxoVEiE6e4v7%2BDOuDaw3%2FGYWvmV6%2FQJxuv5f9vhv%2FTrRGGUJgV8DKFa9HQ2SOsQf0efqALOkC9sy8Ge7NtHSR%2BRJMoGM01Eimv0lBB%2FgIopBGOCZlq4SE3%2B3VzNl%2FtlORkf6ecXcKWWZR3tU1zxdo6nEI80KrQzJkdUJzm8E99AWr7WpPUpE6YaGtovYT1JOgruFzs35ISSRoHuMcMDQppHeCnjZV9tqhqnu4TE2nTEdALv1h%2B%2F5GX7iIlpR5iB2POU%2B10aaw7rJnohe6ecT9AV89hvaq3X2GhsgOumUYd%2B4SXFJc%2F3UyVGS4sB%2BE5%2BVpZT0gBooHWFsPmTuiI%2FkzRrwCu7BZwBP3YrpCYneFdFAGVDJBU3iSJJt3a2OXlpI7pUR8HR%2B4Q2nBcRYZa7eo1VykwS3yTiGK1xRFUdCR29o%2FOV0AwpvbRzgY6pgGyxyF4Wzh377Hvmrm8Jx6GfIN6UockUoPOIq732KHvmo%2BbT8%2B16O%2B4tfX2L84suG6vjlSOrsQFoxdyDtppajxPLzUt2%2FIO5vdZSEMPHFEGfIPLJVmTAePeXy2KYg21nApqRr6XlCexfD2MuVq6ZnQAKhrHcXptt8bBUzGJ8uoauSKwrhwzd59zsZeiP5RbDq%2BZuBVz5GjrXWjySfqJh2%2FIsWCCmW6g&X-Amz-Signature=a33df61ec7b91163e36879201cac861a3e214c42b0b1f028408803f5a0d6ff3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


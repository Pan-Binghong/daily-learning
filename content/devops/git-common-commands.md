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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z62LSYBT%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDn28x1j%2FUEA3P8b3%2F1cP3M%2FGUMMnINE2HdKw27RFtQbgIhAKVvScSkeLBkwzrUaUZnc2XU1AP68AaOmwocUvipi7HDKv8DCGsQABoMNjM3NDIzMTgzODA1Igz3Zd08J3EL59AQdL8q3ANvvm1O1s2u8HmuiBDg8q2wNwk43SD36Px6Gp06%2BImJDjaaf06f7M2Wr1olx2Ci5vsUw4Ap1hWcYyCYmOriZEE70lDJxmXne%2BhWZlJKgA6%2Ba2uD9bLg0XgIZYfyS961wGm9c0PQy1I74yoM4d2GHxjOdraGN8SmOC4zBGoljBSovCpKUv8nY77PY1bS4m01CbJ94gHE6t6M4WnnR6wChWqNXCnjT5bVu89%2B031mdjAu%2FIXH69rtfgZgz8BSGEsUTaidQ03RqV0nmxYCL7x%2B6oBsL6mLWaaSKtSqCjJo0pNhQLrGbR%2FPy%2FQ7jjWTM0z9yc25UkAG6ObY6X1n5pEFUgPoEwLFC3qvh9BQ2TKN6ZYGtDrF3ANEwEZFs6Pt618A4OMYosHKOsotaIk%2FOi3aPVPlM4DxL1h5WootnwIs0vj9XD3Z8EcnZDxI5UAUao499aWosR5Wze7hJWrEuHS%2FdgtVlA6FWYSM4NDHdR1BnjZ27bwkYD9Txf5B%2B%2FXlT%2Fd9Uy6T520ziylsHikXvuzhTGdqvNxyBY%2Fd1PACQcIy86CBxFYUThiiG5Rk9hg7DENbRJ2%2FLhpt44wPR2ro2LqLXMKxW%2BYaXbNp6C1Dg0T0Y45qIJSsPgiKbOFM9bk%2BJTDdssjNBjqkAUYy%2BHgM%2BQ%2FECu9ntmM2C32hg7XGKUaRi6ZXIM4ju5H3guWIHujbb40C55ry54WeDbKGUheAelavz7tEvhAYGBu1Qa%2F6ClY0NIlWBQ5SJiTDjjQaYU%2F6SSc3OvqdvGlH5HEW%2BFXjHtDy3khE0RvfufCuZo6jYdfZ0G7IdKMXyZ0sEF%2F04Qvc4eFyyOS9bwuxycDhJW3ItZpg7MJa4Y80FCuW28OO&X-Amz-Signature=70dc04f2dc4d0bdbdf50c2c9087786561414f627f66dfb851bec43a743a25bd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


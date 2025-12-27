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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4MIQP2B%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcvItIvoAyok6eNas%2BKn8LCgiTX9rnLGEzWJTuRDIGYAiAZZr%2FP%2FcEc8NNrXvA%2Fb479e%2Fg5XSnq6UVgeaz9Ga%2B6dir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMjBtoPIstwGLN52p3KtwDrM4BlqDNjtWgdxoqo0HfeidG3tDq6%2Bp5ItSTUr5Y6j%2F%2Bga7Cp8pmd%2F%2BRR1cut0RUoiwQZnjTfnW7ZaiGBO1O%2F6Jhb6QSyflU83%2BpozafJLwzTMx5%2BFIFThg%2FkeFNqlSOWaryMKojLP57MWiGgh3Z9vTjC7%2ByAoIM7AimjfIcwqAHY4roDz69fa6fw%2BcHoW6%2B2yiYmUYtdJA9HstWUtFKpd7fjoVuUJ6oeWUoIHMCGABqlNuip1XyzyVNOngQ3xSv82cAVqRaELEcXDvNG7%2Bjp58EfY4jQuOH0Mn41Q%2FB98v1NEJknT%2BTOrQzF2t6f%2Bok6c4NF0rn5HoqgcPK9H5c8mxTiSBaZ%2FNM5eBrvPbPrF7SDq19TdJbf9z7RsXaqL4lrUPA3yg30YVupPRjHBYj7n6Bi49dUjsJBX3o6752JFYwtmPEMIysM9rWqsphhpW1SfvpTPEmvxkEu0mzk7MSoAKbUx7gFzCIiF9NQLpca3HeQ%2FzxE%2B4zzGuw5I0nBLfkAJmgOFizp9gYGZDWg4Q0LieX3TKixJf%2FIWPde6YbpVLklhCAD9mLzI2Us%2FAp1TYp0bw9Bs%2Frz2vOj8WZnrW9kCL4Brx8yBBJaCrK3IcIE5VS5tclLsZEMZ7dAW4wseW8ygY6pgEi9sHZcUTnxU%2FHG7d16flQRcIgK5MdU1KlaEeWTzT1puSAiJRbZLKMDFLbSz59d2E3W156kDGFViHjULlJdJ44Fk2bBKZj0M5e0vmHaGOYnBPF59YBiyh1KZzX%2Bc%2FvxIigD8LfjZ7qCmd3kd4HCGnrBrL6CpoY6DWzgJCBXXMuOw76%2BFSbX4anV7%2B%2F7AYnsKdHx5RIBYjMMlw%2FE2Nbi4yqXoI8nxuZ&X-Amz-Signature=0d8fd3ae18de205ef528d5b28b7b8f9bf485c67221b20f5486ef7decdcf43ebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


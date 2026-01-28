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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXO2IGKU%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZKjBu1ufCznEazHbuKXWny5liBStDmXB%2F6WKCa0RZrAiEAgOPybuTiwzxJHdolVc7tBctsYsq5WmeVDxBqrfNbLjoq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDLOmXO0DudF3iZX%2FtyrcAxMHnlNf1qqrErIJsLiTrWV8a1TpAIl0JIYJ5KMDVEN%2Fr1JkAal7acdHVV7S3LMFEjBkDvKfj%2B2AtY3TrreCWcGYBnCxPcmPDmauMyu82lWSR%2FIC58RMCCW3oj1TMelToTmj2ya2HqLd9QwchbjD%2Bm9tZwZ%2FlJgSml3VpbEwnVmMA80i6PVr098zMXZoglG7%2Bvt%2BaY8GnjPjG6YpglltXzUbsenP0qoU8FXyQICmWAj6%2BaA%2BH7l2eoOiz2UsJcVOiomHHpO8AlYGBFSc8vmnTIwBBPva50j1i8caYHz1hM%2B%2BEMJ8Yob9WWyfo2PmV0kxvWZX4SMn%2F2TXPR3Nq9UWQndtSd%2BaepKc%2B6Y6fRHI5v%2BkGZUrYw%2ByIZwoV3e0Hk0XZW12OKywEoyL6uK%2Fu1ILBlCJKJWJuMi9QTSIlR0vJJFfiemkdZDWEvUCgvgteaGUU6rtBfKgbeMIb%2F7aZYCuVrOZ1Z6ehiCDHqOA3Ryqxe9efE4%2FKAKVLL9Bm1nQpJfo%2BVkHC55QYY2AN2Kxtrgq6wTgOB9IPj50p3yzL8W7THT5RohYkqLO%2FZNPKIzVXM%2FaY2SLx2Dl3P%2FCiglZnf1OVDclcCOPDxmQFRUIDTkjF04NZTC7Qs4b53NbU29nMJKW5csGOqUBmOWV6gBhJgA6xncPSE4y1aYEcWg8wBo7fxLPIxY3DY1KLj0ue%2FBcMvtIk7KmCkhe3nmw6ixHsfGs%2BFLH42DsoNOL0b9H4keRSRcfJsfqSAwl%2Fl5j97O7VwkWllSglDyiRCuemot26zIievg%2F27M3KMaMDKQ0sjzNUbxhw1Wa%2FXVJiq%2BgON%2FUtc%2F%2BzkzPUGO2P0PtJpsBrVilzKCtgB38iQ15LSJt&X-Amz-Signature=ba257214e2885a66938977506679d7ed9b656bcfeb405e9b06de96a237b97114&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


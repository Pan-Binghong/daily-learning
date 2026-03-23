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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVI27T4A%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGD6SJKN1%2FynVU9okaHBfVwvVY%2BnrFDuXojGVxmO5yJKAiEAwFES%2FoOsObavXs2mBY0UXKN0pBSnVUNBSU37GLLNjQUq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDPreAcrZsMUtKKPpkircA%2B4AKZEYKiYNr1pZQ0bg0RERdCG2N%2FMDBcg4zWKB%2B7Vuc11KOII9U7XMZQJjfd3UlWg0RVVOgJ9PSpNDqAP1p7PA0DxYFuT0rwJko%2Bc1j8hncp2qfvVEUwB3Gx4txve4WfBj8wcEdQwbsilOZczOyTlh38V9Sry1DWO9DCxenyXXpmQchWdJyP3joQpu6HToPXnanvkowGgFkrqL5jcuzk1W6qAEPwO4Wkd8ZPs99dM9x21kLb6BVTMx2IuRi%2FUK6NHhWkBfBZfqURJIPj0UsDEVrxkcCz6MiXiu6KMTZWSAwx91hPAX1ganDoVeVByAVdQ3I6xWACCzaz1V340jOBdD56ly54j8Z4dmjb8b8DFPH7Kb%2B4iiR0rSqlxVd3hXocCgjgS8IoUCF1XRGiJoGmZVy9abAg%2FkbtAhor6BT9IF5pmrkiZ8WdvqeqtjvsMBEM08g%2Bh5AFX6oB4d1j4dWvO5xoxmVi6Yhm7QkKaFZmqpMy4QX7TdItiLa3jzzcr%2Bt8n%2BgsMqW7P6bIIHtiM7VIigdow0IsfcsVXl45On0MoC%2BoGL6M2uM24qdEHk1QTcrwrntqbPvjMrMjJBzRCnYKsNC%2BVVsaKn7EjbohTFNTuFvXwg7YV42fJmUATyMP3kgs4GOqUBCAHf6yFQnqQ%2BnFrJ52rlgeMiejZcFJw5KtLetTpY9B%2FhghSa3PWOxWa0v7eCZ5MKQuRqXK6r9tStWeujz%2BNo%2Ffuv1%2BKj4OMF1i3ZHtznP1Qzpzs5EKPsOodLlJW073ysQ9NsDp%2FPh3tvdOre5O%2BwX2MxewvKkQRXS7k%2FmiwA7oBdBMLtWUfYLnILqblNag3WxiqUIaKXpIm35pcPUwmYRh9fy6Y9&X-Amz-Signature=e566ae3d392d3cbf395cd61fed2597210663da08eb7c6199c5185384fc0f355c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


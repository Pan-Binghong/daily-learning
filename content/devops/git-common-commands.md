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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U366HC5N%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCdYq3Drm%2FfgIrRDS0zGeD0pewMmzCg2gRfFEJeT7tq8gIgYuUHxR38N9%2BMaIGrBgx3tkXVRmTOsIsuw9ufL2QpsnMq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDKvbSu4sQWehCMsA4SrcA3FO2zf8FRXKNmsvHYmKItgsUtBMBB99vymlKmGyniPMS5LSBk3oXYSsVs4wGclukoqw7QKgVYQCGyi9QAgjnswjUbMmoTmsfA87QTXnnp4sixofFu0CDNTNeGnQvVVgf3RWYP5Ce6EaYjx5DrZy6NYRDAQAkcaWlVV9Srl4Ec%2BiCMhHFouRu9Q09H8PE%2BX6JnIYhiXzxdYakgu8eTgBHChrU0t2DDfhPxIXFq90F8TodRg07l7qVxt87qqhvgQZ1TF58Lhkjsxdnzh2STVTxWVgG3WwENxu5F8uit%2Bl99JUG1WAZiFVCaTxz7Pw6VyeIX%2BLGAWu78ZdUM7G9rp1aiW%2B87c1dKz7VHwSCGpU03Ace5Lr7ROphYnq%2Fg33Xv3A0n7xdI6c4pozsTUrxCAxkEsvLouLkCHt%2BvP6Mnlg2qx14AH%2FE2H7cdtaVrq7VPdxYM%2FFrCRsVGdOEqTNl6CHUy5kNyJqrCe9LB78HblIqAYLWb48KCBNOEXr59rKKefW7S3EMBnyLHB7M7j1%2FgLtDqmRFJK%2BmZVQgx0MAoP7eilViKeEoUT8g9c8ef79FBgcd5jRJjhxyO3F4MS0crna8ll6aigUwV%2BXKhgV8wGscil574FZ%2F4W0JA6k0coOMKy%2Fos4GOqUBX3B%2BYw0U2LK6JqC%2B%2BGWWqyty3bTvXRS1WpkXRcbahznctRX8luffYxlMaEqD7b0xGyDeol98GVkWscjpUil%2BRSwuVRCLfzL8vecRIWpR9unlei8ZYTpn259Ao%2B3tMywRjXAeiFSxYXg6HmJ8xJZFvifdln5bh0h48yd0Qgn5oRqe1pNftzrZf1yUaQtnkxkcJLkYAGH%2BCF%2F%2Bi45XFf3O1k%2FYufKO&X-Amz-Signature=70444476168977a2169cb40254c1f71f4d8c97566391caf8ec6a2da15b7d249b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


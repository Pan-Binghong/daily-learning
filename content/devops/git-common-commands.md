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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYYIXUHL%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC1%2FTs7ub7c5DbB5UMnOGZvsthpxX75dZEtfP4o0IBwJAIgd5tTXoa50cIRVetcnHxszrbVEj%2Fc4LgNs4ixJn0FMcMq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDC5G65umfRrng%2FatdCrcA5qLIiaYhY3EnbsqALy0dgNATkQOOHBTD3GVdWla5VrIKKM%2BbgO%2FauOUBH%2BJCjLBQP7PwjtQYisx2JTEUBqbDYH7X%2FoE8necCb%2FwiFIT%2F0U7kSi0AlkfUWaE34eFx5zEWCs1bK9jCOrt2h0DxxsLFXdU8nZ38GoslcdiVpIE7DO62eCHvd7ip%2FI4dPA8R6si2%2BMkH%2BlVQ0UsTeWwO0QggWmjDoAVAyIMJs43WfKXzkUEOzrhZmzKqj2BO2%2FUD3XMYcXFcaahT55drCF%2BrTEkD7GYpCpkdBiQgW0HjImqZQFMEtZpb9cQxj2TDIcVMx0CIkp9GunsH6%2BqjycSipYGmJZE7LBVMULFZjejzdlkRc1%2FVrb4aCSt%2BnJFO0OYQToFbGDDKt%2B2yDphOOa7YgtPnuqeAAlXK7XELRYmrbnmDoFG8U9%2FHNZjGBwi5DUOZhZiolSlnR%2FvRLvlQBMXfRyMZtfWQRhOTasjqYqn3zRf0xwBHk4bYFNXMUcBGSkNsEbieKxFVGWC9JiZcjDk2zOxRloAJepXB7ai1Z0TyeYf2LjY7ezJZ9%2BCJIc23pk2MvN8Vpx9UKJ05H9%2BSWhpRFZ33CPoMSPY%2FGHT2A2pdiMTA%2FWdhwOKcnI%2F0mv7V1hIMNfeuMkGOqUBWK4Ml5RkTYOC7Zsyavtiv2HpjXretEDdOeHU2Q9Ipckq6BLVfxuwMKtDYSpcu4cma80AuTegUNnoKH8dZ5QXHD%2B%2FpVLT6oEKmJvsRa%2BSQbeIMcbMa6gOVK3W14tVsfZ9G4C79FDKSUeTv9oRkUJACZY10kiFJm7q1vrNiJ1SjzNcnvdRvrgBKUruvWNWXGMMwIadP%2BEcaRn9mULK0eaG9ujjaXrQ&X-Amz-Signature=4e5dd192b48284e4d8320b5c1162899789a180b47c4891d38da92590cf0eb184&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


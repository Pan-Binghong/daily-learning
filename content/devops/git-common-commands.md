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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NT7XS4E%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEVCpWsqZ8SQjyEcteGSF1vl3RbntSepWsB%2FVpHYdvwCAiEA3B99PGgGHUXIUhPhIEOEfw0cVExcQlF7sgyKE8TYv4wq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGCFU4LX8jFvadL82SrcA279jN2O2zDQPrpbwD%2Brrnpg4D0BfUXwyYT%2BsCog4xiRAc%2BXizj3%2BCn%2FkQxyAG9zuPK%2BZW0UPn22kW%2BOFus9951g6amkTg%2B2SEOqgweUZhsdyaeNQEjLVrqBei5QJFvn%2FXIU8d01DqUWRkogmNnyBF%2BNNP48KoGGHw2%2F57mNbA28yR3UUa%2BSP7o%2BRW58OQpWriWAL5MEWTeKvnFWHfou9wocqxg7YAcA22QnhdC1kapeJTgmP7Hf8cn4%2FITQn7OjDCyCSDDrIOXvkprLEqFHXc3YcMUYgqd1vrO89eZlOL1YmWpFQvz0WRsndHQYpWG%2FUWbEYWtRlaEPagfG3PIYm5WHD4iZqliUM84RdnKDpPlfVZ19W3%2B2MVLvUXOkII7JwF0aXgZiLM%2BEBJJbFkgrsMVHLX0mAKF1NH3UPj2HoE2Q6CKm48ycjcpccszpeWnt8U2yHK0K06hGDaaxM9FTCGVeQD%2BwfG4mO1Ty2GTqSsqL1c2FqfwvvtFj1vtCoRDokeKcp9UgilaG3fzavC93ef2v7pnbW7bceX51zBLMbcq6NyhTN9OYkBFahahb9Xkj8JtjZ3KMJcx4lD930j8csgv1qPKbfoESWpJg9ejGUHVhF5uK%2B683j%2BOHKaORMPSyiMoGOqUBFd6eWlNgmVt4oI%2FkSW2o4C4KBwCMRvsL4LkmItv435cFPqF%2FzoCnZoE8GFl2UY19Nhx3XmL0K6KHUhXpqzB7QQCLhFyYWR%2F%2F8zl0dJlqAZHv4p3WLgG7V84f1dHbhw2yQDcza5no6GLxrAYQ6tYyMWGSgRMpSZpv9HsyI%2FgvSp9OnUyvCxgvaRsw0%2FeTR5WsgDBjez1mapzx5w7EGUESiGzzmauc&X-Amz-Signature=03fa736160a09f8bf4c83cfd917ef87ff11e43190d79081045dba78ef88e12d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


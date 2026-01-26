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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5S5ZSB6%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIQD6aQEAU1uxy3UQ1u5uWnmeQg9icyiLargPjdVJpc%2FN1AIgbz5ioa7VTz1XiztLq7EA6uaa2q4psViaElgrx0eWuFIq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDE3ZK9YElZfyicpWjircA5GVKJ0bpmfkNOXfDvhVmES14CPC%2BnuVdwZ9RUeL36YpL99BHx8QgbvCVZoVmP41Ebr0FrBubZdTU3tgPSswL43NKbSdpmipOWGvbCn4IFgsKYuU8OEqOeaJxJnqney%2B%2F%2FteWNbF%2B0ziisN%2FcyezM5RW2NZ2EzbA6f3QoErAQQNcsHbFCCFsUEUrqHs5BWQW1zTf7%2B6YThrEDI6sYY7s0KZ0dua0sFRoXEmwFaSLZqa1sVp%2B7DQTnuCslamRwOX6DnuKzBBuhjKZbL3t2rHdxc6L3FbItmplae8zIDxTL8LiXrIhzu%2B1JRrH5vUQbXY85K95PpCqIQ0%2B8FBPELKdi3ogQx51RdJpnpa5arcrWiYcRhbQnVID4SpuUquCk%2F%2B9mieHFmohAiU5CyXoytUXhSnfCC8HotvakPtixm8apLS6cFnGqlmQP15wGos3TdMnj2H%2F8gx5N%2ByNAkgRSeGAzxjejmHfps4zEpoy9jxvwb4iQRpJBbjpRVPjO4H25sguLheGUIVi4Z5z0u6xvDrspdrzBpzQy9urhTNHfF4bWEvORELUX7ZIKUB2RS2Njqf9wIylLpPWHuxbBMW%2BVCceKKgXD4PDko5oBR3EfSLJqqQtPANGISf8J2p76pcKMPuw2ssGOqUBO6ZpW1b%2FNNd8q2qBrv4dqCY9UmaNvlLGnHaojt7B%2Fl39uK4rVOwB05AOIgNbfigqtqjaLIqW22kbPxf7gm70o0pZ%2BJMEQkI4xMKuidqMB3E3v5OYAkog2Mywf%2BIIFjqhHKb9o7af73DIHH%2BXQCCU4gKmTIDXWQDud66pBn37HvDQmhSEfeLkLsQqCKgWe%2BtSEOHmsQW3HK3PaoL5TvANf%2F3LlF%2BZ&X-Amz-Signature=9955ccf92591c0c270690663a2cca7c5a5dad1020284b404470fc3d720c4d8a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


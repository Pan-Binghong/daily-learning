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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BP2EXTZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDRyoTKBk971XSO6apzQJi70pcuOIl%2BKq1Ly51u%2BNX%2BEAIgPYrI7Vodsq10NBA%2F0Xp9E0xiYH2X5ZJWEJA6o0BpTlEq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDI8nNBkAcQdNuYsAzSrcA9eUNGyN23VLSmTjRVXOctXrPbBJwOpUpD8y%2FZGhP2%2F3jLtGDX8fVYz9g%2B4qqiHyXkgHAEbucC1WYyT2eQOBGCCswgDO%2FlZcjiCXChvlydcg0GuScdSW4DMjWPkMSZAHG1WoiO%2BOMn%2Bu8rVuR5%2FM2dd8l7cTB4YB25wz%2FmvHrU3wbXRJN3PZLykZtq2hO6kDjwYOtCiFgp4FyMx872kcM5WRqlIkNKGa8%2BzaR4lT9Y7gQj7FP5Hg%2BQhKKRd5YaL5fCO1UEOqgpyquhuf2iLRz1KNggYdgxVz1hNEh7RHuX2WQ7aViMIVmKCujMQr0aD8GWP0IDxfD%2B0pWSoxlCojptFkzCCiOD5ROzqsa5Mt%2BgQ1oZClguCEBy%2FZ9lPfMB6SO39NF6%2FSQdnxgZE2%2BMTxkL9sQ7mE%2FfGoc4Kaq0hHwhCBJ7gFup%2Fy60%2BJv%2BhXeHkxLp6Q5kDyRQ8yxrjXTiHnN1j1VQi%2Bs0rYZ5p90dYwMOOAAgmqq8szANgysayC%2Fy%2BRMlwvUc1dJaZozmQQq2Rx7U5GXYdzbVkpgvnxy8D2PNNLk8FH0Sa0EPvayQs5QwC2f0iNHciq%2F3swW7EgcbYmK795BxxGLNjMdUg7oxI69sCrw5qJtWlyN%2BRmqPyOMPidzM8GOqUBmlBwTUl6fAxhln5iRmG4h20bV%2F2nVYn7jUuhwF9EtAkUQXsnNeb6y07e8BtbtE30zkbhCC%2Fg0%2BzkVPObJllzAfU8biRQrHy6%2Fqr6%2BWc9E6jt83whMp1cMlhAUg25YqQMwIbCBPgf%2BS0gm6c2f5Jr1Fpso2kb4mGKySpEEC96dEsbFXXSe9b1E1gMz66kfRQDk4chcxOTn%2B6Tk%2BL8jiZ2pfb39b%2FK&X-Amz-Signature=418370e5b62d39543cabd62b24ad37a0c5dcb4ee52c137a6ea55132d682246ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


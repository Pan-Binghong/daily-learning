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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SVRWPR4%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQD1YT2%2Bx4RhStiWePu%2BbOzurS5%2BuunCbcP%2BnevO2F8zfgIgdCtXEiie8kdZWkNeH64Q%2FGiOM2jRgvSSOI1qJegYfWMq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDI75wcMjUUDXfjCmHSrcA3IDmBlneZKxk8A8aWeCjelEmkYWeF%2BjF9pLZqhMb2q5wP4mfRQB8ReETdvFL1QwrXZa0Pv8Yz0d%2B0QoXssqJq2pXODsdiZ%2B8a7nxvG8IF7oNBn8gsSDOTjffX9vaFWbDY6koDLs7FwbO%2BM0RmkATvxH2DJsSGf77FH6ErZdr9RmlYldvbGCUQbj7vDWrMA%2FUNKjST59x9MHx1lI9CQoi2niPtc8mzDyLZyQk3avF0ZLISx3lL%2F4jmrBdJZj9iBj9Ozszsda2ogF2DHWxxuZ42tFKrcvRba3cdyXQ1t68FXiE977K4u840zmRCMe3dS4q0t7do3vuBwxwFaBmVYn9f9ZEo0c62rBUGsAeg4SmjadAxKRmLYlK3%2FC6Xa9LvqVFgC0ahsLqto1B4%2BZ4wjn1e%2BRentv0V98DJcnaZ%2FD1KZ1v5skBq81spOgLsvXlq%2FTSAASsD%2Fj%2F5jnAuUADN4siI%2BBDyWLRUESjuUZW1cWkTMb9TQ%2Fqyynd3BnAhnuojLcsPiQayGm2tFXISrebBalJqAfxxusiPAVBrWnkupm1%2FArmfuw6gI%2FNvVap5kMLwktCLmm468FJc9UcqtWYg6fTTqI2R44bggROznfMkds81qMjIrieLbOzlneh%2BaBMICe%2F8gGOqUB6a0NeJeuPH3oIPNYf%2BYK3pJ7tmdWS3ggwMNmm%2BVEJuCYUKygFeDkQ60WLwpWPzhktRyaAIkbSJdF%2BZdLGG%2B73XrTA3AtrOQPTihgl7ofP%2BPLK4uu3lU8HXZujtNkns%2BWPrKumDDW3aHPuQagqWwpamZS19ZudPNhvENn202G1ooJqXzUg3u%2BJv8Lftvp7ytOYPrL7Qh8HsDvxV2EXsIPw8UZP6HG&X-Amz-Signature=2cb423253111e1ff29337ee118315f7c6a7a1c4b59d8ce6fe176b356c1db14cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


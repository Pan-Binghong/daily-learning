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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QS7FE3IC%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCwHkmuFLbV9m1LqypUTs1eUI3KLTBPvIJyUokFzISSJwIgPMmIMS6RMUXI7IOij0bY4J8LomSEevAc27lP85b1gbkqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMB5p%2Ftetzz2HeKq%2FyrcA79CeClnNUX8dQs0U1EZdBsDP3OG9dE%2BS9wphN8s5g3jAAe91RFKWpB8TiN%2BEyWk%2BMOm8IUr%2B%2BlTEHMRZK%2Fk6%2Fkyvkdmk6y%2Fyc4WRDYhWAleDWKefsrhKNiZJVkeSjP74YTA%2BNIwhcftc0JWrCPW3u6OK2qzPDNaDbtKnjlj9NmPOGYNdwf4FF%2BuqCcAAkwdFSDUh30otaEPNf2WFLJbtoBaAo1SauRP9FeldcnbbeVp1TP6PJakA5wBT45TVlGxBw1YCFFKN4iQPy7x6wJAaccqwrYAhxz%2F5UcO0%2B7EdMC%2Bdfop7AP3C93xiP5z6qrs7knDiKVa01sosXSD2yR5iM5lJ62uOMrNmhJcPH5BQP%2BFhzEc4m3woY3DXYkITvfsLkk9KEWPfiYRcqnGc4T3eDJLA43OVnnQ1B0hsf7v9wly4raLhQCGUenUCcI6jzYEJhT4rCIW6NjXSZjhPf%2FVRalj3EgX2C0UAyu9MHMIbau%2BmNa%2FoVOmn%2BoD22Kd2dBUbsdmRdkt0uI77KxIzD4zhAQJCeWUDtJzWGihFRGMx3Gq1e7WozNzvGDWfDS%2BVj4ecgnFty7yVbv%2FpNNFuSfnmlpcASLaUtFNzyDSMOYaGt5ZHtPG8N%2FtbbIxNAKHMMWuy8sGOqUBWLFU%2B6FYcS2uq4NMD99AtZdql%2BbUVKQ5E1UQu7Cg7g3pg78a5aXD4wtEI%2BsEbvVCHN1oABqgH48bU8CGgdfVjnDH5J5N9Gn%2BYB1H6%2FrAf24PDo3J8kuoX31BdG6PX5XoxSi4HQt2OI9zkwhDeCtiY1oXPZzMvCsrutn9LaASU%2F9SN5YAiOg3fWWkwk0LQjrjo1S5I5iU5Mo7Oml3Z%2BrMStR37%2Bno&X-Amz-Signature=e991ae6ca4432891ba40ff019c30181662aa2b3af17d6f3b832c0c4970a878ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


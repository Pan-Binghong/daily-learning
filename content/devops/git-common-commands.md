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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTPISSTF%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDBHFbND6nxHyY8X0cKsiF4q4KqKTdQUXAE79W6%2B%2B%2FvMwIgYNFZ8xydogvDk89cxbxyy99H77ShVsq%2F0iayyYu7bzMq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPg%2FXRBnKNta3szFxCrcA3Ghkl9xa7lcIjxMT4N4SRrTUDN0pHx5vgxt48sRtD2JdGZ0xnW%2BVV%2FHpjsrLfLB6EI5OhCE6KTpA%2FYEJERLTjYt8asiuHQbaUEtyGtJ45AKqv%2FFLv0ZyTzExxJwKgYigh%2B2Vcn1uqa21MQnNUs%2B6GPQvXUioyiEb4TZAjieCn2%2F0ZL2PECRetfHMNNj0l%2BgLUi7CAkzl%2FYXcTUjyiytYwUz3s1B5NKd5g%2F3qu6ik3BlIrNPrtop5ReTOHKxteAxozmxlUXqrL1AdNwk5R9ldrMMhidKqfwONCZy2wXS0PikbyL3BITRxtQzImuSeVJSc83Rcxnm0HTZljPoxYrcux39xsPBIny7akcmUHIj6%2Bfv1U07rhFrl%2Fdywrl%2FMgrpAA%2FWUK96QvyHcpp9lTcZDbbZCWJs9j%2FeoBLrn62kiaChXE01VcFvm3VO9qbrp4l1uQdCOsZlhD9NxyxwnZRDpfoulaAi1iEKf95bipyTEnYX0GERBdaTiCqScPYkGYcKTZtdA2amaZr8qCIgM84w5RiHYZajBdONKfI7Lg8KU7IhiI3xoc20%2BmR2LfAT8F06107VCAHAy4bTKDcqFqyRVc4oHw0aA9MCaMg2DLprSoGq1GpBM25k8KmQbZYcMKzwrM4GOqUBRaxq86qcQk5NlKh95f0M%2Bv3XxTSnmpB8pi8Gno6Yoy75LzP7d7qdhAliPd7oabfTLlYiNZnBtKl%2Bl830jZ5x7xHWQBcWqgdsouuerJZ5NADTihHEI4mg8Pqg%2F38aAtBvaAtOwuBtAR19sA%2B48DNfhdFHVbxSmw6k3hI4TtpdF5zjUqLDYUbcEY1ADprFpTqMaRDGcx5x8zaejKqRHjwEd%2Bme0Uux&X-Amz-Signature=431ec0bfc4220954b2656878a48274b93225820dade3479a15b3a041daedde88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


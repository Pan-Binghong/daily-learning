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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PMHH5E4%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQD%2BzACSU0ckNmrQ5Dz3wsrABKwuNvnjBTNjhT97op002wIhAKCpvBXnMOcJ2MVwBITiBPy4APlK7bcBPSvMtbyDp4SEKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNvzo%2Fi9K%2FNqvc16Uq3AOOb0Gr7UuczpjEgcJT3lS5tUig8kSJuPe0g03A8oaEcTiCX1XhApTo1Nd1EloLnTonBh1R0CTkG7MjiSCyMwsvgjj%2FI1VaimQtVrc9COMK4FYhSuAg5pq2fK77vB3W3asmSMQOOyZRdIsglvnpJ3BVviupdZv1K4JzYBU7Nitu7ZOw%2BSwIYkIeQzjeGKpt%2BhPQm4ons2weLg7tWZQj1yLNOHfsdnG5YY1XPnfFCmMQCsMF1USQShO0YSA%2FHLM78xcKGf9GjddTgZ9y5wxCUc6IjvWaZRwSsINqv3VQaphB5Iy1%2FxF3oVWZghUaip0RsksbDX4sxE89yZR9ITPi1qc7FbsE1iTKUP03U7ShmMJ3%2BByKjdOqXXDRGHS1Nvaa3xLd%2FwaZp9z7qnfWOLMNF8vYgs8gkSvO5rhtXhsUTj%2FqZD3TdNZJs8utzPSbr1kJUH8UiTfSP1bcDm0%2FQpmGU6jxM6p0KV3CRCRMHpv%2BzHhMLCapDUbggD%2BQCeo4wOs5KhlfIIFBzZQO7ipeZnipDWfWQy00LAbRzRyPo%2BHzYOz8hGAlPb%2F8KdqUEx5B8kKH%2B8EMZMGjleSv6ILIRMv6fyqK1pzdaqb9pa%2Be3vl3vBpvLW85nAsTpbEWcHpFXjCit7%2FIBjqkAdRzZblxcP48Z5DdCHIO%2FU1jL3sRQ21ZFaaSO8kM6ial%2Fa2o472xw9dYT19cFfjCxJohaBfFaF2OX3vP5WCvBxZmANkgghxCYuuiC688AmVVxJRFc5A%2FiFWUUv9jGedku%2FS8nE3ca8pLJFsFabtlTUcDX0prB22RkZAvrnQ2YRHNoylakoZUN1l5Pjp0V5K684uRQ6MMgPuoWzQVUQ9uW28ro2s%2F&X-Amz-Signature=05f016abad5d045c8703429770e6794dd4ab9afe8dc989a572aa27f41b730376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


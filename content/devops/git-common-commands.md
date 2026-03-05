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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GFE66AZ%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzVZ4KfEjMOid7BTkYI7Y5Mv0wcBOb1od2HAEhyHXJBQIhAMD2db2Re9m8P4DpxCe116DsM82tCz33Xx8OunmhoH8eKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZrUc1LH0eCHiWnZMq3AOiBRJKgz39PlXPOBL5oUjwQdOULU2eiPX0d42sIA9RPVdvWx3xzbpaq%2B%2B7S%2FX1dexl%2FzQNNXdkpsTtjB%2BAnrMHsjZP9uJYUhrEt9HO9%2BhJh6nzWMJlTfkP%2FFuMjrUgFqg4xkEGVhFyIEQDzxsKk3XoLWV7DaP8FK%2BMKF6i40UWf1o5fFv3DsikPRFs5nS%2FMr5uCZWG2nl1Vna3IcEAp7h%2BuoSmmRNJ7JacMcUsuS9dNJnGp9kaNJcIoV6a4ukawLXILGWSFCUFNC%2FOwFaQaSUBwj3MDpaGy5A8riWaEkklYoydhterLvO4w3F4ADyk6TWY8obaVb056o%2B%2Fk1bFZCLtcNjhgveII%2B41WELXDxhRQfksDWfO0aJlPtgN4P3oLp%2BNhjUqbNmYIw2ts%2FM%2BPN8kjF6D9kEwY%2BNs1UG%2BF2xKqJngH%2F0Ox3pOBVUOSHm%2Fahiq6zSbzQudjDw2tp4KbaTkk%2FFHwZyxdJaUmlPq2Lzg%2BCLpO1jZfuyNYGZlPZQUnE%2Blq0LNFs6r9S54bHEquoIGybkeiPhJNJtOnZ9rKB8ToCUgie%2FuB2xrEDsXez%2BnjpfqHFdmgf8pFUTbusTJe9VaiXmUqul619IHAdLc6ELOMyb4fNSEDWYA7IbMmzDY3qPNBjqkAalFQ9jAUCWPKu%2BUPTp%2BC%2FO86zEfbHCuBuRUbtBM4YowuRggSEt1G8SPoudGiqdwgwUMIYMA8SJH37IBk%2FkUwp%2FiXTL7xL6h8afcPRBSm7Deos%2BJodtcG4MH%2F5Zxf%2FuPZAGT6fH6MQDk9U0Jht6pbv2Cmyi7wINBvPVXu9Jp0AqPdE6eDI7Uy2CKc3h9uog0xpS2uBe3hVBYcGO9AaVzJnE36t%2BK&X-Amz-Signature=196a5f3209f2ff5be050c506d01897311aac60b0d554107ae691da8770b7df97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS7NCQPE%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOuOFYgasn3W7DRjTYtCzoE%2FkcAmor%2Br7lzHpfoo3LvQIhAJ7eNTzRkzrkNKHO86JgN9BXr%2FDhaZQ5SCofcz%2FNaX%2BiKv8DCE0QABoMNjM3NDIzMTgzODA1IgwQgjKiUr3%2FnvWzUXMq3AOw88%2BhHmEl5stJc7kKGFH4zGMRbaF8EWc9mqPbgzmM6kO6igqpvkviAo4kvrBvHfpG%2B1wAWnNBBgmwyIOJHI71IcCfIYbGc%2BREoLRyrUm9ULHdYjd5mh3u52ybguZreT23LUX5MPBQTvIhaOcYvU%2Fm7rln6jQ8M0KrrvNglBsoIC%2BbrMyaUp7%2BW%2BiNkn2y92XGTMcXDB%2BinxOl7vWI%2FvAmupUuHrej5uuRZP13cdlAw%2FIhpLtgIdgd7k64fGZpVe8QyTdcaZT4jsMEkruWvwuRp%2Fv6iEvPTUfuTP7be0vSMGBQvShBtYb4Y3UHGQqPkeDydHx4OTQvmbwVri17satuCHr%2FwVNWkjCe14AsFsYPUafR5R4lF0Og9zAH7toPRMDcZ60TbUF9Wxl9zBiRSl50718szEX4gRXW7pNyV8%2F%2F%2F%2BrtaZMlJ8FEot6FBECtWZ8YaibpbbQLjYo9rGW2X4QR%2Bw%2ByVRqVPq%2FqrVjGHGMDUSswOUtJr8TBbM4BCtRSUnPvMznOAj9h91ekjuvg5f7coPejEVqHv81H%2Fz3t9blqp4EYTOsVAEFS4419sivRokKs9N2U4rolqmhAuxiuLgmBfRYUBQLPl71V1OIsV1lVcTZ8EIvgTSlC1KcbzzDroLLOBjqkARY%2BW78JBaHGBWk8ymKAWybcvGxV0KR%2BtRPKat9Ot2XESaYhM8HO18hodAVag0O7oNLZ2qJhe%2B47l2NtFcGQVvUqec3i0gLEvuAe7Je%2B81no4if%2BuXH3Q2ruQUJQUYg%2BT2gK7E2al7KHpndS1Htp1GFfb19XUGpE1bevkCLB1lU4lwLtFYsgmCqQJtRSozo22sv3qI9woliWl0WcM%2F32rU4%2B8YQ2&X-Amz-Signature=744008f6addf9e5dd096ba4994055470755b570450e0b48d4e48c2a4d20d9f06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


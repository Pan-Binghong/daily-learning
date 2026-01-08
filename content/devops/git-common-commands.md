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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV5JRTIE%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAJxNim2HxfT6uKP5ixwwI75gaLKGj%2FXhK02Dp4JGX0QIhAL26bMDAh9VEd%2B%2BiyEP64wpJW%2BA5%2BW2sKTfQEqHdPK7LKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLjZAGYknl6W3ToIIq3ANa5dvT%2F5eNZTw6aQYAdRlRcWXmllr8kAxKzZdoVD%2BsTWjR20BLfiQAtfWb2kZaQl40m6KBgugLRSifJENYOvSAEzIADUGXSLCh25xtXDhL8qH30L3lxlTUzGExPnDHB2wajVZ4xr8mRJrZhP4G2mte3x7nnmA1umCbFQu61FBoVIUsuKP0L7SDyyIIBmZI3qzb%2Fa0VByMpDPXAqqKUwiw0DA7g4fDDqmYVHmQsubmDfEEv0gfZvms0fLlMVTBOzpGvnD2sqXbtMkxR%2BfW9VjVF5p8%2BBsdjbpJ7vmgqp1CnLo5kWp5cJ8bAYz%2BJcaFJcqp0dzGWQnKoz0%2BQVrIqSrlb16g1OFPbBwGJXO95awNFb1M0AvRbv3t4yH4gjPva54QnqnWaIOYk1zvm4k6vP9S%2BSLAqaZ99yUqXXCAGrU8Qv9f4v%2BLGVK2h%2F1naZezeaISpig1rlH3%2F0%2Fr9M6TMurWY9pOxz8vm6SqMZNVTs9Rnh08TTCKGeVU%2BCiNdoNNythjzU%2FywYgCvaLcXVRNwvkm7w8%2BdS%2B6VP5RcKPWH9oQF3fGzt6bV8q%2Bhy8%2BRFWHF2H1rN6C3Etd7O8vwZRJTcJi7H7vunIu8yUIzTIYpjjRVw%2FjlcrS%2BQm78L0WUBTDrqPzKBjqkATeFmlf%2BIVXfflOum%2F3pEhpoYhMVtAej7BlTQNrYqyPbWhVgyT%2Fx%2BVIa7BEvpY5PZdGZKss7gfu8lBoyExzFbPuzqfXU6zdMhCXIpLXq6%2BvwSVVPCbpSJpTj5xOyGtzsavZ%2FbcCdV3JI4ocZDRRe5owyUIoAhcpT53aqrZDPQy1emEAnGRPrJVnCUnZrGPz9zOjwzXDNQH5P1dv5qnEYEhXnI5Ba&X-Amz-Signature=a4b83e985ad39a4b1d10ac5ccd5c253ab2988e32253f7edf32002e35cadb701c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


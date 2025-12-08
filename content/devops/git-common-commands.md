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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642VPUZ4Z%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbXnWcGSpYkx%2BIijXtrW585juxRRXsHIflAU2NeRGWNAiBnC%2BMlIbynR5ZU7VBQGL2OMtCArbWn3eZMI3w9%2FG4IuiqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdGoFzOPxF%2Fwv7vCBKtwDCnTve87raknTpcHsSA2fbhHOzElGiFDjy9BzAgExdsCw1M8xIIj15R6JGGcReaTrClWrjdEeJ67q%2BqA%2FACYudeZ4c71S3y9Sb0mb1iIlTPkal%2Bb%2F8znLFGMyTBC1ANo0U%2FlAidHcO%2F3K2Wh5O%2FEhRSsM49%2B%2B%2B%2Fc2OGHcD6%2FccfLa0UG94Gw80UfeaSIag3EsUvx1onHfYVPxJ20i6eSspAFYmqcdPxUX4AD4zt2ozzq3AIV7LHx%2F%2BeQHCZd%2FPzj9tOvKwuNvQwW2DrHvjenVueXBEKxngwaikUH7b1p5Hd5vduWynFmEAEuV7oYhkFiPnBba0LplNjIj%2Fv%2Bv%2F4hVrBzpZhr34osdeEOTpPe3QBHaV9pxzHaOJ8VkS1EyzxEJiiFE27gHYI4%2BNne%2FcOoiUo0b7d4cSMsBO5YHkl9MpZHqXY%2FqZcjyRpHEFgMGeG4jAchnUFw37JDtlU9bHOW2rxIYwmcLVHK5QPD4mEJcbGKGtbTDqH5fqODnDQ2vSoVixZphoXKs8TXSMYMTZ1nRcEEtMqWteecy4aMuy%2FuRZE9zEUHOTHLJMD2SeUIBtqef2IO%2Bs2IXdtBGUczwmWXW0ZGVe1C%2Bub7Hpq70bv2%2FsBBHiXN5Tn3%2BHTo4MDcw7u%2FYyQY6pgGCpGYR9e1b70kpESZwN%2FInbIjMMhK3ZBhH53NOmHUHz23bn%2FNkV%2BADT5Y99XKd%2B5JoSGu7SF9niKVud4rMBsa6J4CQ0eq5l7otwxstb3WqOPx4HmCyqX04f7v%2FugWLL5nVxIVK3LftWYI8Lg6CrjpUxTOMqWx6AAN6Bc5SARaUDPlOYSqrgWTzJObpOqGRBQyF5MjSXCsYVcTJnczwG%2BGKkCmlqVm3&X-Amz-Signature=d138e3d28d24419173c4dcd67d5fea2696fcfc02a7feeb94d7016a30261a3998&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


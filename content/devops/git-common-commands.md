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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6MHRA26%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgf3xVWjaUey5QrBhsnchBD%2FRL2TRPWDDN3nGjq8P8yAiEAly1Tz9fAgmU3iV%2F%2Bt%2Fxauown2sPLltm7ikc2A0SLEDYqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FLxsNCcWlimKb8VCrcA%2FQjHtamLqWuXQSXqecPl99PQD8BdkJkxPBHQ%2BSIE5jnEWOx1TSWfJfaJgegCSuYTGcL%2BUQbJvlrWx2v8Nwv42j1565u9ODcM%2BYsbR20RVHXrfoRm%2FaOzwW6oaPFdP3OHjSJZrR4GvxN5zZd2y2Y8mB%2FSTCNdKNQU76YMa909Jd8WkkH5KAUJtfhhyn05eAbOkFLXxUHGtMFCCNZQRffWRcmgphujBMFo5J2K3AMRVhfbeveQfXGBz6BdD034A0YZwfAt%2B3sDuulIapTYswcjBTdNZ1dD%2F92594J3HsQkqZisxmgkPboB5%2BFGbH0OwwbINxVbQbtSjWqYnboBSTzND6Dct0qO5oIlYq7dgCiFUaR9hBC%2F2vbj4O2fLx3JIADXQLbJcgLz7tTM2hHr9ifLtcCbx0CcSRIpKdvmnePaOtTRdpK%2Bg4xnHr1kEzkX%2BioFLJSnxNErFcvY0p%2Fkknm%2FK35yQxgUpasjC5dPm3Dwb5KI5pVWE85DVaqboreBRn3ReBzjmGLEh1wCXndam1TEULfjMSpiiFV8q%2Fg34m0wPjzvxKWXpYPJZBVyM0ZO9QuSAucwyRfhQXV78ZPEs1furtutoFoqMskg27oIYTveKPMvn8FBGak8lF%2FhTNPMO60gc8GOqUBm8NXXZMgQgNBLM5yzzab1ELXhuZ86xz0ipFydxTHt7TsuKOcuWsCrxXEDtcwBPCsTSleVb4A4nxpc%2BQNAFD%2FldKXkE4WgpPDW%2FlwdOzsh0CnHUzaPw8POqX3pPgaOuBCEhnbcuBEiz1dAYy9BaVFqlhDPptsplBHVkr1kgY%2BgJljIpM%2BHKkVpmtBnV55M8eHIeT5xmRhX2N2e33qVioxud4%2F9nn3&X-Amz-Signature=e95012db984216643172aacc20186c3c1a48ecf58cd58dbb2bd4a06127532d05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


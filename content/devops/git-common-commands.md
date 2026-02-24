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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NZNPBT3%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDytue1TVioK4v7RZOvLWlPzxTw%2FkXIdIKudybd8mEa7wIgBhLOPsro6wWzd%2BOulFQQkWaroQFXvqo3oq1SRH7uxEIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOImC59nIAAjm7PZDyrcA8mnLG9mxL9x8mfnCGadv%2BitQrO1AYmgp%2FAhhK5FPDuN5ZNT6WdDy5zQrPXvqQtuG91RzCMC4xPZ8Ci4600dIqPX%2FyWFr3M7SBVQVFO7axDsPwBf0G84P0UngpfVSaHYTjVLViv2i3aecnkUOl2BIBkzXDMrsUuzj%2BT16GXEmfee8fRVuHYR1y%2BoT3emx5eJ7m91r5Cfv9rxvUX5Q%2FwSPtIQUrVz3fo4vvKFXIAOPm4yjHxE5QpLRV18ByBhTCGOQdB0AuWWZfaXnUOoxDaRJ9TDTePqBumd8z8w8IOv%2FeWPIZIGbpq2vIGVvkNGTonMsdJZPEN%2BGNoplVnyQAMg9XJrW1Fb%2FBBEqdI4aWplIxcr%2FPru7%2BxmuPj1qmAWL0ofRkqE9tZGcfwsnXnmz9aDmyM2wSMsyWbEx4%2FIxnOWJb8zLiaAuEiDQMxdKrR0GaXwUnwcBQBQEOaYRL9JElv0PAWVA5OtIYG0a%2BkEHsLwhVqjpEPjAto2cIWQfmD9suO3hGzmLKt7gPZoSEmqB38siRGAbwayvNmeI8UuqWMz1CcnYIDq5l56kcIi35%2BFoCBl0PFOXWXRo2w7PKKTzc5goIGPijVemrAsN%2FobhVCSgtI%2F%2FaJ%2FYP64%2F6dK8rcUMIm29MwGOqUBNyBTA%2F1jCO0HmOTgHzho6tMBVNJ6lmLqds%2Bq7K2gGzr1Y9V4VFqAWu%2F3tB7w0ixO6Z1%2B0ct3aT%2FNAEI9Ot5TVfqaaEYR7Bi%2Bv1Xc1cuOlCU15nB%2BWEMXa7%2BBcVbPEm6zs1HemZvvI7WH7LhduxOagaFyY1V%2BAbUlUo%2FLlju3EVdajjYOI5anVVV%2BwbcGieEr1kDaCDyrQgxForP6%2F4JDv8StBHha&X-Amz-Signature=9dbcbaf7208dd1278f23e49505a9bb59854e7109655c906f3dcd941d14413bb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOUIIVNU%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGdGNEELCeR8nWvVajYF9vWabO31WhIPdqpEqvptQRFCAiEAjEm7e5MCDg7p5xpBhkOVxWR1ufJhaxhSfglWAa0oN8wqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN5OxKHseGkCamG%2FzircA2dp9NYN7stv1sdL3pvNlynKDombWWsbLRlPPozelb9QCwH5fsAAoHHkKZTT4QAuPdRYRAPHTkS6OjGCpVRoYU2Ddv05ZWPXnZJXVlJI%2FDoiCDemifh7fyAHJsylT0C0YdUY8PBLZsBH1YwrxHyYwsSdnYg3Cz1KSZp%2Fm6knndemYAjkrjAI0YLCZdRZTWJyrDPC03AkWIgi1qaMUlkiVvDhhMaJ4Ct6HOHB1PnWYFfPuH8Prfv4GFteB84ptciNPRP1ptR6w6ZsMBqTovASX%2F1Lb8m9Uw5vQwqHdhhKF8niEYPIEf99FFA2TD6EENoBhk2YvcLw7oS%2B3ZEHtcz7zIqtSldAK98sf3s0IC1VcMIez6nECVmjr%2B2Kf4qgwhlGTe6db3GpAarMQnQWLNnzYYbLNfSaJS2D9nNuSL6Jmg3ZEa5DAAIHeiceeU9twTtqmCh4GeigJVv3vsurWjLz3LVNveZ3c8%2FwV1KJ7ZGcSDK5pjpFywvgCm61QRGNvUJb7OMEkarJoB6fCi2g1evHiwJD77j1fF%2FxeIEmc2AipN8hip69WVPfaMj9hkRiK%2FFB9iqIkSzGTw7wcPpVP6j%2FPVHb8wjfaYfXw%2BNoQQCD3%2F3JBrGsnV0Iel0e%2FY86MNiXpcwGOqUBkTKRM0IsLcrqr83bL%2FU%2Fk9cliWuxqOaN1AeEHtwJbLTxvcrd%2BRcZ9748GLWfCCOeu3e2%2FlVkGq97L1Sl1go9ejMzLDy8RYzWodfCk96P%2F0U4YCP%2FszqDUSlR%2BTCfGX5%2B%2F62AGuwZbwoYHEz7Y8QCSbUJKt0tvfIy%2FdStFrNVZzSata%2FC0oKhLRWIjBHMKpRap9%2Fb5ut4SzS53hR5L9t4xNmHszxX&X-Amz-Signature=9824c8aa3bc0c5073822e8a9ea8f7628ee02627d03c7fa88f700876cbcbf85b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


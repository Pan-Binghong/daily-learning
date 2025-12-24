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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W4TMD2N%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHxHq4WNTIouNndRqqG3jqQWSNKgcxJnTvjSBWNRIyhrAiEA6Zu9w8E73M2LOVq1tMgLL%2FxEji5sAsUtHETvc72JWxcq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM8lE%2BuldgHGQUHmwSrcA4mpH4NRyhQw%2BWk95vXLmKBC4Pn%2FIJVuKZiozd%2B6YQSZsMSr8Clfk3j%2BKCW3fZmT3jTWMhTbXT4vquJoBQaAz8b0U3rjCAmVsG%2BfAx7i0VL1zVG62FPZv%2F9NlDg5YO1iPOLG5%2B0vLBtXNp%2BOXAlYHF3NsEQlvKb%2BQ%2BHoXMKpVqxzTy5sM9izrXp2DlG11mVfbWqul%2BxCkPTAtaob69my%2Brx%2BMshBRstXFkBSYu0Qym5tMJJP20IrKuvzIDhx5H%2BLUieexLEPjHs6X5Aq9baEpR2YWEwTB1LVc7UTtZw89eEDhiPEoSNsXTSJXS4B6LkPSNNGPhZ4zDRJoku3WtEUE58A5lYg7H3Ix%2BUpI76b2AMTgrdCx4B7QgcML%2FO4oa%2FS7mqi8kLOYMaMVPN4W1TGYKp3p%2BPmM3orbhWlLmutKn49dmsQRtWMt%2FtCoaDcLZGnYTwmTzwqrgooCRbcVe7oCmqomlIc5o2ihttRvy14Ipubhickovkc5NSpWnTnjq8f2k9aJ7YTfRnRmWZN%2BvBwCEnt1yiBA4iPaKJM8zu0c%2FWtumwwAytHD0Mu42BV4mxTgN1Ma2CbUYC%2BrqJeYHnwT9vp4zLLvNhdPBJbZp52x%2BApnhIfbaiwuoDMOkQ4MLfgrMoGOqUBoh3Pqxom6odGb3sVceVGJvtZQzNOR%2BqBHT0wailVYGgpsfszEiiei3a%2FPUFxqGZVFaz6zpnXrMCBRbyYrjUa5qIzJarqgAdjo4PkJrboDeeqCdvhhbI6q2pMb24tvQjKeJIvVTb%2BEWZ9E9%2F6vGnwR5q%2F37XeCjtL3SNT2mjTWTWQDfUSqQWdHTku07aUBy80OphAuEEXWk%2Bcx3ynRe9ZQZ02TI5w&X-Amz-Signature=7fb4d809ce98c7ea881e6a4149d0eb4bf1a234c2fafba0cf224e2bd43499bfc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


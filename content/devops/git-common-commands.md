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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2JUFYAF%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BS2Zy7cHaq%2FRGd0Rywj%2FubTPI3NdVN9k3wV9jfvIyXAiEA6IoMwsyLV%2Fa3ucqP0BkrrLbofHZOO6414s2YbiQvcEkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfQqW6j4fMwqTRJAyrcA4E00g1EYIkH6757v01XCAzl1bP2E%2BRPWNpTUKzj2hgEE31H9McNuydvnnpTDuJfHYTNwlumoik4UpF2wbnxM0OinqhRYXFCHXlyO96qdXTMVhbUU%2F7pRg5cfaxYoRAqvR46cyw2NY5LCnn0%2B%2FbsJCYUapNKO8sBd07nr7ZpGkrznRB2jqYCDF7ebMBiTx1sAy0xpkBkfaoVZeoyo%2B04u1fiwVnctBexcOAVkI8YjI%2F6AABSmE%2FKWfRZdmQPnLjGDG%2FOPsxaM9u31bECy6aMgYiRLhOmZzADbrc2WwpaknH419sU5urxjLHLFbcvThovaivOVAuvCGtOXhZ8EmkdNRVE3mdbqe%2FGCupWScDMSTeDI06rbmBthuxkW1T%2B3raChPvBQAAGm9elcX5nEEM4IKXp%2FynZzry6ZWR%2FMOORfKxia3Z16jWXc3DfTctO2LsErkUh8CkPb4w%2FiV%2B2UuuONopotUTC%2F3roEIp4%2BZiRf6SAycbZP7BL56Keu6Q8%2Bquuisy2ejfV%2BJs3eIqUQA%2F871%2Br9QpNZgZTs%2B7buLESvvoYdNL3AwYwioGU6Rr3scuFSZQMSG%2BXan1c8SchLpPbNK5b4mNlMT5D0XT3pxmHc0%2FAEzmum%2BgF8CO2D5bpMMCO3skGOqUBBFyffUdKkBv9xl9smud3QzJS1wz7N%2B%2BB2AQjgFEz7pKdML4DghfPGJSFlaSkK%2FDXgRd4ocWmrPnnBJQKKU%2FnZvDf4G1%2Fqpzb134n%2BLjYa1gMzmMoPPlD0FziQRUUwrZreWp0Ct2LwODhJTON3o8bwzGkFeIEdZDcQTaYqk42h%2FmX6EJgJhEqEZGbViv4f2oh%2Fh%2FRVnv2oAASE91WZZ0xR4nom1uc&X-Amz-Signature=18a73d2c8dbba36c05d6afedf7123e465516a3853e442016eb7732a6a641ef8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


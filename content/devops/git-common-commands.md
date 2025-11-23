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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HDLOQJ7%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIEwMMXcQJumTEaXvF3P%2F3u3DE3o4WVGzlYZ101VBi7kNAiEAgFhNDJ8mXV0cM5czpfxgwmyrxuQ9o2%2BOpR%2B%2BruBl8XEq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDLcEGLWnb4lmL0%2BW8yrcAzUvkm1%2BB%2BLMuuwipLb8t1SDrLp1t%2F94K1zOaA%2FlREYMgdt7lJnh2oyxhMJcwtNZ2GEJjedaSW1y1UPHXFuUaC4UIQfnt8NIu%2BPkCCFCD5VEt206FSm0mWbL2aotuQg8oD8F1RveCqecGf0UQ9ydCwvzv1qbqaxJqEkAXkmx23WmTltUGORWnmKf44m8Iv2MP23esPbCxSsgWp9SiVfrAQTJDRMADCKwkUE%2FjdNZpAXC8CD76f2uBZeuYHqLZwqy1uY1FmiLqvUj3iQpYegqAv0LyEBFChIYSBqOZ2fWN8nIVudXjlHqgi1to%2FqALFM%2B4r8c15Gb3T%2B9Z33jNFW67Qp705ZEWrtTp3OOs1N86eaqsheaNrwXbeojhNPBrkmK1UL%2FWCJG%2FPTRgEuxsYOKzTPneS1DtAysMYRCJB1uo0KcXEiHBInyzMU4roVnL9lvDsePCdkV6a6bjeAfEdYNQAWFrO9jMNK4%2FoIQGFGSkmfe0VCpYF172OVbZcpxApzPUd5YwX73Q9YPfaSU4LTMihDNP5NvDQWUZGMF11F20JxLDE3OwTxAPu2WQ3C8XwNq%2FXAVHvusW9FxZF%2BiLa%2BBd%2BEg9OEkUlLLroU%2BWi3zLlVFJwdcaM1yPVzfuRhAMI6xickGOqUBtov3DAV8hrWHri3iZb8b0ymxg9bw%2F%2BkXoVPXR79SbUoXyzLNe4Hpyg%2BlIMWBpP6cO0NKli94HpV3PaJaDRkaLLLOVFUKPtQB4BCLr%2B%2FMVWRnnF3sDMfJbhoHeptT2%2FY4tV5mYkRCmIHo4N5u0an4ucTB64LK1FRTFyykD89QV8d2E5JT8%2BYsCwGxW082O0fKSKX4mFM%2BF%2BCW9DBSUdUjGZCdsV1a&X-Amz-Signature=47da7c9bbcc60a3094c52809cd84c0a4a59f01289662d80f8f03634bcfe4a8c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


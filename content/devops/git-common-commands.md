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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466332A3OGV%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDKi%2FbtCJrUtnCMP6aYxdTocS%2FWvWOVdpRq%2B0SRzLpMUQIgUz3PsluPc2L09BDOih1qPdCrjv43CAxkomS8zOn%2FlTUq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDIKTU7ALxg%2BP1Et%2BCSrcAx542lSk3wEWxhXOQcXeuozzEtgV3eWvRrylTWE%2Baq%2BroV5kHeBUOF1swQla5EhljzS3YBKJ6Va%2Fko87Wiq%2Ftlg%2FwEdYCL7xcgt4Ota5ZF4hFh2P8bDEFBJ67YegY6jxRoG2ohJ93JBtn6pg6NiMDsw2Z4%2FUz%2BCIRfyEwqM2X6wVj2Cb8C%2FnNcinTu4BkOocpptAj7regRrOCKpbF4iSOon5UzRwCl9YDHJ5Dnbmyetl4E%2BA4Ik54UPW5KQoaJnHSKsAw94yrGWWz4Ujc%2FC8IzlPVJak4wM2VxBGNi2nHrjFy2O%2BLSpCziROLFEOWTAWW7H3hzdI6gLshy0%2BA22kiFMr829%2F7HUlisCzqMYhrq3jZRxm98P3ayE8DLCVqEuG6f6wwueH8XDIoUWHtPkIcZHdRGSlitsVM3A7gD6oob8%2BH7WAN0H4q0R9Wj6nuQIGa4qtTTKtF%2FNjZ5AlM%2FegyuqDZqj9EImPQ%2F6d244xnNSUlbrxoykooNDnSKiJratmUKGi6Hl2AudAfDRjY9IxIW0%2FMl%2B%2FOA1phN4wVLo85WQOUs%2F8R5vA4u0CdxGrzJE7IAYr0Gz2BhgC12fxFX3EryKh5fEuQ8SyitKVUtJbRO5pX8cmlGacdx7qFQlcMN248s0GOqUBSWvsWo7X9L8KqkzbXdRAkgSKIG5yshiqAzS4Rx6cOfqHJ8lSQVIbGgzACe9H8HHl3ehNmhkW%2FMWNf9%2Bcpelz%2BA0A9R2BHunHFrVim30zpYNu8CojhBVCM5dlRTiwBTDuCr5tGSP1fIBHRmk%2BpYx3SXDquT07q0MFlv1jvoWajVRX0HRHe95D8UXJpo6v0iY4FFUrNFxwVnY1EtEXFfVcOL47n43l&X-Amz-Signature=078db075a110cd5bbf761a72b342e1bd8e07af98cb3b20a7b5ecf8e9a4194149&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


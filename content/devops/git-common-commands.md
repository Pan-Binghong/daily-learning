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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662EHERFV%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYWrTw675oitzh6xtsfYsPUPHfNBU04ekqUGF2V8HbVAiEAsvwl5FB%2BEsYiZgg3uFkSST0gro%2FFlFLhQ4bgs9kj4q0q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDKZHucAT6scK9TZWeCrcA4yiZ6hDx6NZfODi%2FAZCUpBVRpbctguvRlaWy5FUKJJZFkLnMgRzDlmaFmeUeORUnipxr2wiwob3UyEynhhRUH12xJKtiqS7kqmXDSf%2FaNGY26TXwAWgWTVCjGx5JPflnSIYzh5H2ThrxioABFeiSosi6tweHepKVJMx7z5tNZ6PIu1RZd8iKxvW9rGkMerbpJHhbCZEE5KZTRDiyx2mRLGdU8M9jjA6gsebpolNRVK7CV9cpi6apSHoeF%2BiEaD02m73AVPdqZmRC6K%2F7tK0Fm4FPNmmuIcG6YEuKgH%2BfekBya1em03JbQ7CeLUAUUuVieEyh1oXEV9wi%2FFiH4l6OeTqiWlLEEipor2wggY3i4c20qvGHlM5ZDXi0NuRUvmckI6EqMA2qI%2FzLqNiTvSTv20Lo9y3OgMIfPZn8hYJemxRza5z8sphTXFbarwRNsyJTVXtTYsz9QRNNhnTyih%2FEFYOJS9MekzjMski3Y2ltDQ80%2F93iBJAN2D2bEc3CQ8xt7pyQsDkUfRtmHc6a9jhy%2FaQ6KOFAaSXlKfWJCLt7rnYgDks0%2BB%2F3FYVKQ0Pffg2pjP1K0v%2B5sf2hqPLSrOxgxufs3bCLfAB7bnhZ8mvbbfcOBwt0j0eoGWnQeYGMMWI7M4GOqUBHf4fTn2%2FAd0F3VRASiXjpIH82b%2F9GfX%2FM88Erk9cMTxRMaXbrdhvpscHM7SkeGpz6pcRtTDEEwXHglqy65gQ7816LZaqGR3VTvAbjgzC9waUjgyqx9lSM%2FWerUVmXAfWEqhVF%2F7qtESYqAetHNioPeVoB9dY2hkuxRQ3%2B7qEaj2s9jBF5%2FDAGxJHCRDyIPD%2FJlaHDGwRJi7yFmiwLcbKll4A9hoA&X-Amz-Signature=fd6ff0bbb385b8fb2385a7d005fbb3a20db85e360eff20ec62ccfeed599c40dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXRYXAO7%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC80dToYwaMwvcoDWSvEN2iQv8sOjBGDBbsReO25kSsMgIgQ%2FG9eeLuBK3fzv%2BYViwqRbJ5un1CqGR%2BuMS4YSYTeVkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGUtdyIaISdaR0H1rCrcAzkqs2uCnT%2FpyEbYR5hJ4vsq3kcN99Il2MG9a9HVAoIOFn4UtbmwhcnimrravFvmtreySG2GQrI2xcaDs2SgkIxDlZgXpzgJ2NlhHpjB%2BUhDoYAiJRmFg8ahb9X8q5Qzow39C35jAAGKOXfDunoARsf3WMJ%2BfzWh2d%2F%2BDFCJpkgJ6KB4Z2x2Di2bNtzxZB2E9whpNN8VphKyOOC5WHeJfxetS%2BVKl%2FmjDy%2F%2BVF2%2F4jEi0IFYis7H1WnCSg2vapjDHf31RowxZC7%2FtgQr7uQ97%2FnWjMu%2BWd85IxhHUf3LbnYQsYxoG%2F%2FBGoAFuEAY7s5w7t%2Fg84wrO0Fn25LZ1og%2FAiS80%2BeTPn6%2FXs8KMvF0SzFlYRL9IzTaXq%2B0No0BgIBBtB5oxPWYe0iglMjlnluOeeXfI5Iof3rhGHs1qnrYKTNAH62GnjrHeE6%2FZJz14MjjBuOEUalExKvmQa9VzCuiFF7MKWUTp%2FWnGf7cKMU7wHt8HThVN7x4j2H4wHSQqhCKijdrKcIeBHHV29BujFTZTtGnbucixQM3XdcWcO5WCBgWvo5VRBT7%2BXvJcZmO8MHmgBIOH1NfRkT1ISBFqij39s8SoobtlmvkR3Bxn3vVH2rznzKjqOQT3jKVG3ikMOWljc4GOqUB0r7skOgWY80lLlcR7nuPXw5PfE98DCGCeh1iwjUpyMxWDcve7y%2FTfQRFTM1fhCRdsdHbKybz2O8vo%2FuSmoP3j4McwITkcJHOFy2KdaQ%2F9s9Atnr3Pvkko3ur60wsA6N6z36f6baT6adQpsFNkTOaUCnzJU6WZm%2FS4h0VSHJ5Zdu5WS3N86KMoktVSjy%2F1PtRid9sFW0KICrqRab1mTbhNunVdnSU&X-Amz-Signature=c9a93ebb1d1e7dc84a05e1c9dc729a39ff0669b19564c1e49c3e496f163df1aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


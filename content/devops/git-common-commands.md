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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V62RVN3P%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgsY6tD0yONvDLSK8if3mzgWUtxb91jB8bnD1xpyhLNAIhAK7zC6zKPr6gSHMR1cr%2FI1f6%2FYmmLz2L%2FQ%2FwZNsoMNnTKv8DCH8QABoMNjM3NDIzMTgzODA1IgyQT152ep%2FzN%2BLolisq3ANYU%2BO%2FmFCw91RnKULTgHrxpwqmBrw72oJkdBQbI3NgHdlDIYLj3FxgUvDXWisg9u3xaKZWWSBrPCaxsohywp6ZUF6azFivHUtCzz6HPe7bGj6vTRPc37OjDoVH7con3%2FQRkVGvNjth1djYcIAvesmeoiwN%2Fg09Cq2ibY0b40OwdCqn7Wli4Ap%2BLzm9ET7PaHNLkczApWfEms5RykLisr8jwF%2FAyoOhGdZ%2FmXD4IXzT7K5xvyGMYDc88GmNG0aDyX8D5bIX9ucB2lJSxhzYRReoPIsqBs1%2BkJmN7QMW988onRey3OrfU63NlgRVQUxjJGpriIl0Tgkj%2BA3jSuB%2FK6RVbxGlbU%2F22AubzPwYaqda9LQnBW7pIM973ZgG%2BHympxhHb3YepIgCtcJ9TQOy008AG9XvEmdUzZvXWtTpV%2FQqEwXh0pPoTjmanKJ302ZjBUms03%2FDfs%2FDCATlPm5ilhv%2FBT2nsIKWWnkZ6xsrr5MBpV3y%2Fwd5rg1MpaHuAX7je25VfMi8U3orDMKeOG9k5P2JODke4cUuKmJSOZycEOjZBy486dAUKFVSHbNSY6Kfw91bcD5vgGZyNnbcKX1OnQxK1Q0XFC8PrYiMwIsvpUHtC7rjZUnid%2FZ95pUgKDCUrb3OBjqkAX3bbfPS0gbTvV0Y4G6cywOCRosLyt4au4%2Fny%2F%2FWezWaTAr2n%2B00b6QG%2BLteFo2%2FqOH2kOd3AaduTJeqaVBcD%2BGlxw%2FXVKJHbcTxvS0B43i7wnvu0JLHubuUagpr%2BIhcvG0atLXYFglSa5U7USkPSE0xm8S4IGmqSTe8YmwvSeBTw8CKVNcYVAT3DACMyclB%2B5xzcY7E%2BvQIOmt%2FkTxZAxjxrmSK&X-Amz-Signature=d5b9ec2c6507d00f3089e513f940a45eccc0f96cc57f9f4c1488acc5916df619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SQLD7MZ%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtpWKylBZ3uyH%2FL969ieWiPXu3o7DqQ58GNTIjWItslQIhAOEeQnxNOOjJhnx3%2FAM74%2FimFcSfQOsWa%2BrbA6Um2H6rKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBEdqRh%2Bbn4HGI7xQq3APrEkUwx%2F3G3JhjygbQ3YbgvDHQdAVqTDx4NGU30PmaOwOJ0KskbjR4T6mj6NNK44jnHc5NhJRdPlo6cCPGGMJkrTqgppdcvMo8GSLUVlm2dUKjVHYSYHFc1UW%2BztFAjmTrwnExcXUxtyddFZmME9WcRuhEbPALxlOvhiIVpwnBnaE1Uqlsw%2F94CXtpcfN6D%2BOz85F1741yVuetJGWzo5yQ7sR52Ty27iYMkWYVCOht4QnmbMq7BdpEbqPD5f258X5Bim4IqZzHg1ZXG7dacRof8ZEcNCGro0oxG0ujkMJ7dmUN3SDpezIMTEqpDRvSDUC6EUcDK7WvHVOuP9eiTPAiP2rwCsifppykLA4nkRvgmphEdE0H%2FFBqpws6fOLowe0LNXh9Wo3un75GVrIgakXFbjof8qA2QYEFJtWsFcSNJAzZAYottNPUktMVAzYd0QRE56oA%2BLH9zh31GsA64%2ByaFtyZ4LhLpQEDxlfd%2F9FdNDK2l%2FnMyREyaPgSLeZbxnJQ4HHKFdVCbgwQ%2BUCU0CNfDMFAiFfI7JClCP5uviNE6BDOeuYpaBoOsXRdEhaQtFKKLh2PQ8NbrCIN8KU2ux6F9FIz3Ni6K%2FEWWTHe5kpOxOXG9Us80TZUy%2FMRCDC4kNjNBjqkAZbZpFYwoq4uX0oGlStRio346%2BK1WZaDswJloptUDQmh0O33tKYlqUYbZmhFxbyOg0f7lmUIR870wUcoZ12LqOON7cghOknLlSwWydhqhUCLEPN%2BR%2BwtRw%2FiXYQvt5TnLuB7Utae29aBLas%2Bd15A%2BMBFgtLob%2Bylmcy6y1vicPd1mOdkF4uj5iUEaqN60MYKuhKxbYvIqJMZ7%2BZnF%2B3hzaCinRzF&X-Amz-Signature=dc49cbdded5bae53840b4c96e3ffd7cc86292f1fc72c133950a8943119603d9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


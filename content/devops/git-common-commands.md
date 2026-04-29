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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CAOXHQT%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIF9Jkry03zQ3rXpRhWKePXpPJigz%2F78iO%2FJQS0zZ5eOqAiEArqnagjaUYGMj9p93egwEKzEJ1kBp5MW863gNz1QTjLcqiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrhli4vGAli%2BJIBIyrcA1qDY8Mff5IoU7dEUNq5QeIQWxysjNwzgN9K397G%2BHBgHU1p0wVeuebFlRL37Pv0ehW0Xh%2BWqgDZQA5TXycAvjKnAhaUlND1u9JyxtckFplofKOtz7hAZFEL27hMn4PyCJAqwmFraU%2F3f0qI4VnujwjjSJtF4Dunbeb9c15XkRlc0NVzGUbwrvq5gBYKqqSLwoWJ2eP4s9nHT%2FnhtCGD%2FqgxGDlsh4flxEuAEQou310KExlxW4Lh1%2BKF0wzBRx7BqXYBZ9AYm1AJdMzUJqCv82tAvxWsUc3s%2BEU9gTH7I%2FVGMgDX7NoOpaXmrmUuFoXc%2BUjO5knpYzY0gFHyf1fj03LrN2PxhpdgHe5dngwCHvNMzU29NZg4sCroOShRZ8iwvP%2F30OucjFvOxwZk0Z98ZglV7VHllPorTMI5FfYkaUHXPXcFkiQvywkUQfpspdpEKUPdvtDXuTVA29FL3pyjlO%2BTesLYDauXrbiyHHa2jvtb%2BJ%2FHPtHLUTyt3vrvTN5gKrlBJ%2Bnr4s2q6HKgCFhStslSPRmN%2BXNiRyQ5OkSNWkbikal7OqkW2BJlL%2FMo5efbdTByEz1r8fFs0wA9ses7y%2FaJu9AaswHA2gzJe%2BRD9Tevpz7A8vTEYZ1Vwjq0MOySxs8GOqUBEl9%2Fp4algV%2F%2BLarxCdkba1CEtSldw55UKJn3fkt4t1JAD7vgYuPuOSm7m3XH6l3ZofEyxW05ALd%2BQ4%2BI2t6%2FPILb3MRRDwQ2qyBM2WXdTCSyp1dSuSxblrs2llqjloneO8aPGZST2%2BpCB6B7yvixJ7CYqyHbjSYUjiTO52fXSAN4w8EmUvR554fwW2FEj8XISTbj1%2FSQzjtN84v9rhtOiUFZMnn4&X-Amz-Signature=79cff2fa17a4c07d176085a06b2c3b7e606dfbcae8ad753fbc447119bea50cf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


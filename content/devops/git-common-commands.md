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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XED2JHS6%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDEGO6iETKIpOorXHSoY3sCyXM6icmv2OddhPIbkCsNnAIhAJ6dDp%2FShKP%2Bd%2FItSmwv8fwV4H9yRdWvW6jf%2Br9ZNUllKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzf4nZBXIlARvNPo%2Bwq3ANG2tUiFI1bQZftWdGbd9tm5%2BCb2Q5GdXU4jhQKlbraI0mOV%2BvoRlK1pctIIn%2FWu746S6ojLSXIKhUBuZJLhPRrZEWLwhlYtBPd1nYKqrwlDtvNuBS1fdvnD7Q8W4V92vsXsu4TKSlV6qv5WbnRaNR75UjnfMC0TpzQ0AFya24pDv9WK26MHrjqcV1PyQf9vhllJBV2clfIS6C1pU905IeHfP%2FkZ%2BeEbKA%2F0vbStAneE76uNPGxv9RG3GOuM%2BoDQN7stqd7dzHkHhhZOpvgtACu9XOTZG%2FMvaxqebpVLymdyqsZ%2FEmGPHPPJ7fo4G3wi%2B6Lo7NQ6sXMFYzyUvNKliDr%2B6dMGr3LOD%2FzCz1sNHymEhu68AVMDS9N5QgPNl7cpSyBRPqrZ8fH5qwH%2Fso7aaKSRMzUKwbFivaPck0YCxEVjJVtd%2BV5TZRuZ9KSQERPRsNZxms3rqk3HReecSfme9yYZMoO0msJZs65NZ2x%2FOrORh9JT5oWP0MHJ6bI3nXF0nmdp1teQSEcsC1pAUxHe1Up2QzG3%2FN%2BKYZFqLIZORiX9q9txwPo900Vg8pGJ8MsrflKchE7AHwZrCv3Sua5ii711eHXGErfs%2FTWLJmd9f%2F1%2FKxMDl0byMwzxgZmPDD%2FtOjJBjqkAVzCq9pSgussCAOQLqxj0fjoDRgmPj2okVurrjId5bKcqmQ%2FA%2FuQNz%2FtSHZl446CZ2QzgEWYxU4SqtbTP5eAtpDXhZTLlTJlCuT8kyvHgbGsbr4o1vnRCEO9BeaIK0EVVOTJq%2B8muDaXitmO77HHaYQ5nDe8UjbXtNhalUoOg4A3KAVSPYK%2FQaYO%2BHd0qjJ98XLV07I7EB2H%2B7d1phAbxov62TzI&X-Amz-Signature=0fb560d23893bb9656727a81963e970a6f91f5e77617f9c1c2c892e1612560e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


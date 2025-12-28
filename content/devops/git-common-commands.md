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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNHADMNK%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhOURLRlkdURnVthBVLY5JQcQ235t7b%2Bx%2FLaM%2F22RvrAIgcRQik7sRVuGGqOGHaauxX0KRLie%2BA%2FHAJU1MwKySHzwq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDMBmXKkOe8LYBhOu1CrcA5oKotSe3Lg6l1Mjvsg8Z9sKLG9q5OU74H2rQ2o3sIJPhUkkjJ8cWZZgzlrC94gU5ZQmyQFpEjER6f78CDEbS1OfWzCju5sIQR2M7sGrUB6QL1R89fsX%2FgYAjBxIeGTKva4HBfwj5dJ1tB%2BzSAEEAymasib7tcSSYrzgJ77qpMHEO6K8lPNoK66R%2FDNUjlTzKGbq1%2BhIfqDzvl2ky4OmLFs%2BnJrdQFarHar9g%2BfLdwG0WQo7YfYgS2FnvugrmXCHN7P8ApkuxvXWG8F3wRLI1%2FwFNN6%2Bpy1jb3cu7U5uCKS5B6BSewol6zJqMrI34IF2h1Zz62dwe7Onr%2FX3ZrxnDFG1xerd5vZXUaefq8AWzipSaa%2FWDa9y2kUSsUEERpmnUTPsvoPxQyiJ%2FzATenhWoVhcwinO9DYll%2Bo6hU1%2Fghk7OQaprl7ZLrSWVy06c9Twjt1h26wHB0jCExzG6y7Z2XTTFVLygyTOkqJ9bcQKQAKbZwBZhasCWFn0yjVYJUaPzOo3W2EnZfKvZlynmrNVZxTdZE2fyOjD9e0Dq1zc%2BE1AIUp%2BjRH5jp8Vj0rSxXA9bYrIJuSJ%2Bzy9RRtoZKxWFXfEcZwKnycgEM77T2n7evh4nsF%2BTwW1jqBZ8CL3MITswcoGOqUBJMpHNVn0mV31plZcKaQQaXa%2FMN1Bi0sbDkiDjNko6FVCj40gfrhj%2BomH%2BgNVZ%2FaLlSixfI7BNAJZ4Eh9zHNjaxx%2B6pE7FZDlCrd36POYgF5tjkRW75wcNZX%2FtODifduYlBXdn5GASuClFdcoydRgRptET%2FIKZxhoYUzoYWv%2FlZ8etD%2Fxyievv%2B5gzChwORUbElJ4LtDU0Ys1pP7iwNbmOOSKYtkr&X-Amz-Signature=f93fb990f36d4c58b892c45171502e3ffe9b58546276f8bb391fdedcc35b98c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


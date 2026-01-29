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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4HI66V%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T033004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0e2DO0AiJlqAhEWH%2BPb87y1lWmjl%2FwC4D1QvI1zjwRgIhAJtcWof2NJff2nWO%2B0DmXZkpOPaZDc%2Btx5H9ZBqM2mPwKv8DCHwQABoMNjM3NDIzMTgzODA1IgysDlRwYnfLRGkEgXAq3APrrqdm9FFVyiGUOIMoLJ41B%2BlIzUpq%2F%2BnCyj6H%2BoifeuD5xXteRjw%2B0HUQxKCM76d2kWeDi1dAlow38YkYqKKNEjUHKgagn%2F3aS7WSVAYNWXJdVpjROFdTE9VNQq8kGXrG5hNreY3l4MYLprfdSKJ6NLoWzSOF3TNsPkS4cR0YXrTAX6WeYd8%2Ffq4KZmg7tpurzLYxtBkpSZNf%2F4s%2BSQCDAvo3g2Sy%2FTmbkSCQ78pULx%2B7pbfrcrNm0c0W1%2BtpCH79vE9Lci1vyw5fk3XlSK3DhvB9tcPdFlXe%2FA5FwcoJ8kxtjPrzhxC%2FwZlxsmNp%2Fb0wRqpyGQerJ1p16TzRYfRShTJJGnmnA37CZKVrX%2BqM4UP3cFDdhJi%2BTLoYD6b4vV0DVgdgR7CNN8n7n1MtwE8hi2SgJxkBMb3X95t60G7TkBY1doKKfIfds2UPaZVelCUwZUnaGvNI0UiW50JdNIx7X60YwmCDKcd4OH4mQM%2FHYt673vqQEclRUETqUYSH%2BCPsgroRSGXzpNCOVtIZT6b7dST5Y15OLCJBDHd1d8kmX58by2DxuIkLh1Xoj%2FEjlqAQWYE%2Bey6EkpY6j52MJ92gWGXSbM1PHD9JWZZqHDFcoSCRm%2BDgDAAL8yF8WjD4ouvLBjqkAbLJYkIbaS1PG8BJEFoa7IINNyyJ10lpIPI5KBFzlonJBG13%2FSOryJLnis7T7yy%2BWb269OvXB4m4d%2BcdGNpu%2BT%2Fs3EyuY8cxzeABG9OAmHmZJPlSdW%2FEk7dl%2FioRVOnn4yk%2B5c7xVl2eUAQ7ruxc8S3O6y4i1W4kmDPmJ4jqhPJYJiJ324V%2FFlPw2fHlxosHoyUfUXCcGtxIfT2ME6MqmAdBOPUU&X-Amz-Signature=162bbb9c47a34baa5deee5b8c1b86864165b7fa642534c842ba14ffd02599fba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


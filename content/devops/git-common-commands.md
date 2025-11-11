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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOBMXJHQ%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGPMFWnzGaUhMCwL4dtZbPThgIn67sxRTTteSTcFwWKEAiAn3KQrbuxEO0kD6sprcPAR8h3B%2F9LF2MGjyeOVybKc3yr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIM1YLU7Mzh35UKFeLyKtwD7HQXvR0ygS6RccyULONwy6GAmoXSRarxZk3szp0x7P3ZoYBaxvjwtHLdev0GVqfIDUnH3mBeMiVlp5OWgSXaYhgPv7rw3fGwq8%2BlYRDIMrq%2BJGKuJBqpeh65B6TJUfrYOtBUrlSoHqZVjKH1AJLZ5MxqNsbfURdUs6IrQZ3hMbKxajv8P4Emxbs4LFTDbetfrkdOAeShJTR0Y7K1Cmoq%2Fg00hLic7EKhEi0L5TxWJ6otr7PILgXt0ibb0y5w4ZeWJ7Tf1fQjNyZORZFFJ9v3Ag7ggS8U89RlcuTWlPjsm89qpWi2rrhHowED5Zz6jnXMfKQf82zBugrYRXdQCvWvAFxSxoWakBtqguPy6e2xgTO3Aq27d4ymHG%2BvBbLvzpkLNOyM0xwsYbEsoH6IBnOJIdNRuGmD64GW3F3SW3iaz4NSSXB%2BesHPIMLgHMZA1IxwGfIlvOTFuiJ%2BOhx2RbVoV%2FcDlV15r%2Fv%2FwsLSVGvkBon3J8PFuaQQwQOa6GVi%2FnSj5O99MaspQDP%2Bwij0mukkGco75QjXw17k6%2BA5q6WBkcW9gfqGZfXCES4VXu6M5UInbTMr5cqlcWGSyKDiJefnbdPQEH77Ginru3mt64PWsDWxzYp%2B2iN6hl2pf3Mw2b7KyAY6pgFFtCZoqLHLFvGUPXzTUlWGfs3%2F5HCoOMcn9kJxqBfPEgpWz%2BQY0uiOGF46Fye7yiRWPMkLB%2FQ20n2zivEJw7zWuHm4tumIvluovVxRYhYce7mQk68iBri5M9B0G6MP%2Fem54ex2FLKo1RN019ApjnlHQJz2rfeLEngFr7HdZodX1iI%2Bk3n%2B%2FPPg8e6mvX%2BTuIlfi913BlOk5qngJl1N3oRzIEoUy3yP&X-Amz-Signature=51caf087959f7c2551fdc521158dff99c7445f33076462167abbcc6ef49a9c24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


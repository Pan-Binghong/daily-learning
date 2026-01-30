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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RVSK4J3%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF1%2FH73caV7tWc%2FfmaMezCkPDbRHdFjGHyVnxG9XFQelAiEAlRgNsQt0JZHTpQJbJE%2Fg6udm1cxXHSCe%2BqQrimo0ELAqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BrjMCj4hDmbWHt0yrcA5%2FDXlt8FOU1Hq5k0fLnGv3EgUiwGpfr7xlfGw1LIOQ7d9kQjSKHf7yuh%2FA6P34k6tkFPtRtJ2lqWmkxgTVrjSFn%2FK9otkmIqfpN%2FdhwQCdQIlQAVQIYxqf79H1vUfqL%2F6KbKBrTyLaY0guDMsrNoSoxqsWT96crdT4PEBoz1nSRWdYXCjwGfF0pSQo5E9h6nEJHOFG9uTXnM4tpKG4f%2BHNoSrMuqRDolmhd4qz%2FX0HR%2FpWCxr5uL8IHZVTELAym7KHgSSCn0C6FGtozC3ezdVEjQikc8dEvB%2Fs6dMqXgqTyfBFImOhj5bb3DwDA%2FryTb%2BiX9csyvDWk7s8xqwGAoUtBT3CDWEMApaU72hR4vlwo8is59EtPLdW4hxkaoqufOhX6JE8ZhdXqnCo7L8TgoZHqVzlaOdtjHMx%2FIsD9JJL7dpsigdt3iGDkayuNXlUlc7ge%2FLagg%2BbGd%2FB2%2Fn1rpN%2BK%2BLxoyxI1l3EfQNPx7FMFUozJdLee96ttuuZl3amcWe22Jw6pcftmN3wCJRAJ0GH2Gp1RkZ6IcYTstItd30zAQacQrZ3umVnYx4MfzRwTvBaXsR0oIJJlc0TPa7%2BUy0liQ2xHLV0N%2FaK1VUnKyrf9RdnF%2FNiiICscB1TVMLfJ8MsGOqUBML83%2FXwZsGw%2F%2FogGZPb9N95SM3k9aZiKhZyG8Ytp86y9sgSHt%2Be8JhpbrbCHjxMmAHFeqMNLf54loLyAFCngscx5NXdaBJUU3rpY4dx6lefbYlPRQZuX3io5VUmzLy1B4MWW9dAFizdRWng2ladNZULcTcYCQShAZ7E%2FihIZ%2FB7f9paH83dSnIstcnGNXfA%2Bxw4auCi5IhxG7gGkOoNxJZeWHK2b&X-Amz-Signature=1df7b27b6819abea449a762063262c7329a6f1eba870b0c93243478a8ea548f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


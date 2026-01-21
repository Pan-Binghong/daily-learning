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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y42EM5YJ%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7R8mGdmyAhV%2Br9X7pcljQNykmQY27S7ByI6NqFFKsoAiBfCBYRa22R%2ByBjFll6BCaBc1Uo2OgOHQeJsd8BJKz4KiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0CnZxr6nzyO1MuxKtwDUt4q1ay0nKF9CVeSo%2BccL4tcxi%2BSR%2F2pLQ1fGat9jNqJyGMADaysMO8wdhb4BOsPT3PSR9xP%2F3mVqc7Aly3SvmseiklbuuszJJdzP%2FVx5k6lmf2s1gPJEccMQxlCgS1VoXeDYS3zwCYHq4LX0D52ZfrUBVQWiQr5zE260j5VSvuNwnZ2dS7h811rY%2BRU7ganbeoI%2B8ysoC%2BBrftzD8myJqKWy4Qqwc%2Bae861cJcXwpQ%2FkP%2B1n52fyoH9Aee8WvY0sHwKlr9a95r9kwaReBG90mBR5dlYiQyfMAGydaMl8JNNQQXYNka9Fe69m0hmHOOK4RB61oq8RCZ6IfCs9uGvbALhi8y2YIgW4k7RimwG3Ji4XnLZ%2FcscsfG%2Fehl8uBbloK8G0pAFjXB5v981GYgf3zd%2BEq8WzuEPWKbLg6DrQjRtz%2FnaPBgRh0uYBFj91ua5Agylacs8kiYH%2Fs%2Fipfrf4T9ll5SJRNWe3%2Fs7NuViR5qMSCwBzg1AtYLN00lnU4JoGeIK7gAE7CqUw96GX52uUND4K1KsjpO0BM08yQlUtz7ioabpuRTY1k4e23kI0OpG8s3oI9EwS1brbPnAIm1MaXdxSj%2FuTTL71hRGsLKLe0zF9lTVPVyuJ0qtOlAwpdjAywY6pgFWUsP2vMO28YHDg3JJ3R8KVgiiBg6oDyVqgv3F0J8jdOKplcQBzPG6kQJtfi1Iwv3sAROToph6UK9HtMSjSjcwOhLg0nC0ALpTIZb7lIGE68XjCH4YOniN%2BEZe6WT3KEwtiXPZWI8%2FqN2FEsbAMkHs9axvFtv2RM%2B%2FtC%2F3JAdBWSgh4Dqwg0EQgDKnIXICG265HHVHJaMypmd1rx1ycl105CIgSrhl&X-Amz-Signature=5fffde1b0db0024f6c633d3309b79c6b8e63a5bbe6f5bc47d6b1979b8eb109a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


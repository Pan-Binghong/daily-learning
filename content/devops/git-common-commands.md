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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6PA2MHY%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwBZXe%2FwxBoyWJo6IAUsqkbEGSLjHx6hLF9RDUxnmsawIhAPVFGEpTw2iHoJaSYCXJXlDBdpVU3DDHZiu5rpbOf2EqKv8DCHQQABoMNjM3NDIzMTgzODA1Igz8l5zXBf7pnlLdetkq3APvYTqGFEUG5RIi1r0B5dt9x9Q9q39acT3DsIqT56Ox8jVBACbk7UsIfLAH7cAckUKrYXuYT4IGNmHyMEyenI%2B%2B7YU6ujoZFyFgK61hQGoHUN3hXIakMZevi6Q38%2Bg1ic6Fl6YCgKoZbXRhYu8NnNMwSTfttzKzPWTQmf6ix%2BxOSM2PRUlH%2F03u9Crhp%2F4AkGUTvbmw8YtNPmFA5iFGcggBNwgCSjD9K4AC5BbYTzT8teKMvWAqSkTmo7GcPn4gi8v6SbSV3KY1XRTsk%2B4Z6%2BmVmCe6QFLxQff4jribeoJ4Vaw0EtO5KTI0aEP8o1pusyyUV4s71MqaZRhBFVaxwKmdQzL%2BkN86hh9nVVRroYGkq2OJ45nZOq%2FVjf7B4XfgFh4s%2BT6S56XTsfNs7K8U1V0xrFugEfWj%2BNsACXQaXqSaar5GN6FtVD8ynJG8OgDq%2FwPbFoRWUboCgKAR4oGO7y2WiDalpkpShF2GhMr4frt%2B%2F92eEwV7PZO11UvI%2F8KshT3HRh0KRUgjemPRlfGyKVLyMzJYB4KFFRESo8uOLfOsULSLAei8%2FIBewzJfZuRv%2FduUs8E%2BE3gWEY6HWY2XkvWZCov8QOxphVkX5aYvV9UVXJQYhvyMu%2F0JK%2FcOPjCXr6vPBjqkAW88M86FsV8%2Bdc40wYtbXAnivSyDgx4Oazq%2Bp6j9CuAHZVE3RhB5g7YoLv4ywJR6U12zsdxMoEaXyQ9ktgYBuE1YK%2Bogd2tj5VSs9Zpy4zXl79duEI96XcOjagBiAst0pkyzpnedL1z6wgRB7XKL5nlHHzZOBcG8s6oZdeYmZuLylfsmmoAPedicJvepuGuCCr9Nc8zj3nDqUdufN5uzlXa87aHL&X-Amz-Signature=61ee208302ed2a88743ae5a0a4a59ddb651aa0d250e39fbe86c8d83cf5257512&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YVKWG5A%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHRMbwR32GToDZLvmklpQgEf16q5JFwBjxqtxjrbhf1%2BAiEA2BEG0XMOvj5TUUe76hOZ%2FyVDevQW0GsJqe8RSECahfgqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAzNNhb%2BBKEmECjLSrcA6XRL%2B09%2BUKz1k%2FOIuSe0FfbAnas0Axe%2BSnu5ydBgSR7jSCr7drUkpeaJMdzOpPioPRrjEccPooF32cWhlx6lNEVo0sFs7cMB90r9F7bkXWGgvBfidONR%2B%2BviZV8Xi%2FyAP4OGjDz5rzOu69hm01rSAAD%2FwQQYsovH4khKGBTstnMxr4Y3eBs6ZuH%2F3uY1OFYEoFyY6jzq5sTO2%2F%2BCq9OjB8YAbfZYNGRU5eo%2BsD9LmnudVdf8Xk5YNnkDgH0ORAASEGzNyCZiB7M1GY2s37P9Vy7uUqf4bhOyhwb2ROI4RQQXTmKohVfBtYCY3GfGx43hd0rBciNPkoy8LsVrEEnGswrXk8GH99w17NeZ9dX7kL4U2aN1ZTMyu64L3QwmC%2FCP5WiwRfb375jg5dJa5Q7CKYBgr5Nj4KXzqVpHjo8%2FJQgP6HtCFT%2BAu0Sfg89P3jOT6kcB1XvyoacrQ9EMfP8cxz8WLuA7nr93c6%2F0gbHOpltHAD6jS2D4v3XT3ghGYxsCiDNsJDe5XDAdh%2BTrZCZEoFu5z%2BoLngpjBckWZrbV0jWMo%2F0PnXzN2ILdPxYOQAo%2Fg%2Bhxgrs23oEgbFYeS9aNCUuuDfjG6k6%2F%2BzrJkf7Yqclrm1r4KcC3wueCZGEMNDMnskGOqUBH1Jd%2FJVpaulA57buWmHc9PMylxqhLvXbpJWJ2Y2O3q1OpPbRw2Hrv0sWl4gvnDe%2BqnX3Dwm%2F%2B6r%2F%2FpsWCI1oVuaRrRNyoNhTnIcEWM3K8y4bOGCC4pvN4icKuqVzQSkj3VAwcJBW0ST62utFKbutfXmN23AYTw36iDarqZgHOLBahtdU8Vtn%2F4hSvV3jHiuhAijna6GeYgNKlzj8xpcDTs9JZCZj&X-Amz-Signature=ff6eb7242883fa5d81cd51d8dcb73cf1b3bbc54710196c2d2bddbd28fc31d7a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664II6L2RC%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOKXVpClms0UA%2BG7EpRaD1SurKv9MvWQSB6BkLTozTfwIhANn6mNunkwYqEgHTHmruYyz17gQn6aWHZb1hPR6%2FgkzXKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4HoPaveXVl%2BtVFVUq3AODud6CcGXJSGOvOU%2BPGuJt%2BLRjveY96le%2B4MmCQiucn%2FQWP1kPL5lQR61pq10lIa71pSZXpUJ8LCQJJohS5TYRcNnO6PUl%2FBW%2F0QRhbGfj9LfvfVeK9rNf9rEXm%2FhBfzcQycYESeVXVmzrDKs5LQXFvc%2BSDvUJ9nQKhB%2FITBz4lAiWY0kco66p9mAxBwgBkYz67k9jaqDSjdOASVJeKpm93cHIRh1HzvgFKy9YFdadEJmdH8jFHYSv2wPEosypQHvhwGefzyL55gk4Uqoaw%2B8yA7i5xukffa5BZBqOg%2B2eMNdrvXgIZ%2Fs1IkFqOZBHbsTxPqa%2Bd1aaWZlx4rDrD6ve3tAnDkotyfCKRxgoP1wS%2Bx4YdZTdQ%2FK%2BpZGnEDjvck0%2Ftbu%2FpgK1MF28gpIcZ7PPb%2BKmu5CH6bp7CrrRREKVlrg9uLAU2x38UioShGQ22lKZntCI1nrFdGOor60l5cQeianvu75ejHGud%2BcmPVmQKNR8U%2BOOkTqsWhkAgGRlR3ot0l8NKzh%2FO7rzI7CgRG9khhuCk0fgQmmFlRCDQXof7gwkXA8ddthWfmOyuGGhk5adHSAYXJa%2B9BiJQglehmnvy3%2BZ652u0xS8XdODuHKwJeAVd6rG5N0K3kW2qDD6lbDIBjqkAaKSXVuYKgGd%2Feu9hQ01FI8Sc41fyg9hYTJqKAi%2Fh0l0kOoRr%2BSpZyPHsJTibU4%2BRZbMslfDSVXRin0qara6G2xHHDQXUikEagUc5QeU%2B4rFqetAoB1NFQlTnfrJL9TgoIVlBdwmwrM6zgm%2FLRvm%2BaMHNlJY%2F06DDLo3SEprqqbDnZDZ4bJw88cBTk1X49Ya27W0vX5QhILh9yNnlaWpktFVWGPg&X-Amz-Signature=f4cfb0311dfee744b29b272f8b361c983d45064e37f37c63ced5bf852978f297&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


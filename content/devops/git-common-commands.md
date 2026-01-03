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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXOORHGF%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIBYNP%2Bcqkkg2lgNdIWcdvLHcASSZYMrTgP7qRRpmQj0qAiEAyEJ3RTPsx%2FZ7gcpoa3U7jdebw8VckWB2A01WpmfZjVEq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDGDlM90yqROKKk0%2B9SrcA12Y4CtdBQbf2t47sR5gSctj%2FDyd1j4d%2Bj1x3n6HcuaxNSEgfcZ%2FbIGW09Q00LeqfrvkXEGlKicZkeeXIh6SYZieVNsPp75I4EnZD%2Bsw3tD5XiwdqooJsG1dFPmLuS9YUs0PmKLP6y6f7SOUAeky%2BNwLPqBciK%2FeblRrfqe7bDOtYS7BqGRaGc5AThjO7Q6C%2BtOrmpFF8fkQQdhSQ%2B1209QqQw5cCN5jIXvTl%2FMX0ih61g9uAVir1zS%2B8AXlYHpyMXJY6tDkhTnSb5jynERQETC%2BwUlVQZajMJGWX7H2FUumnrYUsNywKWeGMyu05eMB202rzzt%2F8yHANLgS29L1Ulo%2Fth7drCH2rhHjUjmU%2FvVDvOQ4V6X9r5%2FkK0EWMRn%2FANMlK0oNDmVzH%2BnOj1kEKGbHezDJN%2F19BNIKYo44Beeb6CznJljiSeGVLPRcjJX3WB999k9PcfY4d7dw9MDyzVyhLRW45Eu3567w0qegVuVmIH0XEXIYVM%2Fb8BtWbrLGL7YKiBbUQspQRG9PTmQ2UbUDDKhoOwE5L3LoXLt5rOXFbMhcl%2FQHVbjwt06qNBAThCVr6yyF8YmNGYcFgsnx9GUiq4kJt0q5fjb1gv4u2n%2B4OZ2IyAm2KZ%2F3AYRyMLTs4coGOqUBZHXM%2B%2B4joOHiYk2DDajyDp56B0Fz9tG7OAVki8ju02gTPCJiEC6ozrlTCrmlV0eX7WnwgjGs7begBGfNsPFKZvEzEl8eM3Unicr4NX01IUKwyGgWrQIxGOYyMxj6jvc7lYO1wdCCWMQ8eV2ktrPzOWmzrWg07DAyPTy%2B9TEoAFgCTQ5yNVr8Ofkjo7%2FMQfloetMEnt3e19ome8kWpuWGuQydtOzS&X-Amz-Signature=27f23244f88be23343962d2df58959ba1b7fdd449ae653fb0ea8aa378541f973&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


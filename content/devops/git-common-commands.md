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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGFAMZ6R%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAwQxy6GfqeZSKRtMJDna878B41jkekuuGvltXxAFKpjAiAC2Cst2r3NSbzxKfLKwntvJKDlRAyhcbedfzC9EGKSdCr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMuncbiEW8uPBiHdb%2BKtwDMCqWTIqjP0jSlB58lNVXM6iAdZ0hTloqM9%2BMWEZJw0RBYNfSMMAef4uXhLFi9EBhgAYEgcvkeEZ%2FtB9YJ7owF7iFMs6y9ueAOe76xg47ufTslIiiqeAMaDVrBLHo%2BWdcYsZRdnq3c92725CtJeKbvboMlb6Ju7Q3Rt2chlfuXcYpDGAbAkMwS1l5a3WK%2FuQUgOpzSazAr2VgsdEr9kB5sLnlSsAIansNvlOELw7In%2Finast603ba5jSZ%2Bb8K1EGAd%2BvaUq%2FdM%2FI5mmjAXtNiMba%2Fw6vrPcmLKwkLajwUeddtlEP8%2FsiY%2FLR3Ux15hSpPzMloH9%2FYpOXgg6yTqsXmWHszTEd%2FQtGZa5ClF8wHhHuNOr61dOxGGEx%2FUb6NOrYuk84yH9WHgsk%2FD0KOnI3EDX59yv30gHKjqszNjLfD9yjdG3%2B8VNwKcM3N47LWvAiV5NmvmKYP7pxNYTqcO6gcGNxR46jbzWg26XjN7%2FLcZu5ltPgFs6i%2FXklA%2FDNLroxkln49o0pfs8mTdKDa5n48CKmUbueGX2dF9n3tVJI2OWO0M%2B5xmmYRJsSsw9L6l6%2FO62qub0Qnt7GkN%2FKEcUYgVhDvd11HP%2F80AIjZNwVrbwSHJMLlUTsex%2BTxjagwndPgywY6pgGGsXwXofb8kLw1Y5DdN8%2BKjNWOt1UcDyFkLl5MmCb8Af67IQsiPwhR1qwWPoRceLD5vQ3AqF9%2BeRCmKpGlzEKqgqokPzGsWrVguqo1yFKsC4ejJwEqxilXCnyzcMac6R0mmUVAF1Rdu9wGB05VXJc05yE6GBY5FtvZW13tOPn9ddOog52gQWejVPW1fxQMOWH4M%2BWZYi4zlsFk71oz%2BYiH9HHFEwF%2B&X-Amz-Signature=14ce43b5b5a0d504965f0c7a77c6c72cbca4922020731cfd9b7279a7f4f5f432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


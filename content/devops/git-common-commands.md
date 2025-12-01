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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WETFKPK6%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIEQX7EtHuE1JnkfeXnhxOCeUU4jMtMoRrL8LSXFWRUIkAiEAn3KjRltblTmTP2rl2TuVw9EFDJrhZn0%2FZA%2BFXARJiasqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7Jr%2FHDfM9GTCj85ircA3K5Fq82Fbqt6Fjq5qrZ6CigYZK9lne5mZpQntBrWPI8yZX9RILbKx2fySk3J45hurk%2FfP6XAavWmVeOYGg5jJJS2DJfX%2Bm1YZpwux8VZ5ETRJ8DW0vy3GCbjAsRBNO4eivwxXK1Gleg8%2FZPAWhC9IYAgwvzQDFUJIALnIrr7dam96PYMWwuP4lg2LdapA6Wtr6zqf3D9YvxnkZGMw%2F72wcpdF7c7BFrvNfEPw7FwYVZXV9%2FtSG8xPWt3GqKfir7567PdbydR1yJkDtdoe9rE9n%2FKHod4k0bZP%2BgsyUYsp1eSeY29b%2BGeKa2eW%2B6V1oV2nRIhqYkH%2FvvK0O6cN1T2QKaM7X1%2B8VkBG6b%2F9Fczws5xjWHgjuofYxTJKSI3XxMoIdUZxt65XVDDHBxrtA6umVAy8Nsmg5fWf2MAr2C6q78gt0u%2FkhBTws9DOIE4gwC15F%2FoFvI4pBgXKCwCDQbwGU%2B%2FnQI66AsyRU1FMQZoi0DQCRAtVFu3j3H0tUlcP6mi83lY3uYxKiQctZkkVvZ3p19AP2NnW9HDLf8Fjbtjfo5oigETrOMj44k6BNgbpXYudhYAGURJgkBKS%2FHPZ0ADKlCeQuJc247I8zqyOgdRA4JXdZkVI%2FMMEDa%2FMwDMMqAs8kGOqUBCeQerLeWC13mh4R0X9La%2BoBV95xuQjvIMl580FJiZ6%2FNAEZU59PVitkOHygiZrgwe2kCEaLu3ZNMGEiAQt%2ByzytfV2ujpt6mpOCgXebWDpEgLGU16F44l69sS2hnodE7JJslqR%2BBBLq1%2FJPXWmn6PzyakkqqglLfttmMnPWUyAndLF5ckq13jWNbej9Tn02iffAqYR86ffd3fUCnLF5dlD1Ykx%2F9&X-Amz-Signature=76da2230f85092843edd678b72eaa473331d299d93c978d1430d9bf4d2f58964&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


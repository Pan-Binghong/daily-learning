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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSNHQPNL%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGYBzeXaKO00opnz0DZ8VIl0qdpikoqrp6TuV9WtuwdnAiBdX%2F63JKvlZNxhlWoLpwdHZ%2BSDdSMI4fQbe3syJxK8RyqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMt99cHzyTWszxaPpQKtwD2LmGg%2BNlfQjf1DXYHt46AjtJ579rTCUwzjzb1%2FjPHtAYhk7oIhLQoah0Hatpn8%2Bg2c8OXAv49%2BvbrO3M%2BohxB%2FSQnhoSjfgAcqnJERjl6ic4mgxm%2F886aPU5O1ywIr7r5Idy%2B85KvxpFB4LB7YBBgZh9iBuP4tStjhtjPk0G17WWIy8LCknBjwQasa%2BnXeL%2BN3q1jS3qSTk3uGO92zK7Sic4sUA5OPLIiXpcZ1VoWPd6y%2B64Fp1m1f3Eau34obLI3HXWgX5YyMO8nK9N0it2ZeymgWS%2B3gvwyrc7XX2dh6seBgxmD2pLmY162K9ugOXgknyL9Arb8By383BdOV9w28mP5%2Baph8MBZ10NnGY5JGkz8tPIDXNbLyfHwee%2BmkMLSgVH7NgnaZ%2FYMjVncuYdrjA3YbXJVTwY57LfzlRqxP3KuMxuCgW%2FdzsjuwwLMwCfKL1MjhKdKekutrCXx0ShIT7d%2FwJzpKT8uQGMyuM1TRLiINS5l2Zy4E%2FmGSGXfYsNfHRpYfj1XtJE2TnoReMti8sFr18uWYFyAnfju%2BUQCcbNcGsTxw2Gc4T%2B6IBKDQze%2FHvoIpf1nJ7M0%2BkP9WZumkWxVuY98p9X%2B0KLXSdoMAYuT7zoJKHIQuu9y%2Fww8LfNzQY6pgHCJ7g491d9vUgx6kOZNUwnT8NPn7%2Bmeirr0iooj2IzaqhiojR1US0wnJgrt6gpQHtg8TNtQ29bh7ZxOyXyWaF6MqK1SQwv8qawSbPtV3YgEwjZSp%2Bv19BwEeqTEOEB4Lzjgk2j14qH8mGtkx7kT9aQfRGtafz2D%2B%2BuxpcT7lcwfFPgw5d6KJkyL1j6jxB%2FseEl8Yohxf6r1cYFTOMENjlwoRv7aMX8&X-Amz-Signature=b89a804e75514d2cc13567fce8e23884607800b3395d06dd8945329d84cdb031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


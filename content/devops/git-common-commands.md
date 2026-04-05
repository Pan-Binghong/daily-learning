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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKQHVZST%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrC2SYqeoRBsKkuluQWTFytSCmR0voX8PgcFViTYX60gIhAKMh4idEAf1doWCr0TFOzspPQXLLgOWOaKk%2FgYypPE0sKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkEwsSV4xd%2BlaEIkAq3AOWek08onUiE3jMBw7gL5naPS9SRTIiuLAOI5bVw1%2B2qkqPiLCWa8820qBaeKIT%2B4Qae4hrwfPcGWKv3S7t0DVJDpAq8KQh%2BgyK4ZQ7JvsZgr0DAMQTgzV0wufL0XQOAyhp9toHDRhmu0xZw97O08GepH8qOuhLZs%2BkEwIF%2F2ZBVUbUL9DSudI6YSLjzOYa0KsC9sQ3rk1giBMUObvf84%2BL9V4onn3kcbrb04lNekaD9xuX8bN%2FrUCIiLcQFSP3AEk2i4rmu7QcM%2FXyixbWeSuZjnsXKylOgPc0l7E0AtbIO9XmWKzMu6IeYDBp%2BMEiPGgh4L1R0gUAmE7dlUhfEdAytZyLquVh5PC9Vp4V63gYkdHHpVX%2FHO2dZWWNVQCKwtHWnSpepvqOFXA34zSEEUJex0544EqcSMFXNp5FuJmwe4CAKaXwlJgYXQqkb806ISVL%2FUvds7XdZ%2BN7DnipwMNIEftNlpi5%2FFa4xpB%2Bs1DOnuCzhva35jPNDvJ8eoRM4gGPxXvxJWBGwpJfsasnJrtaowUm%2FXy7VMgkNXMAdCjFFyBy92K%2FClYIXVtQUL1kEl6z9u2StUyMyDFkE4MJBO213itmn3%2FOR8jbq79SkA0sYpo%2Bz7mTUcHr2Hz07TDQncfOBjqkARhLBOmyD5M5Lmv28Uwmx7Z5UdbmJ5HegnwOW7fhTHeIkyeoHiLRYfJddGBKafbTci8sH%2BzYrRLtcqbIFJ4dZ4ZGK3mE2clkKpEYh%2F3ujn9cSeQ1m4P9EoHMEK%2FqdP4bKrPBFJYyfGz8pmh80n5L%2FzVvVChbnBw6HAfoborfHQ8mGrukiy2to5e9gjgIpXvMktJRPATBAIkWnMZCOi7kPCXZ%2FxT8&X-Amz-Signature=242ccfdb66559d317379ee39ad30dbb7bbbc1ec895ea9d2239a4fa3bf7210146&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


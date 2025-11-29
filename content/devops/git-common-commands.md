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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TDUJPQ2%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNxHlj4IsGjCTYC8i18BG%2BzrIAKltmqxm09PgB3TA33QIhAPoFksPXLN%2FAUGNIKwLzsJqQ8hF3b5zw0sOrrww%2Fl5Z0KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy2%2Fnhnz8%2FUEP%2Bnstkq3AMMFzlvOoYf1IXt46Se8rIrfdd2EGL1rkgXpbBday%2Bo2Kfnc5PU3NhGynXKHiSHqkGPeKNq%2BGPHet7jrPFbaGMUUBSlvndw89mgCcSTvnuoITijo47KnyYKYHHUshrm%2FgVEo778aD7QNeTW2ewiMxZ4dHCypHoxbXzyF3Cesx4MbBH7Mr%2B3Du%2B7Nf2ZyAdSBlgBcxIJbvtKl6RjO6MIsY%2BAb9HAbpnI6OP%2F0tvfuv1aN7AQIb6wvzr1sjQBQxmlP3nDkIfJRwpnH6b8YMr%2BG0hdOy4EbqNGFRhHBVeIPB9TsPppepSpiHJZpopKvESEKaxxVKHC5Vh0sGDLVtyDoBgzweOHRIUxjF5FIYZd8WOSkNYQ1gikjMSYiEmXVvMdXftqoEE%2B1tn3TKgQSb%2FSy%2BaO2RaE%2F%2Fj%2FgD3pTfQ9GcHu%2FHYECiIPD%2F%2BDGBdk9BuUXos4nyJvfHVtJINQ8zYKHnl5isVEWyPVDtM1KPiCcvUWBl5FvUBKQdbzNqGE3YFGlfOt0K%2FVuJFKnbh89uWPr%2B%2F2v5Sr3hAeZJwmAhQuF%2BNnmACiZetqa%2FnoUO6Zw3u2l%2BOwjAJWyvLPawXL8Z7UCYfll8TGrmRW38Q%2BC%2Bw20BVc25%2B6ELHis%2FuTkt4g%2FjCqlanJBjqkAZwgLKdhq4XLHGLHFI%2BerjvPa59C5tbN5aUgCUYwthV%2Fg6BxK8VH%2BiTFmj%2BAKeiumHdA8I6atj%2Fta%2FX6h6PKnfEr47EU79MSsTqW%2FzcZFsfmEJwBjGhf2Q8qykjEGJIy2j%2FsArdrarHPZGSxucYgpIC441wLANNg89cbvCA%2FZg%2F%2FVZXDqDVSYcGYT5wKV2SshDWPi8RdYK2%2BhhGqYVCYkF9b8ysd&X-Amz-Signature=64954d4d9ac55253a02c04a2d3292c20c2d17ab68ad9153bd916bb606537694f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


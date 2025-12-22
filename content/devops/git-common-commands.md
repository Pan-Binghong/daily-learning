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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJJBXY25%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDmJF2K7NOA0Rl1t9lSoHp5THI7qw2XwjdbIrQarn9yMgIhAP9LXzCgom1AQ8Be1ZbP8GA5UGSiB76dmsTFrLm7ehZRKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTT6T%2Fiz0Uf48e5LIq3ANdspCORKf9DXpV5MW4iYLyRkF1CVpkac3JpFSii5Wj2lrwSGak7Ko0rl%2FJnEacP00F4ulcz0iNSzmC8JiNfKf4LbOqCw78P5WJh2MUaZQfQrUEOG2liezgmApl4vOalB3JZUXJVZNABMR6wglbznghEwn8oSWeL4x4xLEq%2FjDuhGQnhLB3OtGtuxx66eQ13yoSV2aSWrZzhVQ4IT2bEh0uRGwYpfjFHu1qJpHjuqqBE3kRc%2BbtNH408pV8Oupm1HsVB1P%2FTwUcrp6j57YXgU2N8StDkR675I9Jng8a5EWcfKPCKDppmF9d48GgIhDPd4c38kRPHW%2BxzayleTHqtm%2FcRXg5sq4fWzbDWd%2FCwJsuRH3q42zNvxoer0b%2F0g62eU%2Fc08ItKKBYt7F1Q9ACvF8C4IDw5ZyjmGJzPL2Xk%2FOhHiHotr%2F4xaFVZmLwqLWDRK9G86e0%2FvD39JbfJ8BJwKmEKBrSInv6PnyoVVNr9AlrHMC7%2Bj7OIIbBAiUrbXlYb8jLkIUoXNbw8oyquvqJlsRU9TwQssVBkWZBKTphW%2F5azjP4daWS68%2FE6V66G5tnvYmwfvBWXbQe56DQ%2BQtKcjuo%2BMGmLSmFue6HZHI4y6a5CLDc4qw9RzOb6vbPtTCp5aLKBjqkAZPhhx9a%2BGQmtyAxilx1hLrSzvkXKjg31uRhQFBe%2Bp8gEfYZWKscxG49j5pPMPfJFry4t9GC5tiXjuyzFLp%2FqB52pt%2Ff15ajmvvpiPY11BvBBWOttsK1n4y8CoEhkAsGfvTiSDeq36LdhD8zIN%2B%2FHANuLCGyumxTZDHV%2B9h19B2GoN%2ByPbwDS5cjqLeCT2JkE%2FZRaWXFmeCrdTS3O3%2BpzEa5m24C&X-Amz-Signature=52170d1f21773412f1fb2fecea217bcc6d2b5b447f1f94401fc9fe6848b095a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


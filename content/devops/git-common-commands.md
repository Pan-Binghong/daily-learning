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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MPQ4ORU%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB0OtIrZQS%2Bg0J2t6X1IoF61DiYHPrTnLJr8pxiliUkWAiALAE4QJotZ8VYgBmRu3UFHk4JRQRkztj5C9iZCTkzpbir%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMvcVVNsjlYej66%2Bp2KtwDUbAmk4E402aBqgdPE9E4TcR6O7Cv9bE1wY6HXu8LNONqS1d6DbWDHNa2hyYOZtCfkbZZvkaJzH2zYUtyUpevwp2hoPHbIToVaBV3YSNAmtFVyd%2F%2BR5%2BQ6xs4ojFpltHmrrb2pkXdohDis1V7gBxNIX24TghR7Ms0tjtXM63ewMbcxPRynU85h3bTTu4oQug6KVfasDRsyT%2BcncxFUp9R8NRU53VCfqMTPMD%2BLUtgVGdU46J9vxHghuE%2F%2Bw3NDKOCVkpprtsb1TrBTId0apT56lgnQxfy4TVba9Soah%2FrRl9ir1foeukcBGnrc%2BT3jWQo2Q6EBmGKLyXsCy90HMqziyAcq31HbHu8%2BjXkW9Byx0OyZGgEnokFhXnf%2BX79X45TObapb5fLX4HmwxnLJqKIE30gpYRMk2icYkD1APpSU1QWwiC1PWXxSkbtBUERTqmUw02shqtT7nINzNEzTHhY%2B2f0DhDTn7ARfmELXVzdpGHtLaSE0Id59wUfWtV6Bd9zbXqhdhjvJPXvaQH8jEIpLTsZNlwxQ7B3yafrasbXlr4cbNUZWQGxGFft8ISOTEYq36sqtxXQYbX0NHeyJXjrSc8zFmOTdqk4yKxhSK0HDEbMgRN3%2Ft0IiA2HQYIwnozIyQY6pgH%2FVLfgyKfcN1ZUu9O%2BAYzzUnNitHGlEGIYfssbuZT24P%2FHry5bQrJGCpz%2FtrsWmBCdlcW2Nex4%2Fiqkd1vsqpB0NkXwREvwMHBDqxKKymFnaaKDP2uwnMLgUUBzB6%2BGYO3m3XBCc%2Ffnho%2FDxjEDBcC6eSZ%2BhiMC9%2FaxGcI%2FEwOgYLKzuBBxF%2F5tWbRnWe1g5kmaHXjK25hgboXWNiaGQBjb8k6des8f&X-Amz-Signature=f0fa0e957024cbeeb14db7a925517646022cd99af6f6461a061fa42b2e5b6d20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


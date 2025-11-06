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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5QTVJOC%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCq7jX975t0%2F8yKo%2BE8pG3tD41LRROu1Ys8kCWK%2FY76%2BAIfUtfIFrFAxe%2Fy%2FM8ZokvCNLNJq9ouzhSvGrY5ZHaYLyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMu7JB2LQHet5%2BRhA8KtwD9UQMpnAze2lZ9mhEjPNXQPViQIgKALg8ajLnB2i07rPZJxnB7W2gTe2S2dYsxqh%2FxrCClJvt8qUMARG98WUvFdWiGaETyKw%2FVBdLfc4nv3mowQg94T4QRajtIfbMBd2ncoJUaqQer%2Bx7PVBYFriHcDx6C2AJVTjXilLM%2BJvevZ7n3u6Gg9f%2FPAscd%2BkscPp7kKS1EFYyAIAjGkC70N5WtSE5TVXp7Mt8CdAvHVH9EiHEmFsY7KwUn4fUoHmT0z6Xxfanz4DoD%2FZeKMkpI6vGxs4N03Sj0q74oA4%2FoNozvmSmiNZP902poba4KIrNF%2BQ30xabF0lnR597sDGWGyXm%2F6E9ED2shaZJdJRAYtMqNi9ajBxAyKTUSBf6wj4M8VLvEYfJcfh2q1p5WGU6%2FivV%2BmY8EDF8L2HxkaAuekLiptYA0Ze05TOekdabUJKcnk%2FomQ605HcynN24t0E4Ii5gLMzN%2F%2B7B8jlx3uomUlLCJHl6TAl4daojA%2FKnC0wjEWYsVZDpIGt3ig5Yw9NW7zaizOfiZrpNOowYXhSRhcKCLXa0vFa%2BP5qDGsqf1aBsIU8vj5udh0FqjqaQrR5GfC76lSwFPsAmewn9IhX5wyWgIN2JWeTt%2FVHyhWUjv%2B4wivKvyAY6pgHEfBnLMyaSlrSfENUk0xNoj%2BdIBf917clf6oqhHGaBVOnzEkefEHoHGGLtCYjlYQ7rvTfDcZZ8WvEkQnNyhN%2FaA%2Fm3WZuJI%2FYSWmMF5Ubz747tUiZPsLUHvtUk6SjetBcDCPWQiZkd4mBmHKRVs1YJVdbq6Q1edJVnMahvnR5FymPOAAPPP5DBfm2zgbWhg%2FblVMadjyJAovkW4odhfzgdj2BbE0ND&X-Amz-Signature=2ebd6111fefc5f7c3fde3e248f819c68e818b421382b68d4ec131450a0b1e644&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


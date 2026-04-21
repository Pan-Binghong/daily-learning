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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS5EVP2D%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD2IsjM8GfYdb7sMeKv3ZadZ2r7Z5Q%2BmWXb4HH%2BgyRh6AIhAO6ELOWo7Ii4OazJtsq9nJpnyA5yyLHhuz3egniFPZTiKv8DCCwQABoMNjM3NDIzMTgzODA1IgzC4bTXsqGsSRIe4VAq3ANoMv0M0c7FrZnuOGiCtLLqKvqUcrPdKkY0XbvS4dQU0zBPyhFYITahEwyEZF8nBR6iCU7Cmd6JJJG%2BiBFRmIu69nmSk1VZ3%2Fp1rEHpHju93RAGZ%2BXUtzXY0pQf1mfEMmHhxeuXgXZrt80W9lS9MDlRi%2FBlyfAl5ylALJfQ%2FCYYbdsYhlEYz1I4R4TOYpu%2B1EWIc0Sa%2Bxk4jt9hCrv8LIOtVioWdelTtJuuYtZu4wald%2Bh5L4AkZhEBMacdSuyll8hUcWmzivUIb5Jyz6peEtgQ0BcVdBJyICsqPdNPA%2BipwEChp6HNSP33os5l9oRLgGfwMSDJ0VlgVZxHKiVtDxOmbSFDM0%2Bl7kcNE84O8BTgS%2FxtWqiFDWYChXpsK3lwHT6IDXkGtcQGGC6tLpKtzQXelzJH4i4cKKlhsrDhs4snpN5VK4gAM1t1xywkWdDQeelG%2Fu%2BhDjSl8B%2B%2B6I7ospASJqT1wMZH%2BDcX%2BJ7zArPAaQ3EKLmZHEnbcMJOVogT%2F5Sf%2FQHoxB2WDnd2AIM9r%2BJ1SmOQVwJ0jcV6HC4Z1196sJDaYzP9rfxKK%2BbAcEtGDo5aDzgCUVAwEtgDtbrnVeVHvhqkbMLqUCg43gJQBwnqfSNJZyWs6OzXIZSJgjCf1pvPBjqkAUmUGIGPKk5R2U5p%2Fo68eU7MHs432A646wOb3si9SmcvDNdr3rOdRKRcXb0UcXKCmHow%2FSnnCXv6vMMEEevJfZj0mWMd4ZSQr3pxfmob%2FVXpi5HUjNmF1zK6eJCJvTa5lISntTgnQC0Ke91N5lOL5e5dVuhnwoJx6snlCUII4GzjQOOBPxppXgatiH%2FkzmZjZ6LT5HzUxMqSIJCGxflhAbXIpz4Z&X-Amz-Signature=4d65ca92dbd87ee89f1c4d26079478f726b82a0f2481ece15cb23ae715f43ca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


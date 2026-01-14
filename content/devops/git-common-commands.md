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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCLT5YGL%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDNixki6ba%2B3CM3yCpnxgdmetdFPId6nIltv0%2FLDNurIgIgAt%2F9wItyNaQNAx0PQJtkJJTMK0s5dQ3sHhk2b0k9uTgq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDDmnEDF6I3w8njh54yrcA0oLkopRalylrrEZGAXTfrCVKbXAPXkT%2BQ1uuhQKJPFhXP72uo9ToATd3Cj7oFRrXB%2BQn%2FMeXhJuT%2FYg7mkslQnYtzhVS%2Br1jAogfLbPbwSq2t3Zzgaia7WpFT%2BtDPLErv3FPj%2BeQIrmO0SPxFEs8SOiCqFmZuoI1grotIwWsLHrMREq5xOW9K2vAgsMIOp52%2Bu14EuqwiCBX20MoQR6aXlwwMef2dDw1VlSh8UJR%2FAW55KHwwhkR36%2FcsadYKMRy6xfaNIbrVce%2BXPGtC2XwJltk4pfMPB7shSMztyk6ujc9y%2BzYSYA8cp9NhBbSlhntAyTk85W7OmFQDD9tu1zUMu5wJkymNW6zi%2BiHORfPdeiS9GzVhxnIl36HjASSLwpI%2FH%2Bx29umeqNToc%2Fv8TQ8fxJqSEmkD3PtNU4VtBLsW2iOrv83RJPEGlcXbp%2FxUVbeilJdEQzkQ%2FjeX%2FMdWaKiQZVT9T%2BdkwJ1XUema53fO%2FeEiNw6DjYn3mHoAfNwI3vWGv16LVq2C5%2FhasR1umWfOflciRNSP1RIv%2B3lNoJDtq9v%2BAI%2FuOFxhm6YC6mlDwDqZJ1C3BN6oid2ItK0di2EmZS%2BIjcizOujhTd1bifw%2BphyTsPYMFJ%2FFxKixMbMMfvm8sGOqUBLvVxlgqmkArsEb90udiz1dNZeV4AikAkjlngag2PS6wH1%2B2A1FcgD1caGAn2O0iRKQm5ZJq7L6seY75%2BpaVlDIrD7TqQhMHZ12%2Fka%2B9%2F3B14It6eriyqpz5HtKkWyOFXLJfpv748ffg%2B9PbIUqqImEgWE%2BW6US1Y6oTh8XVx8IBqBsi6N1udULimpgFlaSHJHz4KB7bZDWYUawjLyZLLfBzuTdle&X-Amz-Signature=b6e770d43e1a6b3c0a621567e60f20983582ddb861665bdf1fd0cecc61d6374e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


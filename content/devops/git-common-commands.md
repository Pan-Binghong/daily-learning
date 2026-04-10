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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIQILT7C%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIF9sgepaHOosXt1j%2FBJATe%2BvbrBqFoFVAIjSTn7z%2FwVIAiAC7OmVNdCBSAUq35QnhZ49HiSHtKmWqQS%2FqEMfkZY4rir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMtNeAkHwWL7O7BFzFKtwDud2FJLP4Y%2FAhdwoS5h%2ByOdu%2BPCowzTgSsWHB62cxhVdkRDpO2QeChg5H7Tsdeh2PE1izjClid7fhV%2BRr5xdgo2kDYmkWviGhHiQEuaYn%2Ffr66AhwWnJArqvQ1SckOpDuwTzRCGETc%2FzLClTfX9hHrO8gf4RQIQN0ILPwQWB2HJJtGBWpuzJIXLDhlZ2boys2bVQaQXfg2yRf8hs2p7WY%2FVhh3ttsIpwZfZb9GcRbnZdJxo6Yu1ktkvn6Bl7J339h2O1DAL0nsQEPG8qcWidSKL%2BJrurgoIh%2F5q%2FoFYYnFzFdwUoVIYYRh5Sl01e7CvAQQYxJXPEqH3hTUUS1%2FtOrtoiLGCDO2ZzcjH2i11nMpQ6q31rMxInPNJcVPTPSXvPrV6lbQ1VJauxBa625w9FBRUx3FMnBJu0bizTYG8VZCAB%2Bp0ca2%2BvaGxhcbWcFVp7M4RMdqvvCzrNWMX0jtF95d14ECTYlWgIoc4A5toMCWIQ5SEO8SdhmuUXBXEc%2B9h6j9WBacl9pXzAK5XW0%2Brzfugrt5c4D3S6zys01JnUHMMBx%2FdhdoFm2CQjDfaHry3M9cSZVsH1Tsv%2BHKVHeZVIowZpNcGPzWWVH1upjoBX4VmoKllKpvUx4GKlpou8wiNzhzgY6pgEcpcPfQwlj5H2pOUAUUqGIq6pI7aly%2B21L%2FDoOu07JRALD1Xc2wZ0ejTJjPkY4xV34wmnpadX57F64sqDOuLPhrFHXqpX%2FvmNcj2Zkf1kXd4zLhfRcwapldso7nJKSCUn%2F5dMa8bCkBr25RSJs2T35wF7CAWSx80x3WNcf7ye7RXY2TRrMvyrML5LMtM%2BWe7vYudT37Pt02oAUoJK%2BHp0OQBInDk8t&X-Amz-Signature=d5ce4af31968901a93c04d3ae48ac80bc45b766c8ea131c547cd347719b7871c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSOIHXSF%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCCsiqG4poMFnVrUd%2BNNLP4xu2Jfg8y948LPMVoee9s%2BgIhAPdNIjRFohKPuS8SK4%2Fpn1zzVCLaYIWpQh%2B3jb07p0NaKv8DCBMQABoMNjM3NDIzMTgzODA1Igy2f4CERinMu1trpigq3AMr0pVGTNFRjAjnI93iKUmV7LW0fllhhteO%2Flf5eXAeuIdqdLqOQDO1Y2MJvrLIhrurcL89QTMDlVW9PlKqFYgqXDW2lHMHFy3vHXwYizS7e9xcCf3s4jr2anhT6wfGz0dpaIP4ui4mgtG4hRvm1OcGrPoSJ8bD4kH150u0Iif5nItFbRPzj2alq6tmW8nmpoIMXjwG4klT5lEdFmCMcniV5mDxxCTkCFYTYf0bfOxdSvTHPK0aG0sWzy7J%2FPnqpttAmlqrvNmX%2BE%2BBkNtA6aRRYdGdZ5nK64U4fpaNrKSi3W1efQReTeilkHx05CI0aas%2F2dMMXcv3g2mqdJIEEef%2FkdOgNrJJOZbfsG1sBamKTd%2B3VGcpqXqB5gb886A35ndEpgsjPx9jWsvuYzJHcJYO7g3Nor7WYkM2qZKo6skIZHa%2FOhc%2Bo9NuU2E7bwxZ%2BpW7Xp%2B22FujL0WI82j%2Bz9zf%2B838a1o%2BIq70it0mshqffxUtw7IbZmLXDPZir5bn9w2P6GBzcFLZHXB%2FXubRcKsaaALrY%2BgAOZ3Is4bRW4nl8k%2F%2F2mFazWrEIdNvTO%2BZWkc3NsbUf9cenJppfm46ATvBPGUqaGrVnbYKjICCGf2W25HRk6cui9OUQYtgTzCKl5bPBjqkAQcpmzKHwf2DlvDSrfeyFgSFGhOh68rpfgs9qe79r%2FIz8%2Fa8xo0%2Fbsd0xIo%2BQ0IXPwday%2BoiiqT2ZSWbeF1CAOvuSXvv80npreHGUOHahzFEcQ1UDamZc54qCzaA6%2FxyWKXoHo6m8W3yEu1J9DrD5fJEcZFmPdt%2FZ2pFsJLg4F0qNcbzc7%2FSpdM8GZj1%2BC%2FJF4x8YkCh%2Fpz7aKjNp4RSzNeikclt&X-Amz-Signature=5746e379e70040e4531b1ac2b3bd19acd4804cc6daddcf1973e46954cac238d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


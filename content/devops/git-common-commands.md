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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPRWCYWX%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIF3m2QQCGY3P1CBTIK5kLmYjEgsZgASULK6Me8UjiuSnAiEAiWGUwJZmMYp6y0bwrg%2FCRpvsHV2UPQ5azoGaHnYEVHIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMWPF4pHqhJEkJm3%2BCrcAy3uWvYw1VH9RqUlpu9%2F2wUy7DRbBA3%2B3%2FkTKtLp97X8t43vcFaAnLnb8wsnZbMvbEXuRZkI27MzLSEtQLSXjXbUf4JUxyMeA5jmU9A9L7kf6Y1A6UwcVc1vWvdxyzU4ZZVq21UfUvqvER8KkkAnQM4lU3y6mMVNgEPwUtGl7yVZFOgA%2FJvtT08rDO55l3qmL2J7LtA9QsSYWkdihNWVF1y41qjzKPAdHtP3Z8CfoX3%2BEIXA5i4Ri6ystTQQw05HTTFPs5K8tMb4olvahvpCGotKFbys2Gdga8kTOb9834B2DJVQYEV6KtRVMhHy7r5aMbpKIwji2paxnJX49tnecpbuLLv2N83qgxZSNpKQu10SyctZwK2QvuwZXjUMzN43VoXHyEeOLwHUpCmIz9WszSAGp3p2Dm6oDPiL8eHI1aYwLlkh5MuKP0DIQuMWc2Vm7EWyU7gbGryf01dhlruSpbO%2FBiznSE%2BTFf6%2FJDVSaCY6mkPvVmt3vMHyt55LoLv4JvgGlBnJWXZmCMG%2BkUGrNbkdspliV%2BWbn0W91z%2FeCe6zmx9nJKexdIAZG%2F9ojnsBlMCgIFTBI76rxxo5UhkMe6jXc%2BRw5XiT09iEZl0uHKfriLWzW4XrpPV%2FI%2FW1MOuexMwGOqUBPQYjVRkp7vMgUqR1Ac6QdCHnqQel%2F5vpIteppEsveFDIlqYrN0gF0Tw1Ua6%2BAIujHrzUnxq8b1VbD2xbqIZWSd3z7YzD%2F4ywbqPSidWJoEI6Vb5jq%2BMx6akgRgdebMearM1vY6EZ2uzVhhh1wPhhIi6RanJYPlwyljC70nHXX6319M6DsonL6O9MJT2iaCDtDklvvf7x0dsEFAY6l%2Box9j7sWAxk&X-Amz-Signature=fdd6cdc3033c86d692da020753448b41630d0359b4f7dea6962223433b96eaf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


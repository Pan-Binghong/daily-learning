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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SNY32FJ%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBcoCkrkBk3gAGOxZZhcYfRj2bFJzEug78RQC9g4evABAiEApHQEW9SlEjuJviS8nVW3soTrX74yAarP7ZJwPdw8SfoqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBhGKHRkLggG%2FM7a6ircA2z4bJQ3OUNco3Iz9U0vbnXEwMboSTp71OoKmEi1PPijLLzXXPoAg4qMoCAOZCMTva7%2FK3ARSi2IAOh11D62ClCvoGsifQOh3lGHUY1vnULDXOppVc6sO56xQs3eRNRXJ1W%2BiwhJKkY0VoY2aTpgCbDO7LOwPuHJCC7SS8QdbQEiRYDK9weOP8HOrHXKbNWRnagZQM9KOlbAH7up3dASnX14JCGyDFLIw6Vf9ULOaeqTrdHawai1ahEZh%2B5J1WS6d36Yd6wZoyfZsih4QLxTNbQ4NP2gNz2ZiJ3ormwRMwwXHLtqzjv3SUga4DzkPWPzNfYFrUrPWT510poKH8vSb80uLWrkfQz7DvEq9Uiy%2B%2BnWvNTovioKizcGZ9nC2uqQz5PH0bBORNsi805jPxIZFZh3garXnRTp3zdEcn2lh7Gp6ugJj1uUMcGlNa3My2trU8mAKsYnMOv7wcTvApRuA%2FL7OfLvOcrmyL7LTt5mLSUMzgIPr8SMTx0sjBtu01eo8rgajgQoYX67cWRLtm9ZDKTXue%2FWD2HL4pAwymZ%2F4i81dvoJK%2FHtjaDh87Twqk7joiKYh8LJOf%2BMcDOUWnVOCkx9KGifdlSybHLV%2BDtp4C8plLdp20s2m0DjT%2FF6MJr90skGOqUBmSfoedHywTa%2Fz3a3mI5Dzh%2BJ5PXmjqQZr3nt5eTnBm1QORzSj3glT5pTa0lv74tsUOhr8YZaNiyRRSgQz3fd12C63cjt9sVvFP0xqOgNMmo2xyNyvwrqty6ljdz%2FuJb8vf4RC8wTWvQ7d%2F6YyYPUDU0sn7xlhkJxICvr%2BRm%2BXuYJ4nu%2FL3EK5ZUAoIQ5GWAQLCQzV1HiQ6xpGM8uYH8FjeJA64lE&X-Amz-Signature=b51220916664740c7510f1807b872383ed9dc739e895a47eac67a8881eb2b361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


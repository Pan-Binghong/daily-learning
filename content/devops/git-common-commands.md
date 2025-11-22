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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4II22CF%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQC%2F7czE2BfbRBMin8cDnneHxnAb6bmr%2Fguu91N3HYlrGwIgBvMI61M2Vp4tJlWw3XJ%2FLqtAeUdo8CEtqJP5%2FoSExUMq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDMNia%2FBnSXHF3S5U7ircAyvGlpxtGVMpbu6fJu89pZD9rpDm5s69Ub3KsijvkLyiuNJ5IBd2NEJL3ZsyYI%2Bd1V3jER26xYC2G2nuYfLuKcUymPQ4GSfea8HFpBk09BVmhj7aJQ7ZIjngsQkqjvbYbc4PZk0k0Jpg1wR9fqyMXyMYQ%2FF%2Bs8IMp1JkVhF3ZzXbJhi0x6zHq%2BTmzCkEanMMBXOzt4MTm2VqJ56vjXYb1JxG6Bnj3zF%2BR5OGeCUhKwhxdkau%2B1b00hZeb%2BxT0Cy%2FiX6ROvnfHbgIY93MygbwfdeaJWC20ln98b3MPCKBz8kkaNKZMNr6cPVb3cYhZWoJaL7412BtDlj7yhrx5ZChQcv9kUoLgJ%2FUMp0kB7VjDk%2FFYDnOoFqFKNiLyGD7vVye%2FoicPQRQbPAZ3TVmvHmOQfmSHmm4jVNw3Qf8WpKkHhdMDHMP%2BFr5UBwyzT%2BM8ERRW7BDgDBuqDAS9YILXiNJ9bDFtUhAe%2BJrm1f50WcKEFplzIzVRj4OWUnn2GE1OwxrC7gU7S88R7G%2BU%2BLJUsm1PvUzJ4pq9IIM12L4Yq7vvT69ER4rAwv7qKAlaw641iRCV3we983%2FXrgPLq3EcNXLNjQx%2B2W9z%2BcAFb9sTgk4XClh4iHKRkzyl1bVw1SYMO2ghMkGOqUBrpEbC7pgcxoPUQOtTDvAyEr%2BfXcXybF2SJDf%2FsVaggw9e6u1KPVc5i1kTMWiQ00j3%2F9NT8%2BB1LXe6Cjai%2FHhx2m9E1O8PtzM%2BGoG2DJG0494opvKSWCGaKwm2DhYE0CV7%2ByDsuSGwYLtafSxtNk%2BQHguceTocedO6Km3jEdbjlZuKmSgdHLXcXplPju1PWl5vk7QX1zlSN1Ix%2Bu1zTlryMJQdPY6&X-Amz-Signature=2d18c7801206c177c6d6094dff8b5b43460cc5c346dcf6e386606330548706da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


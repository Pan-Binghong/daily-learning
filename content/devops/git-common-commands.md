<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png)

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

=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAK7WJDU%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAy3QWo5TGQDjrJO8F8UZUkXPLcmig02VDvK43jJ%2Bp1FAiEAzUCsVWqKdZXOq8EcA2%2BaLBUqPIMfss7gfttUISmnLxcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDD9F5eGAGAZDtjHhWircAwibltccRR4m%2BOyI4F9oNZ5fRyiuBp7loD4gDH8fpSl6Q%2FR0XzbGSe29gj5UpmM4%2B42TCwzsyTfuvho57W9SW4hs0tGkWqn99Qpz9cL6iWDf0h5lqp%2FbNVerOhwqVeT2hgofWoB%2BYdfSIs6n0fKkxJ8%2BevtxPJqrF5TOriuM920efPW%2BIjnFUv9Kx5ZlNTQ6YbmBHcq9gMZ7H2EqTOIxPdN%2Fj8FOmBkE7YLGQTy9dO0TgGx%2F%2B2svM3YwONVcA1KpuC1%2FsizJ014z%2BbQhulTgSM%2BUWPSm3dTjI8UgOdU2XN7D52S%2FcCbx5Qh7F51clXUm0rzuAQNEdjCy1jE5tqtrOyR2SwHyKcDnO8AhT04Y%2B%2F%2BWwFbJlR5dGojtgo8kCwtKfrg3gE1H1%2Fsi16qqiePY7N1DTATXqH8fXjYX1QHII3FWnYAz1Jolj7tuypk1adfcnVbfqOSje1PdKP8p4TgtWxS3rY1x0%2FzOfpLYdzZsfj%2FfEeEwp1LAbzHLJkK7cRJfImfKVf4ODNugQCRM3bTdTWQvXC64ffx%2Faso2D9iBOwJCCAgvJa0sMr21Rs8c8yuBhJn0JJL08OH%2FIhH7QpFtSYhfNpmFgn8Vf2wQ6MuYkEigK0BS83KekRpLXdDjMP%2BczM8GOqUBLUIlto8Uo9fFeBVOGhuN%2FwNHVOc%2Fv6bQ%2FcBS9Y2zPBoqPyjE4P6ruFfUnmQkWuY%2B7IdEZx1mI0angAdGDl7yzL9s5c%2FvoFXrrlC9Oqzoqb4uruomJ%2B80imeVhbwkk5uGj0CPVjz%2FfWT2%2BDtzUtAin%2BYQRsnPi04u65wXRl6hDnD75WWq0Ry3QPnmQ1RpOpvV8Ge7lzCKuTHMYdaHBeNqCpQvFYNi&X-Amz-Signature=5f8d3c4489795ba2b5cfcaac275c64b2db02cd0ddf60c2b6edc2159d161131e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176

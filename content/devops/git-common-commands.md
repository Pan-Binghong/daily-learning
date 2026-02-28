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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBGWSLBC%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDqlL1WeVeTkCJIvJ7YOiPVTzePs9Ym7gxVSCexqjc9oAiEAgLG2g1LUqf8xpoKL5yGO2nus%2FWS21TTrv4ugmD4yKIQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDKt7MELRxFulMAM7OCrcA5E7kvzGzLOkk%2F9d%2BTzthjQEJ6fM5sXqFHpDPgFOgX5uUTlzmLdnW52yQs5lxmLDZejnoe3OLxEDUFjwNJh7oQ1uricuMN91Ctsvq9VpxgvBmgSigg%2Fxn7kQmlu61AmHbJ4Ribi11cyOzRvi9low8OKuGbNRvJJ7ohC9upM9fj7QraPoPlb%2BoBWq1CK0tK4Fxkk0HSUc9tJ15Yzz0VOBowFsu%2BMas0nFNS9aQcAxq%2BXKSeMccPMz9ob3mB%2FDnkRavnFfiCdGwwo0jQc9Q4BSf1cAkv10V4Ksgca2%2B%2By4UvrG%2BRd6VHruvFlBYrHjJhZP%2Fpl386MTNydxAvSRqL7oCuyjFx24sbwYjGMomUmxN8AMtLEODx69%2FxmEdwee8zIwrWjmoAnIKLpIIisKc%2BtZ%2B8swQ7N73DN9aX4kWhEdWJnmcyeQMrCE5tglu5%2FI%2F8udWMaPVHN8c%2BlCP%2FjIy%2F99GiAJD560vaZ5unX31G%2BqOGp%2BKHhwX0YAUx17VGIc4fU102TZnrhi9sjWrSavCjgsDJxRLJ%2BkTMPM3U6KITa9%2FQgTT%2BDpB%2B0pbVASyxdWBh6V7B%2F2LysaTW3C16tWtkl0satH3HjvJL6UkC%2FASnb5I%2BhmLer2OF0ivL903a52MIGWic0GOqUB0vsaruRmioAw70Y1hWGRe%2FAPNVwzwSHVIX%2BAJZLlpGCu8PMU81xMNamx91EWdzeQqIxgzqiYZ2ZswvpTfAFL7c8jPv4ggD7miVY6%2FApkKS5OVav9QJtQV2Uam%2BMjA0Lxz18U2G%2FDPzRdxyi%2FFhbmjrAWYvemDyUiHrDHxiFmuMSFWIJ6gp439h3zHM1szuVthxC2QVqdPZ8AohwNDBpY3a8wykx3&X-Amz-Signature=ff0acf843a5c2ede81eba51e5f095f4e355d213fcff9ce7e7da0e1bb7a06a455&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


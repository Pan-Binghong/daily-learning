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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAAPCSOD%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEGyyubh7ZVFuVUXwTPZVoeRRyradnSeBzZSyeoGPo6gIgPMCnFQV0Cvz7QZzbrG5lsWZ8HPe7IuoZPT8Ye9m455AqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCRff5%2BbrtsMK%2B1uBSrcAyCwhn%2Fbw18CfS6y3LT5MBeDVoEGonDBh0GR%2BR08qHI%2BYbkYwDJ1yBBHGqnkhPYYhzEwajRpmPtx3i0kO9LKXiN6SjIzLtKOCjbWDVutTPmGNWL58fp3xWw2iJ6lv4nx6YNpsCVaPm3v7KTddywzxLkJx%2Ft%2F0bB9gE%2FARoWpQtoifYebnwbTEpxAYJaOqMFVly2XTrcZhk3x0ejCJo1GLv8R6AElhjL11vHkXqkcg2zI9XSvWer%2FyYBzWPQdvjl3UH6CtilukxuRgFG2meVfoAFn%2BPN0Z9Ido2inBmAwwaaHMfKIC8Ouh5OWy2rIrZuDuCdvtpEbcYlfWu%2FrPBQW1LCljVeo4Vp%2BUTescnB1NDHGbNARXjfkj3zM7ImwrtraQVFmsAw4SH9fgrelKasB3xHPc4Bg52S0iwU6foDGRJQAh3w%2FvnctU2VwWOActgdzcH1yQ45hZxo%2FHSFThg4gzwMHRq6vRVYi7mTSh1JINqMVdZxturAcXG3b4RUV99FieQEQN9c3Et7N3uBPH1klfjiGZaClO7rJpt4WmSl2%2BFcNRWeq9Bq7Y%2BIsjP%2Bx1HYUroeR43pegjjbP%2BnQEhmqRsfNpEB9uskpTW0cKHBmYie5Kt6%2BPVIVdy9TtSw2MIXxsM8GOqUBCOlKkWYYXpooPs3VEzJUjwaHGWC31rWHbqUkM4qChymWaHdFLU4JnkDknrNybdnN%2FW%2BRvwkjb7uFvBRCFEyclUjQKArjcBvaDdtrTiH8cBQnJNsu2k4ebTcGZqMGmmz29gkLTOd78tF0MF%2F4m7ONaA660a4xouyTBk2JCtoPxvkqBVOj8xiCkOVofy9%2FZWQbTRqSC%2B33JB93Q73UAFozZPML%2BRz9&X-Amz-Signature=2b22caf5cce75e6ed93a90fa578ff7e6268ddf0b458fdfaaf86475d6398defa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


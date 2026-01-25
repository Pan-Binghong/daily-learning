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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7W2OEAY%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDglFLpwUC3zaA75T%2B3mrgcdMloG4R1dst%2F0kwdah8pOgIgYD0c1irtGLhwnncmqTLANYWdzJwZklsvDSpJVYbrh0Mq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDMSRw0uov73d5vLmNSrcAzGgd5CdFBQlLOXrVzepgGK2Qq0SU7ytbvIwDWueKrjDxjszsp%2B6GW4k%2BAE%2BKLBncoMaH8zjBt4DXAZ6k3uz15WUCJhT%2BhaxB%2Fxp7wUwWJK1HstUK9ozLrLau%2F8VderPs1AQ1yh98pJfxofhs8zkhP%2FEMlDt8iI4v4UvMVCipIhpdHS3qf%2BxOSIJsiPiY6GOS%2Fb0q9dhEuAJSDxWQ6dAEk5WCadov2bRUnJvLuYIXp8f%2B0fqilNotw5jOA7mAhkFHLrf%2BLxd%2BhM%2F%2BoGDd5AZIkkjiSdr0i4TwABaVWq2LiIESM%2Bor6aHpyf0uYtpnBiU03iZxtXXhfEh14OYQBbbmhBeku%2FYYKw7zWM4PaYFkNvsCIZCh3EJcZMMqC1Rscrfsk%2FIyqoUalX859luAkGcw2GSd%2BXNLC0g3eCpQw%2BzD647rm7vWswuWL4vwUfSFxLENYZyOanmnr6aFsbn3wdG%2FV47vGeOyPorWwT4leCZpUTuUEzfwn5GR8C%2B5GjmSFVOUsJ2bMtKdsEPHGUBbzrrW33NjbD4r%2BNY%2FOp9lkzgZkOtHSAyIaPIMb3pIgwwurZx8JEsWqHV%2Fx0g%2B3lBewqbLUBHtEz9iL6zL5ltXThT%2FphI8K%2FFfqXwTgAi%2BMfgMPmE1ssGOqUB%2FWeQ3tSGxgQvIK%2FDNlrKZdcy65awuMST5KbTwWooYqX5ZJoip60toSfRiwbcihI4G6qTXtMPiq%2BjmOENKIxYxjT8nPUyzVzQjjEWEPbS5p6vu02xVKqYA%2F6IRbvugHcR3iG23aXjMPSTyei%2B4qKBKoh2jVdKbUJuSu8I%2B%2BZt%2BBhAp6Jc5v0So4CCMy%2FmL21JviuHytuQ%2Fa0P9It4%2FUL2Gc3qJzem&X-Amz-Signature=4bce9beb666a079dcb1382a0f9185ea86ac44bee6014a2ba838ac35fc15bc2dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


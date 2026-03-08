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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TOW3MNP%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIHuYGousNq4juisZhR8nXlUzD53zTF8q6Ww%2B%2BPINffyBAiBzmqwiTMWzfkOJeJEk%2BdLEWnwSNNtObb%2BRtOixNyC6Mir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMb6xkhAMonw3eYBUJKtwD40tbLY6gZacF9BnHL7%2FJw3dtqYL7G7KfU0%2Fc3JGKvRXKcRh%2BfRO2g3%2Bc%2F%2Bx5B36tjuzwFZCNja6PzNwlaSpRtBzlyiyq42k5T4TgaZZQwfzn39g%2BLCKIK0av5ML4KWwsRssY4vxlxztAHpODOu7BX3013r1Nr3Samg7lDYeVyp6Zlvlc%2F0ZjUhgHpSzpi%2BhCRRqTfznizEMv5lFxlUHWggsX99N%2B7IAr9TBj4RntbmYX9%2B8twcjsRgr%2FMJWVPuh02VClMVmM%2FJoxdqjepMhikbq2E%2BqQtbecErKGcROnmglswVRHj%2Fw%2BdDyVOrBT2thOqjWQrfLDNycXWAwE4zIwVJOqN3EqTSl%2FSItjyx3UXYXOg%2FqkoPWufdgviXq%2FcPZr%2FMrJlg2vl72zJzGROQiiYkS1jw3JQBj76RsF%2Fh6%2BCdqJBJ6oiHtFs15LfRYSvtio1G3WrRTkj94PpIfCM9g%2BQ1XxPKiaDRtMdNUFjAVzDteYR9TcctC74n8nYcy8lbPisl0E7usewz2RcYPfV09zffRcrVQFLnkyb18A35ffNwYk4UL%2BMCeHzcM86s2OYhs3RYMWW3u7JLbgP6VjTBkIxxSJFVxugc3B37cJS8ngDJo411ppBXzcDSNSw3sw58KzzQY6pgGxft07qT9LvZMcHeP2NZRzYUo7oJiN72SMAdj2NaUYqpNZvnOy2VeymbgKOe2Lmws4XET0%2BOCLoStVzh4DJ1yZUMOemz0uyWK64Om7ZtXX61D9g%2BDeYc8gqzU61kjv8TPefIc46%2FseB9g%2BSAzlnRRGQF3OK%2BqmSKH9Jl044QummsWw9syxrkkjD25a5%2FFqjUA0r1qA6TDhjoDzKDMPZpWrx2LVeYJu&X-Amz-Signature=e27fcdc5a9f59d866ba5a415c34faef88b2b2373e56be9ab07e7276490f50fb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


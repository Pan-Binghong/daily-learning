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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYBMSLWI%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpWx7oMzyypsQmNppmh7xIFsUpz3XONBDW%2FWLlSfJ%2F2AiEA0%2FqzQb0MFOEfcd6HQ8T8MuMaYV4Nw2HOES07MmHJtvcq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDOjQeznm860gwTZRhircA1M%2BDOv2JuLcVLqfd%2BHvtoi7%2Be0zLgyvCCHTWpfQsmru6lMQnFGCQJod1QY07ZeL0dU6PfyLptGwfm5OwV7iYlSU21Crme5KLyqf%2BblDEuwnWwIBcP0uXY373d0kYdXog4CR2CHBPXg%2FO%2Bs2PFGSbDwXV10etToIwb3RlR2KUBsO75qIdg8NaYUFl23E3aphNUZGl0O1hWus07U65RvKyC5gO9boDwdLBotQPfKZJP2eBi565KzByKNK5QSfnJj15pr7H%2BLhrzuiW7tw%2FJjl6MxLBJWRVLhjUh2hOj0ea%2Ba6NXe%2BmmPUmJ1iLfX83xsw60R6l9yGORa9kmqBH%2FdSKGkRp2qZxcobx18jJZxGr6SqXr8bPw1UX77dytDcrt1XGHXP5yGZVR1flDejWHCs%2FJhMtRndEJYS4nTJdKCq9t3jGRa1%2B9ohs1WsVaMBz%2B963RWXLYA3whOkd3ua2KjEG6BNdyoFZGMgJTMTkwsQ%2B1dQK5JwJXQd7kFzApmlcLnc%2BW2o7OUuxHb0b8IugQfQVIqEZ7A9wvAXdznJIRbDxZO5Ig5DZv54Y4KP8ohBEaKTW5OhbpkJIKdrh1nUQq9ILfzB6%2FB4PH8btqTHY83%2B7FEadEiDMMl%2BzEFAzOjeMNKLoMwGOqUBuczSWHl69nVUvdEZaEgw9ggXX%2FAa8X6cyQgwXMHdsGH7bUwm7CKveB8Z7D1r6l3uJLbZIYBvIy4PwM7fU4kXw4ihXkFjxdpw1sXbvGbqo66j3BqOy3oE3JYQpfSXsPgtgJ3%2B6N8olFM4%2BbZgUK4dbGge2c4VuJ2Weh9xBY0RxItUzgvvQ51tyRcQb7cRDSfG2lr8HyUpLRDTbYjtqtBPlZziFmYa&X-Amz-Signature=97125e81c15ea83302abec45abf1ba1a9f52f32613c77e2378fa856686a4d85d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


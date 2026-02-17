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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKU6RPNI%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIApIwR3%2BMxojv%2BPks6OxTUFRYzV2gYn3bNlEjW86o8vEAiEA7dmE%2F1txHHhHlBGwJNIQaL7AZnvYfoE131VMSreUXBgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDHBmBE9XdUKJnITdACrcA%2BZ2PsFmqj7F7bIVByzBZ%2FfARB%2BvrDO6D%2FSTkLNVlV1fzaf%2BLMiUp0HNeydEnPsxqVwUPEIN6sv3jPDNQkWOgKi9OX5LKkraoiCq8PojCn9Dmvw01IG%2BEKinWDt38gxdFtlev7E1DtyuyRdiJEBwKm3RvitG%2FUjnA%2BhOISjgULorCW601FrQO9X6kxbyFvFSjY5JkkohZ9zUdEh7BocHLhtKnMcIZJr3JPTjv8pqzIvlEQFGvTZxBCa7KnW0Wwp1MjyEzeeXLBxf4JfjE1ahz2W3eKZZ65ay%2FAXCBpSWZUD1XtESIw3CpdaKv4KAQyRdx0H2FBfCov3oXN0ifC4%2BSPvXmqLGL5YOQcFNwjpxvBqyByzK1V2GDxKTC2TMh9AYdJWGi2D%2FPyagKhKnTohragT7Yga5zUUgMWsiU4OirCepcbCNQQlVLdME0s7AiEfJ1v9w3YS1UZLZbmzHbSq9CwtFp7h5W%2FKv6K1eFrxjdC6goaTVGZeA%2BM%2FviFi4449oYqiW9ZDCj0RKwxOBTl%2BcsxiWj9Ry3v387Aq2eZHq9jx86CJHvaFqrlTxwj6En4ZtiEMlAe%2FXKef7XZxcXxYzjPXNSsxiU9%2BD7s2o%2FF%2FHUjuMKn83Lx6ICmRHWmEzMMC%2Fz8wGOqUBC2rBnpdF9svyAhAnd7w3NFSMY5TCyxrGmRlYZhD%2FY3bfvY5vwQpFQ6vQMCWj6QfQdnh1RHwC%2BTdg%2FbEzL119OvMAkTJk8WN6zI09oZRuPb8nstGR9L1Ns9FC%2BkjUCoLt4p%2BLdNHP8jhDcB5nVTyWLLD7OaEOC96kW4RhaeJ5I%2BdN4XPzfk9GLgxeSuBPnzVRTZvcGZ%2BHmvKsJQQgWM%2B5MNdUpgPn&X-Amz-Signature=1bb02db6f620ac09c9f295dc51b5b8cd11b40186ae0c32d86adcefed7765f7a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


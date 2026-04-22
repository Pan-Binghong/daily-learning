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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HJTT2VA%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCBbU6Rax%2F4i8QsihsET9JyQUkafh%2BJzRYvrDGBelLkUQIgcz2ez8vHPSHpjKGL1wpYLpWPDFfe72XF%2FDLZFfM8O%2FQq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDNJf%2BW%2BEt7o4JQqcxCrcA49pxCJT53xHpSmzieqjJ3TBAJ%2BygRCsVvTFLYv%2B%2FpPqbaipVhApV1v4uoWaggVDpMiruDnvnDr3A9BXbzQ49IpYbzUrEF6LP5J8OCiCr00GBsJQ3sUkUw3HxvDnqwu48fVv5pnuV2YBt0gJSJfxCVu5LKA8xE8fImrArJzXNZ6hOuU7hA9ckeTl7zR0SAPKYIvxI7k7q2g3bQwE0tzJOXUVQdfatjEAo9ibi4eX3OiNhYbfvHmfI1ai44oKV6BbBVQTaPEYRV6SftjquX488wUKL1MqcWQNqANqGMDsKvC3avjDRQcaaK72EoLdLGQeiTI%2FOf3Sp5yTZ3IWAkcUYkJYQwzfsTVc%2Bav3VBEiuLvUBWNVnLlcnE%2Fs%2FxmfY2qzvYV3t2lipjb8rl8je0LNUMNfawF5OXsZYDZGggIUcXqRhBrCmNWAmJB2FghFGgRxRcBTTaRqYgnp%2BQzlwfddp24oEU%2BHP8AQFBu4gYPnxkKf3t32weYXpYr4KZDAaJUB1B%2B77IVuwx5m52I%2Fw6mXk1BC81W0Ur0F08zFfASbolnDv10OdskjtdJJX%2FJhAV49FUkPayA9Ivu0zBWXBiE5NuqWIzaJjX5B9xZC21S4gz1WrFvW6RRvbpwUYtuQMNz6oM8GOqUBWaq%2Bdq0us7Vls8kG8YafkkwWQ18%2B5z461mFwprRJWU92%2BIzAnvMMM107vGRurXmStYmbz3KvDQ3Vk9EFhG9xo5CXiBmmk00lMeAj6dFWP%2BTeaPiDsH3Uau1G1RBqKHOcc9qfOZs8dpJwVpgG26H9wGH%2Bw4DM%2BjZCD0saMG%2FwGlJaUrFkzYpA9qT97dY8qu0zjY2XtZvW8Edf340ppmAm6mBmsJWS&X-Amz-Signature=4fea85c352b2fa3a074ef735043303c88f39951cea019af2de7012af73503efc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


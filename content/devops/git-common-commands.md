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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW6K6OPJ%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQD0JCDBrsvCsMJ07bPZLYMKqoZvuSlpSuud8J7sl7JdngIhAIbQErmzwcqykYMsUJgo9wVxc0MQBCoK%2FQIYGezoKN21Kv8DCCsQABoMNjM3NDIzMTgzODA1Igxw%2Fo3hhT5NOh%2Fex%2FYq3AOXUd%2B72iaHadfLbhVejl6RA7WhDask6dG2hWK4YRJ62BXPJTfE%2F49RcK1tJNembkj6EvbY53PJn93AihEm0a0w9L32qgFOTJ5GOYbUc%2FVvKYlkzmPW8qtKy7GF4yV0C2uImip78klEFZemjiWMRT4k5Mk0EDMy4Nv0%2BBsiudnsN1WQuKFdQm3QN8mJ1Jnwj9yrfU5S15EXCHV5Dd0aYwOTXFd0GbUQ4J9qGqtHRtCGsu1Ak8Hu%2FNKv7nRblg70TKw26tARykAjaT08I%2FFayTFzvHmn4bfgUM6dWLRwdOl9FS6RGk4%2F3HbVQ8CLuAxRrHHvmrljtxW%2Fi1P%2FeHb8RaabJSxeEHh%2BY%2F39QlPbKJo6LCNGSXjYw1yQrwm5RDBPkO8G6Xb0EbCtlH3avYtfYdqFF%2BHePugdPfF2HhgGm94dd7toqcUoTIvTU1kl44ut6fgNepUktD%2Fe62O1kcbCVROglTdpK1nAtwBkhKda3PlBTCRvhNYXztN624VMOM1wfSTneIdLcdNYhgd7Cfojl7MyLVltUPAA7HuSYUbRPIoDp%2BMa66QO2t523BBnNcjtY7te%2BB%2BNU7H81fU7HgkftxdKkW3qRjbVxo3wj3WHAIN5%2FuHjYrTsx88xAwK2ozDSm6HLBjqkAUwCrOozNv%2FwFWEFTdXOS%2FT3pGJerbl6YfP5sUmK7Rgr9cF%2FSg%2F4RhUsHbd4DPVxAldzopNa2c7p95oTzzggARzrsiKmhettBuoyNdgW4OnskFwqOhxIvEHvHgr3Tji4aU1M190geAZJ%2BmANmxThbR5hKxhbAQ3%2BlWDRvVfKGP%2BcBGRE9JoHC0ASk2S5aZWpMXGy%2FghydVYwtIWDmxTuDaEr7Ijx&X-Amz-Signature=d2c2300e3bef43b40dec81f53973ea49b5e8a910920d7de77e9918e78958492d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


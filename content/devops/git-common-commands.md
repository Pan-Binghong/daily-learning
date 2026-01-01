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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XTU3GLO%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIF%2FiCzoEtSG47xRuQTBw0%2FzcdEQDqLq3ymF%2BtXTtNKkRAiEA6B%2FeS6rNtbJ5ea9PswtVM9uLsZDMLHm5saN358ZyfpwqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BeXqpO3G85h4JmMircAz%2FXUTfGzdUctmgDbSmF1ozrfv98aEx2JcF0%2Bn6QeoR29rahEGPJESAR7iea0RZHsGnWWOggrN8tsX4UIXoJxUdm3rfworNHjhnB1QSIxcO3GRM1iT988W8Elg8azeXIIGU9QgjIcc5pWqsyEGqacHPApLJNVC0fSlbAoIh1j4JmmVe3Et0oshYLGlszJ%2Bc%2BmIJoi%2BkmdK%2FNItPrnVPZ19MN8urZLZbxvVW0bkvtT01Fb26ZTZmKtEVyGG2PN%2B8U%2FWmsRVXAOYefbtEpIf3H78TBddNKPqur9kGaW4qe7D4etT%2ByOiL1jCWZ5Zm2Q0pVBnVR51Q%2FZQluiPyI0bssD2DwFM%2FmRZNM3XKkHiKvOVIiNYXig%2FRrF3R3A1GAXvSwaD6dnm%2FJRJrdMhb%2Ffia2QEf2T4bRqR84D3oSkAi%2FkXR1lNqAR%2BAKzaFAlI0z4oFQD6cl7X9H9Tw9PUoCk6XUzupeIkL5cOZlSHx2NMcTwHqoxdZ5SQW9uY5fA8woRbKlHh%2FiG960TeOgn9tmYmBUYpcb8vr3xpv6wRUV0MBU7jpfD9r5XKWZNeJjplB2kLGgjBhPObojBYcTPR7tQHQ9%2F9Z9kquYoPIfEtP48iTURaiaRv5A3jrzSl9cc2iEMNiY18oGOqUBvPnhgNFs9%2F4rRj7sucOMzqhzhLo9adMWVuvQ6pa8mPFayFwJUDIsFWeyQeUACbdcX3wPL6gvSScUPn%2FJcHgVTLzfarxwODN1AViXwsmS5VDnogKAS1vxTOk3u1RMOyYyrf9VOLut283EiYF%2BdZDm1NyTodSKThViToaLkoZfpkNz5ERpFTBLUHai7DD6I4ZS%2F0psHSUmtwz0cZDHahWPu%2F3i7YD0&X-Amz-Signature=c558e3c68132fd89a4fea9546715f9af5577fa50ff12ec0e4dd2bfbc10056d4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5M5ZI2%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDJKUPzU4e2UWrjbzmj04qkWFP%2F7dePxisPwZcFKeCslAiEA3x4e%2FE%2F%2FDHmVSd7t5vDuZwMEocgo8UBvVt4%2FIVtsojIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwj7Qg2s1x8YvKTjyrcA9fzF4iKMmSS1x4eAGVc5goCeEuLKEMzYSePbzOTyHfobMXViucvlbN9WHXPMm6alDN0EvZPR4B4c7FfBi0zmhRycp4frbKGzkuYb0%2BbgBq1Jwv63ea5xAt3OssugFDV1%2F1xBUFkXdU7AY%2BsKzmjK9jrv%2B08KO%2BWLovk8L9i7PSu9QAFIpWfaeDmrgkvSwCW%2FH7NTxaI0Emo8tQlhWqToImKYuuxf8R4AvOwuNQBVdFvMVLfV8ZIijbw21FhAyloUZOI96YlxukBUknBTGm5lnRvs6Q4nlsZk3yugTowqmCRcI0nDsDzB7ocB%2FH8zBlA1z1tbpzVmJB1GnNh%2FLDN16Lki9Z5%2Fksib3yJk3ijxxbOyOpcUo4n6157JMmJ3t0yWO82vVXMmovN5Can%2BGo%2FjMMTP5lpVCT1mw2NBOBQaxFZUdJc6lz85AXHpxbKWSuzyrngHa4ESwo751wliNoFXbVRsXFh9PTkDGVn172IZgLeqcRP%2F3q02EiJNGSqsAenR80%2BsQDXg3G6d%2BOPwwm1exLZPQv8WRsltopbLm%2Fa7j%2Fo9VwtCAOsVNVqE9C0m1neJgE0dpE%2BPC2ZR%2FCaVaxebis6sKjPf9c%2F%2B6E8weRCHHaStyVV%2F6sEkE92xtpwMLu85MwGOqUBc6l7JaEVIvHQ4xmyewWRsOyDD%2FYRJ1X17RQJHLPvXQDwYnXMd82YNoGY9RjFrpvOP0i7xL0Z%2Bl3S5rX4KzsX4LjPyz4tNTPVtdj0DdMP394QRj9uP%2Fx9Bo6ofMGgZvZPsBHASFovzQZ3dogzbInLboAE2zhWBQGUgH1MQZVthWnU7ZsJIgU9X0u9nVAQXrnQ038sZZGTcJ4MH7FT7eRr5HZX%2F2aU&X-Amz-Signature=f7bf4eb3b7e59a6c005040f360020fc51ff6532873e4751c30237430cf723360&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


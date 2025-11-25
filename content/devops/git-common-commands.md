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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGU64HUG%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPL%2BkY9QG9AF809KOswg5mJcYiNT2ZNP%2FXfXyefgsm0AiAQ5SGtzK%2FujAxqM7sFJX4uzaVs8FIyO8Tap1HQIyL40Cr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMlZ2NaCSJEgR7T20UKtwDyuJTqGvc90A20G1x4GFd69i58y92PtUnDob3YkbatFDrDUhFHALxKYAv0wEBC%2F47VG1K3Nz%2Fxc%2ButOXfkndMJJ8s6bmXczrEjMU%2B1kfMuVywmf573fJzgWIoEP10cpZkXmtRtYla8segiOlMxSlf6aseoYMOaxd78OdtnW9WHugxYKf%2BySPfdVUn4W2GFHk%2FGp19eWEdFqD6ROY7ewYrBm4GFbxSqlwOxJ9dRbwUMdL%2FTlJ67tMdAiXIOvZDIZ5UcTAeYZHtqtjSUo7RksnGVqIJp5ILKoD3h1CjqnZQ19mBlOIXKAInlX3j1H%2BDf4P4%2FiKzXBQceUdB5OC5XkvWZdRvH2hA%2BOS%2Fs8uYCrccAHuIyBpLD9PORc6fhV%2FcH8zj1PH0UacDbo3pt4lJQ%2BQk4jH9DpYiDj%2BKodvUtRqkuAehPidCAxBUixTKfSia7uuyptJVCqqS2UIUYlhCo6jtrWnwfAAiyGe8YWlfXbQ0jFckZYG4hFGxhEdPdoX5GlebEcNJ5u3T0ghT7EBwXGjxWBc3uFztPpvosZf%2B1yAUC9QC08ZvIg7AE6OaRmq5SL%2Fn955t67ewaYD2mYCrnKCVAyCvKB6b6Nmx02%2F5ruGUbg9pMsAIcHocL84USiUw%2F62UyQY6pgGNa81XCC1XmXKRkZGUsDNFyoIPbliotYyjJ6OmfzMEk3QeitaYLUIXrKKtUCjNWbZC2ebSjQOF2OiFiB%2FMIV1IX%2BoVHPjMLWqBg7sKBC7O2%2FaslIYNU2O%2FVCNFG1hpStvxlaLjVC2ZQyeXr06jF98oNWk%2FWqbnrXQn%2BbwUTMC3D4Wu9Lh7aIRbqzSqecnkTP%2BvODN1bu3o%2BCOW%2F505DWbqVBrOBb97&X-Amz-Signature=e756145ea5e901419216f7ae1c5da587ea75c88680b9ee31f18d3874264c4f80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


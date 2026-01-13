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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWROPW4P%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDHdfBWSXSe%2FJ8V%2BsXYQdBrQI38rwPAP1m0MlvlfleEGAiBvi%2FqndP4iTbuqLySUHUD%2Bw1YwEFUSD76QzH3SG53jQiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjG%2FwZHKhPwymRBmcKtwD7u2qZqLoZB2hjEUYvldOlm%2FSD9y2Y74ZopROWETZEtb0G%2F%2Bt3ud3Z%2FSvnMOZru2nX79IMrOZYzq8boTzBYOXCOoVnsls9EvIfKnq6%2B25MP3AVEpbgV9cjzaFoo7uyDA51znx%2FgI59HCE5uBsm%2Fz5tZsm7vlV%2BegS29Q%2FogbF2bUr9Y4jSRKQK4xybyRZSaS6a1EgzY8LGA3yZ2Xepjs11TfW7A952wxbOzzhWoGe%2BxSTQ95IhXDDHJLWPpv8mWEaTHkFL5IjJk%2B%2Flj%2Be8E6V%2BacXWsKO9qmOPzs8f7zfW83jYl%2BGSXGyxQzSOdFrwHoAFPLU534wxj2iiX86FRHCHU8fNeFdWiMbmAnzsFS1ngJGziAVt%2FKasqXViljowE3FCOTwUGKcBQHw8JFtrzS3aCAxEvVBeZIIX9b4zGN6F8YjBf7q77vuSPh3ERtvIKcNrtQ8HMXy5a9Gw%2BdwD8S5rieDzr7zy762yyg7ad8vomfqpau7cvB4EJQQCrQvrTJeYfYaEHismEX3WSvBInI4gmvos5QVP7btpXHz9LXbicyffNTom7T7E3M8Ox1OH7NAt7ZqYtEKKnxOtScaRJkJEV73ZkQRBrBdaQ19NHunefwu11gHhSzLcjslZ3ww7OaWywY6pgE9Xmaerj6mHaLmAVZwXI6xEF41pEcOcIZK6RdDHlXF3j3HgYS1qB1O39e2czSFalabYZRpuupZ2tnVGcbIJVcnFlOX2E2EhaX0QL6Kgo8Vov5QBao9vAiJfxPQwMYZim9szxayxUzR%2BDVuuTrgoA157KJ%2BybpW%2BJ9BfyOQJXJo6RnF2OmS0ct2EXMOOXZ0A%2BDzgOe5v4KfwhRr2mB3sF0cd5TUODbx&X-Amz-Signature=bf25995b809bf70de70648d233590e95eff384a0755dcc555411e6f14734d8ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


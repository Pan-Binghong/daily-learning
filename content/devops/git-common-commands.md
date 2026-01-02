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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NU44AB3%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCylhZuJyYzXyH34kaVPu2InYpXMQVJqOIBdS8RqzzXjgIgdXneEqX4BVGXrhhyyl7tO2rEtQ7Thk2gPv%2FU%2F9bkDBcqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKo0btQu1pdqAL7jyrcAwF0iuvJC%2BXkYdaDWf4xFcIArF8zrUd4JAdU0Pvj9UgVUpGqiFGrIhksxoWaAHbm1uyKrKkZcEMnW6zmSffLupricRtaCVJj4%2Fsc066agtjgr0jX%2F55J9nSeOuBK3HxVvTbXP05M%2F%2Fc%2BX97pvJ2H03fCFXJ2R7jj9ftx4T7GA8MTcnhphLHX3vZkwxhQuFfgfDFzgSN4xoZjvBRHZRTU9zbi263de6suhIXuk5DhZifkCJDX5tIlLmDnh8SxPKc36VqoKlJJg8oXHLsfjbjNptpodypo96RUpMA7kZy5cHKz7RLPbDeuY3Vu5WfRBcWAfLUUSrKUD5jDyYA%2BnQAkAK6nsdfrTgApV3YfKR3hZrvd0gx1hiW2H4AHdbihwCuZ2NzBQ0uEF62Kf2zrx9c5Jo4RRFVLo3yJAiDgtG5DmTXI7Q%2BY8jSxiEHVwvdrC4vWsNGgPuhkNy7iOOmA3mJlUnZy1Wf%2BiBj%2Bs9K1cDmrMUTZVc8xyYnJUVMiWFTmaPwxiVulgXL8Z2o67sW99M%2FQF5IPsVpbnUKFw4O1Oyvg9A%2Bg%2FFxoeAXzj9iGeWwejgZ7wZWBHhtb%2F0dCzOIjBrlMqAvAbHsN4c5DaMG4WIaZW9QCi2Zoqx6WN4gvJigQMOC03MoGOqUBPMVOpCeUwmJWWNF2FvaEyZqn39k2ilDXQfi5RNr4R0rRUt73zdfVSTEcdpowQq6s9OX6UPKbrfcpoRMwyDKeytMNIV7d%2FyA8TGqhh86hSJ%2Bezoe6%2Fj%2B6P3fZQQmA9ITHI%2Fk4DrBlnE4ajCdATpMRIX3JoFp%2FcmLK1QmLgX8p3ADRFWonQD8I080iHWnxBTUfrzbAC3Gvf3ZNuE1gE6zaDDrK35xP&X-Amz-Signature=4b9d8f0fc22f25f266e4f2adb3575a8dc071792209b7a28bb5fc52867eb697c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


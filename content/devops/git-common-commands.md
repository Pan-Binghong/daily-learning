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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7NYDMU7%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCVRr17%2BpzbKJewQOdj4rnDPmOWlNtqx7uU5psmJ4DreQIgCfIgIqxe1O3tajsGCgncDGimA3ue6s9lhs8mrDbPyisq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDGtmwrIl8XEfYFBfoSrcAxMmJAqJI3z5RgRTN0pu7nYxdwByWxLwLTxSYrzys5zEyijBBAIVbvTBbyobcbLVupDPxmscRW0s4E%2F7njuuLPSQA5Zdzv3ntF8vURPCs6MO2ggQdh6KChx%2F236EGUVkXKw5au2wvapQLzV5wLE%2FnYFuFt1wq6fuQq9Y%2FenpoYMy6fUvPtTLW%2FZEV0HU7vyN%2FXQdjz%2Fj0Jo2KdGtn8TBYHn2QCO3gkVUFxayVmCYx%2BWb8r%2BWgSLn9Ftji5yUVTa5d%2BwPPEEO2DPGseKvzOL8p3wtxnIs23bS803mAqnF4NW0eJRaxq2WHjvT1wvvXHu8yuapTdgH%2Fn37T%2B0SIM47E0187tjQdV3vY4WoIvZi%2FHShHLxBqWleZA1LBm9sxqb8W4f4XIi%2FVRQJUW9dyUQrNU%2B5ZEcbLM%2FY5ctLHG8%2BsqvKSK8uEin0ttTxaxc%2Fm8BtpF0Gm3c5gO0DbJ86NzJCMJB84gp7k%2F3%2B5A7iCSyqIOzWYCXIRa%2FQ%2F5librvAl2kjkytaEer2b5%2BQoSkY80FPyb7XoXkOP4O6IGCu0AFFxwT08BUmej7a%2FkKp7K66boy4TRQZne1%2BQtMwgjeG84WAy2tXwTBO1P6n%2BxbPGk2zUN97c1bBF53cHgb6UnJbMICP%2BM0GOqUB87qWk%2FN0TGjBGrPf7E66nWISdvLnClH1%2BnZ2htjSUJECZLXjUjygXfps%2BkqkeffJ2tQBp16nNx4euvMwwMi%2BqA6ZqukSYItneUQZXJmwXPS7gCbvxbVA5as1AIMmH%2FrScz1Z%2B748XgP8YK0TOwbxRq%2BlAWphCQEHc3oVTpbJn2JMDxBNLOhoyY2vzSOQ43iN5GFqu2zM6Zd39mqQOzvxYx2%2B9200&X-Amz-Signature=56bec71e963304cd834f814614e7b8dd6d95d51a12337d249ea3fddac2838e50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


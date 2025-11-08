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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIU2XDUU%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQC3xVvN4X6vY0WlJdNTuZjrl%2BOm0nmpASSur06mifXdCwIgItBXp8UlNAPL1GN9ZkVP8auaY%2B69v7NN9aQPD2%2Fm%2FOEqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDABvNMRWAuKn09KQ3yrcA741YrdNZdh5AIsN%2F6NM6w6D4oq8BRF7kiiJWWALxyfrcpaUlhdarMqxjTs%2FXzFPcnEC2e2s0w4Hhm%2BlALzv5PAPgJQCBrxMpsuS5d0emhMBeDn19OAR4QO5LF0HcmhbnzwNf%2BWlAkp2ShiR7B6JDx0olzj8AGYbTgjPUVB3Ej1lVIDG4zrT%2FpjNwEBZgVE0f%2FGXymMb7BO%2BNsv46nEYeimRr3OSrRY82S8LSp%2F70oq7EKYLCGM85maOPs7V%2BxS56yUkUBhYWP8B3PZuPtn8MdXwVrn9I%2FP1tPrIIgEYd%2F%2B1qiOLmEqaAkz7r%2Bl3cyAq3PsMdBdsKWgqZtbI5h5oXT5ZTpB7apcjK8QSnz63pmLYXWLNAg5phB3iaHxNOHxYl2bQbZEcrdRBAq6PQrV1YrvQLl0YpKphyDrm1lO3UZBH6Ym3NimPrYeorG4wF%2FBX0MZqDEX5dRvvKcpnJS8jw15dl5WLQ4Z3aGcMQKnD6miM4GtSsVcAcqSk%2FhmJ%2BBLL94uHJiZhXavKMnI5TZyxyVYNUyRWSE8GNyYqeBwTSgfpas4qj5hAeIR6swx%2F8Kfusjp%2BuhbjGm1VEnHkxbAz%2BVkvQsiO8%2FvNzGSCWPvemoOQpS6LRuNFj%2BmibUBJMMPQusgGOqUBhZHPe%2F2LhFSkrVmC6cg%2Bd4fRlmS%2BkRTYemPxDWzqQGpLUzJCIGjlWfkQ%2FDsySc6UEdHCLWJcqF8DcQOpbPIkj7W0pmcCl73sfq4xBzBubNKOp7LXVX8VRDvBYM%2Fz2h5%2Fw4CEZ2aKBtD5a4uBGCfsJC35m7x3In1GWW0rigEMcahBxpf0d%2F2uUhMqCwi2ZaJoapg18k7cz%2BlCVCXuJnrSRJHrWX%2FN&X-Amz-Signature=c8f8e650fedcfc869a73727369074f3d9947322cfb05c3232337bc65db15111e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


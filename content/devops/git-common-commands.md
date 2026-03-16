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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXTQM5ZF%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDwXPIl66r6I6akRufGuxl8ztm1Bu0T5M1ggQt57H3XpAIgIKv2lBBz9TkDobE2U%2BVwkNWdituL5Qd7zuG1qrCXeaQqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO8QDl7Vl7ZIEZRNSSrcAyUqs%2BK02sCVmkAHRVgVIRQRGXmAwmfY1DoHGUwG5VMmPoXPSBL1rEWktI7WD%2BOVTm0fmISvreIq%2BONg4kGniBACcQcYbUPGXqlP10k7XF3OJxef4VioDO5m2S1Xfi0%2B7l2jMs5iIFVetM3SCdqomtt5siiF0ISQ2jGfS6%2FHnctlO7pXC90sSWG%2FHNAwCT5ShMiAl8NVzH8gHXFsJFTVP27uFX1DBMjSxSSLv5v3yZHAjTx4c%2B0dCN45EmRGXhkhfgsb%2BCRO8%2FOW11Y%2BdWgIuTpKfFNJCN6bxFq1bq9ed7VM5azjRQq5DSxcDEPinhuiw9bmzfkTsjpfmHqAFr89%2FDEqq0%2FkoMJLrLlMf6LTKLybUa1Rr6GuJSnBH6uDLNk%2BO6E2IBi3hxDA0m1eiLyhHMEJv1rhst7WkBIShoKy8LWnJ%2Bw2WXAMJqzNTn4swEeEv6t08JGVWKeqOaWTOTFswCt0%2BRjXu3q6mhMPkYE1OfY%2Bx5hQ4usNYKcDRrPUvgTjhuhPHMbfZGSAZ2YgCp1Yjl6BjfhTKnD3lXViztSH9zPy1hy3LQTueyTx1B8MlnL%2FQB2%2FVudv3ykE3CDYkmO9GKFfF15LKnucPdhwwmv3rIIb1Euf9VxdxVqwBfmkMLa93c0GOqUB5jsmUKXQ%2BvUS8yAE%2BScMKyU89rJNoD4p2w8l56z2JK12JwmWbff8FwyD%2BDAgHrO9TLLvLikA75Z%2FjolC7dKb5DftvO8%2BmfvoPalzAw0zyaH%2BkOcynGvOvvEplEUOnFD7S4gHlWa16Eh9EgkdJUVmUzv1NXk2%2B3ja00NHaTjHjOcxRDZD7oqNTGs3%2BHjuR8%2BOezt8%2B96Cfd0i2zfqSzd79k%2FjUPai&X-Amz-Signature=4c3683d7f709dd420ccf9c7b4fb7bfd2d52cfaa940996dddd48c4c10e47d6220&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


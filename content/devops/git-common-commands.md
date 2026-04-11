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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLYY7JXK%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDLFCNConzqIRgT29g6oDaQXeMnp%2FSXq0vaBZZ4NdUiNQIhAI2ajs8gM4yWOVmbHJH%2FHyesxpbxtBsNQnhVRlMIRypIKv8DCDwQABoMNjM3NDIzMTgzODA1IgzDfyCJNzrMlzyO4SAq3AMCkAgmmQlQe%2BFDsB5b%2FX8IehGxBtLU4OfDZY9MsRMcBMIOf%2FhlOp2YcMAfqgwediTE6EZE2zMkOxHIzGpQgWA%2FRXRxYCvJYEfujQmRA4XW05cYptVcHOQvtO6B7tl15%2FdeVxVB8GoKQvWd%2FJwHJbzspgVgAbXS3ddvTw9KvBvjvYf3P9M63mMJEjUrHxaXTtUQca%2FLWh0wVP3JPcdQ5dquwq3LY%2FwPVoifJx%2FZ0%2BtdhfHcgHxYhnlQdjRzoNRBa%2FgpeQDpsmHJEgttPPVGYnktqqn98NLW2lvXsJqmAL8G6FozyX3l8ikF2vgDsC%2F5gHM%2FCXu%2F5SFjP4%2BW1acpF%2BlIlgB9evArptPbO4znLAT3efBZPx9Pyvz2WabgDYEBJ2FIGGyqdf6zS2a7QubQhdxMZULE13%2F8%2FvpHxYegPr1KXJ6MDb27LgcsiLz3zq%2FpoCY4ZYW%2FnvZF480QAA%2BiARb2uFqQZJkG9mzUVLjEpjsYsoOi5HGHYZfCu9TGVwC07%2FXJ7w1Ky%2Fi1AgVpXIw9Ce3OlGcx7DMFbYeXoU5j7Lr5hFZSjn8l81JZ2Tx%2B3fiEQ3JESDs32b1cudbvva3ONlHzQaNWse6YeppRBPuh6IUh0NcN8dt%2BcoKF%2FLrbazCu6ebOBjqkAZNu10j0hdXywDSkIN0L%2F3yO%2Ba8AGJ1FrddBgkA2%2FBMIU3wiYE7xCUWZFf6ywr0Vm5BrCuxdWYGp7GonHMrUyyzm%2FB2%2BPz%2F8YWgrFKw%2FNQSxRtLyz5V49D6GttmzLT05kQKEux27JDz%2BOMNWBNudosjhi8zCp56RUIRIbcFeDMX7PeAdoVsAbKB7JodXgSz6EO0AWiPGK9VBCCd%2B12feDt7SbdWj&X-Amz-Signature=ec644fcd6302656b96902dfb76a63c7ff094d18ae97b7d32b2e908564e7323ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


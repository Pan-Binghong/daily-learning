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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMO43VRY%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEd4I95CpXDp6ezCYtSHe8k1BJVLhoBjzEK8B9Wbr3vBAiAmxqSDA8BVOOwt1BQARtaQI33O9boVmXTxAihkJwucbiqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ5649X3uWtuvzjO%2BKtwDRglfucOfcjJu4nAOaKqqIVh%2BHnbZfp6dkYi5lpLNi7Nqp2CbWeQXGepFLYy3%2BUcMYGCtWoKuCf9VswyR5Lutc43RpczqXZbUuAcHwKk16pwvUCm8wFE8YlhxXpCKBJIvau1CsjBh4mzDR9y7K571HLuy2hIqFHbVXvzQDn3M%2FpFh5x8lSsLrI9lRnWI6bGbpf4uMGuhleriW9LTN971cS5x8DZ%2BhKbhg8KWC5vqw%2Bpx0KMQCWwG86m9cih7KrYFdrvgJlbXccN959S%2Fv7laW5r7CcXD02bTAKw%2B9%2FG9cyaaQeQ%2Fe7bqBrJhPSH%2B1J10BCrC5lzPaOAeAPshI%2FVrcPGJtRbXjlTKy1ZcFS9r%2BzPc1VSTlu3cjHBFzaVyeVHfRU60JcZU7wCew%2FGwrOJZ%2BYGoCIVV4wGC9DeGCfGDFEIh6t6WvQ5lMdskZo9jEh8AJPx4YrV3eJcMq2aTA5bZQnugaBWKyHZxL54oiJIUcQ0prhVAt2xItgI9PWBn0uMwbP2VcJeHu79VDG4EO1uEw%2BVXcR523AVeejZnRqdhTg9xyf%2B4yLFHxQhuwszPEFixMh%2B7umgiM0TBjhpM6aP%2BStn%2B0NAFyGnPFlnqGdSflwxgcWf0yl7GLB1NNvjMwhJK1zAY6pgGHWIXThqpHfFhVUQgTlsOuHKefb%2BXtyKzTt3j3X06wLre7lR4fuT9hvsdr0Gw5T2GcUznhXWxGIuaQLvKh9eaHiDVcAy6INZULhD71WcwmPU8u3b%2FYKL2TbJcJcgrCL6WPEFEMct8YcJB55twIV%2B5875%2BQAgW5BrRBqFf%2FoJrBDLsZAoo%2BIwNCQ2Fxx73LVtwKbKYDdY%2FxnTEfJcQmYM3M4UAySr3V&X-Amz-Signature=6b5b37c27a5574569132f322352b44fb770e2e6b35834975f66a275adeb97b02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQR3ATNN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHgOVJcR2Ztuwri3xzNlGQ6fYnMEzIyTlj%2B7ZepCxxc9AiEAwhj83BG8WR6S8prCPXj32mIDIJLork8IdYFyRhb6Aysq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDD3tBHUHXw0JIzTJvSrcA8sL2MM691jwbCR%2B22Lc1PIn68scKU5hL%2BXUy2faf%2BOw9HPanmIPAK4SlexPjYZ2H0Nb4zTij9N%2BygCbhhElgxKW62nhF3NSvtnPSi7y2%2F1BeMiAjEo64B1yztxMucEkEwW63%2FjpMcKFDJaK0oFG%2F05sdLjFpRr4zSHt1jOT0LGnZj8XPXAvRedAYXzO%2Bn39Yp0fA61K2md3L3AkMknBLuO%2BYIfkz1mLMCfFRrEU6QnHeBPIoC%2B12IT4z6pPoSJKrnTCoJt%2BXtol%2FLAZeCt6CaKiQ1jF2G%2F8OvNdi493vlpQvo7ZGp99qnwq2tR0gRWEhP83zPsBfCIX8%2Ba8XEGr9ayGdn6HeWP25o4%2BfFMReyxH0hmeRK%2FHoztgcyXGH%2BvKTW6zOk6nzNUGCR4440t55S3OUHjLT5c9RJK9N2jkQspdGNz3YaU95Mu971Y9CfNXrff8Bjdyq0tmVX%2B0lDc%2BTaP%2Fys%2F08XQoXpJMdUtwrIMaiJFdCEV9s03TGLmSz5%2FbcrrwrZqJmqlomNpVkCY0NtXlFfWj%2BBvCMG2G6XnsVD4aKcNL%2BVy4DT5mG4V%2BUI4y7uLAFPd6WG7g8m0cJ3fx6Xb5C3KlLjihLYxvExSh9A9yf8PhDg0Atw61FCGJMMbA38gGOqUB54e%2FI8B8i71BjfGUEqvgEYBM8ZCEM5fXonVPYVhcAVDdZ7eY5mjLXgcfU2qYdsghBtYYixMbZp82gK0X2EsG7mDxjE2JRnJa%2FyW6el6otGgQySRLHswGAzrFsU4vaoilEhM4k5NC1R%2B8o2Vf83pGiO9TzMQVzUVl%2Bx3PVw1XWznwtguyqAQ6wx6wPrOT%2BUYw270cML0UNSaZBcTkwn7qH5DWcWZd&X-Amz-Signature=6a47fef33c134fe51f0deaa66cf68acf5b91aa2cd900109064008f9177882c2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665V4U4H5D%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBdhqN9cRO52J3qQYU6k3tLTOCZ7n9sGn6H6qQ5OgzSKAiEAgvKeS2p6C73U8ecYO6Mauvd8GeYo35x5R5N%2BMr89O64qiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOA4iT1OqBuCaQC%2FeyrcA%2FCRgM4mQ5RbgWSEVhTrovtF0qFtLjmO2Kp97caflOV0FL4CVJx3hrtqHjyL6hdpn3yrHoHcLkXy3Yq7IuBVCIqfqVh1gnSvWCHAYV%2BH9j7zWdZqdhYDkZeBNzs1DUT0XnOsAahpUb2cVG%2BHtg9Iz5U%2FKummfAE94l5finMVVkB44II4mPl4NTF4iUCvupu5ZkWyf6ikJ72g%2Fyf8uGMEYOT7tccNEa8P7nttZODgH9ZXcgCykcmBn%2FqvzcW6J%2FHH%2B7bRSVWW3bO1jq%2BE42GiNZOVbXKg9OMNQjmteiyGB5A764NgiB3Tqz8LI644JIhMt4zNIG0mHNIu%2BDnFo7D7%2BNXw%2FNQTycQSoM9502HC9sSne%2Ba9zeKf0ljF7MjLWvL8vhcBpa%2Fmb28YvHM5Guow8sTZdxyzZTMZn4tOR919IAy9ed6x6pkVq5tpms4rw0pHKgrJ9ROxZaoNo0i9dhW4wAvjzpx3TzgQxyypkcUuu%2FfNZt%2F72aYVeLn4ykq8AIwlzWal7F9t4rNk0kL5RyTn4LkphosFD%2F58okJqMRYpyxjLGP0JpJlviuDdckSo30btSJwnMgOAH3HIblFIv6pEHGuQ5ypN0%2BhDKpu%2FgNX1h%2FIrCcCUAzc8AXG9ysdZMLajx8oGOqUBitf8Y1X7pQcIo5W%2FZa2tU7vRR%2B33z3Jz1MopREWh1X2CTcDKguLnR1yMOZ6U7LqP39Jmik7sWToxwrx%2FJ%2FvylKqUEJyWXqbxujeJ3LmUS0otWCeowh%2Bob8s6KkShhEQ3qRbH2A1ElXcaUbH3DnGIJrhr%2BFKtVpfWZ0j%2Bb4b3tW%2BDiYm1Mf6ZGQ9yMDoxqFOvCTCyyWJPSTwkPRd9Ebm2PHu7pGpZ&X-Amz-Signature=d0f2a6608ffda1fc7c96ef2a8988e24ac0a4f2bce486196d462068f21939bf3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJGIZCFV%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIBbMSrIHad23S2TN%2BLdW%2BYK9Yy%2Bh%2FOL%2BnuWQvpq7g9AaAiBvqWi6Tsj02gCN2zjTuBQQMetV69lQPg3bRqbe1PfEJSqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq5lbZ3StxPQcQLQKKtwDPAVCgiTgO%2FNsiH%2B8pa%2BIHn3c%2B3VrCYBe9oAT9NhRASV7UrfrvfryAwWL6NaPtSEu82SC9LrWzyhPIFUBgMbWb75EJi6ifvr96SQ8aZLSOvZ8jvoomGle0QFfF07OBVUTX%2BMEA%2FnXodYc7jihsX%2BiZLAz4r%2BtO9VvCqkyXcwkmcQgNwuRRLq%2BSx%2BUGvaGzEHkBjCJ0DZXc%2BJ2UdST6L%2FgdIg3Z0dE7trMsrgz6fY4EiJVSiRsRdZ%2FZHbvmQrOXV06SYvO%2FwLbV%2FknDoLIekiB5GLGmM%2B3Q3hbtcrl5zGXdc3%2F3pB1kiSDQ7Zq2ahqcqKlFK%2BM12DDyIF%2Bd7tPxNZcPl5iudmNMU3CXa7B4qyMAmdk5vy8QvZ1JiYQiPAazitR6K7CoKGU1rrzsYQ%2B9GYgi8GtfwjJL7BEQr%2FDyOry8zgF0uruWTfgBUP%2FZSrpfEVjngnJO7%2FHtaNTcAznT68n4zct7yPt%2F4FVi8R6VuDUJYVqc%2Fp66zNOv7HB1u5G%2BCwsV4mpDz2%2BSKkPoWk161DN2S8NZK5uklnzS%2FijPUPdbg5Yn3Cj0JU3AKHCB2rUkaEgricL2egwSAn7UaPIbLvEr5TvfDd%2F4VnCYLV64hiwG1mVYOYYtzw0xmc1UFYwqZTvzAY6pgFcHTSlrwmDEizGnlEVnyms51KUGz92NhI1SNIoo4qNZ4Hk9f%2B2aZp1mJXHW3cQNajXGzJ0T0qqZwCXjiy6yU0NACmcbGyNWG0HJyWhnSrxSdzCvQ7TjJIswr6E4JBLwB4bDuOqawxyOdSLhFG113%2F5VV7y53t4OsyxuyW%2Fc9A1Nxb%2BzSnqHBQst%2FiqKLuv7%2BMTZdC9C6FEOrF2N6RJSnsfrZ%2F72VIi&X-Amz-Signature=ac8655bd6fcc5f3da5d5c80160bb759f1ee8c14b7e2bb793a56b5427226864c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


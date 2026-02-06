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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMPOE345%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCICdOTRJqJ8fz1FIH6726hhwzvr7jf1WAVoRbojZ5LL9XAiAUvjO8UcDwOavLDPanrImpmm0%2Fpf3hmFtcpN6UA5I3fCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMVu3pdKs%2FX68586RSKtwDdn8D9voeXK00qfwJYCzVXdWUHDQaNF47W%2BAIo9DoeSHauVu4icRGW9B%2FkYTXHc%2BPndHMm3EhoHv1Q%2Bdem2pnk%2Fah8AVN6Fb99ryzh5nJf2Hs2aPf7H5Ke8ka8fAWPpZK6q9p7W6pEVft%2F7UpqhTWhDv4OmIAH152bLf8QNGMdUmYrNtrHlSvfWJx%2F75zYg%2BshmmJh2KIjz1xRL0LO3OZ7nxX6%2B2Hwy2usuFnFnvHneV6yiYEnr2yE%2FcPI2TRD58RPt5tbBWLPa7KLNc7%2FibhTKenJId8eEHl5ZzOsmUcvcrRY%2FyobMRQudFuaVg%2Fbva5YoDSxebGjfQ05%2B1RJbYeqRmiACl0%2BnMU1e43GPto%2Bfy8XxfeAxbV6Iiugtbd86jbE6X5%2FV1ZQ%2Bf4PwBOeOQmh3xPFsh7p4k8FWhMBOMR7ay6ioneTxGzOh7RkAKWkwsOCBh4vKwOsw6lQTaw5XM5QYy09ioIvQaXnIQQx%2BzH8ONbyJk1DvyH%2FHVEpOFKjd8xC89ZQ5zosmdmi7MIEZMc37xc%2BhoXLyTIWpHwDC6FedL9pymzY48h7chJ7XtUf%2BtK7AFuBw9tzpIDYrI3Ff0sLdG0J3UIwgleYbj%2BX2ZXbHht%2B5q3J6Kgy5Z1RbUwy7qVzAY6pgG1%2FWhbRhX5WbcrV2pr4ZAOvyz2ZLK5M6kQHHeJdFetHTY7i6gkhfgMtpNZO8v0zfTXRnJJlkalInSvdR1iPK%2Bv5sym30HyK9ifhHLSowXp3qtoohe8%2FNcrG%2BD%2BEMH0mmx%2F7DEy4woP9dKOTAVxFu2dgX9BkTaCEooy6qrzsLX3vAwa%2FTOXSE4Ba15LQKQido8m86ljNgS3KOM1a5zmoMSuT4dbwXvF&X-Amz-Signature=367a13e88024f5c082866cb7fa5f55735f9d2b53a1148d834d128e84720d4cd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656D3YZQX%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHKU3phfjrHtSYuQAwMCOUyv%2BVDY6yEgL%2Bcy7L3XwO7oAiEA0ES0ePZLkZe2QoOxKwPWjU%2FcZ1DBW07fVpJxuSj8hBIq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDGxzGIIqcGZ5xjbCZCrcA3XVPxj1GSEj%2FTtNgy%2BCdxhzlVjyGTmpzyAH9T9ak2s%2FwbHbmhB7gAoBUr672I17LdNZ1LF%2BNezFMMMzvaev7m9sGRYLVGZ%2BHzRe8R9B2stUSGElm%2FyNWQX0vSHZljZxkNNDoi8L0EDUQ%2BLPJO5SDHyuBpfwcRt2%2BaghF0jcyZqZv7B9Q5WwdUJtDTxs6p8t%2B6YexTKpPiMyOLGEP8mfpJLSfVPl2VIEzauVVQ6IxHN31Ow2wqKeWUR9VJx%2FcsapclLxfkxlHnu39xgodpZZg1hdCS5JGzAjpEGXUJePcwvp0x9MAokCnegMwtXo8gNzAvEoMXO8lzlBSlxmElK5LAXbRsPOv9oxrxrr9dSnyPrLwVJP9IAMY2ManwdnQkF9zVMb4dIf%2FF0m3Zd6mxg0kerrrbD8OqzvIwrGIGvHTwH5x6msijtUL6LvU1iu%2BwPfIpeqsFKOoIldzsHtqQFmC8uOZM9VlPUKehCXlqN903DPGMUjZU7SslbpsYV7p2kH3N1r352NYLwxFOLn9Z%2BXyvAkon%2BWFTcTSTYWs2y6WKDOJGfecEOky%2FiLID27WBODUlS59MSpCBwBMkFrjuPfFUsAaXgcL%2FE%2Bed0MKT4Knvs%2F%2Fk13Nq0VKxHzI6RgMPvDmswGOqUB1%2FhnO0XJv6okwDlMsuvmMddMHCAJ2JnrbCBC5HvJI5D3qOol4SDzAL9yiSi%2FbnJLxcAIlyocN693hWnqZuJh%2FplKI98kI2QbbeDybCoXLqAdG8VZoK9hcYjAowVaSJTjdePGlddz%2FEnSejpHPmWjsJX4INUSkcVBbhXi2z29UQ%2FaWriiq1qTYrq%2F4ysVnpNrgu%2BfyUFv4SKPwLyc%2F%2BhIJmGhVqXh&X-Amz-Signature=61c3da5b356881372dc2cc5142fe3d5c6f9104ce3f77c2a2f23a86b84735662e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRKKG43X%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7tt2cPQc7povXRQZsKh3cgXkv3oS21UQc5%2FHnrLyb%2FAiAencOYXv7RIvEsi2P%2FEbHDxrUgizKE4xCmmp3wQOUSxyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMGnu48QCn9vUXMBX3KtwDgP%2FzZmsx6dQ7HxjO4JTrr6AFlZvhuHrabopVRgp0m1ODPRfY89Mh0CnGFDOvN3SM2CGdS7pEOG2UZCUhMDOFbWKlDxo9Z6wTxXotE%2BdyZ96FASoEhdJgyp3uVnPA8d1rrwAPmCodScnftxy%2B6u4gTmAwX3Hz%2FmL9k5wRQw91qofRyUsixEOTQPterph1jY0WOsvgvZyy0%2B8A8jtAZJ0x4mDObmsKBGb4QXmlbba40Wz7Q7hs%2B4%2BDGLmmsbSCwUmUarS7Gd1RUlzw64T0qLFP5Gja52DaZq8%2Fc08GVlQWXE5F3d3tTknXaLq%2BqK8sFBN2WxULSnCsB9c1OBh4gexKVU62tJhWA0MLefROBHknhQmGYAh7OimzlRnABucpnxzeW8omUyAtgu9BoSpadiPxV40h66W0fEzVxTNsZg53v5WG8z8bvabzK3RoXBEQVsTtLXszAO5m0%2BbqA5IV3ughgtAIfoWp%2FB4YNzz8hOUoxCGtyd6sx041ndfMAjL1hsJr719%2BQ%2FJXZH0ShrBQ%2F2YUXQ%2F8z2TuQSogQ0mVvrytZHKLpWQJ%2F7OKevWIiMGLYS1b6zuaR2X3FPfL2cFVudN%2FjU%2B3BU2niYhJOMq8chYyOxkvi7MT9GQ89Zn4y0swytqlzwY6pgFjWV72G%2FshJz8VJdG6EcfcIkrIMv%2FqX1D%2BUr%2Bbk1x%2FzE46cIs0eus9tTSXf0rqD5IBhIQjiNVkdlj3vZ0yGBIY%2BLfppwJAT3ygSaZBMx5Z9unr8HGxdgMm3Jm121ZwV0mdXkMVRT1UHVeDxpDJjEuergwnhNeqgNoPgfi8f9zhU9jtfd4TQk3rmz4%2BOE7IdoYetp7h4EGSIskhFlGDO66CeMSqiCHo&X-Amz-Signature=0a11bc65e17ffd3dc150ec2102733074b9a80955ec8aa9cc02295ead35308153&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


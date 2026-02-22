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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNGGCMUC%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC00xJHiaksQR2N95wFC7OK9W6vdVpSm%2FVWpjVu5Zh5SQIhAI0PURGDaFvmCGEwZZEzOygKeWEXSe%2FO%2Bt6Qos4ug1%2FlKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwaOXrHSTg%2FTPLrU2Yq3ANxeETSqUQlV%2BZiwUWG8YTog6mguPDsRZvgPbWCKtPsN149rJLy76J%2B13LzRdGQNw4ElTJgy7BlvmBUkwiNOXk61%2F8kQ%2BQ%2FvF4uHRDz%2Fe1fYlVl6VUhypb21EfGuBYRKWB0GpSJs96QAbKTnxhm7z%2Bhkqpgv0xexCNuAu%2FdQPBDjwlxvY7OFkgXh6NprvJ6MB5sLFoHx1NxgnQ6VMXCaWQ7sC6y3q7Uc60bIZ5xPbP9V3dTEBLPNvFn7gz3AmE%2BZSGjPNFliH2ONlGCu4lAWoHSAtilkvgKqVoYgJ4wSHBJ2h7qEwDD9Yj5UHDl8Brnn%2FE9Avl%2BhCffxi0tSS5r%2BYprtyFxlt7FK2x%2FGrvB850T2YSoIIw%2BDtpfnmOXiqnJ0c4WEspN%2FBIafNaAZ0BX%2BlRRVulJKIY7dC4KOYFrlNgpXiBhIlDlMbp5IpOZeacpiPdScDyVgc24NInmWUUc%2FBYqMKr87%2FNI1q0i2%2B1WSPGlx%2BkoT0St82ZcZml51xLH01LAyKUlwaEi2hC3G1Hbsp6AF69UWpx1P3H4FnxphdunKCbul5nvTs123jDsGzF2Qjzn33mD%2Bbaz2a2BprjuqA5%2Br3MvfzgHzXAb5lqM9ZitMx1DtB0%2FjerE2R4kfzDp8%2BnMBjqkAQK%2BfovkfO6jKr5pXk8RXi%2FhEyejt%2F6w3V1kRjP14Th%2FJuuzl8AzKAWSz%2Bp9dPe9OxEjOTX3v1jZvClew4dz%2FUI9k5JYwxGmYXHH%2F7KFjlIBkhY7XsVZ0FrSun%2BdXFVVSpufqJAcdjcCLSmnzSZ7%2Bs3FFqP%2FJi9cwRGMVaRt9AwCvnIQfa%2FqAOEFMzA8fSebYRHLqONI8QOLD6in0dESiOF4bBwu&X-Amz-Signature=2fc2305361775317781c3b2ca4f7cb40aa157e83de165b3b27bd6bbeefc8b473&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


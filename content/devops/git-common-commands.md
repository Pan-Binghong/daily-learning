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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZIW6IJW%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8c506kZcDbVxoEk%2B7ZFfhOR%2Bgx89FhctS%2BELa6kmE2AiBZsHL4tVXWK6BSSUmfwUmQbwl4JesXs92QolcRN%2FAVeyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMkacuQzsPp752mHFsKtwD%2BTPp89GiRC6plUI0SfeXhRaLtuBo2kQ8Ru9q8dYLxQRbtw%2BUAj1BpFCVaFikzz0jNwJr%2B30wWgwFs53EScoCPUtCVwrTTyzE8iqDNxSF%2Fnfr7wkh1o8vWemBKLL3iHatytuEdy0Kz0vWLGWz3ybimcy3dJnOBHeQkIlpR2%2BTcrbuGsOnX2LrcA%2FEncizJobU4FWlwqo2fINjZIv1T7ubu0DkIu9Cm6DTTh7UARqaZp%2BIrUaBi%2B9DWo8cQNvrIlaox2Oby2iYJjY0z6sQ%2Fm94FgH0Dnmn8nRVIscjNrGNBhpSm6ZhZy05%2BAuQ4n6qO%2FY4eBIvNBFdHOUsdqHIT5mvJRnx3iH0S3K0IBf7abBIoOAR%2FMwVb3EbMnqYXMf6zlNycp4ZLcWKShAemBSQVAShRUhTDsGiwJ3y163mmx4Wz9O1Ay0huqOvoobI6R1DYVqJ5vtmSHvA0rVD3gAmeSjb%2FncfbsDVk02vr3x9dcvHMiVpBgdbMPBmWrTToWOmGvE9BU5Ggqex%2BACKunH1eteEF5hntaBfVgp%2F85QYQz6hlY00dWIyhVBsLSC9Em%2BL4avXywPgfokvnP2bTLrYbNGmY%2F%2FVh54GyQOGTMI3xw8JeyFkIIzttfNfxBL1SYow%2BY33ygY6pgE7TkIQSd%2BVR722vW%2Bdfha8%2B9b02SGQ3%2FatJg2xlb4l8mYnl8rGHlDOp%2F2gqc3GvZaQEmviRGfJa4Q8LfYRzHDdLvZ7aocB120tUxQa6HhG1PIBZJgZlL2Wu8k9BZqMZNSTgdlIrxfQ%2FG36ubRYOAvlcPR40iVvvXWJ0z1pGey0RN9%2FA3Okn3p%2Fdtx70bqcpANkRVd8a3v0nra3kvOG1Zf9rnXqXOmc&X-Amz-Signature=c618dfa5f2434a2e6893c6f360e5b6e4cc106b81200512b930b6f5d9a18147a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


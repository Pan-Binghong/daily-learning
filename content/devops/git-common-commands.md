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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O7UNTLN%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIAxXH7dYVn0dCFTGvCg0%2Fcn7GRhsRsRcx4ocqVe4q0qAAiBKSHloV9lQH%2FBnamUdrzV%2FipPDHGxAh41gQtjQD8VrmCr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMIK1aXP4UblKqmxtUKtwD1lFRSi2xrv2NFFO1jhy4sWCobN3PZiRj%2FRNfPjoHk0oH8V3N%2FHcueFaFUWFg5Rrf8wpXYPLreg0Z6znbsewyCIAJPJoYQknKRRnQRaue0n%2BWLMbM7XE2qhGqBBQm%2B2%2FprS8vIJc2VD4TPw3xx%2F9q%2F3%2FTPCB6PNb91VmB4k3hwITGd46PTGPKQ%2F6kk7S2qjtvmTjCyRJwkRHmdqekhg6KxUYx0da7N4pyEvBIUjpmzKnhxTVpujfYKESOsuvRU6eJn7d7NU%2F3%2Fy9f7oWsIe9Gv70idGtQC1rfUTaghCRvH9gs8Qjy0xogtagQ%2Byr80yJbKzYjOGubX1O%2ByH1AbfnU8lgmnSetH2EDZKlW9yt%2FHO17SBtukUMLMCPUxyJGg887rrrKTH2v2Cfas%2BNlWW3XeReg%2FAtNeHrKUIhfPesdV8byYeVxk%2B0AgoVcxZeR%2FWgw2mtw5WLomqHEgp3rFFWEMYr4CbaZuhWsgThlYUJYGp4Y0xWe4cpXisPlpGFbr9eFLvwly%2B9mMvNCZqtTUsS5cd3WhMTYwY77%2FbQuooR5zYUBJGg1WdvwH%2B5bu04N3GADiIGqIKakNk4KJL5J5hzIkFK9OwJR19ddJGHt4qS4K3YVisOm%2BPft853%2FS50wh7HLzwY6pgEuuDfz1Nkwhl9xC3NTGpKgdmX%2BlDJSfJZHvX9OXBARn3662QndO8lYTh%2Bea0tdAOrTNtNs%2B%2FOhhkZclRhGmjQ%2FUqRZuf3oZS%2F2%2FSKZuOKTYgaM6wZ%2FaOsvgg4kUOO1LxRPP910vXYB0iI7Aump%2B2HHf5HBP6%2Ff8nYqTmZ6jhNzn5QFRULebqpAaXVXQwyx7RkBDqI1vCDcZMN69brXRjKqtT997SH3&X-Amz-Signature=515876dc9d798a7f5e3ac1ec938b89ea4356f3ddc8fb389b0a3d586c3d280e30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


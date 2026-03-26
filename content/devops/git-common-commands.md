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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RET2MQ3B%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDlO75pLJwamCCoLwIf6J3X7gl4k4qxzmd3%2Bm1M4sKnGAiAIoh%2BpcuwMPSqN54Ivc8TCldqUVT8cBkiyhKiMhjrDUSqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrOwu%2FCs8FZb%2FfGqcKtwDkFC4wtPU201SeE9QMo1HPRLn2HFaIev9eQP6zioS334MHfSeRS82nCRKXZ%2F2DDneBM%2BdJb9QXWXG4AxlHWbGCXQ42zUxwMP7jSEXXw7dOFfD4zLX%2FUeroOOV9BIsA4h11fntb5KEbuOsVYOMZagd1dHpPeiRv99h0Lig2DTEtMb3PaOjz4MuaYnzTd3li82RIBv%2F9jqOXwM7E1wyd%2Fq971Kn1%2Fg4%2BrD2lYq1OqtFFi4dpoGyMHAssNVDje0IIIpmBXj4rOLtKTK2HHYeMATya9x1PVBEStYHJne%2FGNaBqNMpJzIAiu%2F8%2Fdy%2BC0NVNfQezq68g0KdS4lZ2T0Uk%2BurP5GT7W8O28oOkvWYU4c636Ac42udgJnWhXolx1KfJ6SdbypnHoI2z%2B%2BLly3fNiVIn292Vb%2FyaS6RBL5%2BpgbaU%2Bq0Bxv1vDCVkseEG0wua%2B1xUfRNz1OXlY9SzKsjnKo5fFOY%2BqxDAXqgYU4Wvda9ZP7Wd0Ge4Kj3p9zWn4c%2BEIQTTjhiO25DRo8xoKV2jL5xB7ChFSHPD1hUnrd3Oe%2B2nhsGsRQaipcAXI7vkwl1U3EPGiB5yyZRsO1lvHmlurFXWjnoZfsB73gYG4kD3nDPxVG3JP9PmGpQXb7lVe0w1cmSzgY6pgHCEYRSMh6O8ymKJZ0nZ3O8%2FOjq1LTjmmWMzK3D9ykfwRIGp5TYh1KdPr52PHKSaHqFvDWTJTM9tqWl%2FgbzRR3w1ne4PeqYuBTIg4VefnHbQduLWOVOk08d0Du%2B8E0uaKxQrDuFgrsBKL5rdxe5KqsmFeTMohSkw5biZZD50PmLmxcmxnB0bPfqttv8MWjUNyxrVCs9zgLr%2Fh3W%2BdSzVniTor9unCar&X-Amz-Signature=570a24cfbf81d84a166d3e3b187631d03840ab6bf84b78b28fa2d2075dc644ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


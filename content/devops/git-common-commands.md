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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGUJ6LJ5%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5zHHU61kMAHTp%2F9pnWNIGO4weCZB4ma0HCbGRn5JtSAiACYRbc%2BB7%2F4Y%2BgLTNChVgUlNxKSv9Ccp%2BGdYf6E3%2BMYyqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTshgqAzT3UexngIVKtwDEI%2FuaNZ%2FQ8CCD%2BEVfpGfDYpfb073nqavZ7u6r%2F%2BhJECjuI47Ut79aDm%2Bbrg56wgmzMpz88knfzLNuoYZkhelRFDFFu%2FrmDBZkRH4UAbxMjWSrfWmDq71N1CAG5tFAYCKDe21HF1oMoAvYHNaHgQ03usRSxXtvDFp8dKAZ%2F%2FsMZs%2Bj9JhYUH3aBxLZl%2B1x9HqWeLF5W%2FeFrVfSEiX3f7mf7GirhMPxrgXeTEs7DKhDbEBx97aLbxw3A4cn4A6haFTIhNkdKCUp0J1nxB6wxmxJb3uxCsiptP%2BXQE0505hJEQbmv31j7Yx8bsHsK%2BgH8V%2F96Zsxv2fdTdJDDdbqwIxQUdfSLgsD5a16G8n3ZosXnBr2zzEzDemkDlCJhvrmb69RSaluA9Il296K16dyOe2JOECQbRh0kLyJyO3ZSaY%2FIQGENn%2BxVQXfxB6fGXOzowQrcsLPcJKtebWCFXD0m3wlKAWNwvXohd2lUaVnhACk%2FTg2TFNBY6XLQnVtjyGciIHaQrUvqUqlJQrxXQ%2FaQbBC%2BhOCy0KIr19b5L5ssv88DWzGjPaFNc6sCrfrKCkK7hsnW6wO8HHSUdkoDf%2Fx%2FW%2B7H2QG07CgD%2FKluOB0N1qHs6G6F7ojSSkjIIvoh8wsLWYzQY6pgFLAXHFqKxTD1Hdb5Iv%2FZS%2FFXLCNFSeRspifpKQuNNRf281t25tUKX177rX2bsk9rXTzxbppWeYTE9xl61K%2BIA0BpvYtCjaKi0q3SxwcEfchLex3vugXJQTOpHm99060x898Xc8SnDFrFIPtGd5LExR%2F7XJGVUN7gB0G5KWn4kLS3rB8R5hR%2B4rBfd4Ma27lwBwgLVSc4FRHv5DzTgWE9oeCMeh25Ug&X-Amz-Signature=cbaf88510b529c0cbd52f20543b03b7c17c615a6e8c9ad9317ebb7b01ed3b026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


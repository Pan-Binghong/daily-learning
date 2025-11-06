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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTYG7S4U%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFTuDsPSh1umhYt8tmzU2skxqsaD4ZF4mjvgPrdQSF0XAiEA%2BbAVKs%2FEzfPjpkf2jeYGdjsG%2Fmsib2Cg7ZrR4kiJbf0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKaz1M0tBGMpaBvjeSrcA2Dq%2FRsZYTFkOXK4QkOU979CqdGLGXZy1q6uzN3a2oIQISRL5TgCwScFDNC7KFY3ir3uK4xGFURVVfuXdBjVjv4MFA7Gozt5IhkTxejudRI2x%2B5iLysMYaq5kwCTXYJGcnDfEy9L7tbJUb9XofrI3sXJcB9zS7RcUKaBNGr%2FsCPns5RgY4CW2S4GPLYkpP1NBu%2FbfQGLlWc7XUSiZ3Lw3VWHeA%2FJBtUa8c9mbKmwq7yXsaTmY%2Fez9EsJ6OxYl%2BFfLEair4VSkQ27P6pG%2F5J1lfc2OlQ601w5%2BCcU27Eljok055POgt1EeGH2rbFCNDbBOLdqORcTOUrSzSVNrmEkFx0Hp1R%2FlhQR%2B4bscXcsVOyklqxzsNuwDdL8jW75YKLGytp4%2BZUw2kTwPOQgQV%2BOga1uhtjbQQZYgBmvXWKFzYU0o2mvMI%2BEE8HfzynIWSRfF9A3dwvZp1d6gWa6AQ572TucbvC9IhTRekpqp1ntFBIclcNTm1Sv7kk%2Fz1IBu%2FwYDlVfvUaqAXiexfFkweKr1hRJFi%2BcJXRS5guRcg9Hhl7To5yHYk3o9KPoUeVc2EAojA8EszBMH8TGW6qt9Jle5IrjpqPvSE13bxUDK5g7y35Bm%2FjbZxo01w11bePiMMXwr8gGOqUBTi7KRpJD%2FND2Klkng%2BFtt9tEHpFdJ443ZZobNkKd19DTVt8rZM8yxg7dnZMDSqTpAeakHnjoAmTiGLZlxWz%2FRGfavjEIZk0FJWjHBeDx0VF2EgUkQYyjlnYhKI6CD%2BbsSv3zgyRJIGdXUCGrSAJm5vbfOhaDovOXd9BCEhCDvLptaJllIJ2bOiUu4iInZr6H6tWxaTZCVyALZgHE5f7cQRXv5aah&X-Amz-Signature=0ade6452383853e874672b419e8ed171ddf31361559e02c8cbc40614d09c6696&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


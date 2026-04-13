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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ACPIGDF%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6fXQ%2BY6P%2FMBu4HQG5pcrUGsy6n4zUZ6B8fEFRCDv0JAIgc3y3eXsvFoUARxRsifthgKNBkTMm9tprxJcPJ87PhVYq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDH9X4%2F%2BrDqO0JTYeNyrcA98CPCfmOXalFivm%2FxRCDtngBqGhPJERk%2BpZ8LKWcj4yd47KSOsQgj5PeAzmGlXsv8ZEjCVsQ4uIgmjCIVnV6%2FYFq%2FO20myYGkIU2AYdxmDu1FOXpST17a%2BGwOWPvbRVGregHsfes%2BmgNqHCTIZ7SqBMD5nnkctBAY8rMouAr7G25ZlVnAYdx5Pg8zTKKBmnXSpqEYSDotuScfX5OCrvXS7zQx9GyguH%2FdaSy2dOQzSu7x0rrc8gtCnhl3ZnIGAa4Hybf4lZ7dAwSkayi7XUDE3n8pU4lkhTan0%2Bz6IoAywPaG1O%2FDSkIO1AhHF1%2Bkcs08dt3NXGKU0tdm3OP1E8%2Fp2rEqVst1goT27ua1whiwiGXern6Ks4fA6evP2Kz9IXk3QgCCLt%2FGTkmjrqvlC%2FBPtQSUxpyrOgjIJfcnaTxS4uKq6MOETG%2BlyxvvaTmxHgiuQMVa33UZcITBZUdJ3Ps9OY17OTDedVrxwepTd4Bs3laGyXsyNA7%2BrLJn9eYwZqXxw274K%2B%2FYp8lBVfvoryah3RoulgZCPyEb%2FXFAyqJLBJJA7bNRJH8uLLz6k9bw4AnSEcZl8C0TiKHGVzBjyEE930Z7gj2ssgYCY2RhYJjKpxXEGQr7DWbeEKpG1kMKmy8c4GOqUBystz%2FrL3mHqPOZ23u1y10QD9WDnzsZjvpRQ6IfNqjTuoEAggOLTPz4y4QCfzw5dz1YDBtkzsU%2BI1o6l1Ps2Ls%2BjK4sYrP2fUXO6JRDrNt1CDlXSHEpFMaIDSSddcfk2m4ZNt75sPdt9yql6LBH25zGCsBwp8vg%2F9TTythkEZ%2BGf5x8p8g1FGtSvHekAk9WCScgvqr9NTpeprdlwpXkBvCLKZ4Zf%2F&X-Amz-Signature=506e62aa127b4ff0c469a3ac403369e47f0a623be4268ff3d590d21f9c1c4e44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DXV3HF4%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCyQaC1TeRLmXFJXklPoSbeT7oPe44qvmPk2Zyhf%2FUmrwIgZyzJDZMz0uyPDWtZIQ8DJjUnDgBBPyZ8z3%2Fl5TxC61gq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDFLny153rzB2M%2F29DyrcA%2Bghc0W%2BaTuMhAzqbIMCYzqUv%2FOSX5%2F3jQrwGN5G9oaaL1LTWElMqGJoX7oFEMxi6lPcvhqc5QIeR038Lq3GgeJQrImfiOyjhu2xshi4Hs1m7PL3oAN4w94cCBcRUK3mB0CHJpjkSmks6vgMFFHf1bo46oGhK96hkowpaetMBSMQdDbtOaEvBkh1XJwn2rjBvP2lkFg1CJhUllPw2ONo8KgjcW663ar8sObaJuOSLD8Y562qrNPqEVOPJ9yFNBB0lDfpiMZKC6P0PLmVjfjXPa9Q6%2Fx%2B5m2951KxZInkrRWBzKS78XLOCx39RoChPqfphh9TLnRD%2BJX%2BkOaw9lgVmVZSbeN6vWEkqFYnHY63kbLf6w8SXQQSzEt71ZxdWNA5mI3gemm%2FSbA7W42PvaarX1SQUnYRhaGFh3%2Fc%2F5LxQEMYn378b9qX0caFIS7%2BlAh44r3PCQIv01qnu%2B8QEbzaGTPCECOjmFB%2F5z6fCeECm0owWw4eUc5%2Fbkyli7iFKRlpIGzN3MG5eTDBAxOUS6y2GQ2VVG1YHttJFxxB0mXstHUiR9bsgVS1TOTvGA4txxa4S6bpuXECJHDQNKjc4lo9rC5u4tdMF7NZqeHySJYbf8nhp8XWBoZLT73gN7NzMJfjz8gGOqUBfU7zs5iPNr6FFTVaz9XbDLZnSHudkUdy2v4bIAdxvYOjhWLXAbYE7f37adMjtT6O9PQt391xPXs5I%2Fv7UzODvXjOGH8awy4r6PNrG9ih8%2BAy%2F1t%2FJzf%2B5NAE%2FpZFpWxJba54qpvCKUGJmyD2voQLk%2FSjvf%2BJHZ5Jof9iD%2F7Oi47a33WgoGQH2RKOig%2BScHWC6ayHaHJmSKL6I3QmDERGGZJ5RZ%2B4&X-Amz-Signature=ef1561afeb72b3e921aa35e2abc0ecd808f4753ae8201fbda9ff2177e14a33e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


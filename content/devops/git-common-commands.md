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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VLIOJZH%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIF%2BXuEIHLOCu%2BTqPaoSzTuUL8I1mKr1qD0p3YItK8Mn9AiEA1mYeL0pCQ5ABUSItn0gxAFR3S9LYN4WLbjNluqsKmqcqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHmKoyVlvJIKdIymPyrcA7MA0M2bjm%2FkI4AoO5%2FQMyvN6CX6jzoa6sey7xn0hCDptmfKSbZkaKzu1biuz2UaNh%2BcydoI4n%2Bxf%2FojLlE7Vej7evv9JqwHddjy9w7%2BKOGu%2FYvVfCcptzSvbjcKXgOcwUJSzZfWhmkKvTdSLSVvy6RYQsHYNZD2%2FZvLGg9LxEUk1ovdxvB91eQrKpkP0x2IJQ0aIBSntZT%2BF80JC0YatA4nCY3JFoOjd3FhoI2zOWvVZR5ZJihSElupYIV9MUI%2BuwRNuer%2BPO%2BQmfTMrx08MYNumFWAax8YkBt6oa9cCUBo%2FEMFwWHPB6Fa8EYcJWPXELIfmMYrbkdMo3%2FR3QQCOxsKHvsty0yz9VH37%2Bgtv5pPIx%2BMFAK0ATW9jVkyexDEAuC2fzmfYbXhvDtKsivxkm5ZeTlkxclte4W0wNU40cA1HZ6nuuDsE10WhLDkHvsW98eicjwAvhbe7WPgQX%2Fn3Y2RJP6Y3cAa1Xtof1PFyoICATwDLOsXtzFnC6hvbStW9FByD4YSBdR64PhnWcSNm0DZxVY0sROMIeb22ED5v%2FJHUCSMx%2BmXThhykIdvgdLm8hW3CHNCCFw7qhFXxJ3sq8M72sqZzlevmPHpKPF5moVULaJdqSzaAF0MK3%2BeMJ%2FSrckGOqUB6NjykH1DzX1QkYs6Kx%2BGr%2F9aD0yKIsa2pMRDNMSgu9FDzeNsiQF7B18BdeHGYpuuIXStvU1xYb8ISSg1id7x69GXR%2B8VStTz2ZZ2BbFUQurTxCSmxfLoRsbZzWNbxqm9msdaA%2FW7EcG1qnUkJiZXlS3yOigkchfzC2mjdS8OdriuXIx7DxDqJVtzZbEn1zrh4ODHabEO7u9rCzLXQU3IIpULT3os&X-Amz-Signature=11262def53bbe591421b7cd5bfb17c3ff5ec46f6d39d066421ad0c4fa1039316&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRLUYGNT%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIGNRRLTtGg%2FhM%2FUM2VYzJv34A%2B573WR0Z7h%2FPgwKghSjAiEAsNrtEBtupWgVE5lKgzrtbMTUVugbIVjGBACy%2Bk6YO9kqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRRF7CK%2FSr2XCANqCrcA7rhk4k6iWHQQMKcIzzjdi38uD2z6Rdx3EbWx2wc69wUte1QPLtgKQpNqjQS7HTQ%2FGtb%2Ffi2XtnGRaGnkLXQLnuHw8Xr7KpdEzRfZxNAxFCGjyR9Z1DUo4tVmo5gyRgc%2B7qVkcV8WBZr7XKyjC3KTh2iazn29AaWcndASG2osfMcHyWqqmZ7YnjnjAPHg0xg3oa5yh%2BY4BESOEWGiA1bJpTXD69P4CRVPTRR080XxeBcyiJXXKA%2FLkPSjdtelcvgWHEPWWQuehVQhqjIKw6aW4uk5xBT7BZ%2BDKqCWHuVg%2FA34VJ%2F4s8JoDAWIpC5OR61UitO91A7JE5iri7LYevJyfBrT9saCbUWrrIw32ynddtfMvHYfrENKchQuAGB4cE5pvwUpvaANXbxoGIV21otA7wGRAYXj%2FFPQU6avCkT7Tll3RGwDld5wdY6cY0qs8X6kcFbCiYAdvhxfYzbiuGQS2UV0p7i3%2BvwZQBYLr0w%2FiuRHn4m%2Blw0bXTohcUApF93yhgpTKK3gkt3Y0N9a7CX3T51nor3higUNot6nS1J0LOMeCH%2BR5drXWrSnufiZ5lrJmxumQofzebkc%2FE7wgYGXyt8c9mlxtCGyzyW63wsVNCdPClbElpKnQkMgwvFMMjvls4GOqUBLAOmk6Vnv1lwhUQ8ml9P8MnovEUMJ5LE8QOAdes1Ar6Ye1Q9S8xghdtiA4aNBV6JkQd8kCrdm6FhzctD8FDvKVtJ9Da1DN7ywd%2FEcOdyz5q6RCM466LAk6%2B1Jps%2Fdo5o8B0JwkM8UH4PqRl9aYcKReDhurkPv%2BAC0jmTd4Hr2mmeLZp9rC993bAPN%2FP3lqGQ%2F9h4R4nYODrNUeaV%2FhO3QZhM1LB%2B&X-Amz-Signature=3234c1ee9336df992dfe5a47f671d4e702e23d174ff69b8ed485aa5b5e7139ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


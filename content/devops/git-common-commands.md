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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z7IV2OH%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHaQGWGaTs8t%2FiM1exkTDnfGas9fWJ%2FBFnwjkQpZ8uxGAiBNI99pAmWOq%2B5apLuxDr8FO0p1VqTJLrL%2BS4YGIBh%2BTyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMMq7xE3JKdtmhzTIiKtwDYdaqlyNQoMcPtCA%2FKkUVXNrq3r7ZCa9bt9K1HnHyL63fZlowBzI9c8Q6Mvu4sV%2Fb6qZj0eyUI77amMgHyjIt8FppQPRk6tuV3ULA3W4pQDWKzbci8cfLforJEZz%2BKNdhcNNF4WDlS889XJKgPpLPnWt0TBrSoebqwF%2Bq9PYqa0HdyOZWyUn4kYWKYuhaQRv89SVnYAVUQbl2c1uzWMJ96yf%2FmJIbmkWb33cZJwP%2FpkVtsNtfBsifLIYSwf5muHZQGbRnYtN7aCkWN%2Bk8Z2tS%2FfyE7FTdB4Ei2AVO92PsbWk4UuKPo2AhZTiaNJAcBOpgcDUbW9uOA9xPu8hG%2F2tWMhxKZAywFcz7yNzAAUOZbH1qa%2FiW8JUIcXv7P5BLEBp03nKvxZhhTry1AtzE51e94p0FUdFHmVtGIr5UfVuwxY%2FB2YUiH4As830omCwcrfvCAVv7Ivk4TDKH%2BjZFjUvGDtNzYRdnuodl6b%2Be5MlQRumdx7c8AjQKGwsa2gE1qZUpfPY0zscoQj8Br6MflpNwXd4O10czASHkw9HyYjVAUNUwhvF%2BWktqMB%2B%2FCstzYXa5N%2B2br%2FztjFzxNdgVh6dhbAxwqyRcpGO%2BKKFrC8LmiyNvDrAl2AjQmbu%2BKJIwwpvMzwY6pgGPp1Ysfemjlse2xOfiULkGdLjZlacQG01%2B2MtjZMgIDfDfgPTfrv3Nb6oK0gqAlRyicVASIPYDSmcZJoGOxi5kUi7EUyrOWB2K%2BPLVf7GqG8QeRT7tPOjSYbDxe%2Bmj0wYFHhpQx52W%2F1wiyYo3qaflG%2B%2FHj1NXPOAsLlJIy2ZtkwKR%2BMHcVavCX3Mg6V9IidwdUOual3v76tC9BEY5p7q8695Evd0j&X-Amz-Signature=64996f48b42c3c341ee242fc8e7a34b1b193a3b79d5f12e745175a1cd60c9c78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


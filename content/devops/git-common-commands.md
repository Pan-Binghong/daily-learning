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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN3XO4JJ%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDdeKpbfGKnyzi8KYeLXI%2B3E%2BmZj1XkxhpRL92ld86UpQIgRbECTyuWKzPpHH5%2BPVkr1SNULATV3UnJg15VHMR1l8AqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNtAA19STUPm2cMMiCrcAwLsnwCce%2BtnSIV%2B44a6RPs1ByNDi2fF%2BZAtrawIVE6fXT%2F9Opf9CVlvwXdzoayxzsKyjFTjim0lTV4qQ0F884raKzG1RpjkUifyiIud6v9FXbzy%2BdXsDwwzaTk%2BmtYsxdbbq4JWu0dcKtagMCWA2cpEDcXmQmtUBGt7r4qpC89CkW%2BAN3Ov6LLDs4%2FiY5oHKJjoBenpRiEYr3YRpWK%2FBSqMKqp7%2FHDohaP4qjkXM5B6YE4333qgEJXlwl3dqwTZZ052pBaTRN3QnXn%2BGZqbhI9ySZs%2FjC4LQWRipCJtEUO8xIVnCpVe1DVdoXcnsnS3tXoBisARNg5IauO8bWEZkoSFbpqnCq%2Fkm0oywqlbUbj6DsUqLJhuO6qxHrh1Y301sm95WuvO9n5Lk4zcW7P9o9ryEShRLbMZuy73Km3BmOhLnsEpRZsmSCxJr30NDg4pHWtIa5gsVN8QdUBOA2O8xcB2XmLXOFrxk1Hf9rLgQ3uNgRsYYK3ytdO7%2FEzP%2BF2NIQ94B0xcVox%2FnjEUY8B8lJ5z1ZV%2FUznXkBzG4FUUC%2B1HYhGxhthKfcsK16vT3AVj8G7%2FG0G5uFQKiI5GfnYPVNTBOAU%2F9wZMsr2DfPbHkOoV5NHEIwSZno%2BKcCAaMILW7ckGOqUBVfIVp1jkM71xDUwi%2ByAH9msQIp5ORJ%2Fh2ynunNgXf4exm1e%2BmzlA%2Bb2lx%2FdSTI%2FO0tgS57idr7Hg7xvLpZ1W2FCLGB5dyi%2FWA1Kh%2FhfiUVRpQVN8XRDz8rK0dzjOt8ZGsv7oZ%2F%2FshJl2XINwBUITWUkXtK9PnI0OsmbP%2BAhgGjcU6BAOZe7XA04Z4ZDD8%2FVgTHodWOQzkflqmdeXnoiKc9Z5MlI1&X-Amz-Signature=7864dfe346f21856281358e24d2e0cd5d21a002c6896810830886b807a048b06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


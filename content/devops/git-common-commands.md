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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USVGNPWK%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBj2IraJJ9XEGJV%2FZnW4xt%2F3VOHpgdOXveDGNjbppwlVAiEA2RSR4DmBknx95ASgm0wpXtSvn1AsvpOCtHtL%2F5O03l4qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1DkObcOsI49LS2DyrcA9HF3tHs0HDN%2FYEbKjSm%2BhFriffXtlbdOT%2FhnUaQHF6uX1%2BxTpkL7c8s0uhpvgotA4hRQbptL7Z1TWL%2FXH3LnAN4DQChpprCKw22mkiN%2BIJ8Zk6EX7%2BKwEM57GZF2qJkB8lTNcd75AmnR%2BRruCOZMMON9PMJ3ZHqphqCdhbJdKlOaVMMs77F7uVP6nQnPUPpacZMQd1yJBsVkj2kFq6T9T5Svy9jmTTJUMXjclBM7KSNH8k0enYIOfF7qsd4pY6AB62OXPOx0vyvdNwMjQx1l39TesFWxziWnvMo4roVhB9PvAnMaMRV2KnT4MuaYOkHTD6mE%2BHunzElYbE9IPLtsi0FCFOd2ReBP7KfWDhfL8yIPM%2F8zyWMiO5lor6h9gsp3iC04yJC1xOS1LkLBIDgZl0LglAjBVQM9iD%2FK23roXu5OWZ8s5tyfL4mRq7Qpca5rT%2FEBlOpi9T8TDnRP7kP5pjdbV0bwINkXU8kB5qrbS8lSg%2BaHo8mN%2BCuXz1XT6oqLXSbX4xC8Zd2PPrgdxaR70IjCN9mEyxwWV9%2Bj2TWKiuKeSDB5uW%2FqsVd%2FPXyLbJb%2Fylcn8qU5eLoZTJzPH%2B5eeVwS9zORI0QBBj5%2Bru0agevc8l5AEHQ2eoAXW0sMN3Wjs4GOqUB2%2BYDEqPQshvVlyAWPgcsMCNc2Yc7Qb6kjgxcgveqzegy7MbkWXNOTLta73x2MjeZ%2BlvDGOWYBXTbhXEc4nlulYk07nH7ndfLO%2FCxetynYaw0tOAFKHNDeUPTnA8ES7XTD4okz3Rp0J6SBIy6RGgiwXl7m2VYfdTnvtPh1eIPem2ESe2rBzzPmGF3igWIcnYhHxoTYcyo24qssnXrDAVrL55dERts&X-Amz-Signature=0236dfae3e7dfd54c008a2fea6d2906a3d824fa1ed4357f03b10411a1561f48a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


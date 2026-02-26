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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3LM62SH%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQC1jC2kjSoUfHi7FuXkqLkAvBaWNSruLoj771GebwUToAIgB5zKG61aov98%2BXZVKGPZ0q%2FEU9HSiMqkFHP4fkWOM54q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDB0aRPFdqTSwXRx1QircA%2Bmge6PKdoM0FEA8qpAYGRTXoaZ%2FBlcQ7RvdEPFcz3G7dcOvPPFbSHbFa6aLsveCLWG0SF1aKlRN6K3GDN57stzrM2ih7U%2BJIoklff9tkrw7xL5BBOv6%2BXJ4wS2fv7%2FFPVpIBcA%2FCXCZ1lycV%2FXOtijhuq67Jg9WPzsAq7Wkcj1ZGb2xwO3quvHr3%2Be3vTz6jG5OTDdw%2FLjRzD%2F%2FD7Cly1PDtmXjspk3D%2FIXcFkz2LS48X7OiAbolblDMMlKn6YOKppLRczwQVcjstM8eVv0tae1WYZEOAg1QqoTN63Tno9sNh2PlzHbIE%2BzskHdTO%2FGYrbrlg7C1TdARxwPkpD6g6%2FyBSk89uEvP0iZpHLTmeceekPoBLArFZDcTPeXuNDe5he3sramrBbA57JMcg5GG0l7DMNfDw88YI%2Fc%2BOI5YAuH8EfPZHbpMu1TU0pHppBvRWsnHbiV6O9MROf6EOL0A8YyfoVYWUe1HmvYJkeZt%2B6VuA7Too0hj23Ws5D24ypWv5157LviBVc1MT%2BUl3r4ADnCe5dXl1rIU1%2FiMCVEITpLN9rhugOlepEqXeyzIhdJMEcwLnuwnomtrMXdE5ncn5MMP6oRH191HzsyD9NvSdVh9BT%2FWDUMlcYjpC8rMJT1%2FswGOqUBZ6mCg84CpPLqhvu0bLalYAKRoY1sv%2FqTIMFOn%2Fty9PAd49DEQu7UhXiGhPyiM3P1QelC1CJTgU%2FOnw6G1smt%2Fnyr3Ra5sEgN4FJ2HIC%2F%2FjuqPvmfExa%2B22ODC5vw56UjqKNlm822DFbUsTk%2BwTtsXuT8egAzYJXBupGgVaI2j2DVSVNk7Vl7dtTJAPmU3ajgR6EYRZcwPb0TwWeV08KR9a6%2BWoTb&X-Amz-Signature=3eded7e09b44355a4ddb32e9b91130c6d2e598d5c043965d36f6010a863d4591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


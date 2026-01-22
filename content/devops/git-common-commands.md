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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGGDJCFG%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDbYH8cetyb6x7PxIRq0ylUX7YA8mSARvsZvmy7lE55owIhANy%2B2mfI6Is4julYqej3p%2FVl7ygzfuKvCR%2Fp8TzKx7x0KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7oABxGIXT7dyw41Eq3AO8KfQ%2FFyVzTgFDcwG9%2FzVd4nHnw4OsAECZVA6gCVJJpd%2Fi2zazkehuxKMt8k3BIgcKUuASIZK1QlGez2BOVN7A8kJ8EA0%2ByrtTvVOPH%2BJmpZQxL6jeNGkdDC5Xfa3Ng8aSjhkTM0asZ2lsZO4TzxYI2Cn5l%2BuAljlKu1zyC1u2LEuFA2G6apofE2%2BB2LfTHxm7KdvpGTpmfGo%2B8%2BS9UxjOKWWifwlyqJfCLrLtJt6Xon5yV0aPoktNepvKdZJzFGBHUeJdZxGqjieSyQdZRP5ViWSdXlyQa6VSHa51IKnc86%2F7gN%2FHgy50PbJg2dH%2BiaTT1XFZQvA%2BqVfmjF8qFnvDKD%2Bf8Ija1NaSSLJQm4xLnyhfhBA7X56ojjrqeXkpJG%2Fvu%2FKGcHhHXWRcthiaMk054t7ZXoDeaohqG9HWdiRMH7BOfPqTVZ88ojuUOR%2BWHvr3CkhnMEp8fsL%2FPmV2JnRdwR1UsyrDbaaFnTGTj7O9uLP0CJZkwdws34JoIsBBeAvurQHMtgot5EVxe9J40QJicJyoBry%2FnTh8EypHt1nC8rVALlTLi5t4R7JoUjk1x9bkDzynaMOOJKi%2Fw0OCM6Zq8YEgAk5YLSnGq43vukzibDKSPYBeaNkE5Uw%2FVTCJ2MXLBjqkAUE0kU8LywcAyiLi19TQIT57Re%2BWmzoD0yPUIXtNEZp%2BExedp4IMMY8qqqj6bJidmGgFgdAzilIPebgmznxkTWp9wHHRg7d4o%2F%2FOIbykJ%2FgClbS6OhppnTLH2PKFZfnvqmUbe6LqX1kRvBFaCUcNVFQVDCjDRtbc2xJRTQFIhwvkWMFhnRGnJJxblqp%2By9lyf0QLLS2ardfl7BOYK40eDyA%2BMZzr&X-Amz-Signature=b74dee423530c314cd01ab8203e988f6fbf902a899bc6d8339a3588b91c8900d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


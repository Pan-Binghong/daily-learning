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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJLV6XSH%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIERuJ%2FbuI7bxFxHCOLI6BR0A1%2FWMmjkMxthkdoodHGKtAiEAgVnBxEQjaUnR5Zu23A%2F%2BfH9%2BcfiIBK86uG4lkj%2Bv0Zkq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDBZ%2BvxOvNbTib6p7RCrcA3caqNJecEbD8SbHJXUt%2BrZsNZdo%2BQGoLQT7IHlkp4rGbXWDUPU8YbNnz7C%2BiE1eqp2vYBmzGMiG8sDQjhdb6aE52FK3Z8nqTp16aQa2FgEaMWif1XFHLKCRaT1G%2FnCr44lxIiqnVv5TR75VWe%2BX6w7wzX4dc71SxJ5FoL1HJBBilAdD8p%2Fo%2BMcDtHSKYW7X9%2B2GeJiJdY%2FnzqNIcXkPjhsQJ9VyDXyZG0aHoPkBc8zF06ump%2Fi2qxWkNHCYx1p2b%2BrZOutUoaw0Q%2BgR0j55uUgnFiqA36gN3Qx%2FwmPR%2FS6T%2FD9Qlduzbt1%2BODufFB9UGzMKUMA8AWI2UvqBKEUzoB0cW4xvm%2BUgADRwyxWttUZwbuQGPwxicBX0dTGxLcx7LNRk08%2BychAA%2BVMqNCty3imLSyJPb2JkWV6MPXXPYyBgl8InT8PKBQz%2F4SbBTT9M%2FIpULfqcDdr8L2ZWTWXz5hWZhVC6ExMf%2F3DJSO7EiIZiSCKgHnivHm3ESoZDThqKvjyZ7oS3NUZ3UdGJpMUwI1rZpSpHSPg1KzhjCBBjx48IjcPV9jNGGFZsKgJ8vfwiuB7xgQfc1yY%2FfiNPHUlazhlCup3WiwquNkehggmFaQJNn%2Fc2mnojvrHlOxB%2BMLHBw80GOqUB7JRELXtmOpKMkqPRRZgXuXDe8tJbVJ8WHJ21J4DxtjqabPz65TO6d1AnF7cJPj9YTK9d%2FMqdixmqAm9q60xtRTiGX8VZfEbR6xVuYgoANsN4e%2BUDp4%2BgRzRydJNKD%2FFjL9VCpg4k4XLzoiINw5vpRFf4RrJTlII0x5kBpWJ%2F%2Bpd%2B3RytK0rkvIMyfdAQUdWNPyS%2BkUeOHqHBOqqgF%2BuBz1FzyCcU&X-Amz-Signature=dfe68412fab2ea69073e51630636ae9de042a53d8833f1981178d7b43c90cb4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PDQREVO%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGdj31Qq%2F6W8D1vbWdr9KiejA7TJG5oYnLQ0gymvfou6AiBim5pSsgKp%2BWNJU65HgW6ozVf%2Fj9N1p6ca%2FgrvbbQmoyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIM6N4YtbFn%2BctDpbVbKtwDes2XPGngwwHplB%2BfG%2Ft%2BmO4f7Ip9jYKJbP4do40z1Vh%2BoX8%2FUnbzuWayhcDDdHiou%2FpmD4EpjLCz1s%2B%2BmB%2BccMuEdhGWfUmvkQQ7fQC5s%2FTQZHEIWOhbMqBjQZDovvrEqOor9bjx3Q3gdaIm5molFoV%2Ffps6Y%2FoqjzuWcusyyDF20dAfh65hsgeJvfd%2FkEuawf53%2F6Qvht74O3y27Q%2BEVS3yKYF4NH22nrsW8nlrslwb4jkt7vi7NGnULLZ%2BsZBIEYbScqPR%2B9YVzI2jIOVu3KqFqqCxCv3tVzqzXGPU%2F%2B%2FUe51SVSRMsHYR3kleC6kyolwdkhrlGhrJG6bZoheXgD6a3ox6oMt4Y1fvxQ%2Fd6d6CljvQ%2FVQbZSzazQUbzpuP%2B8PLx5AVT2Vdpe2gTvFP5XVCaDgAhIBEoTb18yMp2BjCxZEug2xQFEh4zmpHvy8psSSreTjXCibmEg9Io%2F7b79ackELN2y7QC2Ad7zp20QUo1Ly605rq7f0xW9kcnpRL0%2B9xDIUxBpu54mZhxj%2FG2g8sBd0xwIUQFGslBdj9SY4Nq%2BAqY7YQXgYigO%2FvsuvCdmbHKYzIG1EH2EwCRyjEzFjxHABV%2BqkBvpRpFi%2FSyjmeCVh3t1bNGWi%2BTIUwrfLZzAY6pgGjbtaTn%2BabjRJWYw4A0pejrHdFiF1EzWqwg%2Fwk4eEuU5z4KZQ5iH9hF1dzDkJa%2Fqzt9guKc%2FsTkPPKg168u1VqxCpxHiSVa1QnkzqSHkZkjmTwoqKPzusYmcEJ7l%2B0kUopQg8g7XpoaSkuZrGVPZAPpgiyupCkHwIXFV4NyImGrN7Jfyb72NSuIY2IiGAJwnenYN57PkTVUNBo%2FpYv6zO0iNwWkI3P&X-Amz-Signature=d3b58c4bc81b21bfc0e3d51f774caae4fb4113a3ece5749e553f555a60a4b6e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


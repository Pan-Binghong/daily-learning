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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MTBB6F4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIGVC1LQTb4o62%2BtrGVHKhZrPwuPyiDg9TPy1m7dRMmQzAiAH3AShWnPaYd7HZeWMYm8tkQfMA1alEg17s585RMOoZCqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHHLtMVrkh%2Bsk8sD1KtwDRWXxjtylJ9Tx9D6GLHvRnMfJXGU%2BY4E2XJZPYcfjV0qe0%2BDaWnFitM%2F19bTRBgvZK57PCLhz0hFGzCMg5ZmzLWOQbMctFtzwecjbZuIZ1mGJVly36j9Sd0pbBEz148gU22R%2F7TFAmAJm6sTbHVm6KuzYDmc5r2n0%2F8KX2fMYPqDO1FsTWYYr18lNja7%2BjiuEAARmfdY1AT8jplRXeuc5N3C8QO69HRdaFUDz6HxXlfq2B5PbnI5mazLlfBYjsY4q0RwoMcPVPVwOLXYLwxtTh7K3w4fFUuac1asUM89nG%2Bzh1lRcdXDJu3IUC0492qjDdmTJmDM9rcaztWspRhdaso4nfAgVq62KyRZ%2FqBQKTgXy1sMIV7uWt0714aNmuXPSHr%2Bd89CnoQe1btzwhZxhPAxGu%2FAD9kYasLEx9nDl504o5Ioo17gAmDgNvfbpvgkmE9N2oYJixE8arbv%2BLpXfZWzvHaW6T4BGVzUMxCHvWF3XBXHub6gK%2Fms2vGv%2B7p3vYoRVCItTIzSNYPM%2FlHW2rq9w244vByXrWECybBYrUJsJoI3yUs9z%2BFuxcSOhqRceBhS6ZIGzfI%2B0RwNBiqkDkxO7j5BZGPw1YgKsaeG7VOyi7n4qtJxro8yEvSUw5eyczgY6pgHT7CXnvUosfI3tieeFDn0Vk00g9OpMllcMY6Hlx8w6bb9jyBGLLTKI1VVCx5gCSc7GGplFJU4tpEPiCt2BbWybskeCI9Aj98%2F2ej%2FcNoXjhb%2BfyYfP7I%2F1Gl0ZuDvG4uqTDNak%2BPBZYLCAPmUZsaOyuhU3LLqHxpJtuuWJYN6KPyhUQxa3lxhm8wePwjOrrTMn3mRyBy5IRDsSu5rc%2FBB8BjxkWqCS&X-Amz-Signature=5d92ef14bfc4ac0b14458c820b52f3f87d5066ead1d64e46f50445455a506668&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


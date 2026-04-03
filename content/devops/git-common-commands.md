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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWBIXOVG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYXJxwA3D4xRWNuOBEPLwXDNMVNQJTROOL6hWCLm3CKQIgJ30MTWJTu0WXCzug3AkUfkBhqaRnTkp5JmaT75hKAh8q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIk34p%2FhO9%2F23zyclCrcAz1nlv%2FqtrmrMMQPZ32Dp2PlSS7q0XD96L6oPFnekhzM%2FyLqy2V5QiGorr5ObQMPJarz3S4HcEAzIXuLN1rpSjpioa4InDsCU68QJhV97XYwvfCCoVbeXfurjAmA5JwO6nm44tNiNyamn8A%2F6noH192hHzGJGI%2BIpHCleCAAAjE3xZHn6SvKxE%2BN89Y2ovDLaDTSp%2F6mqnCVHE4h64awoFjYmiRMblFhZmvCqvlB%2Fzbj%2FynYZto%2F89kIYe6ZvkPzfgCmetVat2kfAir%2Bq4xm1yj4WHLYVvhO4b0nXI0VJ2FkS5jRQlO0h%2BLR6xZLq8UIlW%2BU7nlAltd3T7AyvhPMIwoBpELyTz3FkXS3cAdJY6COnJR3%2BNlWh4UNuBbLK%2FRRkbl4OUTBqn9SHzeB9OeRkhuu9qo20AvpkBFRT%2Fc4l0tUigauTgZVeHMu%2FxtfFf65L3Azqt8uF3UM%2BVmZYpL8EjQ1jd8CwX1Fsp6%2F4VKC%2Bzs0yEliudtmgjK18f%2F4N6DvhlqAgpPpjU%2Bxxi6LlPbE5KC8XXLzmWX6AWaDG2Q9q7q%2FcIrSQB2lMVRXgowheUAvjz4cxQxpttzzHELdYiB7KLXpOFlloUbWOnXjAH22esKQRJAZeGuI1YfC4w1KMKmvvc4GOqUBlPuFSgMWGl4Xe53SnZM3xc0ipOn%2FPydAB9Yo%2F2b%2FwPRM3yFgbYOhUZFUXA5Tm4Y1CIfxIWZZMHXdDPFR0kTAwoXVBWK2lfjmSj%2F9SeUYCcHOJ0wZ8dUQ8m9sydLOc5nscxmL%2Ftcd4cx1UbiCvAK8efaTrrzKQy4wPYjvU%2BINpLT4ymieVZl5Ty7eFn%2BhA3JX7prGrOCSh6yrp37cI0jB0bIGBhyA&X-Amz-Signature=8908abca7b212b5648113ea069cc65407dc98e8717cfc37431d90ead5ec0a1e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


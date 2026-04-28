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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSZVNBKQ%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC65AxM04ByJBRjKydEMt5JhlpxsMYfIJs1WGA4R4yAlAIgMpfUjt9IZbcA%2FBwKFgv0awAXKZ7PBpbbeRw%2FXicL6ScqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOetFISLKAK9Ye%2Fq3SrcA1Wop9zPSVTbmP3%2F9J4m4a5St6J0fwIYVQshGjoZXWbwG%2FGquIMDjgVNNSlDnsYxctwqnLd1N3Wp5C3cypcCq34mNIc2I08RZV0OOnkcXkUU4M%2FTqddgjjEa1kteg9kbvRObcHx1xZqnkjmFEWUAD1rz9LU7ehFrh3cKjNQijTSsERYHixjijq3G2R8dBl8p4jXSDSOaCyIFWN0fkmsT%2BK3T6p5tSZcB83lHBH5T7ILaNq1KPxXxxAeJ68JAhv23Xm0h5vt%2FV1wrbCwIamXCC1vIlLWBN1WOn%2Fv2DBk1MU4bfhcGyUsqXZlISSlt78aOlZhLGEnJWqrqm92%2FXfjCkUDGSDRgmQ7UCBGK7l5xNOn8wackPckzMa8KNcCwNzIxPLxmTr1XOnlSxhfAoGB1FZxoRpu%2BQPaBg6GWVgF%2BqJ9YJX%2FFWn8weRH%2FdTJ8td49oehpOAp%2BjH0gz%2Fj%2FL0ILuqC3D7pBq13A%2Fcb5gtjaW6KlKiyj5JyBjtMUcfD6f8i1bALqidzqWFiqfpjQEeRB4N34Ss8c3WhCCjtwfE0TbeN4%2F1Z2Si%2FWMchwCYfhiJDDmsmDp1wAQE3cqP%2Bf7CqYsCu8H%2FKb9i0Z0Lhfx9u%2FZcROmQ%2BFNENkHeKSARBHMK3swM8GOqUBMwXstXFpW8j8cDj7LfHMWcCpFpC3NCzd7omF4XQuZlrbey7QjTBp4d6YlLuUFRkjjwnkgjrcBpajup1tqbxQLclbFVqKn5wVXtLR%2FZa5yQIuTAizpSDuHXnyB28I7vE7Kt7sa6SDs%2FcQKLCc%2FwWMX2SEJMflpMQv2FK7mx5MYA4bdbIA9k3uGsWQGxwBbhVdztptEvOYAJ1MYA%2F5gEQenGIp%2F4AC&X-Amz-Signature=d48d4fd64ea1dede5982de760241da145671f42aa93c32c3a44a3c19bb10525b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


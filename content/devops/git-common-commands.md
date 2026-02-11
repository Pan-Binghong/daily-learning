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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GG6XVJG%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtD0uCjpQb6txB9c2fwaZXLb48%2FG6o3A8tkcJbJ%2FM1IAIgCac2oPxernd9Zl%2F%2FAtX5nhZFEqVQzxQmH6h5Ju%2FcXQEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2BBPl6bOonfwWjDGircAxDeow8xXxuEZrMOEpVzGVs%2BzMhnPPaLVIAsRpLRjgq8sZF6zh%2FFtZsd4QfsEQaAxyiG3xWrhXbzVNoJ9yaY4MtEJ3ts9C09iVI%2FTg1UyFFmi%2B55ygIxHxgLH2Wxm7PcpC69bgvt%2BzYjVcacWzhc%2BO34PC48AbHtaZ09x0VHaK%2FWhbtiZhhGE6giIJSBTTCNtknJUl0t7VV8p1cXI%2BakXOSVLojy0j0eVBHmJ1oz0CJMSDJU25QG7ADIh2dX%2BsFjwJT7k05MsGgigkstjpJVNWxquZLy36vo77bCIXZofNkRkiNzmF1DEvdUpr3ADx5VGG5rBN6UHvKyHC5Qp6xr2lRrPGzJd%2Fe1jR0JvmGgzonhbuwPiLdDBWouAJC220b0JwpkPStMLsRlMYRm9WQdkDbeh24SIH6Astt1CngKkOg9K%2FEyyXhjlPeqwzsuwsjSs57kA%2F6JkhkG7pdXhtaVH9JOPIrOui6rI9HPKskP8cNxcubuWJ0%2F%2F9APA%2BEKnfeTmCEqTomPYLdRHMyRSqCMk0s5425OCPvpnytPu36B200AnwfgGlDSIF2YogTJto68lvfpik6LiEineRRUo%2BAgJygKmwc0VXLranG5xLcAsvQjWkeAtejn%2BLodktWlMPfKr8wGOqUBz6epViYUrjLyjbY%2BvwlRc6rPj%2BvB1yIUH8tqED7hJtJ58MtvI45qyWNw30e%2FJ2yiGmKuDdk5SDV3cae%2FhHFE%2Bwqhqiz5djpIEhtZilwKfMBcYN9vNIwoQcaPChjaDBumsNriCqTr9kYeZUA09d1j4raKCyYzCY%2BFlRTN0HYcnYrXgJRLvpcmHBd%2BXPHAbXm90j0GhQxUUj%2FgiyUYE011AZ7u3T0T&X-Amz-Signature=b6c21072841ff1f04abb6d8c3ed0533f889c977e9b2deb3355b54fe1e6f09d88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


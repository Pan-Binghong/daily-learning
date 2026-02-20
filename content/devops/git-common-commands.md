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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWIJCNL2%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPpQykAfaNlpfiItZmNEX3%2FU3AVWtuNG0T9v9Qrg608gIhAIelaWSKo5GA9OT%2FRUc%2B2GzjRvMRnwiYHPf0UBUHUB7oKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyegxYpyEuzeoNYAMq3ANKV872vqR9Uoju1QupXruQjaCYeeMZlWKIAb%2BoUu85LYrDThCwAiRuoQOs3Q8jJQW3Hg2nIqdqkJ%2BGF2YtHG6nDMa7%2FYbTk403wq67K0Ii%2FPS2nU8%2BYPASbu2TaJWoBVXxzQJBw2r3hUpk%2Frn2xnIATTEar%2Fd6iY4O5yktpXoOOXeRvK4jzh6su%2BqSLtL8zyjDM%2B5CRASB%2FauzcuRcQwozetakwnkARFHYS2KzquwDrgs0NWH3TzNHyY0q88bfQ%2FN4k%2BBp2HikMfYYJx1uWWkKSrl2Eu%2BaXjGhkVDV0FF6bcvZ9aLsgqY4jvpuhCNJG6nia9ALnYLHIVBg0IBptoXjMHlprFq7f97FSTU2SJ6SXnsryBuySs62pM32ukZ3D%2BlotkqUTEyonluOhbCdU%2F4EhgZ8KG6ul6svGUlv03XI17l29eRenh%2Br73Uk3jg%2BuOP%2BPexvQWxGkySimczhK9MD%2FLiyEiGYQtAsERr3Ud6Fc2OAgMWLcwKj2jVSO1Yin6ld2SfhUVFR81u3T22JeUuJepTnNQ5PzubHXowh6PNywo8RK7xP4GlL5oQglurh26Hc5XEI6X6p4Ie%2FhpJYEE7RDsqVbuKOK2fqTuRg1IIg9%2Bb1xMQYvE%2B0A7TGazD9kN%2FMBjqkAa8ZBlxvtEQIjH7tOqa6xSj0PAPEGNJxxbm52oWUdkHZUzELUoOGIfmGJtqg8c5Z9YQUAfo6nVD%2FjgCsQYmFOxTKxQlPqjEw0rvkf1P2Zawohh0%2B0Xlfs4b1CgyuRb8ZBetlDHJj1FccilNNwDOXUQUWbonkNIZWYguxpCM3MeYXdaHhfS2IHwQu2RSHtFjBe6lQahXfx%2BZOWuzT6rxKW1nbIdYb&X-Amz-Signature=d7dea2de0ccb07029b80d23c4fb6cd71806c6d7528784ee586c6ac22bc1ca50f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


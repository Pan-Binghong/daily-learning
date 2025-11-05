---
title: Git Common commands
date: '2024-11-20T01:22:00.000Z'
lastmod: '2025-04-03T07:41:00.000Z'
draft: false
标签:
- Git
categories:
- DevOps
---

> 💡 Git代码管理规范说明，以及常用命令。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKR3JSL%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqs8amSlVMruNP8sQCSC0vFRb0huebczGTnZfR3zdoHwIgRKOSmuXRzhdEVXo%2BQMzY21guJkp4Dd7EI4ePo7FaF%2B8qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOdL93BNl2Yx5A6vKCrcA0w6faSL8%2BUS55KENGxnmUak3YXSN0PsINplT5ToSZybRTBKjtgiS7kyPhMJ9Dmb6s4qPFEL8E5aPaHo691X3USmci2mY52CrXu9Fm1r87l238RyetV3E4ZK0mANHfNeIYYHMaB9%2BUSvGV%2BDNXMmA5sNoMhjdR%2BwWkR24KX0w01sN%2B4XNARweXdenCmjbWOveiAKjgnPmSBZz%2Fm9QJWhGkizrMErJE7vx2c0O23R4vpIggely%2FBMoN2fS9zIqiWsaHycbNhv%2BLDKkt48rfI69XaHJmY%2FaW%2Fa6Cox7GqteZ2lrLJkHl4q3ZZzLQo8kHn1Z33MzSfnjwnJT%2FMF1GA8j9%2F%2FIuUqVyydE7l8%2Bt8iBycrBuX4p5EEBg8Hjg7%2Bfy9VF4S0EeWkZC5D8uVqeS%2B%2F%2BMYRBKmcvTEVTJJG00yE%2Ft1MU9NmjZbV2ggpY5KgWQIUfReB3B4MXQbBlTUS28YSK3xglmxteYHa0nBQmy0JKoTiEMwRSl%2FKqreddCJ7eworF3ZWMEHYEWVF%2BsuUSjVd9YR%2B9q2lTBUWz9%2B3i6cVgjqcKBhu%2FNUoMpL3d7zq%2BrmWLuBUxYXkn0UKVV01b1V0GrsQPLoWKmDSM%2Bj8QzSXP7qSD27yCSHubKypkjkIMM%2BirMgGOqUBQLmD2WfEKvqSuJdbtWQCuSxLN4MlA0mAbOVOBstMBxLbGbda6i%2F4Ha5ZbnwCeEX54DnxTRFmvyJJYIen%2FEbqrGH7%2BbSWwxjSbr8b%2BFJoI1%2B8yrJrhXA1XA8YXiv8i3Wtsr%2FLGANZMGhKouSzIlc64y3qHFXnEBA7pniDGHQ7kFS70D0UE2nATgJ%2FEgEExCXSbGMsIJREjS%2BJ213%2FcE9o4CsZd84V&X-Amz-Signature=f9ed62d6820a0fd8b99e9e16c8f00eb30c24c9f53e48e9880c4cee01901d5782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


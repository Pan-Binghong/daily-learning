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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RRCWO3Q%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC2gw%2FxRAylL0WWf%2BZgwT3jBY%2FwzZ9u1DgCWK1vE5lYCQIhAP5b%2BsU437phimUIhhpVI8mcwZY4a5HRbqGB6cdO3MddKv8DCCUQABoMNjM3NDIzMTgzODA1IgyN6PLxqd9ud%2FfwxWQq3ANv9uTjWbfBP7E6L4eK7gjmHBOu9Aqy14RmA7lzlhrggDgup5S7%2Fj0tJZZ3ItyKb2sKg6pOwi%2Fxqni58fQypL8gIGXfdw7QBFwLjI1WAl3D56m9FAgXxvYgxVz5PRdu8H2zvJ4oIGc1xZLEjI%2BxkUGPX8b7m9BYcM%2Fc7f3xfwgIVHWLq235L3DrTE87b3JLfFRaJFk3CndnjC62PIeajc%2BVhKHTUKZoHgdsXMu9m573xMUiIIHfGMuXWrNuU5hAvLwudaAapycImYZ2R2UtaBhgZIamClZIOgG7c%2Bp%2FZbwCS6TLBphtFtAESpkaLyjiXKwx4NHtz8qrvleMBSCF7lx1Xb9j0th%2FOOMoIY7BZNUBYEGsfhi7KRnZaTKQCr2T3V5IhhOfCnz5SfL6y1kHoZyd7839EwwalCbGs2I4K5EA%2BxGGMn1xg9rGYwR1xqp2vWNIlCN6ipV0HopDA3enkrutc0H1vkMMJr3rRPzpynANC%2BId2NNk0hadpncW0erobLh7hc4qXsCmBGjWC5VSZzmDr0o%2FPcsH0WEi5OKtzdZqV%2FqVGOsNSkvYkWYsbAny920Pfu3jr%2BuHv3tfnc%2FbECemHfm9Y%2FkiUGmZ00fA%2BYsRUCoCIICPtT69HM30lDCW%2FrjNBjqkAQEXyrFcLB0uY37T3V5F3KFriGmdugHQd1GySI3WCAVVPQb90hs3FgBx2ZybQz9%2F5KoM%2BydVkmLTAnHQ09M3tdUgu6rhX4jwTvmHbjfy4YJHtbw%2FRI8s5MxV5o%2BW%2BlbCdkswTiEwaphAXwZ%2B3K8U1LTK7DGv%2BHgH8hk%2FUFEobeCVZOxjejmi7qMmPpOS8gIld868nxCX4Ksj1LGQljtUKUBd%2FyK6&X-Amz-Signature=452a300012f026a74cb70b4b10d3743a844fba2b9c5066759d2e73b581192485&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


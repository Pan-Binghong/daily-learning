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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGZMK4KU%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmSgGTNoqMwKEV20VNIfm%2BCiZEBohMl%2BIYYPHmIRlUZgIhAIk3I0eqRU5%2BYDq3ZC5p887w9G4VQyeWCN5dzM3xK%2BSWKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxm6iLpeMlQU63bElAq3ANZ6tbF47vsgJ%2FWNO%2BirRcCNxBUlayULqoGCNOY%2FN0K1VDFhbrUXW5Q8UKiQTGpsFmopn8PCiYjfOMutsEu%2Fm3XzBimjKEgW%2FMnJ%2FVdoMku7I36TW2%2B0fBc%2Fc8EJMrNwYvEAH8ADVFgjuXKw38UR7EtYX%2BRhKGAKRNYipx0hvCoP4f4vWRlkdoTdK9yK6tH6vfo8DYinegRLeAT5gi7kzVR8e4noM2POpwrewdrj8wAsJzyVc1MJlnd%2FwBVc7izqGY8hZ%2FgYvtTheNucHHb2F63K1tZByZv3I4DFhTKTvG1cYdBmn4DUNWe4zUyFxRjQdmtViomWX4n%2BElVWZbbXhFRllxM529EA3FNlc%2FFvQAhtPLXWA9dFP6AgXTPHPVYFVTdh%2F8xmvu42T7KmKNQ%2BcjD7WYWkaGim9ZT1Tr2w1PYWSDAREu4%2BHrEY2qNix11t0ZtI4VhxYsZRZeJYhFaynF9oSc3jAu9zeVpqkigAX5oExI%2FKlNyGFdqHz8KsnJLn5XR1tuml7bGJt7gxGOd7TvpAgPBk7DoCl89NGSVdYTJRTsaNtgM7vhiBhBbzp%2FSkcZU7A7STRo%2BoBvNNj63gMDPEbwmqaHU%2FBKAEz74hYzJXFOQYAYVdasraSZWDzCZ3bXLBjqkAUiFnyZRHYdM9G95Uf%2Ft0O5v%2FwwaqsyoCIUyuvRkP%2FvasyUCGrZiEWEp6VdhcHKmS%2Frkx3CL%2F5EUqWJwyRaJehp%2F2jNJsnpdAxLePGrcJkDVy625lUW%2BQP%2Feves7VcWlC04Ve5AC4WBlvy6gW%2FG%2BZrcRpVQL5MXmE1hhAcTuk4I2Fly8wffJBuygYApfhhLi7YsTwcARSOgeXPmKy8aG1wkMWqaP&X-Amz-Signature=6e72f3d9e8139b81f8325d3d2275106f5a3aea1ef6d263c331f7957a25790e06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


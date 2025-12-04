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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZX2UYBI%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCKiJp24feyNcpP2i14GbBdzAHzviM3508TeePkiV3fOQIgdyxtliSY7EptlGQC%2B0pHuEQkj8cbHY1WKHAZ5vf2wIoq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDN601xpAeCQjWBHRoSrcAyR4UZCY7hA%2BkmvoCNUvrRkVh0QlbN7bzLqhlcDbkCe5CaSn78BzTkNLuuqccM2ZITw3%2BTtEBrOEBD8neKIIdB2ILfN%2BQtObw280zkniLYYp9LfBfGJUQT06qOrCzw0pR0dk4%2BV1yxCT3QKcFbzE09ofIFW0JNLSE5Zj6U3pyftbG9bzruBJU1ec%2BWXs%2Bbrsrv5DIQIYQBdWt9fi8C57BOqBrED2tjCgUeBKDmRK%2BiODNawD8HcCvytrf%2FG3F5bAZMJX8d3hl4EryiLYmIQdiQMF3BJ6D94MKLyKZFaDLpusFFjxbUpRK2TjtrEP1D7nuS6mAslTaJ6ymd9PfhGN7cbvq59b8keJkV5vZCb8jdub7j65tDCwJqPTByVR6y1cCDJ0KMvGFLziqUCeWDY%2FiExUStzFtcgYU7kYJyAj1JuX%2FRIDkJCM4FPxUcJc0SVHk%2BtxbfCDFn%2B%2BmugcK%2FLr2E8Jp%2BFKl2nhrv9o3L3U4lL3RytbQyHQQc1lfxY8HahI8nCnASDkqlymYls%2Ft%2BiIfEcUds9QotQnZB4hPR8cQAFFrfXcKL0KvmMWMfNgqWjstGiXoVjHHHefBCxUbHcIZ3GkC48xDYrOlX9cwSrCP8K8SG%2FcScN8UwvKYE4RMNTUw8kGOqUBtbu4SkbkIgN%2FbRKClCqTISWSVeGxjCCm1sql%2Btk8Vn2oSuUWeluo%2BgkRBMsZQGmaIhTb2WvhB5QTQUQUvZxa4BMhh%2B%2BEtrWS76fI39zVHLF%2BhMvPklY9xwRtiwAn7pVcyPwMWmBIh966evkRhyp2yEtcqNDCv95oUoCNX3F8GC6wYNw5eXuYv6BkYThuLyR2CoLpFN7mwBoRDCK3K71ZxKvifB5M&X-Amz-Signature=255d16a4b3220361ee41d180a6caed41da8a6dddc7460fef39ec1e9c39ea68df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S2VBZZ4%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BMvwi2PlhrdnQbdcBuxKmj3N7hbyZsy0dhl%2FJ2ZxXLAIhAKJPa8UyHai%2BWSYrLmV1XBqghUVi3bZMZ%2BooPOt151leKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9tO7pH54AVDJ5GQ0q3ANjNtwrmY0YP24mCOmXBomHTvwMXylcRVVRKGTQaCsDXEFunXn5RCBXK3JkibVbjd%2Ffg771TAmmXVBipxk886AQ5dzneh8JlxGNbmyJJIYR%2FQmxgUF9YS1n6CGTzfNMwsHiGVCLDbP3v68Pi5u1MHlOqG0UGYT4vNcMv9VUQ5Uh%2FTwaarcwIXxzybj220i%2BI0%2BXQtyrMvhcJ%2FVFV03jO%2BwJYtVEG0qBgtsssi3MLLTu%2FFw1UBLmB0XS%2BBsEAZcr75d%2FxmzToWZPjTcqB68TiN2cthgpBIlXPf5HNd61y9rw9ZWWJeHRP0jgw0I3CBOIFvsBzbB7caqYeueAa2Q%2Be%2Bt%2FmP1EnoiF%2Bbg%2B8SVWqt8KFwJgiglEJfOZTndAfxMZI9Jwpd1%2FtUZpsUZFPnTX2v67%2FMSuF6D%2FtSQ0bmaT0f9WOEFa8z0iqjPX58KlxO7p%2Fcj%2BCFypiXy6z89%2BS6pt3tPuJVcUda%2BOsaTLpVgj3Gld8kHJ4AnSi%2FXxi2xqD%2FioNL4g0munXpBdW%2BRBUgyBBHvjTWFm%2FPIUR88LW%2BjcbBzHQrqM7cvpDYZ0Y7cmUoK1Zl7ogbiuFZF7r9rPo8IE0u%2BINlFSgN7p0lJFURHJTBoUjJYrXwDsU86HrqN2djDUhZjKBjqkAW%2FmMa23Q5i8AzoB101ya4DxCG48EP12nK20PBA1GnxP6RJIr3lpBvzaW6vJ2XKXXXSN5HZRVP4grPnWQsRPZgKDEJoaCV1zR2NKXCBSg0Erg2%2FtUulQfgpVK2HZlfPwXP4wuKvvzNMXkoWtGItUjazTtAvzindOt7qUxgx1F2AY5w25Ai3HBSl9mgztAv%2BUnX7iskfE1%2B4BYPreevMJotoIGh7%2F&X-Amz-Signature=127f1e0c1710bb067d9f6b1f4df5cbbea614a4735e3f78efb2071c3efdbfbdad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


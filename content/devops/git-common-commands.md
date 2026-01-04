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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7BSDQG%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQDWguKJi0eDUNATk253OnJqObCVhPuEbcMeHoKZFTtGMQIhAM7056HSnRWpIZ4s9j3fqt7j0cFfwG2iil034iAAPq77Kv8DCCIQABoMNjM3NDIzMTgzODA1Igx3Ff8RUW4%2B7JF%2FJ%2BAq3ANqOTqQ6P7yiI5xwE4HYmvESrsH91g02wdq58O11a8uHZOvns1Mr8og0roHled%2BAcMl1aj4JrnABwo9NqgYtvBtl9aSdS8rt9PvdalGzDicMphtQCONvpAoLZ6PnLn178ngZmka7BegVxq8ohORTC8Gy20%2Bh4IWw7%2BpXix0LYlVAHAVgwFzJijhSR%2FW0eQQv5Ki2AUIVH7AV%2FGdILNfiptvpcnn67GSMTmh2YEKJZcjQIY2%2Bs%2FY%2BTE53th4LLmgCvjSi4iJ2y6RCHEQHlNhwPk%2FDf9JLxb4jZ1MiX1L%2FHbIbyHubxbl%2BK%2BWdbPO5qf5PitYUstZ6Pxk%2BiYIvLzmJtQ37%2B%2F%2FCmmTmQ%2FZqvi3rFseMV8jiFBSZ9JuGZ%2Bbrl5ASl08Hj97ldudQjEPlGxfSniDyQGy76nFs8fnrBIrv8m23LJuVfJOvL5bMrxrfEg6CY9mGd5Mae9M9FssJLXOHGIU4uV59Ysu%2B1d85lNcsinU59R6sUQLO4HX22nYXjO7C7vprmmT8gINnGE8IdBjr1Ghg6bLGAQg6Pr781L5bX1ZE21YIOgrkaOw%2BFwWUGNPol1BkAE64r4XeAtpx68SnevXxDKB9lLQH5X3SImTwGWD3OlYGcJFwP2%2FGgOJrDDV6ObKBjqkAbF3pmCAjNoEVc9tUFaTEQZcvwyi4dXycGwKShl5R%2Bq1waIAi39ymnkPSKeYcYKTx08ab4zuE32s33NjPF%2F6u%2FrTQCHBjS7oIJ8WuaOcvAerfgchZcchN94BU9KVLhu0mLN%2BybHRMs8FR25UOStdWqO6y%2BtK68v9VIdvSg8kKGsErly%2FnqPqzUQFi2xm3JKzsrMtUxq2JGMrliaW8GqtD%2BwYT%2BZe&X-Amz-Signature=a0cf81536b6b90465bc95050b5d4c7776ad86336267a16751cc31d18973b29bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


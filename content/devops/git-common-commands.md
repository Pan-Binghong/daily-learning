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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDINKCUA%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUbDPXfa%2BByY4ewuKnOxIrcsZfCJfM%2FZtOK4aPb%2BnkpwIgNSFxGZIGUtJomOTKNQrd8I19rK33nbzpz%2B7PmTeYxH4qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE5UhsbRIjUi8e8YoCrcA8Z7LBMJR7D5Vq8reWYmPsX0ImgYjkHgvR0OV4r1fG97E6Cs5tiP8n7Ir9eS6zwiZ9Jok0XqS%2BWqgA5bzgp4I216e4J%2FW3Gs6SiaGPj4cudgkAfYslnBlkYBuG8Sc4obCezEImigtKXlFHn1LQxRN9r8LXBOD1Z4ULsRXXqWHZCLUOCsxfzHZyuZdv%2FDufx1TvUutJ9e2SPcOk4WcfuHvb7Zd8CPhFq0T5Aib7uhZ4UuSFSwhNrU3Gnaph8b6geB5uk4SptjzkaPQjU95n3O0OObKsX%2FmLyUjzI5KAULs9pBVGHnXjSk%2BZtHlpEEs%2F0dfWRSw7Bf6%2BDncmmTuSwSVTTdKjcCqiPjj339DDGtPq1bOT7m%2FY2dd%2FR6GlgE2iHvKQTDmFhMiAvDDXWa4tN4y9Wh9pNJweZ2QabZzEaTrUJb2JlH%2Bp%2FJgovw%2B9fY0L074y7uSjVqFSzvAujVecctrvnfcyq6tJsEGadVf4UpkTtI%2Bb8SUrNc0bQHNxNCNhN8LNAugIRPE076ZJUFAepr8Aw7YhQ5vJ04MK01Pr7sVn1mm0YDO4LvXBfqKXM5z3h2SSWIopLUQxgF7qm7KpcUMNfx2RqsqE7BDbCFMc%2BjwuX3ydU%2FLzLfkaXhrHOUMKf5hssGOqUBXuvGio5mXQOQ%2F9%2Be5edvdLqEWrmzcuH4pT0XzDuWR%2FLph2mcSXc3OO7FZAYsivcysah269%2B5d60qOpHSdqiabZw%2BeJ3rfKO7yQx%2BOy3CYRLJAvEl5WzJwd6yzoZ3KlcIu3Kdd4ieUpdglGCbw2TVNrwrB%2FwRfbEFpVCZpthf2WglBQVVXfg9ophdnQ60SHVSj85EC9yAbJ1Z2LyXgudNfbXVNIgc&X-Amz-Signature=0a5f4be387fadce5ab99ee191376bf8a59926cc7f19bc3a9850c418330a507c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


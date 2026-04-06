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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEKE67KR%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVUPwBNhDj98M0nVtKqpcsZjozx1P%2Byfb35dkO23f0wQIgRolVk%2BNLyP55UC650%2F0Kf9FsT7mtQTdEZLDJrws3ZWYqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCSJMRACV4FSoc%2F9vCrcA0sjRFUKiq0pKvClQR3jaCwCS9esxk17cFL4346AmQMvq%2BSO3GrhO7tw%2B%2BJORncqGP%2BqsvzsJQMm129PTV8zI8XH5kgc4ZXyKTIq7tiC8AiNWL8GWwcFHN3RA4Ca0yvJtNsUTIss9xJdT8gnl6rTXg6U0yi3DkXmWBrx86vRHttyR0pm9QbCWjuAfyfAxRE0CDXqFbWilpF1xbfms98m2JhOAxHerlUSvIaTu8v1TCmoBzvZwkLAZXQsTH5V4DUfQrzTkaT8kzhQc5VUYxZFkFEas%2FuqwH6jctLBfUjvWz3HxSVxIaZMuNqizJqSoG3hVsu0TU1Wh4pkUzbwkaBXwxZiuVfRtxQSJRcTofpBN4eTdCBWpxZ%2BdNbtSvFwBfkhPPwKBS6I7B8vw9G48j1YvmkNJzehrl9wGNtZZBddkXi51SnlwXmDlYM0r7xQKIid1sOS66sb9OAwDp5PiFLsJn1vNBmNT5M5qzZ0knXJ9LDF2WsnegkjFpJY6Wtb%2Fd8sza8TmYlSoBF8jSQpXEvwWGgq%2FruDm8E6p45F0YeN5uOuFezRJULCa87Spdn1enl6rjY9o7oXsKzaGT3bSy4DbIwMLZdFJ%2BPkx7j0QgxCseEMqBvzlF3JfGCyQEx3MLOvzM4GOqUBIpwxNWuwwtP44yedhbVVPe20%2FACLPWkunoo08kxVQTUTb%2BJ%2FQ80EIygkhLiDS7F1KnFpmqL0CEYMF1i4mwQ1XQXQX2oO87GOUxc8td1ociee8qsHgxbpRKuyhjuDf%2BDD8khC5q%2BG9apQWdh1NLfXg12%2FVCMHwr8HLXGTrIZcO9JUCuLQcay65XFzCKbGfLurcN26j3ab9r%2F0pmyKUAJ6kVRqqrLp&X-Amz-Signature=85d0be0d5b86c75b9cdbced4bad67c7e38597c06300d5adcd6fee906efaba25a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


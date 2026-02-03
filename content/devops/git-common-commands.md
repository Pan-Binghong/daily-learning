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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUXAUOKM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIH0DStjKB8WM7HuWQvwiFTWhA9m0q3fYLxg6lqf7ys6tAiEAyowMqvbIqGyfddpu08Cl%2BEqfezwqwLUAF7TkRE070hsqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6L7v4M7JcHIAxohCrcA1WxzCReMX7v47QC3fts3HN7cmI4zNi948WhykqSb%2FxeZnjBmiSLAns59PZyOI6lJS7BYJjiQlWQvu4lNQ9lu%2Fxpsu0UezhZBu%2FsUhU6%2FnWe7rNlAig6C0gcXiQfEY7obmByINqgNsUakUqD3zmXTeU4px99ninLMHy92RZgIxtt39O55DkqwpiqD8VYjcaJNCRlHx8ggcbjCov7DU1yImBnQVMWQv8qnl8cgkYBa%2FXnTtg8MJ3ixr2f6nSv7UHHqvG%2F%2BUNMlAs9yxH62kWBdCwcl0T22ytFjmKGATCkMgJw8bXdtc%2FW6hB%2Fn%2FXO5wU7o4sifTi6VZuoCluIvSpPEHBRyfSxvOUafgPG%2BboSfPfNE%2Fyu8gsUINbwMZYduPDV7WTSnRs5a4Gg80dbeRkV319eXAIPU49G9NAQI5y88TTrn%2F6lEXA3f28OpPCCKw%2FtU4bTMj4544ZPxUfFhSe2QOhdI%2FOSygpaUhGA35BT4wQ1MFvGd%2FvKq0zi%2B%2Bm%2FsS1L9VtciSujbbGEKWuTYyA74Q4zWQEqlHUj052G%2F4ydDGN0yqJ3aM%2BE%2Fnmr9M7iofupy27EYd2fMTCjtHYioRQJgWjr%2FGj9ohf2ZnDfIRUz0CM7k%2B%2B9KQXUqNECppctMPHXhcwGOqUBRSk4hBMzyaH6R5C9a7zyquu4CPSWLn%2FV4U8NlO8%2Fe2hCugCc8DsVNJTKo9SkpZ1daF4m%2B%2Fh%2F85cZ98q9n15Q9O%2FBSS0JnGcvEAkcQYJ%2FgtPRErF%2By%2FC2DkZxjZUBFqIKlkUwpUbbLkTzlDMFLB8lgNsR0VJzpqnwHKHLAW%2BmMZC0qEIBfBXh4ZoeJA8tf%2Fhx%2FtVCWHl4h8zwg9HseuJD5Nv%2Fo27J&X-Amz-Signature=e38e0fea92f77edd18ebe8f9499f21ab72753c4d599afbfac10137b9405cb472&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


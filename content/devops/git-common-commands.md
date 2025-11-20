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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T263GCDA%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCID3m%2Bi4u7jCs0aeiPZ4TCgTNrodyGN%2Bo%2B3%2BjcnIGGfHlAiEAtSg9QbhQHNIc09b8rYXrDXOsRFlDH3SzOe%2BXMISY1wEqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhUbQ8HpS%2BCROqLjircA5SzJ25WtKHrHhzxuDIM7i9PbDtWy8EbvmL87vIo0JUHS78N5Rv6z6v2W5qD6Re6P6d670hIvrXbnmF%2F5vFyuRXLLRaocbPoDhyDC9kuzZ3HN7O%2B98VqLZWM%2FBO4RcX982%2Bx41ieG5EDw%2BeX5A0I4JH42ThkfludHTxXkorytRNrRWIy3QEKm1HNeHe6U3aq0YMnblRo1qOcPsGHDBBRRUe9pzgkYt6Px4JGnHSwjY9sdwiy%2B4VTyQPzHsTYIKS9g9VUMK%2B4xjwrrciZSKN6Fwk0IwmOLj8RXvogCH4KRt4o3u9aIPY6Prw64VMrsBjnPsV45vhMppCc8g1k%2BUpTJGTRrH0BIowaOWeOvPUEalpRp%2FzQbK6vszGuVYJpEpzPSS97kEsTw8tZRWWLyrC%2Fn4%2FAGbMlfxLO011Mqlr%2FMLJLxNf7prTs9OQ4AKV64m%2B1mvxRKwNwgxfO9eEPhZ1D1CBrKBBXLYOZtLC%2Fm%2BahvVrwqTZiuScU10kZc2GH%2FxwUa%2BNRaUidQtb%2F%2F9JkG8cuFWcYPCGZJOYbUJuZkwRFMJGvy6cpqH61IvIjZM0%2BWbZ%2FANAAlaFUKFUwB5YoP59esMN%2Fgm0KdIXMTjM4RvLg4ZOchM3kOijIRjRGROQfMMrq%2BcgGOqUBq70cUN%2FYIzkx1pEuVcJRHzBMjy8jn%2FNgEhJQySaOd%2Fgw7q6S%2Bxk0ydOXj%2B4fL9Aj5i8Wh299nBZXSy4dQo%2FoscZuHZrZaGbtkpzIUsB6%2BiUQgLt4Q0D31iQFBFZkmisBw5a0eikYei86rUjw9QHZH1pNscRu7A2f%2BZFz9KfdLA2cP3Tdx29o7jjsYcuD3Hf4L9oSc3o5yhucBNJ3qegAnoy9xKLD&X-Amz-Signature=b11c7f2e7985cc3a587c3b4476a466f214e55d71892224d1f8111b70f9993b96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2PT33GH%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI8bmD4wQ8WIFdCAf%2FexAhE%2B2%2B9A5FTW9SCunTAGRlOAIgbHJCVHiKxfdNks9rxJ18kgch6eZOCar5CpzrA1caDo4qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHsmnNxFnYRAcGtryyrcA91xBjy2fIEDl9vG6eLHUZkkkEHj8vFcaB3bkGfbnit1uATHLVXlQ5v5IBlJo17CFfDFb4dcuKpPG9zy%2FPe7bR5F9LENSafuf%2BJB3LymgZ06QqsjH5Usrh4aKxFtqRgsTiPyN6EmXTtfJ%2F18HDY1DqluyjcX7NWZA1xW2l5fFzlNqmjTilg7LJ5jroJE4GrRb6RKb1y90JYjikOaATqWy5JS0PZlFl0FDIoLeDjR%2BTw2QTW4vJfkyr8ytRzJdVY39ZFFm5AeylOWqZGImWoF2O3da7G5t0llDNADdd%2BHMobceNoSi42RQZ0Pcg3R9O1pMAYiBuPe7fJmyJqR4AmcrGvmjZvLgNGgU%2F8FLebSiuQtMiVYv4fV%2BUDZSI7Uzu052qpy0m7MdGliY2QkXNrpWHE%2Bj0qO3II0jq%2B%2BdW6abkyJpcofR%2Bl7a0J5y3QYh3p2dlDKhvT32ow9aZnKh7q60czALCQCIo1%2B4dcoGTfk0%2FHbjhbVULl1FgWXWQ57XC%2BoVMRJriy92UbfNv%2ByBFdE4sl2D6zTWANHfX3L7P5vdoTozlSxVZzArcqcKsR%2B0ArXspeOj0Z%2BzZIAbjS5WRyg%2FNFlzVubkDMU3zsXtFb6DQzXfwNTggCNhUDhDy7AML3yh84GOqUBQmHmCT4%2FaIhyJn7onsYfLgQC9tQYEBVnH72uoNTRnUxqT%2Bs%2BcZqPzLPjf79oXmCLbOESHqxRvRU48qaxBL3modJAcZgiVlES3NDCpG52P0ZjBJql0Ywy%2BS%2BZx%2B96LoL%2BD4XaU2vrqIJyTMdIQRwNLWUPEeqwGlMyOstKPCwHpIYQ2XpOghjzYVMRJa7vC20xlJGm%2FY%2Fe%2BwhGc1AH1n5jsjjOSADK&X-Amz-Signature=e27519ac6e5d967dc02b16c19826e2813f3f7bd9cb2309e3ac9762797fdd390e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


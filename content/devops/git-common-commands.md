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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUZQ37H%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrb2XejGNP5M7%2B1yJyqvKS27KKVhrCal8kHfFWamx0ogIhAP%2BSW9Lf8kCeWq3LdcuA5n9cqD%2B0d3x%2BOlgoTlWEnOzGKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRl0jYScTcrAm6evwq3AMm7WlspEsXudWslz4RBu5StQWApHN3%2BkGB%2B8lH72E9ZbemHcmwjbZyqWaxNDy9PWu9ZpHLtZVaBLRLvM8QqAKlPGj1e%2Bg7bE1gC47yJw2l6pc20R1iRPlY%2FJzyzoyyHpbil7K6rUX7bpR33Zepu9rXsdADeFQqKbDS9e5iUg9mQ%2FjGUU%2BAemV5ieALU1c0LqlmWD48z7CdKf0H7zKeKDIywIwlhRYB%2Bz5lWR%2FMupHIreRjOgyadD9LtWHgPkBVlyMaA3wzcEjxZAkcFj%2F8638TBptG6niCRxAcw1j%2FxFg51i%2BFVMXxNwzVsfT1IZ1e6gc1FWz4XqgMhksPeXNMFFJ9i4c9TbmKTxtl8LCYE%2FIMgulviEExJDIo3uULV2ei35vTXh%2BEbaT4XQ2q6qFQOYyBHM%2FMoQMB5tC%2BI0FvkrYnh5s6K3dbfP52kKVuGyckZKZdB1YXWMVd0B6RfaP7q46RgxZg4px5Tx5lPvdM0WODSILIY1FHs4vSeC7njyLcPdItzwWT%2BQlWv5ChnjEggg5EO3tJZIbCwAHQTk%2Fd45FMrjWuwHeKNsG49a2jt8k70Zaw9%2FbJO4fzFUL6sDMatqkK77pa0y4c0DQCgPIXlqGGJ%2FlAMjNYiLY0mTTyDzDAhurIBjqkAcYMbbVUstz%2BHcxlCHhaNaZ7jWjT6ZjHR%2FPWPCGKhI5Jw032accHinr%2F27KbTkD0L2zXiJ529%2F1F5cf7729cDrFJBcw%2FL8A%2FQm39E2vYfjumHXO8m7P%2BgEvp%2BZmRBZAaRbRDQN2fG%2F36U8yUSOEJBZ%2B4oEfu1l2fQz6rNJNj2C3GPwsUNQtuKPKNVVnesc6ncDU3R58%2Bu01wH%2F0UdpNe%2FkIlsb9c&X-Amz-Signature=a794bd6c6b72f24f24b3f223947ec221fe24731d1568311cd1f66a01ce55b145&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2D653IL%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5y%2Fpc%2B7KOGR92Ja1aJY7lN3cgYp4RT%2BJLIk4WC3f5GQIhAM%2BMbVVV8aqIbcQjEYKg5Ka4Rl1RbME9mclMjN15GRaeKv8DCEsQABoMNjM3NDIzMTgzODA1IgzT9sGGist5DyMu92oq3ANbZ0kpT0kVnDkPqcYilOI2RBhwzk3z59uD%2FFUZA%2FnltKjekqvWMhqMaBcG%2BdVebR8YBPTwssdNYEl5fCPKkOPCMEegD%2BfCdlbXP%2FkioCBvg%2BkouZPFgdgrAFokQkkkesiaACiTT2QICfCk6VmO17mLiYwPqd%2FBRP63CdvjzJpB62wI2M6CqDNJhvs0%2FbehMjJKn7uzumz%2FRTbViM5LqcUZfYjCHiiKETTafrxZhdNHzYXrb8gYAIRG3I01IYIMs6wAJLxMoHbenMmj0WRAS39KGdJ7o6V3mJ5phZgUT9klcbT8QO2XbJJuCdB2A5ipTCzNhKPV4wpVQSuDOkZJfvZhYWORQWr7Af6hEpRbZ7Hr2sSZmj22VK0jPZWXVuSgUO1ZgDIWbK1oSOLsqjeJfK59zekMhyFZ4vbI8NKWnPxk9m7yix704tyLF1ZHU2RNaRydn5HvglPEFN2IdYAHufw43D5SsQk3n5KEWe5NtWvhVWCriHuXW%2FeKXzrQHt0wl5VAOc39f5wf0oaqfL0nRQi4MgUbnI3DYgkE3BKoAje9TbtawzsHTpjgT%2BTDtyn9JCy96ZJnd11v1XSRFJ8kLATV%2BVxZcreastRxJWMRp5dWnU9AtHnbqN8D7hS0ZzDUzLfKBjqkAQne4O9NMAW3zapyO0TDzAhxkrHwZkjetddcOkZ%2FtSdtM2cXxNUhXR4E3oh6gDA29GgwMkKUOAsoVf1oz7nybiqp2Bi8IsLffeVMyPPiYfTidGYAVG6vLWefIEdXDgZEk3OCNm8OZZJuQ2sj%2BwrWJ13H7yvX7T56fH%2BbVdeKO%2FwzYEJSi69xpY%2BM3h6HLZyUsDvsILAxuAYcjYA5L4Q2t7L9L9iM&X-Amz-Signature=0711a794be3847f844622e4ff5eebeea8649844325b5c812f1c7f0154e41bdc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


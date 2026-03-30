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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSKGMHDJ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCs0Fy0edyHARqjSeqxYn8Zo0ChTV%2BfycF0xqMH1fIUHAIhAKcHhCnc5HF%2BFdACPDyKlYLOGuG2omJNkAuVfLjoXZqaKv8DCBwQABoMNjM3NDIzMTgzODA1IgxLjKzli360m4tHn9Uq3APmg1feVBKJ0X%2FhAIULo%2F9fn1guEx8owsgoyyzKXDEGBRiQ7KvoFsFaPW39JVg4SlEcMmtLBXABTdpQf5kw4v5knIduvgklTmc3OrJdqXCaaFTV8ehhWa7rNjqg8zD5Yk%2F%2BlB1cADtwdX6CulZ5siODY5HjOo%2FnvTWcCKBAA8k10nN4SXGDc0Avu0tLiJ243r8hCG8NNEAPpWaRjm2iAxfXwgrQCxOuInioprs6y4HBR3uWCwPjgvaMcBkx0REomPFB9wo8r2dCh2Ow0u6lPyHqTC6pmm353DoGAT7N63kR6aUyQoWs%2FMEaf9WvobDBkdPwmsHEkN8psBxTIru5lidqrCn2rOi%2Fli4xMkPy3jeDEItdQFNdK9vaMELKiNeD70LEZQb%2FpcUxppweojBWzoFopUZKzAVN5y54HW6QJTrxuT7OL6JVMtNQCqhFiZA%2Bpqq5v6P4EERVpJqNZlYabIqiNvznehely3DM%2FayZhJDF1aZqEmmICdJzsVdpkF2cjSMvJ%2BLeMf3X6T2yYssSih4XUOxIednXcPRS1c9N5X9ZRlcQAYGhhXiSTBGnDLjgEyCHLsPmEP0ZSvDa87D3iyW%2FvMZPiyTl98hnWFQG1H%2F%2Bdju8RdSwlc3XUN%2B%2FnjCayafOBjqkATOd7r%2Fm4x%2BeUv2rMChOr5Aq602%2Fbpg%2FOCJG5BYNbRkQqjg7Ahrr7uVYgrd3VgTUhLaa54cT4qhKBvpCeCjlJnWj2icZVZz9YJUfa1a6nk64FO04Cqbn7dcrCAoXScgQe3ih1b1pQEJqNdD6dseOPsJ8%2FHT7imm8GG5X9z72jvQZNBdjyfEVINnSK34dT3p7%2FrepiGibq86%2F%2BPDl1nKea9l1I23u&X-Amz-Signature=becb58b48dfc4024aa805e06a20bd40cb89737fc59273f20e272fd533014be36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


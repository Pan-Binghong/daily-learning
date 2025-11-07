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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDDJCSTL%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRf3SnuB5EZSlaXZKN0cCU4pu24VKdmYlIm7g1sbfmBQIhAOet%2Bgt6WgJMFFAbRk7HB65yTwh1PbBCl7aDqrzV0blVKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqbQwHy%2BjqR%2FkDKN4q3AM6pNrv4X2K3IrdG32BJBjueXJix9Y3GojK6Lh4kTPl8AsbrhJqYKdjQeYhQMMZbepkdHD3fLCGgfRJwSBRevK9GzsCEvKxIozy5FaE9jlsqngyCiB7n%2FKLb3SkUUMBPaSQP0CgYfDzXxNwK6N3xnGEoHzVWnNrbBE78EGABwELtm%2FnVWPn4I%2Bn1QzFsqVzJneWCUeks%2BgRWhFL1MKfg0RFI5vl6a1pBedYU%2FnDg0wzTuRyQPcRlkXOg7XYV70fDOFvLJspmkwJ7o1lovMbvFp7AeuoHNsch0Jz0gxNX2%2BNlItJQJxSz%2FqPKrUhos0Kc%2BIeptq0YfTBTbwOGdFk5%2B16Vpu7R86Eb0DKRLixrSoZziL73EsQ4AAhLJpeDdMaxWuJT5bDS%2BzETC7VCXmjUgXRCWNlOT8p%2Fe8MEV7%2Bwo52UlMpj4o5E3OL9Y7B8pzjr4gv6DxhtvTeAZU6p1uLOXWDPwKm%2Blpagcmdx8ZoNF5Wvlg8ZDT3oobwTm38KF4DAQi%2BQp5rBfjGYG8gL2BArEwPI3SxWfCw%2BXm%2Fb1EmvPTr7vvJ1sWQA%2BxsHZx%2BWdrO7nDI8SbtUUBZVEa9ECUdZ3Pek7xFG6QoluToauWZ5W4hiYPz6aGcwKfvHqDjMjDatbXIBjqkAXNA%2BTy33AE1X7DsoGRzd%2BFsY70iR15KZ39jL5bHEESPUcttr1gakJ1VBxvGSE5QJ1SA8s7qZAVho4lKbPzYTQmCFebewUkFcm7T9ojbYym9Ez9K24LES0HJZV0XepkrPOkSAa43WjDXHya7wv67hQJJd8C1cPjxMwDL5C5ko4t0UI6qtsDCZ3PS0blsrBUtqCVX3KIsoC6uXLvRNdwM5D7ta%2Ffa&X-Amz-Signature=3544a201ef39b3c5e1d156922bc2c6a475deeeeb6b5d86d28027528eca8d7c59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


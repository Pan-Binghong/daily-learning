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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRZFXKN4%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQDB6PXDMvWSrmy89fKSRA5jkD3EuGImRV4R3DwPC11HoQIgGlfH3o36osttGb5kKc9AzIsM%2BuAXORWK%2FbXV722VKJcq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDK6D7%2Bu1o3BtYWIykSrcA56iGU3hF%2FE%2BhfCwpaN7Jczp13UmgP8dKtX6ROcsT4EQyJUB4gRVU8Ne%2BoLN4nNG8FJBJrjrrK2hQdTMtnnnDwAxR%2BCD%2B%2B%2BSzoPBkqx0jrLuQUaFfsbyOIs0F6uLzOk7jbAlHrWaPqmgJG6HZEGPEgn5Fbj7TTLRb%2Fzoo88QUUFtabMSJxk7u96P1MOzudv%2F0Ls47wSeIExZ9jgIMcAifno4MhsLyFaITMsgZ0uUX96WtOvjuzymO4JNPtoQgWI6WjeSLXFrH7iIH%2B6eJEqrJQoPSEUjjjjamXhFuqgkWKr9%2BI3keRnY%2BE%2Fpodes5nPcQ8xE%2FnY0AiGr2%2FhmFTqs8Ro9YV8nRjX%2BV3EONMcQCRb3vXBJFjex%2FPcx0aMNUF1xugy65iJ03icbfQEqf487AWDZTiIx2%2FzX4w6X0z3SgGc6LXT9n4cHdEaFM%2B4NDF2bXgqkcIe9gEoJHh3YXIBRWvr2vb08zE4ZuFS3izTyW5iPomvIaAtWu1vpewFVp%2BkK%2BzGKPhMv%2BUydAg6EsxZYrnlW0x9bXMLt5wfZwRadwnhfPIf%2BAXturUrLkrDrFBn7KppKRcK2i9%2Fex8N8NOBDZCVML8LSwYIY7BE3OgWNFmXkip4XtZowGZ%2FRNG5GMN2Qvs0GOqUBUv5us9e3hpu9IRC2%2Bug7ub8p0rmCaEbq3jyFFzrRAH4ZcqcM4oFxastJmUSZCLk5jOWUvPg9XpRm%2FqB0RvBm887S7ppVIK1BLVh%2Fs2JfX2sMXiAr8vgKbPEMbdgw3YKoLd9AwFQlBqniVB%2FErXiANIAupATiprttUkcVTU2tJlTJVnNWWtx5ByRLJQOy%2BUrlLuq7dowlgCqOWkD87WVLZNEO%2BwYE&X-Amz-Signature=d031503a7f7723178002bc2550e3719ddfe612502538cb8675631e9976eeb62a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


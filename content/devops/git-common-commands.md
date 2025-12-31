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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QFSAHH%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEGMlY%2Fc0R36dXAsqZxjVAnUmpmbmkVdf5rnO9%2FiGNtgIhAIZCPPk2T%2FMZeoBURd6TLKSJm2OvKAigGsWkFoaWh0yfKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs6QARO0MACVMJTVwq3AMH%2B5R4YCg0xJDgcexuWRsgImMAy92St3qwp93ycQOb93%2FlH96af4Mv5sfTBMlHvOnX7SdVOAAZlmtd%2BefL7rg35%2FnfeDaIHPb9oVNrSEqtpsYUuWMb3ITYZp5numFz8JB34LEcVMlmH2pIoIS8ld3Z4%2B1TS%2FnwH5nqoOGGFYlsPVZgJY3Y4WgXMAvJuMa2jDIjx8CXS6BZYFemrUMmg20mv%2FuSVQ3TFTRSdEgJO0tNNZ6c5B1tnQknyu1dXZ0ceV5LIy4jvNyHPzq467ZUNW8dy%2FgiI57bBKh4Z0IKyJXiseG%2Fbcx9yOguh64YvfApa4L1Hm2jvbjHrEuhP2OkVuAqwKbUnuzS398Ps7GZLhWHx3LtrklRw%2FOAD%2Bm2dLPzw61sMLkgly5uPvKhZ4freKi79JrGwOc3BPIyn4SECMsn693ESzw69K%2BGs%2FczuGYcKwtmjYj8GplxIBX69d0VoIs%2B5dDmWvfSVi0fjdoYhgP8TY6ob%2Bn1mUA27qvWmOWBet4ONKr9GRvZoG9Af2eU2aCllTPhooEaPOe8FkKWFeiUaBKkdAhUL9SgKHqWNyGxn0Okf0P2uQhC24oDcHz7BJ7h1OCdmPqYvR0DTkT98YRdQvHmqEW6fPzSbRrC1TDT8NHKBjqkAcjx9XiNSkFJ7RyiD4NtMnjS%2BFEL%2BtaHOTu%2FdgM1eBFpGXxahdKEoVOYitSFJJk5WtlfRwI5tjEKvJDI2ZvMP7aSROoB0ypBTbEWy5BL15qLmIv34O%2FeXFaQkLmckGZPIcgO%2Flr0L0hU4lyiOzbulN1n7UVMBJ4FCV%2F%2FfqF3Fb1EOhqcuVu45ioZbmc%2FNsOcIyCfsyGs24iQnFDp0jETrd%2B4Ouyp&X-Amz-Signature=619bb9f0398dafa087ab3b8beb6c6b5f83f5ee18f3f0db739db6e477f5f4cc42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


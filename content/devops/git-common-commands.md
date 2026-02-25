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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U47TFNNU%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T034001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCqK98wO1itw3%2BSYBMM9C%2Bp5Q0E0%2BK9SpxHi6P8RMizJAIhANtDmVSiRknR8Qj8Ua42FFOnTl9f7%2B2EOsXevZOhF%2FsKKv8DCAIQABoMNjM3NDIzMTgzODA1IgxkS0uy7uvT7hRDD9Eq3AOTIiMzD2GlXb0lX2MILMxR1ZvswHmpGV4FODtidtB1iFnSKZLkVeBjxmr%2BUeFwh7HzXjn8DqxZQF9LKeM0P6BVyBtptZ4BLxQT0hnvCnbv85awhtv%2BjhaL%2FamIXL7sZuMKYdm7ovu1aDSInCVrH0LJXRiAjXKl0VtAauw68cRIvaJtDauZzyz%2FDNrOZwC9yC3ks9tN6jPWB60qUSSlNDqyuufOYkElZjnulc8HtrdVx7xG4gbT%2BhGf0H0JikHy1PAYs7YCxMJT2xeITGeLtrrS%2FCVj89NfxoyaWp8Vwpr7h1O3JdWv94CFMdyPBQMqVaHNy%2BskEBFg0%2FrLUILoIcVBucE0yte1%2B8Gw%2Fmn9QKfA%2FIVSmLs0vupJ7bte%2FiCuj9EWHthfKIF4TVJeOageLf8ipQ%2BqOOY5suBfsB5A%2BiCimdA5br0QOo9QcEQGi1V%2BTrcj68bJf1Kt3phN4rlgKXztRzSZO%2FO3R88UAhxg1G0%2BIN%2FuSSXEJjb2%2B1Voe2sM0GYEzD8OMQIIpW55BZGiHX4WZs%2B8%2BTECcERhmd6tBFRcnjgLosw83xXBYtu%2B9EH3HZ6Nb6vnuxHwlDc3jtEC3SBjDW3Laz8lXyMrDar5tVMBlcVcRIf%2BoSpQhXcHuzDZg%2FnMBjqkAWKJjVWkELecLc%2BHFdLpIElA8XB96f%2F0%2F8uli1oFcPU9L9VG3thim%2Bv3%2Fj6oAc3rlvXwJ4270TpBJnyBGWUW8kQQef%2BZTiE%2BHdGvUn2CUFwXnps%2FSPVY0uCgY4H0MUuuQOENmHOt%2Fpc3%2B24d%2FIO7rLvxmcfJwHcjkqM68mdD0QB65CbLY%2FZiW9Ky%2Bq0BEUUWhN6VugOTRQqbd2WZ%2FN5u%2FG9%2FSVOr&X-Amz-Signature=d1d25df8344eaf6512dad273d73f9366f4b3552ed881c5b908afa58cbf6f5b1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


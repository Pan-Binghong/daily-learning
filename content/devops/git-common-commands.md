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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFHOHHA%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuREvt5dMasHeXtGIDKRrsPFschbGPXXunpZ4o3VPtlwIhAOYWFZC7GfuDo3BBDrjQp7aUZ1dN4XwbGDzE4RGp%2Fb4UKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPd%2BsAyZuUfFw%2FTGcq3AMPuYTWlvSL00PKDK2jqdsYs5RztlnlwVaY79XttPxrSWLLWEXjzGfPHlPuT9YekVEpSX%2FfhV9ubagA6rKk1JWcfDetjgoCXcQHYQ257qMuFyjO3Q0SoOcHNSkZYK6z6Ze6zO%2Bduv%2FxizYUdM%2BxJpMO8UUzCpXsqIuMPVph8ept5Ms9snQkfYkHYhm1ZaLGshQW2yNjLYsLlG3Lf%2BgAtlLhpoS3Z6KAO%2BHTa%2BGp2Hzcc90n%2Fw8sx38a4FRvs0VeITnVwNYh2kw6mLw9YV3P%2BKNO14iR0tFyJp9GQWd9RaVxRXSPS6ZaOvUpN9eZZaFfYN4d6f3bfcEitP35Gi3jXdaaeoYwP66JOHAwKe6HeCjCLIRP69i8xJZorW%2FhUvTYUxvfBjN8UvzD1b56lnTYp1%2FDEk1ocE8H0VoLicknqsvOdKT1mYEsm%2FW78IjzaFEzEbBhWeqv1zjX3cv85InzOzpnOwUigOZ60D%2FjNfr4c6k1JK8fAaVy76JNm%2BekDcwNroYjLj%2BLFWqPOgdw8IWRw%2B4mOLae4CoDLQHRJNMQfTSzXNwGckIHNKBEs1lxhaP4zhUqmfLxnLEx%2B2LCl8nOi%2BdRCMTNBCn9l4ip8t7OUASufs4vfDKmHWXbp3w1ujD4jcLOBjqkAcGcuz1vtTri9fgwsRRtVypy4bYJaq19T6KLCuuoChvVONgPfjEOV1sTPWrWDEPJGEDilcqlR9wvM52NkW2oRUtNvg2d4KwiRiq%2BdOOhOaxO1OZ%2FASSSUU2MYZODcBhrtFIBUWSLXPncafN4aZaKrCuUARnBdYo6Cl7LKkZMlpgQEkJWqb%2BetTgCIKFxOwNIiJhJWHoxHXv1Bod5bK7q9u9RVUwX&X-Amz-Signature=22d2c0319ce2f54698e73c8a4cd79be31f9325530e20751a7c9074bf73ed5956&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


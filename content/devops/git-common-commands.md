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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPEZS5DO%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIGLO8EVi93udn3C4UKemYpmLixmYEIbUGTQvhNowZPkfAiBeN6Q0Is8xdulmzWxgxPdVJMvurgt8xfTDwXiW3%2Fjakir%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIM4f02ijxH8Y2UWhx3KtwDdd2SeNWGyE3%2BPdwIJgqyRowvZ1L6HhTHMHhne5NDIQ8KPvIqUnTVCgWe%2FfN2LzOaXASgacq%2FUgmvRItHmyyUDaj8Ft25PMQwq3arGRiwMqEm5dGRnxqR8jWuikpbtPouYirfE2MWM8CqwJZtLpo05y854%2BlEGOPvPYAL%2FdCnSdS4fevgm%2BzheuSox%2B06tzm5NtmfXx%2FbXkj7uk9Bsqhp8iBWGI79a69Cy3rD6Z0u90Sn1GeAd5FvuN05CRO1E3%2Bhw%2BP9jfH%2F98khrICTHF%2FG14XGS%2Bgq4DfOETRmaHLCRl70TqN5uxqP6XDbhWHnmjriywyAs3jFq%2BEbMC2MLiDBb4%2BKAj76oJzO3alXa%2F%2BEzxDdwxkeZXIJRHGlNc1nEFpjZoCSFE4305fI4Ln3Bmbk3ERBKPTWHuvHIWAwzj4UOIhpxdeuPGnujDPEcZYlnkD%2FLGGm0zwXWJ3Tomv8SddSK3TLOMYv6iqY5MfuZE%2FW62nKKpWuc3U8M2LwuBitjLkkwXSZgWQoFLJQlUALa4UaqLLFT391%2BFED%2BRe7ifMJHBfczvIMycctVL3cnLEvUy6fpRV40Q3Hb%2B1lwrwnxguDeZDPuOUTBXkc6muqOsare8b5vbxQro4AAkr%2FH0cwws7QywY6pgFq%2Bi2En0LlT7HR8Svt8xq1gaa%2FVqieAkPxgmSGq8ldg7ogEYFdwIn1kpadM14CVkor4j%2BDTsySF2cxYXTMB0Un6q8dMRJOfRK8jzk%2BY968Li5NKEN%2FAELRxMkUMy8yyYywkWmQUX9DS3kROT3vks4pUtFaA6DOxeMUXmkfftUXbJMa%2FdywTWkDjHltOl3pvzFYUJ%2B38a6Y461w8flqo4O4loNkBTQi&X-Amz-Signature=f4fbfddf6aead9518178617498f3ead991d4e60f5ed081bfd0d89f6cc2c83368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


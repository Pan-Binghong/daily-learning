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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOOEHWIZ%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDnnWlkl%2BM65X%2FVl7vRYhYdAPeGzdA4V2dFsyp1B45SdQIhAJGm%2BEGmxJ5VS1oSrNSht5QHCobSiyCDNQpNZhBGWxQAKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz37M%2BEdbK10jqHABcq3AOLeNor3zNG5CT23FmrFsWD2P3V%2BvJqrfG1pg4104xa94ROo3OuR9A0kArJ0RUGt%2FFC77ZBraU0luWupD6A1QE3cQOYSKjHtfl1ZWXZB60M1ZcfaQJHuCptoVJcXiYL2JIuet6mDBq9P9gdv1aktYhoiz%2BHznBeewZdiCFjdxpn7NPnOVaLn8CI3skw%2FeL%2FjIEYaP0qefpkXiYhzFb2n1rWq4o5HgHBLYhvjGNauIVAU1bS%2Fa0RjAQ5chDu6n%2B7n0WOYMhMsiq9w52uiK1j95s74sWakmlBFffA6jaur7AllCGSBu6Qqeq3rnxevuM4oJthQwJgSikL2qazWGA4RTfgSBxScp4EKm1IVV3Zltwu4N0SOYMpXokvItHS%2BZ4bvPf%2B%2FfPhm1c9THeUTorbBqsuchcvGI9gUyiVr39P5VXBj1kq2kaBusqgMxzG42o6HXs1kWozIsgFZNKsciJmTAm0cm2XUZy4cZAoSeMYUpG4%2BRqjZweDTjWJg3ZXfvxVq0ahRMVLyzhPaIDV1rQPHTunp2cx7M8RDeHCaVVi54YT2hXHX2B4qR6ee2JaD8Bi5l%2BlU9dDNUkwnCF9rGXi4fNRCRcroUczIXUTrMbnvphtC0VbFCxZdRCDZ%2FSX4jDO95DLBjqkAXoL2z5eJV3Weol6UOL7JI90LucZJCxUw9oqJfeW73edQWe2zloFmAN2JLKoczZhOfKEI02O8w089t%2FGjiBN803oMGIxSSg%2FgyPSyC%2BJ8mpz18%2BgRw2%2BBODIRDkcHEq68BXbWO99ckGPI%2FXJVRgJAvBObSs%2BpbGJGnrWkoaEu%2Fr6HuTlNhGtjtS6itXJgj7%2FAjcdStlWKBjkIj2g2K%2BUDoWUqG5w&X-Amz-Signature=4eee02494cac7a49b337fb944d29d7ec16b36fc9aa480a629c40d033e55af80c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


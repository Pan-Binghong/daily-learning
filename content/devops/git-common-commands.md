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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQWOUZAZ%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIFOn0f%2FpzAan6HYLatyfYTdVL8pRLCQQx1E2Fu2wF8YpAiEA%2F9HwkHnJALRyGTiWGbLAlJoGd5zysrx%2F6VP5lz0hq7Eq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDL3v%2FMllYjh5y%2BKiVircA4fVatEydo5zSqkwV43MsJKNpW0YAkdXF0f%2B89jscF71yJ%2BDJ1kYNR%2B7s8v8fyCyPqCiIFCQDQEoLTx2mU%2FElRCFdx5S2Midk4LwstKmGi2%2FkiF%2BRe0WUNyQT5TcuG%2BvfKJVOwW%2BVscegNrdvWuQ1lGtlmns%2BCi%2FL5dl%2BGNArehpmfWRGg4Qmf17gFjpPjBhotiPzRzzplX4WPG4h9%2FV9ACSPoe97T%2B2IjfAprP7qPruyGcc1R%2BHA%2B8s1ZgabTPnBtvX7rh1hO8Cdhutto30XLqLbJWuP%2Bmv%2B0NlAo4vBrY4bLs5etc6XaCmrNVZGrP7ld9GXMNPApi27ao6nKmZWSWDhGN1cEHzA5lIXRnl%2BHLzLqQNsKczHrAQYzkYa2oDTIz%2Fwd1CO9sq0OghnhZEf4SQSNtz4bsOJM651sAng4AEaJ%2FPo5WMaTtJzE%2FiPenOCmjVMiw%2BFpIIh11G0zlwb1AYk8jG0B%2F8f7LOHIfGGFVa5bwa1MqpaWt3qL2wufqyc5Sw50OuCjeAvsIlLQZEWnz6Z1MaAi4EgZyfRWOqSM4u3RZ78%2BHhGnTuWb2or3esFR504egf%2FJI3BY7dLcfzd%2BIMdwhVLO8UocPvbpViGbEuTwTHqik2uYZLM5sGMKrH7c0GOqUBAMcTNUyPboQMtd%2FoxXIcWPED4UqnBA3ouwvZv59LXUOI1vfuKNRv7w2c12c8jLt8ZdXJ8VlqzAsVWBhKzY9yOX%2BoNw2hRyqF5lqLttuHGlaAFQCB2DVkDZilpDDjeYR%2FGvpycde1ar6CTKbi4K9YkqnkHPKMKV2ZaTGD5pfxhu6kf78lodLLKyNISDp1lhyqbk7Oe9E5ZwV8zlThLJMD3WEvUG7f&X-Amz-Signature=77013b35b61e4497a7c04da189250bec370571656c60eb1e981f5420932d37e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


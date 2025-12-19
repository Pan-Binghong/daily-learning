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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466253O4HWX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdfy%2FESM7VUPi7wNNcfuFAU2fUajfPtbn1JS7ZmLPMiAiBDj1U28yyROHwvSX0KmWMLAP65L4FiG3Jra%2Fyk4oFj0SqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVLaxowVqNInOlYViKtwD2VqeAOQCDf9nRTjOtmYNOnIYh7zsKCBfIupVyxBs8RRwsyiahSi6TzGLq8VuI%2B1Mm%2BLmBd3O1%2Fkx4J9IN0%2B9tXH2MV7fK0hG2ss3wzEseSLGGuB8NjkWr4LCDZ2CjnMBwNpNqlBXoTYt2kIrRVs%2B%2FkSqgGeT5l9WedWjmDfQu7%2FkzINRD5rfHQVedqiupxoD98hLGV4CUj4UiTGSawBfCwywhag37dA7nHl0mFE9%2F2ztIgapxzbE%2Blr43ZHLFbfGMFEYaifUUJNA1Dd6dXigUhCfxgJF8dF1uKzUst%2B8uL%2BHoAld33PcphkPoJ5rKxNsoVH1a8MnTdxvNstTYRy7jGSxVBkR6mIufrVmSGPryEhIF4veuaOsKQPBke3ePKZ%2BrpbX78PSXJZOxXGYj76MLVLK0xSVv5U6s1sMJWijwvlQtOe0ifVS%2FA3UgLaf7TRTK5Ufz8l7hS7phePT1O2s7caVYHxpQhY5raLvmd4iDOx4HdTsL7TWtZfbh9v3B1HR08FZ%2B2N08udHKfz9jWLb%2BK9BCs7p%2FTuslmoLtSezENLfM5ZJBw%2Bk%2BoKdZNRVJCK%2B9LHmmrDJSKBaN%2FwrSvORmrqxugfmC8OxjSoQUKR4IJm065QpQEatj8zczxMwvuGSygY6pgGIcb83OkD9MOP0Frvlb%2Bjn9EISs05uOp0Kpp3OYtmOheiSML3QsE1g8Xoq0CrE%2FvOZEC9unum1q2tTNbPlh%2FFgNdbfh2ICE6HnESMieZISqM9olkYIs1CawdEKu4VUNHb%2FTjxxAebYYP4SDGm3d925N9v%2BKryX2b5mSOCdoQCoTJIno02fQQASWhi53M9MSOkR2GWXJvHAFD%2BH00VpquN2F2OYDczm&X-Amz-Signature=08e8338222c364de47cf3de596292b61c702ed83568c88ba34bbd37c5af5cd74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


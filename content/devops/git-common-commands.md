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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZSZK7O5%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCID5wBWtUQVT8fRwcP%2B6oVaMWM2Hv%2F5huIV8CyKMx7phxAiAJrvNpzLoy2s1BywRZ8F9zd2mzTT1bImNMKsIejClKMir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMkRIITbU6kXRYZDNNKtwDS2x5iyU5PUE%2B1x3ShjOThubaYzUfG%2FV2qvaye3H8%2F96%2FBttWAqXRFZgcn1xwKSce9Hh1bJ4b6oPzuaH54MHKhECKYeAk8nSMlfQZVdQRY9mB%2BGTLDYgZVzkfCuZd0SUGk046zBrl3%2Bg6fyAhFjXIgtFJsFmqoQ6tmi5mpy248aEJvOU6E1svM%2FEUegMlQUfpW20ov%2FMVUqBS6SDC0l7mCqfpH4GcyMIClU0BQu%2FIMWJk3YLPBnXtWdQGM0ZDoLqvVrtj01fadsIQOJbDpBgeCdWSAbLecq%2BF8ZcCNinuz0H%2BfEKwejh7v%2BwHBMPCIHiFq0nEvR7TACUi5GS7yAWIW3h8vRexmRJpO8ZJoz8%2FlXhqCuNibB%2Fa30eUxJwNNK7mfqFuHpulzcSuoJ8L1YSTC1LRcB%2Fm5auQFOj%2FTfbNDkwDkIrotfmAuvtHry6uULGIIoi2qsZU9MPeGOaxvpDOI8fLZL5yTlEQz5DecyNiaQd2CUEF%2B4Cp5SCPEcnCdHAjvMG4RIjKmN1pVwyMlCNNllt%2FbqzN%2BvVj90ZfwMMwddYF%2Fy8fndeCdZc7SCHOVsPS1vtCAncFS4KBFdXDmUdZuT19wGfI%2BujcLjKDx49t3jL%2F3R1T%2BN4Cgaz2gPow99r8yQY6pgE%2BbVC4F5Atp5p2Db4hKZ5J4amWPUS99%2FnFur68nzXUQUK39pcdL5Xo7Xf%2Bkyh5cCdQch2D5uQquhUDnF%2B0XnzYJpnerCwSw6%2Bw1ze5WvOUxpu72Ly305A8tvWgNkKxKHfY1riAESIDyQXUF7cYZoKLGBhYRK32LLFMulybqaklTXgPwDcSO5yH8dxexBPlUMvm9E85h4VrYV5xNkqVATTf4kkzKwSF&X-Amz-Signature=69220f0793209bbeecc85497830b9d4c7973ddf535af9a50498943b2a3ec26ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


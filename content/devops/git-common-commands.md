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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7RGPQA6%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdB3JrcPZRQ1f18l4astmgeAgu9RAfJRIHKsv1XeQGywIhAOSa3fWI0GPimvX92WcQJHl3MWHMIWQglb4%2FGPQ4sVzLKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6%2BgQvx1o5n5c1Y3Qq3AOKfu%2BovB2%2Ff9gbO1HELnvxVmzwNYo%2FCB4CZ0fj0NFnW8%2Bzc6Oe7Fq9ZChbU5gagO%2FY%2FEhM2BIQ6svY0yjAVD3wobHSDPk0MeBtKQPAdf48ZMfPfsJaLKjFsOLMtfvgsJY3aNgsUH462lXdKDvGaA4m1sxF14rrDxDhq9HvxBtHizf8LCIfDWDqXW%2FTF2p99BoVXVabEMc6iPD70SHwfueWgT79KszW0x16w2jISAMcjYSD1eFWoJyN7FIdJmeOUFrWQ%2Bn%2ByhnmoB4vrLJbwcR8UeTpwOmNJasjf3LQhYiVfKiF%2Fez1L3MZjzkf6aEmnB9Aqbvk3dQzZFBc5bbOPbkBjV9BjofgyXRmIB4meeCMyMyeiwGmNBQ6JnEbQbypPj%2FZjyei0nkJKlndarEfpqLBY1xEmXOdhVq0EW1jFlyOwXI4wuWF1gvdo401djaKYzxSTPpgh1MunTobvCsBkjEMKVv381REhVfVU3VWzyQZ40wjC3FpV5ie1FgUceQrIgnWsrrycETG4rhcak5QGNAUXB82tQGyYzOvrHM%2B0WW3W7Yl4sj0YwEvKNpoWOiwccOyFN3dqMrs89kVjVlP78%2FX%2BNP7GOf0RtXdFYVuEIbNxcPH28oMGTW8V1KlJTCoxIHLBjqkAURfF7HT7quAGy3%2Bb4lnAqVX3banNU86FrzC5hPIcE7eLt0V6dQlXhoZq2L7rvQa%2FK2aKRfVtszr44SEbYVSgHy6FtdboRtINcV7lr8qxD74qMCp05a8RNFc4AAvwaUbpn1TYoyEppkKay5YHwliknj3BPoAJvV6X%2FMJDZUx5QizTyYg4QZETbrgP%2FcHNz00HULPjMFZl9RVvCooSet3xf8heH8u&X-Amz-Signature=49287e3aa905eaf0ab1a9e16821ee10385578834a9953e9ad4211778f2907d08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


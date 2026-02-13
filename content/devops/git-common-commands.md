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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUXL7OZP%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDHRed45SEoGEyWTII%2Bz72pJiF%2Ftn90qNp7mFhuQYjFGwIgblXDp9YDDyxkXHjTBh4icFT7VZuBVoHKK9FxVebKLM4qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgzjCvbifiTPjh%2BbyrcA997A%2Be5Z9W4uK%2F%2F1RqS1hrE0%2FMZhnrf8zyyNtLAFNdn%2FqDV1yzxjKCFCdsVJJLSY%2ByuRMkUWQm19gTKluh%2FfTBqEUUfjxRG4zCIFl1R4JxfzyVtp0pnFjWgUaW4nN83mBrwUxciD4NwogIRQgoR28D%2FT0CB941mKBGsPxIz41UDpDMCw%2Bz9ogrsYWCPVwR7NbNHR0S75Vaxzr71OLgBiC9kmHQK1zX6SS5%2FCfYq33Wo0HUQPYkiwnqgmChIdrAWbaExVOESZlwO%2F%2F6vmBshMIlWD2RHiJEQ1dbAvGbo%2FdQKBloD0cHkBkMsTHi%2FjXubL0rFVDo5K%2F2VmsjP7ZqaJzeDo5n8UN23%2B61LkYRpQOm6710DNneXaiCQ58nALUBW%2Fyu%2FEOP1ONlPoLJi%2F0rRQdq5pH1GE5MfaepOczd18M%2BZz4liuKIOjsWh9C%2FdZFIuWz514M0ak%2BwCkE%2BHKxBdd26z%2FtkmLr5e%2BkMRiNGwJl7IUVZkiiDFfmfT0pgZ4uRxWG2H7pQwOdtsnvZwWkNASarZ8QtOZAIw0IF1P%2F%2B0mQNLDba9RF7%2Fh1QUlBujRr7%2F%2Bro9baKJ4AbF3bBmng0%2Bg78YQrd81sLzm7lxiLHZyO%2BjgKPIRLwqriP7NC79MO%2B5uswGOqUB%2F0xtgXoNzC9JY7pHjLHEXp1N2yX%2FY0MFNWPng0JVievTCCcRxWAxLNexBT2wnuNs2H8LjWAFy8Lw69ObshCNmqw5dc2O8KCU9Fh7dKjluv9QXXWZmcLgHEHm3kcPX2ELxBofkiJC9NmmWYz5GrrRPWW0ngOVjv7ctQ3V9iW2pTo1%2BOmwBSTKJzHFFQGYk95exLm1UgAvo8CNxM1e5MGzSthYh6PF&X-Amz-Signature=162a415e0e0ff5f56817382365be109c208a123d491c50890e88b71fb487a0f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


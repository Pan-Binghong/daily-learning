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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KRQBB6T%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQDgngvBzr013Uqe%2BhQkLoASmEl4%2Fr5FDuTox%2B%2BKW92IawIgTN9cjKDXDOAklIJQPvnCGyujaLbhzyVlVsnLqiBnpqoq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDA87bovTmLCwe%2F6KyCrcA3FeAsVPKHlzU8uQy%2FxMK4305A%2F5mk59OE3mYqInKgYy059FACeCqhzXNYesGsB5fMzKVThAAForE%2FswpBaJ3PSjZ%2Bg0wP7X0zfsZQ6my%2FwH95TG0%2Bwjsu8FH6JkBb4%2BmweNo%2FrVKKk4VfR5jEoDrnlI9PFVgiviQB5YEZ%2FVKf4wb5SU4YEl4BG%2FrCdlhGxcfSWywHegD2TVJiI7CyEIVBGf%2BKypHw1jgZGhlN%2BsHpF6ef7XFj66evEtnEbzO%2B10IAiDv7eODf9lzcMW%2F96FHaPtj4ZFq5BwUdG3flU49p7ZVcHQ%2F9dBuhXYscDRfNOYQrl9CdVoEtNXS06igS12H37R2Guot%2FRIPobOf6PoYPfh2FAa4ITRvhvf6b9AiK9G3Yn%2Bbypj2w7QJm8pOSOyuHdM7rkOhyQlT8d2XrMsaWO%2BNCeWgJgfMf62sFOkAHxlAUfIECCBtvGmWwuPLihoQ9d1ipF8Hc62siioMuBVQfsJCREF8IngtyfN00eevzNZuxnN7mGICiscjxTfeesu58MjdTyQoz9mL7zKoBpVV%2BrJYistf%2Fzp1ZnKN7Lq7QJyimwjG%2BviAeTs11pPCm1Z3TqVpMOgrirCl8B4kLlK1qXip7G8OK7fcZIePXCVMI2UyswGOqUBi6oYM2cFFmVq1HBvaLI9xrfVgEL3A49dhA7sLv0BdJnpdPC5fmGgAwlDRpt469J9VuH4iql8uJ2ftNzdq75HKFrBtm3PsboaJlYlZD2qc15BVq512cwzNTiKsbnjHLdpGuJ%2BXAk%2BWt%2BRZZjEkWAIdH1UtBXQLDw4F6Re%2Bqc0GSB3XoEl5WhIOQgjspULMVHaOg2fFj48i3rknB%2FQFn9F2tHw0HFN&X-Amz-Signature=c2d4ac25c4b1c5de05ad2decaf2cb449f404d613900b56623ffe725a1522d90b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


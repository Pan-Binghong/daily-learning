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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3WSU6A%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZNRTkRbgvziauDce8DttDFVYvquZeNB%2FF%2F1wjwwgexwIhALnhuI0b9wfX6SLLcrDPrDtaXVRbeTyzViJAwfmqPeOUKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsQy%2Fca7%2Fvm%2FeaPRgq3ANW3ze5dPz%2FVCecwvjjOI55DH%2BBNEToo%2B81%2FFh%2B4Xl2NKR7SAgGLiNkh7fZACLVlqtBL6ub72qT0gPxhUjcccP2Cl61S9CR6j%2FHNvVbyVSLxvgqHTrydPfoR%2BROyqxCaFlPeucY2IKd5M7xD01YEEIsxIpyAWsgH87HEI%2FSS1ACDZMt3dT%2BKdsNj4uiMK394a%2FYxEpWjU8OIuvDqS41MDn6W8YH5e%2F1Une4MELIm%2B%2F1Lnc0wzI0tek3eMWMSzZqDyrj1bFIN68fcA7AwlCCjkOnNer7IcrjrQQJaOGb9oFIvoDn%2F6xoWJttNu5QsbudOpB3r9WDWFWOOPX4MzhYwkDkqW71LxNnB3MVOvrefLD9eJpHjixvvvk7GUyRJ0vf7q%2F6Xn3UnFxbG7RojAC0yVfP7cGT9gBpvNelCfqAjxc8cSDHy9bWuRYyxoWIhovyqBw6eECgG2oRqSbrsuwaLRZytxexSG6mjkAG5TLlXD3qahWdHuTUDaqbAP7PopyhXQuWfUt%2BHwv1ebmEDk0S3YGoaoMkoz%2F2ZmU3MV3VzijBtKo1F1yVG390djFuxoe5G0tjwJmBTyMA%2BD5Xh%2FHJd7GMjEKbPTxk9umnbR%2Bc9XNDfgZ%2BaT%2FughjyTAvGfDD94OTIBjqkAWK6lMaQ1OMmi%2F3x9OoijwluieTKlZ479%2FS2CdLc76wobxXJqKTdITiy9WAWgabd3xLODloBBDxPlJDpVX7QBfBrdS4pSqRjFFvW1sEUFT1eXTDvyiWGoj1ROO%2FwzbShDBQQeWXjL0Q9vyNy2H4LhUNCrA2C8chddjyY8VlETgZryVrQC%2BBLOaWmM2MnkFbV%2BNibXuYpjYh9%2BUw8v5qrXcd%2BzEVw&X-Amz-Signature=adbe790f05d17e04872e975dc05716610c3ada0e095303b10643718f10088cb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJOMWUZJ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6u5B%2BxZfBxQU2DWsLS8jQJ42hbkwwSvYVJZ63nMDeawIgNQLL%2BnXdU9vPvUx1sIA86l8vXLNmGB2JIm0bvmkk%2Bdkq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDEGHIS2GVNmJ3pL4MSrcAwC0dUTxhj2v2%2FumDgfjuTkLFlxKB%2BijNShm2CtLyOhdZf7TeWlW2H5PkiBZXc03UY4u3SCRywwGiIiMKcTihFlF93wCR2e23Kt6W4n28I19fZGOMLizHc7AmwIbKeMw%2FWTrbzSNXRejxs3X6DlOZpQFTUQOiWiPIu%2BwhCMKWIhT9ShRd2dZxH6zkymX%2FF%2FtHLrTBvQgSje78H7dk%2BkM8HbQwl09e%2Fcny5KdJaONX2EdI9E2IU4k6spjXhhJ94dPnyx1TPzrg8XikkS4yckMPGG4xE1%2BTOZ6iwABhWIlPNOu6NjnUdHs8XMe8Syymu%2B8PR4i%2F23kcyI98vCYBTkdlMDAfIkBXvVv0sTYJcxl8MWQ8rb5zler5zE34CMAFRG%2BUMna9d7wfA%2Bxf6aTejUNsPx9V5lxaixVnPECoM55C68t5rqvHaOfHjEU0mr1Q9pVz1T1ntnkAwpxTaHskYoBSMKupHOUpc7vZLGCz%2F4DcOWrWRW9%2BcS%2FPRwNq5OIgiLzrYzPk%2BHOjV%2FpXTEWNpnDb%2BsXJJvzlGD0GoWVDl2hl8rp7lSRkqzeUYeyOPgmnfwgOKFKOwnesWpcXXArhsYVoDC%2BJK79BUoYjVLs5KyviZjCg%2BczxB7A9g2mOUOkMN%2Fq8coGOqUBy4tFAxXX1GT7uFd3Cd25GtC%2BfnG2P6%2BEvpwcd0DNTjroRRRzCJV5CrYId3Qz%2BCsbr%2BujQBhbsxtrQSntVYdEJhQFRwtBGidQ1VByUVyuYY5VihRmZEDMBcqm6KYlxRC0z33FsIS8j6sniSDLYj0o3B0CpTC1bJ3griVEJbLrYjGALRrvm6Lzfjj2TEMvToH5K4SA3NkVM9dtaUQUk1%2FX4z%2FRFD4x&X-Amz-Signature=1704dfbedfc29b95fe567721e996ba61ae91b0733a546dca5fd31c594800e2fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


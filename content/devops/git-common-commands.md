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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQ7N2QJ4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIFItfibUV%2Bq%2B1tG%2Fvdw09RKR1ce2Np8RR7mZA6YHUdq%2FAiEA8P1CVil%2Fcz9NyMjX9HNGHmq2MNXvrLtwhbxg7NssAUsqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHhJ8Ksubgd7gs602SrcA7BYAaI%2B8rVMJfuvpebZ71hx4uac4uUsYfk%2BiYKytSHHY61yL1uoa0Me2x%2B4kk5BaUj0ZaGTdV1HMNvRLXAg60zFb%2BHnIKWPUh1MgDAQJH7KxA51RGzCATa32Q6hPHXz1PshT6pEh19FoGo733fZQ%2F0bRGXW7JFL%2FWOdFr4QHsjnmRyWS8rZakn%2B60f1MsO6jKvLucS%2Bagm0stG6BLxRy%2BgSDxYaQfnv5%2BVFZca7hpEdOCZXh%2BxS%2Fa7vpNWnzRFaMQ6A8ViFYMGT2FzA47PdtgXiTUs%2B9VQQoDmlgVoXbLKOqxajD1xEL%2Bm%2FDwSwOOaoXoADBTtdsJmniuvthfJnSlyLwp7MMzk4uhNQoPqpcy%2BH3DGtBbCVR4h950T33p0%2Fydg8GOlaK179h8mKonUX7fqG1JkjI%2B7qbpB%2BwksFHCC1TdMZpsy1R%2BHTXsaVaPoEMvUAsvW0ONNVaN9uLYMb%2FHad2xiCJ5EbhMRQdCCaUJ30%2FrRiW7r7EhCiQm3Hw%2BNVRziwxwUdaKepkcKLJiZXjy8c10N50u0tEFVyZuNHITkVxtnezreQdx%2FG7zdmq2rjPNB7EUYbdq8MMPBLpf6FN9VtHpxjZXSiqqwZWu5TOQ2PpDLkKSlMKwiaxsCOMPK%2F48kGOqUBIU4e1mbcDanB2QMORk18tye7on5NUmiHZy0AyTTer2vHaLVRxI%2BoDGdtCFjvBVqdyLpn5xKTlq0dmqrd3%2BLGPiclVQrY%2BXSsmxpn5CzYvjoxAsdZ7UciyWUoW7JXwmiNe5s8xR0N%2F1PWTuPsNl7gQvrTqy%2BHWAgTTVtqHFnGJnFcXx4yOnBQ4ptCL4sav47tAg%2FiQ6ztyTt8aEOmajYRrPPVoz3o&X-Amz-Signature=82724929d2bd050744a5520b65372e8df37a6015805eecf956365982a0fe53d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


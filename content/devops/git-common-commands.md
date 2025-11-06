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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB5E473R%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUKV0qdV7aUngoykPtASaxZkwhIZt3tQ%2FuEqGip7TduAiEA9TPDLkj4OeiTb2bnTc4E4ApRgpxHbdFFVkkarIF%2FtlAqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiahPKz%2Bz1icguCwSrcAwvytom71fTZ5qucr%2FygLC9elY71yyHVRp5s1Xh2vpwnhvIQKh5Kh5xuKmF4e4C%2F%2FhhMpD5cbNs0G3QpQ%2F1%2FCabahYwS%2F8JPvUhJtFb%2F0KaUEkamSO05Z6%2BwZWx2KzFkXP%2BaDvak8k7kaJnLQIeb7%2BdOvS2lyrUEJ6SMnsjIrPv0ZkO76kbFJEgXBLirdC3wxoXuAsu9Xu4tTUYA58kY1VgqfRJTJlJOwgwAd35ZQFdSfntRxW0qetXpdw1MugyUYTOGUq3V87TOIzK5RfjcR1yAFmr9UCODXvJ0KbtcfM4K1RANP8i%2BRh5EZ%2FzRgsW3jUzQ%2BiAsChD1oM1eHhX9kLhIy9jrJKxr%2B6U4NJ%2FtT3Cx78qSJp5LA5nm9m6ztCka4%2F%2F4%2F6XiDHw6QqBEpG7HC%2FD2uctauDZepsLGyAbq3dj1sqY2onoPSjj6CIxyWcR%2F%2Faz67YglyMZnf%2FkdZwAE%2FvjtgdHpqUX5U1ODBcKbpIPdDFZQrdd9bDRFNnpG1KxWiDl7%2FXSyhRbcfG%2B9ETJYmi9xAwnguCiKdxDbg4LIECdVj6eq9f9Hh0Q140%2FZ1oJhvA3ufXYsQdainYVsGgEcVX30N7ne6f5r5u7fM31KTLbagzCVpC28g2VtufsxMIDyr8gGOqUBmOJ4KXMD59uKZ1HZJAm6AtPgY71fuB3eAA2S%2BZp3kaEFqy%2BlZwG3PNsuwcPiVncqO8ZrMMpOf9GvNbdMka59O8Y%2FB3%2BvfXv19afrLs7MiMa84s1v1oS8bxhClr1FY615Gy4M0IMnVaRzfnMIXyFDpUr8XY6CMSJofjkBKnpConsZDT8hnifUGYTzFoXx7DehSCP8Xjk9mcPEmU8d8iIkx162HxF3&X-Amz-Signature=2d95327837cee09b702a2e2202daa8ad85a53dd8f6ae59a426b45ab823318f89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


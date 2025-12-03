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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466254SEPUT%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T025002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQCRg7mJOj5m5jZ%2BN0ZQO8KHJDW2yP3DeDEGY5v46FLQzwIgJuEWIqRTykxcN99EuIoHkAh0mf7l1%2FKiPYhnv25PEm8q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDKXbvRY8mua4aQhM1yrcA79M6RmknXcLDU%2BE286qiN4JkdC%2FpQwLVC8LpCBa3i7RpTyjtAbHAmksywCGyXu6Yf7jB5cEtDO1QlX6hhsZQ98pyoaIwbT7q7ZhUdyHWDabUG0KxeHJMWEDM5X%2BpIFVrPmKRthL4RcmZ8%2BkC4KSCnVkQCKpwcHtCD4DFb4Wifj0NaN9jLYu6wC5iQlGxT3xA02LmtZ%2BacanmEDK2klAt%2FIy6R5uYdIY9kt1yprLiz6dajRwbun9Jz3pj7wtmUxDPQbBIvvkOPIBjeVB6lRiMedZIPCFuSx2%2B9NMZkHaQcFtTOfVnJancrW1dq%2FlZhAqLaqaVjIsqJWi%2BD%2F7ULT3j2R%2FHTBsWgOopTWc76qPfYsM4kbxC7xgRT1M58TOv0cVo7Woc4t6e%2BUYn6muNNJ6V9bqtuwyYS91rdIpk8XD4qOpVf%2Bl6A8G0Le93oXUDbSHCxwZZeYIj0SNsbMTlclJ3KtiB%2Br9ubMrYpCcKWGER%2FcuhLVuq7Dfo%2BLQxXN3rnl%2BEp4vmy%2FxuVnQ0yLLedBihgGVx6c7iaHWDfGZTmk9PD7kiHuuiO9ASsJXI1wpNpLCBHYtbTL8tPR8xyctt6M8hcMMBUMCwvIvyImBQqq4Dw9LGHGgx8RBA%2FymEmAiMLaUvskGOqUB3oZXnre4386UwtCW%2FicqoBlZSGNtEeqSFXtEgfwHjD%2F80JYx5qVixjh1q973oVLfmNJYsmmao5mCSXZJL%2F7hDmzI2MeVbY3%2FJG1nrWKo0I3KoQ1728c%2F1v4moUjmcX%2F0I6SbiqDIjMJiZgCHM4qG8M2Gxn5d%2B%2FLbjb7stl8rcxvuZsZmi8hKT47MRYT8bJpRPJMGoG0iANpaJ%2FAGeV1oPRZTTIc9&X-Amz-Signature=a7615dd2dc5e4e7f837ff51cf1dc16691b6b363b896e4a01c618b9452c799b97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


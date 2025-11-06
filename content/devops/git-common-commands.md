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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=6e9f6d2820e294e7992edeb1211679908cca8b9750a27577d31e39369366cc68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


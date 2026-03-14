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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663INCF7L6%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCynSsTCaUChguvXny8byrxHxpYW9rlSnuXTRHyEU9TUgIgMc4rebYOUcF2S33twOfaXji3rwMXtUlZxF7MhEKwO58qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkPZOdrGWQN913FqCrcA%2BNgA%2BYsA2tn%2BMjqw5yv3c9soooQnl7Nn%2FDsIuTOzxQDCRnjIo34p89igc7rLHTm6hDRW5tVGglzdn9EiHSRvL6b4dM1RF6YsKCeEo%2FLGExvrB7BLI%2BxIjFL%2FgtGzzLOFgvkXCt01%2BzW%2FjyIY8PsN9VJxNOu4eXO0RLDENuLLU7%2BAIjsWcWiqN58vhKtxJp%2FpPdiUpfRfZqY2ZO2zucA591cQOQftiWvdfBq4%2Fg0lXhb8%2FQXWya9YFLsONnANlhFHZYtXkZeQitSjPYPdA1WAtbUw%2F%2F1Xi74nsQ3HKxtnEX9%2BoMn7sPEWeXxeDDdnj7GUb%2BToG%2BITLmwO7yFo93uKMqzCa9fNaZSC4LqDU%2BkGgrkKLe1wpP7%2BrYTeifP0K372Rwfqoz2MaorYtsLmyaukZO2kdQZRSmoAsjUYbzK%2BpwrW1%2BGdgwgSklGTt7i%2BhBmnx6v271mZ5pmWXdGEz4X2DPUaJ4S1yACUPVxaApzi9hPLZuPKPB%2FnL3DAiCHLJu5pEGPv9upB16MK%2Brf4xtHeFViI191xirPtDnEDaVrxzNDUR%2F7iuyy%2FJObN6E45kHcmBkIn3MQWBZ391YNB1l1LTD6bMutnzgg2tcAPpxb0xWEsgf042lrL3eiYDfGMMaC080GOqUBdoHI%2FsS8nGGqeq0PzOifMUThFmHo48lNHJjBMU8XWIQYOQQf6%2FNCohT4AbdvP99nTTV3%2FnNGGqnXGtNkhj4CGRVnRFwoc%2BpWJ4HN7NgXN0l%2BRRDysxBjDiijkPf0TgZIL3FYLSZDKzoaYxKNDEhlYMAnpVxRMVtkR213HBfOihxzn9hWYHB53mqzc%2Bd1uZE00wmRylavEZIkvJZB3jKMvznidmDb&X-Amz-Signature=2dc5f6d894fe03e972f704323355f28b30e07de6d5f200c9ce90e8e406c4c796&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEBSAJFB%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDuRlXlFM4gcvnYmI4UBP%2FWGME%2Bk5BL73UrOzYNSMi9cAiB5NiY1Sb3DN6sVbwaRn0DsG%2BT46PirOoTxE0leuI5RqyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwljGsJL5cyTZX299KtwDWUvtROa7kBNk6NWqM1pS2JycQkGYzAVb8SGE37GR1DGGp89ogWq4HJsE6aeBX4631hozCazMCGvilXigiSMvkEaax%2BXSZlaHJra8LSnQQ0Sh6PqCO%2F%2FjlDj3RyzjaGGNM3Ch7f0aRDSwIKYrslQY3T2aSmMe74F5oEvycsZdSuNe%2B1paSh5Czc4YHbMMofMYSq6V%2Fiqhy%2FjzC05fcuDmQy82MQ0MjG1niWk%2F7mMAGBZZptAjUEEpiEWwZkwLFOq7bMBqgBrxEkTokjqvMDMttPFbywc7wRFhQ3XuB3FPaTLDt%2FlLMfKO%2Fa8e3TqDMEuTfZJ899tHcT9rQ3NBpMnMLMYqw7ZNjCLjBeoQ3QbbZ%2FUq9aPJTKl7QcZA3xNX58YVuW3zhYD4iiSgIjp8jG4ZhP2dJUoJgYIvYY4ANWDnPXEJ02%2FagLQw0qMTmfaFe%2BAWYzBm993nSrfXTGe6xKLRWBBv8I0hDeSuzHqWN%2BSwATxEVMxeU6u0v47pjDZMk5dkwkzzozqU8PKo19a4bS%2FPU%2BRFRSw6JNE%2FPK5uux0m2XiENrWfzqqBxKPwYm5jOEM%2FqVA2JIUa3hvpsOlWXRwPC8jJlL4q%2F3h47NnfO%2BOYUSpXQPOtHl25aHDndLkwlJX8zgY6pgHHvRH0xmg5gsqmTdpGMJ43hx%2By6QW0sOwU9orDNsSa2aPKh7%2FRvI1wtON%2Brf%2B7JQ%2Fx%2FVL62J35QfM%2FPf1B2w5yfSn092Ay0i3vYPRL6iYTea7qNjs%2BlvTJLKs7j4TnG7hSpEim5o8WF%2F5W9Z7sIGlPBLaX97L6YNDUdY%2Fd%2BqQCq9KlQqWCDB7JQPtuXYYo4s6vVL67SbEdF%2F19LWROgbp16YEYhhs3&X-Amz-Signature=5712dffcfe49abd52bafd44ecd97bc4613b4499247ca8855a2b60af60cb27be7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


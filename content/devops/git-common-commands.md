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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNRWVVGC%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFgzEj%2F89D32d9UweVh6sNSVzBqisUOlzWzKW%2BODhdbwAiEAvLjYT%2BSLgeR1BJ0Vv7QJsDJtFvySEywkCzMwe%2Blc4XUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJVXnynFr4oJHiXnDSrcA3kXpf2e3bNttZDgRDYUtF8ez2hFUY6Og6THszjL411%2BTXEcUifIDm5pVl6r%2FmO1JiQ9ar0aYv2a1DscckMWnVNBF2c3TrmoHTswF9VE7rTg1Gw1a5OYIongSTf2SUQ0aZm3LF6TfJYtoxMN6nkvDJDUGJKdcXhxfiwFj08I%2F6%2F1%2F4x9GIUABZ5hehcpSPGXDGaAwbKxgQ4lqdHRW%2FRWZ5Wrqj%2FpgZQPhYnSTaC1JLUXGWZIwraWcg3dHotxqZ%2F0WmMKS8bzcas5CzJeQpeA36I8IMZwSnpztBOSS9zjCf4kN9gGdDPv8OVzsap51gI7Om%2Fvg7JALVCD8QDnPJ3c8h0KGwQYZTEkpDzpT3dst144bKUFDSov%2FhLnnDn55%2BB%2FknRxmn4z0EDQrrHfSLyq0NucPi0ED0moUjSuDARuJ7aGIwI2ZxJzE0HZDuABJlXhhjh3wQZ9gFfwzuOi9tXl0j8gdGod8lG%2BwlT3KN9giSjKHIXdANZPvGTCQDnUC97DmvYXXkQf%2Bvj1B4XfPT5miHowH5nZLqbSKru6uq5C0V2wgys%2BaVEyh0j%2BVk1B46MIVoU%2FSBlgg43aNcIGBqEbmTlY17%2Fy4sg7PTDBm332R%2ByuT8Zh2ZxZ7gykP5OXMNf1o8kGOqUBs07WfHYtHb%2Bm18Y4oXOGqt%2BdyLEmix%2Fwln9YdUI%2FQ9yqrwokViiVDsz%2F5QxDIuFi3cb4HVJhpmqam%2F%2FnuTcZe3SYq3btR26W%2FMPvIIWK40RYiF0l3moFpLFMJJHGSgeuvSiqjsrDeK7vSoc6zInDM7nf35s8yuV7OtA5tGbrQi3ELyZOMQvhFIiXkZkILAarHfekrgsrY8a7SeFlM0OiHtOGys70&X-Amz-Signature=fa2083e83416eae9d7e19107c47c01c11fb38587bcbaf8afe04fa14b184cde59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVQDN6ZS%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCD616KqW7gD40oQlaiHpGbjgFfDzpkQmekTRFEMUAhPwIhAJmJyaaCZZYM18MQA%2FtM67D7hMh0c7jVz4UbBZcRyrgkKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgyW5H5P2s2qSHixcq3ANHX6njMvPWyStzEzUt96gmCE9U2vQ18JtCD6yCLfxCY7GVBt33dFQgZDeLFyoCyyYucHRafFUvPQ%2BdyOXr9KAOTAg%2ByjNHscrA9Ud5dCQhxAaTy%2BMA9fWnRLIttPy%2F11IpVvNHWSk58lmcYcBHcBoMn5INUu4ZV2rGYjWDYYTOGUWy7avK1QcYd6Kwt%2F%2F9wxFpMdLYt5LMXjaKSdnX5%2FbsRxarzrjeylpRC3zpsq%2FroZBTZOvGpLpwX4CQPi5PBfHD56ozZ8wNMmmYEkSwpI8sc7rP6H%2FlWMRtu0%2BuV6nN47PK8R1s8UMuSWxzPLF2M0hI6rxxdZVQUo69MAm8VzFYQiok0xD%2Bto5ftzXgy4QsAqNFR4SL3l0YjoUC0ZBbNzfpZ5FiBnOHeZp4Ee5DVOQhBfQlhXm95gPhPjBAEGGNb2tBp78fEx3vD8qJ73gUowbUHTUfiKaVURjy%2B78j8CjH7w9DWMHKsPSqYXPT8eQWYTyRxhvRCiRRlvMGhm%2BIHClXF0gH6%2FFHpadpO3xgivjQHNW%2FoUvDr4jYydge5wwzw5aST5nhB%2Ff9wKAQbg2AkONbSlJa1q9QMsjpVURu2CL30Uq0%2Fit%2BgDRajiaerVdNXT9z9nS64sCf1Tq%2FhzC96OLNBjqkAWflCW0sg7MqiMadr0gzPEvfHlJcrimcX3RcjPbITiwr2sMh5sobz8WdNmfvdI6mOkTD4venz%2Br%2FLdDemq1%2BBBXVDmq9Ja4vlZcmNfwDidcUiMpQpBgvSCaLnZ%2FQ32%2F8iP8laJnpj4EoaaJKbhT9U5mSFp30qjiSj1evtTUzfRJ8L5PcE%2BkSyalHmJYCTZH9%2B7AyYmKKqQPcj6rVBDUU2%2B7Czsv5&X-Amz-Signature=4a2b9e1c2a264aee4f4752c236bbe5c0c29b58134c9c15570aa04f414850882e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


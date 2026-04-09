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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H67MCPL%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIEzyPESVX95Lbo0dydrlUQwYpIPTIExHwxcZQKtjuHeEAiEAkKMHQhJ4HuemJGls%2B0Ecmcw1YwF%2BnQHF8%2Fy2JPJdrnMq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBU9L7UlqhcSmJdDeSrcAxhtRe0KYTM98qTNoRJuxLoKf1RMlKrosw5N8I4T5L8PNJE2JfV7EUbhJZyiv%2FfYRTzPB0B2zxVM01DVqEb%2FPUM9nAnKJRWXrZYnJysIA407nRbufoy08PULfl9aaT3zIKouJGjcui7Wl9bYLmesprmG4DXvTCh2HTmrN0V1RDjJ1ZGA3Pk5ubH9ACumYLyotGPq7XcoWVxOKvQnKO6Kq1iXn6sqwd6Kxyh%2BEjFQbQOJSQJJ%2Bxxhee1%2B70X%2FVJX0IevAlIdunrHOCO%2F8U9xRuj6C7c1m47MtkN0sSLRzYFtWHomxCVaXSuPDzhcVma3fAXbmdiSvOBzQQ52nJ%2FQWMfB7Uz%2F8IaM3Xbcz8qQL3XJY5nt%2FTBTIwVBBfv7TUaSN0HgIlG3Zx2iSLpGdYMR0ub7aO43s8KPuvegw71UUh4h8reZd%2BUYwskhvdguuonAUarIub8%2Ffnc8zbxyhV5REXJ7FLEjjFE2xiS0q01YaH%2Bw1OwECcXSHMQp0aYhkSfhFndt4Gkk4grxyscOMNOHgbFjyeIz8pM7obcTuB5t4bOoNDsKfYORrdBec8qA1qDxD0RW8IdFWy17PnZZgnSLbvRkdrNKko7%2FHWh74TqoLRqiWngaceT5s0EahZmEEMPGx3M4GOqUBEgoI4YxGOtUiuMfF3l9LdECABPgPMYvXLVzFse8RN0yiPvMcDtnrdlAKQuIDLcCdMp%2BvHfrfviaZbkRSgYZcccEglXr4yNKUQaH8lcf%2FGrVAlDkWmMRLJtKGJjEpLeBPWx1s4%2FwEeaLRELxw%2B6VMMnUtNEFSzKz%2B2TM3mweY7ad7XOGSNKLmvZGeb7PNE25aY2s47D1A%2F2zwcIh94x1S%2FVWK8PPH&X-Amz-Signature=d1d1fb263863131063be06dd295a2256482e61d7a91b592e32a2ad3aa9e2018b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


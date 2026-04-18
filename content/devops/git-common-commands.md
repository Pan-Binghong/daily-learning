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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L5QVA3R%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIDsUC8O7Ptsl0U8FDRuq7mXc8viD7XgM4GBFLj7N7gqkAiEAj9KumvFd9oXPPntDBl60teQ6RU4RVcDi3CCVtEn0hyMqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPGVWi2c3OR1xLIHCrcA%2FLktuupj%2BEvHuvukAIYkp6OpR6FFAHEsRE0joYhjcQyas57DGIHW%2ByoVbXoha6VAS7i2FXZW1sMFSK4vdOl361zXQSr%2BgJbPqg3WkYEkA0bHf6yMFyk7e06rtOGPuzKDuckKPUDP72lxUiGmUmYEMJbQ25OE1I9wnl1IbWFuEI%2FZuzwm9Qk71l1ymc%2Fo8oMmFvKRBp1ggHOIqnoviaaU%2FjKfS7wi5qZeky%2BN9ulgMP5eDBKZROhq7R2SURc0lx9hxi0yBcDTM%2BjsnQQLQrd2irwncq8SjGBnlR8rkwup0Qiv%2FvPsFeDzxc2U7fSKtI2EAhnt1zuRGmeEeuospATibE%2F4ysf9uKMyLT4WPKJzfTcYC9ZyqJpwXpp1WWW9m8adyw2Gh5%2BMmb%2BiLllbPYKrCbifgDh1o91jEogySDfvQN3NvwAr90ILLCavYT7AObvGUFW2S2vs37JGGvr83Q1Q7WrTnbo%2Fr4ddNZ3%2FXL5PEvh8S%2Fzlz0Q8wXezybHPl1zsTzgur7vosWiMxDTN1SLUQKhOqZ8oDfFXTnvuwAmRx5klIWCpRmRetx2SWg27NFId%2BiWHsz6ILWRCVKM5UhW9DyxRGPk9EEENtcXqtu2yodxpVg7VFmO1VGNIj%2B5MJysi88GOqUBCnCOaXD7AvMLaYBfp9P%2BGgdZeKNIsTp8lThkWhbt7F4gmf9g%2Bnco1ZjuDq4iwhiH7lb3nVhzI2prZud9sxJ3n2usWuR44UXjNTc7ju%2Bty%2ByA5WR8BrIFnmnvdhXMet8Fg5rUPoM25cmbnyN6YiM%2B7NQunWBho0NkCzGaJkwwV45wauMwCmfaPIi7q6eNRJ3QGWbw9TWaKxBLu%2BpaIXsUuvKMdE1M&X-Amz-Signature=a21871677c460a98014ea4f4540b0addce5bdad10eb0a9471924ae5b06f25285&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


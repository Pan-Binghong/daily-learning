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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EP6SHNN%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCs7oZaDSY4J7xgMCTGqKo4Tl3kWIbLhMYctuHoiYRj1gIgHWJELgb7oo%2BpA5Td4yCBwvT7Kd5%2FLLmhxMxG18ivlAMqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGH03pq3edhQljJWbircA0zHBevqfMGJu91UhC9ZlBtLC11J9mifUGsGFsVHBHo%2F9i%2B%2FxxCgXVnG81fYAArc9Twj%2BnIvDo20SP805hlO%2BST4P3Ss5zuUJyFVC2M2GOeY3tJNB2OuHOl4j9G79tmKNhnkraLT2BlnR8s6KtBlfl9WleuKlcUighFv83HOdoln4Ol9xyOVAYrG1MwToG0p1QyaREOFg6xU4ARayn08BOlGxkKRnXLu%2BnfCJHPO6HhbXNmD45NKp%2FUimUHkE9091njQDr6wvOtiDrvVcCmfSE6wha2LOJNH6Q30ZP87Qoe9teoqI5bttK94T%2BB7c5kE6xJFDdsJyrzzdsB%2B%2BZ1dGi5Y1zB6dyQRQoa%2BGcZ71%2F2K5awFTVJEnov5B%2BmqiIx14qZMadqaMNULmz8J0BC5y%2Fbp5lAu4Q0ThHridS6Tf1qXbiE1iHWUaTWj6cPHPMLWJa0j3V0nWzvLODOhqp4m2g7vb%2FJNdIOa4KUCFo2AvV0pvht4YSgCVxYzVtt2XzDg1MqMVsCVwlY1qSpTVcC%2FgwR9nLDS1wh2jThZxI7XTCsDbRCAumBrQkWnMvIN5ugrYWmvd7QvN77V1vmzYvdaKD9Vzyy0CcNvs7lUyJC1ttjqjDHis2vrugGMFiezMIvPqM0GOqUBopEG2VcPAgVpFUeJ0R0ZQqX%2FuwhfPhk9W%2B%2FTXiOZexKJKHUIOg2wBl%2BObPkaJrdJL4aR4KXmxblTyfPxqkMCY1RGtjtrzmeIjfG5fnVoNLqCbLJSmVcal0gvLxjERQAZVEs%2FsVd35MxmhT8WJIg1YTtrzLB3Uesb1lRmX8THKZqd%2BNBJNOkmwiJEC6Pr5l7kIwxAFhGJ64YjiA7ltRHrVJMdFL1K&X-Amz-Signature=544514ac70ec9e71ad501c1222541f68d755c3c8d058e0ca1f2d8389ea5f3677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


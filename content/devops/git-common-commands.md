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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFGZWFB4%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpS9V8k9tFLdHsYAUetx8bAmmzE%2BNDVE9IAp0SL44NmAIhAO5tarr53BmQbO7pOVEC06LiEhAwOmGzVNwZP92GeC1tKv8DCFwQABoMNjM3NDIzMTgzODA1IgzVXm%2Bx6VNnrU7BusIq3ANTCdwGmR2FFNEKePknNnn9aYrapD%2Bi9o6ctVcPCHGBSHdVDLHmlW77%2BaCLJI4p9z74Lc4iAVA5bCS80D7XBxK1GqB78sx3PfspjSAOY3doqUAwMTJrskC9e2BgKppPUGvnNXv6tvdtSTUqIYDvOJ7G1eLv5z2HgZZhPLYvuLOx%2Bu9wfGwcfAQvrF1cDM1V0PiFuhmHC1jj8USRjrkWO%2BVOtjBLxGUMHvwN1jt9QSjplA3xgdgVWK4txfqeNFaQZj34YYXDfzretCKWCXV77npPyYNIwknmipwC1sbUw2KvBqqFASUO8ZpxlkuvflMAkIScjurocbzuDzdIVG0Nl1j01Vq07fOVJY2sqLQNZQ%2F%2B5grX4VkhpDdMyhrTGvPl%2FSarku%2BGJSG5iQRG5vUUB3BhB17cMW2x0Dw9JVgxmTENPG9ZSeqZGnRz2xVdDWKZVapPmKA8VG0cwqnqNDruihzHKKrk3NDYfRZXwi7bKxcOnO8j7zSBP8l0RmcQDjRuU54ddZqFGjG3xpzINLpxRp26ADgx%2BAXyr6aozx9Cx06GCDaxPk8URvkD9u98B18frqLY9BNIMO2HSVe4ulfw6ASOPA0CjAAqpQ0AuzG1tfDhM%2Bw0ZZM8Y6G8Tz1YezDIjIPKBjqkAVPIqYxvvF5%2B2B5yswawLKiuROWy9dayS3mz117COn%2F9H%2BeBT4Xo%2BsFC9aX6zvSBs%2Fcv20lZodxeNJP%2F11nhYJlauUdSHZOZkpdndiOVSbvSmiKW%2FHG3RFOcVHoLccLP5deO%2Blj8%2F%2Fjg3gOIwQbdK28LiFXVrPveYwu6JoR72zrXvWAEdZXQuFCju26dChLhHONV1wII7KdsZ84k9NuJC5e7v4o1&X-Amz-Signature=26eced68b4813a1957f650eb27ac62f9578337513442ebbea8dee8ea57b81c5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


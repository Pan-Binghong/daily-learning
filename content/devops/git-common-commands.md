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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAY6R4X2%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7S46z%2Fij7CLMd80%2Bjn%2B4M08NI5z6OHyzTqYAGclnOzAiBdan%2FMM%2FnMXaJwQvPtUX0NeO63LWtmuuQaGD82JaoY7yr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMURI43Gr6Wu2oHikEKtwDKr5ZlJTzmmCkuytMShy8iiVIRwMQPV7J5RWtF3srW57hTJDqjOm4zqIU6WMJ2ufv7BwbvHm%2BbksrLJwfNxrhJmAmcE%2BttIY3mM1LG%2Bjjw7W2P1chgYjGZjJ%2FMMdUh3WBeIk46prJiZHsUTcN6UKZDbReIo0cp0spWGGSt%2FJnzbnDV1GBFi9tGI5bUuEJisMBCt9uVQPzj5MyVZLpwhE2MCzj1DOQTXqrIvVB0OqL8sCUIbRWe9AK5ykWS9HxOwERvc3uezda560MzwF0s42lKFPuaQJACDvQR1VEVAnMXS%2F86Zmpb0n8YocBCpRdw%2B5jH4IsR2r%2F1U96FZFmKpJY1oLZ9tlYWkXsis%2FnzmkTwlfMpsk%2FyS0v5ObWRXk9KPP2E8lLSc10DCnSFwWMlcYsD7fotcOCN3jDHU48UAEJ4OwH%2FqbhoC6JeYGSCn8UN6%2BgmphGrmj6kuhcMKwx4fm51AfmLJ9KYJkm8IbZBO3GGOLH6ctuJHcG%2FEgd%2FtvxwMwkzb1bqBQ0ErLz93FfJMisUCaPtSti%2Bn8etoPCfE6i0cM8e2smmbQrwYEOO7nyoDkT%2B%2FoGRFifNO0OSRCWxoRXHBvWoYHn4p2c09yOj5FtopTR5rWSeYeXsG0sci0wwK%2B3zgY6pgFM2TWq4%2BrYsyl7PZLqvzGHRjTYMYAznHyNfMjrgxTpnFHcQeIqiN7PBPVil7b8GpGmBLlCMWJsbdwKCe7IZi8j0F%2FujFr2%2B4cCZpFoV5U3VfUS15qMgoWsFPOFEChAoxRsmwEpcq2RRkBvewCNM1t6Nhxo7ddHJG4KrKDpnc1P5ufW7JShx07sdF0Ld0HvzhkRc7jhvegRRJHZDhP7ADN1%2BtGYTbGG&X-Amz-Signature=42516db97c20d4a210976fef188a2b6d84e4bce9fb6eee269650d7ce619be9ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


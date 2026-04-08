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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LCPZ33L%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDoy83o98y9InvC0K64NN4zMfJLX5pKHDkRtNUV2Qt0UQIgRD%2FL0QZWU8rYDi3Is%2BgxFBCbtyV6nBZrcCws%2FztBgSoqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDTz%2FNviMSZ1ZWSREyrcA6u4j8aYl8oc12PITpJ6rFMv%2BO7NQr7qhwOWyqPUZW1ribdWGHO8BUq2Wvgy1LSJweV04DTJ7hwNkDU3DciDjLQC5Vi8iwpvsPjHSbCQm1vVdIYAqbH8ocQH17xfwsTycaK%2B0uxUfNn1GJujZtLE8lL094ckOl4AI%2BOIM83ToWg%2BbXy0QWhpbaSICSxOSC77jPb2qmyT26XUOyzI8BTPBQIiV3BT2cg2TOYzhfCxzuEnbXpCbCrh6E73Yd08jZpKkxVckpNEwX9j1q7OJllWHJz1NZ8MGeIP1pdqg0MEj4gBhv2iBAsRg9Bu0%2B0LYED2HxmimTVbRWNWvm8C1VdfDBBUimQo2u%2B7gu89LjuGjzc9JerthSpf7pM1msBD903LLXvA22ZMTcstWIhRWl2z7jZ4O6i3nkyS5Li0tqAQHIk9abV7mQqjo6m0%2FGzS6Uyuirlbq2tIBsOZ5f5MDW3chLWummBhozu8iBM9UVBKyfcaLCuWdlyOlqQPJpDkRDMgL%2FItnxQhuEfh0Ef7%2FiacZ6lhrHvtHqyJTOytr7HWRvHYpDXXYBUv84GVRODN%2BBWY1tjw0Ky%2Fn1WX%2BkRV2Hydt%2BGEEhW2AHCnQZ5suuC%2FFt1%2BqHNq%2BRT4xazREuqUMJ2K184GOqUBIDX8kcgz6O5ODZ7CNRWKgFrInAiD%2Brnbz8XA9u1xO8FCBtTpoalu2yJHFm04UHAJWL56Yq4kd75NcWMeG1qdTXhodcNHhDhF91TJkPPyMxr2RqnPFefVNPd55k1qq0ieMXLsrp23EPFJ0Id9cG%2Bsff1xT97tPeX1tuAeMABd4pOecT7yX7G8fFbrjwBgmLDetYYIkUcQ%2BKOieR4nAFQ66DtLlaKP&X-Amz-Signature=bfa3fb07d1a58dab48bd931bc96e61c4d209249e7bad2da3b5e808ebdbf8dee8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


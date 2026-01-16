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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS6BVZHW%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDOUcJp4LrUNKubIuuGsi%2FprZo9ydZMor765JzuAgXIsgIhAKhVkh%2Bz4izzY2jJi98W0buT6r0Qr33dYfcLtxeqsQaAKv8DCEMQABoMNjM3NDIzMTgzODA1IgzQDdxtHpLGj7raQJEq3AOroOBsmVw2iL2EDFDIZUNqa2oVpNAnkwPh4tgqkHEvTMSmJ3cafr8wv9pi9HFMxjtOPb8hwqTzxRaFLGJRWslAHl3dek6J0Cj03rij3vb30SVwgqXIbcfVmHHNIiCvl4%2FWRD6I%2Bfcq%2BwwlzxGnRAEhxdoeKZjMvkQe0pnVhpZMh7AL4X0yCeztMAAIGHorYs0M5MZ5ItkVSxOqJi6%2ByNRJDveOyv0iPf496fTHkCP%2F4tSbllwA9ZtWDD%2FmuQ8WE15seUXVi92UkMINnDM%2BWIYBesKvYEomCgufPcVpS5i%2FVEvoo01I2QzN5TWymOOe4kZ3VcpXgw%2BfzOdKU%2BoQRBMKhAR7XhAIUuJs5POTuAPR%2FqLB%2BjwXZWRbWbin%2FtaAgdo7WRUAIoETS0bjEoqLPfqIRD5KGEJJbxbYN9TA0AJwiiuLP9ugCy6Nl7mQWcPkJU2OpfmcbOsruVJH42jTRde52CsUkNQmnUGH0chhe2ZuZ2X2tSqMZiCsenzCsT6%2BWKqxvIjhobCs%2B0VqFv3yhU5oADzmvL8eBUuOUy11JJX91zXZnJhr6Y2qHSFrSVYFRfPsKsUtY%2BxSwNSyWYg6B1z1lEXb0haCDgKNWvk1qTbk%2FYjUgQPNTMZ2c2smITDQv6bLBjqkAbF%2BZ%2FXEvbR7yc1qhpesxGP2YcXnnBJijaG9OwOKRLrjimPUQo3uRHv6XZt1kbwTFC0oWnl8uqruL9MuLwpP0S33ygOonD%2FrfTd5IJ7aalhnxOAbw6JfMrQ5yB4Zh60RA3sCiBM0F1aQTrl9p4Ig7vKE2YNICg%2FKrGRFp3D5pYt2kYBdkteTNxFsprznEm2EFVC3Td6LTofRGwVydvb91pSfpMpl&X-Amz-Signature=c5926e1b738dbc879cdafdf34afabbefc58e9e3ce7cb53208bb504b826fab1e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


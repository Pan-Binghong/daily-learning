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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675XGEEBM%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIGml1NcwDoiQPplGjwiD8d%2FUKX%2BMnuBLNjKwWat5c91BAiBgbNoXvTjtV3Avw4NAI3UCEAcPW3G2PQU%2FrXYw7BZXjyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJnGcUSePYLYO2TbkKtwDU8312x8mMKuBu5PLzM9xdKwwm788QRaFc0yhQafJjoijoe45qwAHpWNoa2Qs0vPLNY4F7KO8ZjrLXMuBo%2FNLwEi6idKVq6nVfxVa9e62CEtPxt6nJ%2FiyahUiLHo38%2FtjWe4HaAWa%2BHP1UQh0cdlJFNO5nxyXdcM4Gy%2FEerRNSPeywiNCrGp2y6Bsv8Y5Ykm8BGJJ3%2B0TaOE2IT3Rhaugnhcx4V%2B81GUe7QuexR1%2B9jo%2FQMBJIH%2B79HXkuGuPsiL%2FxtKUT8f9ecu%2B1OvxFGBZaiwk93WwipNeveAni4VSzgYg1tWz8GY%2BqifsRBMPjqeL%2BrCr1wM%2BqIoUE6hw%2BlFeqKC3asjwIijku5D2iL640jLAINAdu7GI6bvQjdsXuo%2FCKaYdVhZNOXF5oo7oiTkbU8y3NlvyV26WhLTV8tkXSkNb7Pu%2FaUc0ycIXmHqaMjuvgonzUg9KZCaCZKXHlEnIV9pQiTVeWq%2BqsD8tmpFMxJC2mG9wdq%2BNGXcbIjP67yPHAfUVJicIXfY9spN51UXlKlawYouxmwtW2h5mdR749Vll6SeeEOTlGjE006Yn6xwy40qaqb3FtkizS%2B8LItP8vw68Ybb79jr3ieeaPhq%2BYT%2F1JaG6%2BUP0G%2BAoV5Uw4rXEyAY6pgEOeq4WIYuqNwm%2BUkGxpoxfws8BWalv8cE2YNcQLIZZ1%2FvF%2FeSVD2rZyoQR17%2B5O1JnB71oAeHzXl1kaQTcoMjRDFUd3UXQdZOF8%2BkKbex4ZSsJiYeHmWbkKwM1u%2FR2FKhnWapyMe0%2FxtqJRVPE6jxDgWNX82J9BaVQWbks6Lpv6vbYscVvKDtOi4u9nQHuGjM5zFm5tpuEtSOw10GDoQI3hA43U8TT&X-Amz-Signature=ca62fbff889953bb69faf7bd71de7697f82f2ea5e5ddac27a946fe2cfa6b6637&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


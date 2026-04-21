---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWLAYRQD%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIC8xklM2dmjbJmbNiV7EvG2jK9xxg5sMmIhyeLUigKGFAiAjW%2F0GnpGzmuV8evIl8aEddVtv5lIsfYSbkeuMYzau7Sr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKdQKXawW54XfWKA8KtwDz45yR8ri%2FyMXX1XVW4fD2t0QPKBPDUbKj5uLEgrC%2B6aS668MeYu9JnNblV4ZhvijT2RBZ0%2B7YS2uizsiFxQqlQn8CetgkVl4ej8uBpNH21bAc597OP7a%2B%2Fhoh3tSFLfj5Wprvy0YB3qWRBBRyoLaXtbBcwq3UgXDvYGral1830DZNp%2FsaT3kKgUHxAbl6v4bYoaPKWvn090mtC3O5YPKukeOJLA%2BMMA%2Fr%2FW7tWh2o6vuCk4suBvTIGLhbQvWdZ6Lo3HZ2fWydzR2NCoZWBm2TDlB6DnHkSsFtNiYUiFhmKrdRRSIkgaDhz8HcCFr2HKUqKiAB2%2BKdSD%2FN6%2Fn%2FkeDFOfHy7kX30VlCNWa%2BVMrQFQXMhCNM5s5%2FIkSKTvty40lPMV5ojdt1hu3wxbPb4IqrMikkFyAqYyPj0MA61umofwblAheQ3BuEagNcBSMLJmUC8%2BZ1FdI4zwCVB8UwgGvttT2lyO0qusdLZ7w6qUVMb4a99F6zPY7CqiWYE%2FOFlMRYCjZIUWDB05YqmpTEy9U84kOPKFPR44N5GBXzPuPob3KMD5Xh8twHFpm7Xvr2wqlKYEhEIrsSwjpLHS8BfoEWiMJzrOAUaa3VfDjm87qaLO1If9GZtNbWT9AbI4w%2BdObzwY6pgF6%2FwxPjGR52OK8TZ1ofUuyzOmgReGwX21qjLc2w%2F5ycQz3ICvkserrUnlGoBC2tYAWoDuOUP5cVlak8Jvt7CJ2RkEgawi4mlmS10YA63bTRYVeoKw5eK1QQmddzMkKTt%2FMT0A6gtM%2BSt53zjYLNZda8wG1RNRiAtXfuu5fWY4sppCKQMCex4eFwQdP%2FQdHVUeqs2mKhOBCDbB%2B29B%2BIPzooZHgcyT2&X-Amz-Signature=95b8ede91ac98b2223a56d488536f8e033e7243c55d84262c5bdc8d20e59ffb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


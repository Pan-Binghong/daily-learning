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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2RCHGNG%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVxR5LxCYgSIcEYUtWFEXplCVJoS%2F5KX%2BO2TCfW5D6YwIhAKEkYDyvTuwPXIUe4NMOaSPOHkr8ZwUSjjeCv9VWFPOaKv8DCGsQABoMNjM3NDIzMTgzODA1IgxFfSD9rGxf8BAnCzEq3ANsKIc3Ijp%2FK6rXvck0ON3XAatG70Qqixf3uNqzsd0Fk2NksNdlQ1J9cwpF%2Bs5wLN2GL9c%2B5ZUAYusp7SmerSNpJAeeI1nVDAdm7ArWFfi05x1lQQrpMMRSxjohYGQyH8H%2Fs0euLWWbR%2FdJro8QaZ1Qk1tsXdDAwqyvfRjLGGuyBVI%2BWXoUf%2F7WjndaY0tBiean3UFfYGn9fwUFAT4SczPZmMmRxC6zBpF6f2mylp9Il1BnuoRiWUnfqXCtOUPB9S8Cdvs8HkjLfkS41%2BMIu5HPRyUboPbJZbPCqGwd7LzAqma2XWGu1SR5VZdspPDL4wSWsnExyJ3h7pdxXRsKZxuBAkvFHKcEURjurtNBe4l%2BkgDeraRR89wQjkQ5mFuRSVm8uJ9Fm8x%2FKwgb7TQi1oPqzHz8ONlaBTEFqdVs31fP5a7NKzlPgbXPrXrXvundwO%2F%2FxEwaUUgjpn01RJtHX380sCYeOisBvfFtX2w3XvLkIArEV8%2BNOheHswryN7CECYRTKOivmCh55FFuQ9yvmQ5pSM%2F6H54Mpxa2AQHtlbGvr3%2B8ZZ5AseLwScC2TyTaSIOvZMO7aHCHaIVSUJfRxqHzIKJZQ5GdDD5yolLiKb10Ye4yrv4HjbSHGmvSkjDvssjNBjqkAex1DmDnXjbAGmHPx6YJNG19lFTAMFBOUvlPxxulgKlNYhYBRkKeNkzcf7F1dpx9nY12z2TzGZ9L68iPMBshDgl3O8dtZ8cro0r1JUXqA5CXeY9kGh5C%2FWSKFtRC0w4pY%2B55qlC7LEqQ39At2No53lk9C3Ox%2BDQn1Qs6UGn6Tq41hZAFk4mZMq3AtmO7lZMmVWQKVH7svQFSZLHoBn3buhkd8mX9&X-Amz-Signature=c10cf6d704586ed48c31abe2b909c7a53bc99fd24f42e19cc8ecf322b04feb80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


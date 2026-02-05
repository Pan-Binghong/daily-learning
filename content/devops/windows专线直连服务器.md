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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP3UUJH7%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQChPNVaIXXoarvdb6VEOpXvpiyCXxorRl0JygZYBhKC2wIgWTrPJcIkX%2BoUiN%2BLsN0etGcdh%2BVxnmImrU6BfJS6B8cq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDB94fMwMzf2LdnylFSrcA4Zobcja0BN1jsiva4EF2cfubOChjcS7R4KFqsdYbSLfarh9I7upINmtsf8C66jpIIDyDu%2B%2B2BnWxnKBhTkBMxlBO1MdOOHhmdJT6qII99%2BeFzIaBmzWGZmLkwtDSyni%2By488uOCempB6ri%2BSACPpx3jM%2FA2A363iRLS0doyQ5tsO2auuNB%2BpgF9BQrQPtMAj34OM6Um0KhnA1putP2NF4994jeBdJmPoTRhUbYe8LJ6vXM6Hnw1g9YXO7DXvvyyrbBUwod00nLN3fFlpGjHUnSZtGGWCPJJNuik3qfpsAYDk1RIO1MTQ3%2F8o79bf4NAc0MvIfVfIYGiS95DD2dH3Ph1n6QXmQcktKG8wLV11kkDUoWB9JYlsD4VR7v7zmKlfPCguKBe%2F3xRiAff7Z0ftyHMZjjvjtT8ua5JrRFF0jYsyztRdb5kWzcVqhTHE3DUyOPsb5PK%2Fwfhd0JZp44er99i7F2wyPSRFs1MHRXPv%2BRcdcFsOSSZ1D1FY2tNtC1zN0xlYjDwjXeU1c8YJq5NXekusUTbuhj1uCfQELqeXbXqV7uMqZ6t1IYGxEXvmZRBfskeuk6ZoXHii7pC62%2Bs33Rvx4yiIStiwS%2Bgo2EbvwG2Fd0DHv%2Bz054VXW6bMP6SkMwGOqUB23hsSFM36JRfqlaH0vyHY8RunG0j4eth9GVAec7txcuKLMNFhd6%2Fg1DIK%2FSMez8I81xiJH2AHnAbDdeY7H5H58NwY%2BkMgE54wPrgP1tYFLDurB76iPyE5WGNifim9XN9SjUc9HoZbhr0Xuhg%2FXTaNUW4lDacxv69CJqSIQJU2tLQUwiBx%2FUSppw8AovYP1yZU4wRGBW2C4t5sZX2NzXnnxl97duj&X-Amz-Signature=0dae3abfacba132e3fa85797e3cb1af033eaa461f55bb5ad29abd7a071749559&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6JFTC2O%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjDiueBLZr%2BiM4qfkcK4u2TBfKDL289QUAh%2BZ9klL9jAiA75Ds9nKHwW9THggZsdONUA4uGk7rURSe7iw5Q6tKjESr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM7BtBOfVpclTQTikaKtwDJj%2BNkp2hzWzx1Lc05CwVd6ds4OMQliKr6IfPGsgWslqecKn7LXtS1cAzNIe6ymsHucSDD%2B4UwuY3PUMRiXcAZSTn39HIiIJwXedBcvl9dfNwAllfpF%2FyTp%2BxZJnhRa9Bmofd%2BbnTHFMxy6XXgtwz085rgF%2BoxlJpxiomFNwRhDtl%2BrerTDz0bR4ABPJGf0iYbKDMvJ8pogLz0A8P8ztPFUfDRKt38evYqmk7tRNVBU13XPtZ0218FiENh%2BUMCLI6TEUywxIYmHc%2Fm9%2Byecv0Mn8OcQxUcgszjGkLqMhK2tOnug4g5SWFcjXqhTA4DgCADvxNlHFvtYCpUY6GtDnWTEr80hVvq42P8tuWiA4OixCstDTSnx4dxcAoonuKRtw7Mb%2Bxy%2Bm3cjar6Z3FvOhQL7Bg1sCSW6Y1wS%2B3TwIUoaO%2F%2F8vT5Kv%2FHlunOl9eSInICvD7mCrMUXLunchfQxLhDWUgS7lCKXal2bzID0Zn5y6CLXGXGRY1VlbHBg2be2aIvjqGv6%2BldWt%2BINjEx%2BK%2Bl%2B7aE7jQrE3WEG8Xd3TgIitQ%2BAaZMssDJ8hq6BBdsnTzBQGpyDkrlQ5pI352XXj0OJcN5TSumIdNcVYZWELiSHGoKznLwiBr7nyRFNMwuY2DygY6pgHZIwd4Xgez14%2F%2BazHaZ04H%2BBfLC%2B1AjZaqgvaRry23YKYp5EvYFm5UVUSIN4ugXJDZCWw1Efta81oSbcv1dMf8bY0298WHgSHMqXTkoU3LRmvJK2QYJf3OLFavHmMSHgPYJQyy2JRpwIDEFun3QTniveRPGkkk%2FUMysZn7lZIN5teXAZjczQccxvaa%2FPfSDJY9hkB%2BmPH4HR5OCOemwSJJtxzrXv0i&X-Amz-Signature=b1f14aa6768f3b42f05fa7633898373c2bf229bb6d07f363e4ff68d810373455&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


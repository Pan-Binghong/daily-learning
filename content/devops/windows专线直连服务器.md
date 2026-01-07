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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPMBELTT%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHwXvEfQcCOI5KiuMOf7Wm0noeiIsQ3k3FFHv83kzQhsCIGIWIBe4%2BW81W92pzIBSjNUD%2BNSiehVdMWFF8VSVE6P4Kv8DCGwQABoMNjM3NDIzMTgzODA1IgyN4pA4kyt9Q8zL55gq3AP4upVCZnfnS2dGTN%2F6lGQUOflipEcf%2FVOlZ4qBkXuk%2BWF4bHEc7ybJR4YZP22Lp8hDQ2Qcs7nqWIlpIhTiWQWam6a%2BsXOozLqoU1bUZ6D%2FzzsDrAKuhqUavmW5dKRElrolSF9NLbVvFQcPtszfZ3HYJU6f1sjDpLoWbqJ6dpPl3q%2BNn39sujLA6iKx8XpgYPv7bWodzMMNnsGTJrbahCB%2BtkBhE00zt66eFIWzZaRV6L8xZMJNnpzAOt4o3E4Bqe1MfgX232F%2FE8mwmae%2FUjieCnqa4p81spD%2FbUCtXGxQrPbWJ7p9JKLtJF8uDOf%2B%2FXM6IyO7Wwg8IGVuS6a5sNYIKHR3f7whqFqo8KAI6vf5Zv1%2BupoH7Q48JcMUTIJkP73aw%2Bk54yCdd1dtGGiBOwfxXaKoVN8EXtC7gOLRmx3kzVGuI0n1r7E34PsIn7jalRhu1TaKWAaL6dAHoHkn1qIX1LVbVyL7YpAYdqnP4c2S2vv0%2FMIyjKSP3jT54DU3Oz%2FkHbw2DBcDExWns8dQ%2B%2FrcklsefPHv2yGBLv0J03gu6b7NTS0X4xtWsh8RlfXnStJ%2FXEDVMrr7VepWKsDJ5O7BzEwWMaWjSP3w28ci4GdP7nr2NugAfK48lGtTTTDYjvfKBjqnAcbnRr05o2K798vf5ZgMatFvsAjCXsA%2B%2F84YA0eb56h4fXM7V97nq8IIxd8adSW4gfdaveyBuOFE9pvRfeRwchXAw%2FrmTZf9cbJVQSKSge4%2FdS2au8FhaCFZVJ%2FBQX0e37UU1L3T3UOSEknpBTP5yxPDmLv8637EtcLM5Wlcz8t1bX77fvEiwhBTOLxDhpANm7BCfFGJ3JpVRbdKM0ItqhWVXMV5qOTd&X-Amz-Signature=835d48ed78949fa0c77a86cc2339273f53bcaf4a971fd23307bd1f7dccc13633&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOVUWX5Y%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBW4eiXiqILzalItYVpByNrgzCha5CH1XoFgcMYHHJGkAiBUfca6iD%2Fz8L9oDoleUg9nTQNq2fTTZlAX%2FB4%2Fy%2Bv6ryqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQahJA4ORcNzvsGGrKtwDKeGZ3AvYh5nTICrcU2zlu1cADQdJl6a%2FRztqbmw85jap3BGB5tT0DTHkqM5ylNnB%2B39b4HlwqTzEkV7VSf9wgEWhBp8AYtIfJibc0H9t%2Bg2PKbY%2FaHxfS75pgTIwUi4NsGwN0Pj53tFf%2FcsAwwmOHNVwONG0duz30eRaVfI2Fexb%2BRQ2s9NjrS6%2Be1iSjOxmGFRvCNuryDHGUgGFPng12N96Y7YhjA1hXIYKcqmZsvVY5uQIV0feflRRe6%2BLIf6ZEixgwwCCiDu3S%2FntcYBJzIAkHrRt86XkWB7uumQywaL89%2FzI5haAQf6VOsDxMH%2Fiqx1kzlozj1rOQD8dDQLx%2FEac%2FMzBuDb17g7uKgP%2B09I2HHQS57EXDJX33Q1ZzprPuKcAEHGCQ9xdiOcB5uREKor748RXCCvW48Y5GogKtFyT9%2Bps2BEQgJ4bB75%2BeVZcwcBb8Qa%2FPax27MJ3K6ZSIBb%2F0ja%2FqzvfvA5zMtN%2BFIKnGqF6ukyXQXIyb700cJNfjtzkiLjziwcCGDCnmwhAnnr4aKHKBbCxjP1uWqToA28IxsS5muTmPVLnJwEwL8VP7z7Qur21X2qigBQaQzXiNOx7hfXX2%2BHzdeiB%2Bu7SVhR6uSaXobmK4cJQHX8ww7fNzQY6pgELLD1u2KPwzH5e9YF7JkpWiFCAQYIr9vJEVPb5QbYLUowU%2Fgbs1p0FqOCmfKX%2B9glCkUw4uzAGPyh6HZ%2FCbJ24pMgFMCP5sNQrE3niKOdThjQWPvXGZw39q7gWIqmY269GXRv5h240ua3wB05cPvPeQgZaK9TxPeokRg76zR%2FGEAE1rLjiB1XRroWuEYdNZUyht1ulxgXfcRktxbh7VAqNQL91pKnC&X-Amz-Signature=29c156cfab4bfddfb4ecd0452453f2195e6ab6cb3ba7b43013448d20ae759b22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


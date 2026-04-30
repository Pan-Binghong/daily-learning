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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RMZBBDD%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQC75wzJ4F82cFO3B19xuLKgdm8s0Ar97BHqY73nPGYKVwIgFHJpxyzPXaEj8R3UUhJnmLuPCPVVKdUho5FGwJdHcHUq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHLWJAmiJVMKg7V0GCrcAwI1QMgM6rRzc2PeS%2Fy86i9HwTqE9tjWLddCNweDSW8gZc%2FFJS%2B0clfbrA%2FHe1i2uHU2w4BK%2FOWkgPiqxEiIP7nBc2hc7ZoUEvwjpzmr%2FK0OE6e%2BJhnS5mf6lU%2Fo%2BY7QqybwonhuRCo5RYPV68dr11Xjt7Hx1Uq%2F5dcMmayKlwqW%2BjvMFgNMTA82Tgu7pUIQPMH9FJM%2FTgGQhrYo45nKwUgEfWlW%2FCoZcxXUski1fgNdFUannjdIpvK2sXtoXcy1k7bPI3MRIdvF4c%2BBJfr9qTVwgH3SrzTlSmiJGr%2FKZ2QwYIN7Vxfa7dwAGgzjoLVdeKIvaOoe%2Bil6Ye4UlAmLoS7egJvt%2FMFaKuN6sMFSRgxDXXcwBihfYl9wlM43Cl8L8bcPRFwsdF1amwgt%2Bv7eh2NlIDJziWUSwJL5EwwCjIWg7v6efkhuDJMXMCdKeaQ8QPv5e0q%2FDwCt5VV%2FYUVKk5%2F3Cj9nxHMqmUsaGdcwNhgVcmqaAHpuyrAdKh99iKUNQlbtfQ2HNgg4BiBruCQpSMcNdc24Vrw3aj137oTsirX3LxKXnOz76Y0VHUKMq%2F0KwKyCWQtl%2BHRRjNNZjav3n5%2Fn6JSAndSYPr46VqhDC3XcwS%2BsLznVizEd6czZMLqczM8GOqUBnp%2F5zMRO6fzekY18Juw0BQDdQmYOQhkn5F%2BLkF2z8VC8XfSWeUneFzNE3CD6glIIJUIZBChwypyML2LNjGP1Tn202rCbiRzr4CcDd4jnWn5NAL87EvF8rSJhE22UZy1jx16CIc7egpSyj%2FmBk9BAGLS7mvcmcBC9FFBlOxVO%2FPuRu8fO5OVkq9NxXC3V9kVF8ehxsVMtobtJzXC3ZauLKUh2%2Fllh&X-Amz-Signature=ee4e5cf0002e4039d15e9cae2e45fe5884b92345e32eb3a05202c332842df5eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


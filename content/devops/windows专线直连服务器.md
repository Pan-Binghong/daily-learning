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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFBPYEE2%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIEFQ2FPwIqPJowRthQDZnJdGDlVnzGLWzR2soa3mmQuWAiEA%2FP6iqG0X2%2FDNdekM4nI7%2F9XCrvpbrxse9uHrqqMiUMcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxGlzCQxZJjw%2B1CdyrcAzuU3Bz%2BJJS0AfPbxpWK0gtZ%2BAy2PmDEBnHrFqG3b4jsUL2q0sdx5hxrGJ%2F7yw%2BTYXWpHAPYdZ2KAPTeNYFjmZJq%2FVDhkVlPEtN5C%2F2w48mcDBdtKZC13gH7uMeyXwizeQZA5BiP%2FLkM%2Fd%2BEX3j%2Bvqdg4L7mx1b3%2FkW%2FLC1sSwgMKGcabDTsWAC9lYK3QRZJ2aceubaUrdFYo17jp2T5jhlJYgV1b83wbl37LqueakBB12iRIds1GyqZgEvo9XEiO8QukPK6eRcjfIwca3mkiUi2kmgSSE%2B%2BnnodD7P9Z2sd37dqUKQmJJU25zICV21vk0LY1U4BUSXwqxZZ2ploqsNpYVvUCrInouRqSLsKIHElkYM%2BNQzHXqAPjKqWlzGT3cbpBs%2FtplMn9GokpxFXsaXQsC6MWoogUNKb5694q4XuB90XLIjyiM1FHdPbkIBbdZdRKBtLqaDbsZF2x9dSYVC%2BmcmgiE2VJ3t0LWJ%2FWgkaItvsVN7tS%2F4tlS0I7jbVJq2p80aFx2LkllddMWYqh111lCGURq3vCt7urFoRIsat3GHrs91vGMTyDXXGqId0ZP2alnNeXeHTqbIkraywyBwEdYU22PkepVy2gZo7%2FO9v5yrGBJsqy6THeUIoMNHV7ckGOqUBif8PkdSVxCsbMr7Zhr5bm%2BdH1Wzav65l2mBidAiyYqqWxDMAlx%2BqEphHlOvucEbsTK3%2F9f3xyIFzDK2WUAZVmiQCbq0v8DUfZnDpUVpHlK5HsoAqcqthqWrtVoPrYq1v7zdv0IcADhO6%2BbGNHQuUdNzGfuw%2BnjMB4JYIb%2FOdAnNcSEZ3b70HFEkWQQQwennDgVl17WTkixsX3SY2QDGo6Lx6wR4H&X-Amz-Signature=cccacc450206fff60331a9b6fa7ac23c9dbd48f22f849a51f17c3f012ffa797c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


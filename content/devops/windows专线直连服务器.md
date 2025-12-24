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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HMGOO4R%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCLZJx9M%2Bkzi4e7JqdUYaU8cJHfcYhx6l%2BCEV1oEPbcvAIhAM4A50jB2lemNgSOnT5PN41qMaDnCwQK6GugzEpqYuhaKv8DCBkQABoMNjM3NDIzMTgzODA1IgzTtfuGyLlqfbtu1Ogq3ANxA%2FEWrziQ5%2BUwKhk%2F9jVO6OtCoQUFwaV2etk2PmvAqbpJJ0aVxxr3rMXyF0nQSVygk93S5eFUFiUVgiabdDBu6vK4r22yTGk%2B4P5LSLfdcpetu1GYN75n9exr2v4TB4pSnsye3BnIoDom9qX%2BJcZy4VhDavp79BHNLmmzEzIkG7BG6oQpETtg%2F3BUdwTtYWXWUIqg85aKq9w6YoZSEGUu0V83JkiW0NC5hydZtcrcuXu94Pyt%2Fs2txJS%2FwvB3FTFcCmRgiirJtM2O4AarGZ67Ohb%2FAtwvN1BbjoFfxQPJiSkiQl9db6SBZCUCOSIjy9EGmhcZhabmhsdhCTVOip1Q4Q9CuXV14RWd1qQyrqAEK1By%2Fz3AkV1GvH%2F2dpsVJyykUnegmXHXljkcPBCkWDwlLX70ERg0D3LELK%2F8%2FySDjqmJ%2FEjCVmKSj%2Fg7%2FVpKlBjLiam89ZCu1WVcYHKV3NIokcwEsceDRST%2B6Rh1IrqPP3gP2H%2FyCsR6akhS%2BcoNTKcpXxjaYrpqTnIZPGGs2wCRZejWn4BBk6jUH1po2igwnJ7Xp1l2mtT83Be8%2FtUSJpmswB5%2FFESGmO3lL%2FxJok%2BIphYYXwtNd4cYflawBhzfMk%2B5WgI1%2BuB9kBFi%2BDDT4KzKBjqkAXM2hNs6KwavnPxjG%2FS2U62a1TSLirVnhqrz53aqFmvO%2BGnAU6buiRsIURggmE%2BMTV1X2k42wL6KVyx5IkQs5QD3u8CrYSAuFCcoDI2TEhsFn%2BcphGUumx4H0JVkzSbt6hfTgEB3apXnDnM7y93bJHZ10Nl3MSB03MJp5sdNm3rrZTLk46xjALA7wgqSRhSMs0uuiTZeU4bO3BpjmtmwZH3tBq9F&X-Amz-Signature=eb06477b1393d7761c3355c9dd5bb1f9cd05a05e3efa430b1ebc135d4c63618f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


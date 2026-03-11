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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVRPUY5U%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEPggd%2BAZ0n9JMsKu9XupyVXdOIpRjh%2Fw2IgmRuACd%2BpAiEA%2B%2ByTeEAmOODAXPbCNOEtRwRIaw%2B7RK6OyHIsbtv8t3oq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDEGIZmFRwk55imqVTSrcA%2BhQitlKdWxOiyUKjFJDUaNocprDZbYJG9oIqfs0AcY0X9EvDGfDvN6p9swJQORR1ciUiTHl2%2FCLzO8jtmYcXSp0xAdwGuDO3XaWtfZA2Hw0c%2BWiU7ayQeimwOuFu2m0guH9ki0otq76WfpAxYDrTJRq6cEiaarO7TIBW3ifR9WbZ97ycqEXTBcsxjyXotNz%2FoVw3WI4InIW10fdNvHmvMLjSRO0Vv8UAmG4m2k2x1prjF%2FNKvZqPZrVK2s8rQGWX2m4uKtdCUhfrjYHF%2B728%2Fg1hj8yXkSehw18SGGfD68uihxlrA7YqNGPvST2LEiZgBP5tAsp5aS3nk5ukJRi0LQRg%2F5j5yS0f42F3aejQotnHpPO07LVdLelgbAduRwYiGEG6HVhGthYPN38ucXsy4uPlryp5NJt8En0tPd27wt%2FikexCRA9Yl3WIwVv6ZFCVG6hzS2kS54%2FYcbGSblY5Oz7Q0CGVblX1TjZaPkq43MhUtj1kH53Yqc66mwNCFszRhp%2F68Km6C%2BPa9fV4slJtWtMc24tn0nrvWNg8fP1W8dDAR%2BRTuIWZPi5g%2BuOFPW7Mb2h218Zllqiw03FXn2kl%2Bc9xEk5GX9E8Tz9ArL40qde%2FEMP7uCotBRMJ0y7MPryws0GOqUBYpdKG5J%2B4kUgX41HuYqfLMi4ySiQ7RfYy6selCX%2FaJnSGlQKic%2BiY1ngNSh7ddFyXSTxz2aMootq5LpICmQo0YY6k2O%2FmbJS0v%2B%2Fk2dUhFb%2B9qemhof6irfNvY8dpwRi4It8PicIMfndp3ZDhtqQhziAzX6CcMTE4Wa2T5AmIMvXKSdcugqRFG3PNPOHh%2FKjMnDALUQgg9z1gHn4e%2BzRSayXnIoF&X-Amz-Signature=32de0139fbc97e8e283d38df9edea43aab2f6be8f8bed42e1da4ad186827d193&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


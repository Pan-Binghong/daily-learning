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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBLC3TX3%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQD2sbfdiozJ2irR5MIqHqwT0o5Wvbdmas6KsSA4Iwe3YgIhAIA4puoBdvPf91JZkBeyu7FBg732MQ0s1f5Z1KFFB6jAKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzR%2BdD71fhR8CD6aEoq3APO4GhXU3LHNXYsZ51PBM656xekDoGSZZenRaFj4v0T%2FDGJXaUBEBk5CmCjPyT95Q0yYf5t4fAqwfNQop9p7XDstqCajtfZX2FKHFoSK7pjiwVlDIxdJKYqEV43jNtkE0s4ROB%2Fxbg3D%2BFIM%2BAmfuRaU416%2BxR43LASSQNLAlZ33kg93VTjZ1ldTu%2FuaMxO8FZXNwfGg0DQNwMdRdI1%2B4kYRQCFIv30GtQCPD7v2QZlqt2fb9ZN5BYezmG3lSqIFJBDIMTO7EBCWMRRuDPh%2BnZp5eMX3jIQ8ceWdlensqM0x25BL9T8%2Bfh1wDpKvOD9LfxWNHyZnwqHMKpQuTuyYVRgKeXQrPjqUGxK2ggdy88OoTkWt5qRVQF6Hj8pz%2FAgw1EyD5VhYQmIQce8XFimuG0GbLGUE25g2XYvI9FwaiSfHHNg0rxr7oxTsWBGuTOa2wHf8YRV4ysXe4b7Df%2F2hRBMOAGEfIazghtKgL0%2BtsMNdF6d7RnOqcUcPgSMOpemWCO0BLI5OnWxPPORpcD6m9X6Yr0JtpLBku0T0BTnd135FrLiuEvbpjD9lwoGnkViLEPHT8gEkFrvCGrrdYNfMwdU9y23jy0G6bizg2jDaVqPMzOLkK5pPC%2BQPRmmWjDircvLBjqkAbca%2F49QulFKZ2wPNcqjir28Z9bR%2FROYiACKdtqOyKhlexYMVzwTeGxG3brzrPlizue1Gstps9eQOIr88HoPbC38K1ZM50x%2FHaCvaiunETYw7RcwReTXDacscwoNB%2BjRIQl902JdHd5ApMH50nTF9kpoRy4km3Hnj8aCmHQWckWaAuJ7NseEloiCevNwSPrmP3%2BP6SOL7NZ%2FNkh1q6BQtLpqzb0N&X-Amz-Signature=71eb2c72f62eb72ddcdff32225774cb62f5a43b080df2801993482b169e53cdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


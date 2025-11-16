---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IGFQNYK%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYoRkEYiiM4bAtb8x2qgNHXOqbqcrV10nOrFpro8m0OAiBGf2c3ZYOcn6XsyehcEFygZUmY%2FnQl1P3EYECslWEEQSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbr9VZDqfmVpNdWnlKtwDpNfSx1qKIf6dFxyfi8WMT7si%2Fp3qpw3eMpN93xN75zwEzBVOrsO11O%2F5qk4yzodZUWjG8tSPT1A6Q6hq4QGepWEh1R7KZ0zZDDwMT1pMnj5%2BZuW8QW1IPtR3EGxKU1eIPWtLiiQQmlsFZNMb3wGCkGkIj9MOotLd1MKU3xbxieYycdp9%2BGcLSRZ5GIeRFxbjrxOqHf6HKnFa2VGJAYkRQStqbpiyCTohf%2FWxopxAyB2OIDSZqT7yqQVVbnL7FUt4Ql%2Bcoq%2B4ucimvGD0HytUL1sH98kGKDZJD9aifLTHUydyk0SaVIbh63286Bwm%2BpBkyQPtPRypgfDtdDrNwBH7CVYlZ6U%2B%2BmzdleuyxTceaf1Ssex5yDFZFiV0QBUBnXJYvSiZmdJoNinW2YJAqa0o6%2BFUaenahriEBztOhGLuWu0axGGpc1biqQ6TXWYCUXvYZjZcbVl4fmd87RLQQyHXYz9gqsPWiUI0HUg62ei9Mo4RPrj%2FVZoHhm86kFcMRrP93%2BxARDDNgAvQ21IDMMnk6BTimPGUJdBecerti4D44y%2FiqSflt8fXGZhq4VFUR4ELgyOydBGuL5ttPUhbWpIhnxUuudaIrDa8feG0E%2BMbUIB%2BxcLdB1pvsaR%2FTnkwiOHkyAY6pgHGwylLXjq6erBWKg5omya4ig7RY9VsR%2F1UtJy6v7Sz3PQ2zQJGECUzUkTjIddkbWeWKrhlaCTs%2Ff9KyrtWi5kUkX7xP45FUpRtaXDMuCF4lSsWXpNbUGabwdST5bZNeJTHxb7KhJZmBhf3IGRxKui4M4ssbHXTSLXGoWhhsIekRk2kul%2FGV2sTfrTd0aA2GLy5rQ3qCrclzMWqBH%2BOvM%2BMcppWboGU&X-Amz-Signature=61f7d8ce0d27d4af3ca774087f093d4d76a99630115b4de4dccf20e3ad45622e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IGFQNYK%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYoRkEYiiM4bAtb8x2qgNHXOqbqcrV10nOrFpro8m0OAiBGf2c3ZYOcn6XsyehcEFygZUmY%2FnQl1P3EYECslWEEQSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbr9VZDqfmVpNdWnlKtwDpNfSx1qKIf6dFxyfi8WMT7si%2Fp3qpw3eMpN93xN75zwEzBVOrsO11O%2F5qk4yzodZUWjG8tSPT1A6Q6hq4QGepWEh1R7KZ0zZDDwMT1pMnj5%2BZuW8QW1IPtR3EGxKU1eIPWtLiiQQmlsFZNMb3wGCkGkIj9MOotLd1MKU3xbxieYycdp9%2BGcLSRZ5GIeRFxbjrxOqHf6HKnFa2VGJAYkRQStqbpiyCTohf%2FWxopxAyB2OIDSZqT7yqQVVbnL7FUt4Ql%2Bcoq%2B4ucimvGD0HytUL1sH98kGKDZJD9aifLTHUydyk0SaVIbh63286Bwm%2BpBkyQPtPRypgfDtdDrNwBH7CVYlZ6U%2B%2BmzdleuyxTceaf1Ssex5yDFZFiV0QBUBnXJYvSiZmdJoNinW2YJAqa0o6%2BFUaenahriEBztOhGLuWu0axGGpc1biqQ6TXWYCUXvYZjZcbVl4fmd87RLQQyHXYz9gqsPWiUI0HUg62ei9Mo4RPrj%2FVZoHhm86kFcMRrP93%2BxARDDNgAvQ21IDMMnk6BTimPGUJdBecerti4D44y%2FiqSflt8fXGZhq4VFUR4ELgyOydBGuL5ttPUhbWpIhnxUuudaIrDa8feG0E%2BMbUIB%2BxcLdB1pvsaR%2FTnkwiOHkyAY6pgHGwylLXjq6erBWKg5omya4ig7RY9VsR%2F1UtJy6v7Sz3PQ2zQJGECUzUkTjIddkbWeWKrhlaCTs%2Ff9KyrtWi5kUkX7xP45FUpRtaXDMuCF4lSsWXpNbUGabwdST5bZNeJTHxb7KhJZmBhf3IGRxKui4M4ssbHXTSLXGoWhhsIekRk2kul%2FGV2sTfrTd0aA2GLy5rQ3qCrclzMWqBH%2BOvM%2BMcppWboGU&X-Amz-Signature=64ce3cd96db2b81d834e192cf9456e795077b846989f2a023b2350c49148861e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


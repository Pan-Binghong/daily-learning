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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YO7LKKH%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQCl%2BuFDF7RThHCRbHDWlwgrGxkChvRVfodrEZYPh12T%2BAIhAIrwwG0SLC2CeBAVj0PbMTkFDpjocIR2wGsxe48Y62FXKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPL8tU2gGxozdmPQQq3AN%2B4ZnrxKwg6mHRXdtGlfack6OKpGuh9MDdlY79sRAzASZmcVdqYmLjoHzoY1ZhASZ7dW3imFux5Ar78GrsTKFo7nSi%2BAkrRGajyVfHdRCOQ85Ma3W7bTxeUExflkKhbyIhyOJZmG2NXV0Oc313hzi%2FdPEPTm8e8%2BKJ1s4nxiDi4v%2FDqDUH%2FGbDAMtXM2JW%2BdEyQRYoLAzBvbs2np1TXja14Cn2iQI4psHmnZJeuSP9n9qV%2BPVe0TuB9EHI4ianO9EBRvuL%2FIpwCwniPXLWzZrXykOJSr0JCl1CyfZMnOT1mWABGu4Ib%2B0yeDAaRwUo9rEB1bgMviQwyLWdSvSGDEtJzpAlR5IvCaRucwGnGrPXWiuqgNihOAS%2Bq9u6CByZXsXkBlBXG6zxUy%2Frv75gejXqMlofR72DfKjdeUiBSodanjceoAMcxoFjNpcrFMEJgGEam3t3NNpmZDmcnDXTsJ1IMFO7O%2F05rhuGpJzFgbvNbv2TZ7atPqWF4aKs6dqQthfJ%2FYOC3MNtKARBivefKCxYHoRG%2FJnyuUseAQ4gRHDZIQ0tG6u2blVSKJB2%2BdR8zS1aknDP5kSKzWDOJzz4mEs22Z6cAJNThHubFAGXYSq0lAZ1bTgTWmLbxchPWTC1k%2B%2FMBjqkAVLpzuD19sx1raiWvRpeLf63kZs9brQqr1kbWpgIlzAXX44NlcBGJEFmkk%2Fy5aSjg6zYJyooPV5%2BGv%2FMjU1FK1EKY4i96KWuYqojLdpA%2FUf9bP%2B1%2BHf58JPEc4huUjiQJZB971q6XShB87PPOL1lGv9BCFezzkb9rlNjLHeIh5Omjspn%2BZM9AiOQvLXw2uq3bp6RyTngMHlwLm3JhWXg5%2BZvDnze&X-Amz-Signature=1bf55985caced81a24851bd0d44280632dc2db9a771fccce0e32f0fd183ab99a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YO7LKKH%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQCl%2BuFDF7RThHCRbHDWlwgrGxkChvRVfodrEZYPh12T%2BAIhAIrwwG0SLC2CeBAVj0PbMTkFDpjocIR2wGsxe48Y62FXKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPL8tU2gGxozdmPQQq3AN%2B4ZnrxKwg6mHRXdtGlfack6OKpGuh9MDdlY79sRAzASZmcVdqYmLjoHzoY1ZhASZ7dW3imFux5Ar78GrsTKFo7nSi%2BAkrRGajyVfHdRCOQ85Ma3W7bTxeUExflkKhbyIhyOJZmG2NXV0Oc313hzi%2FdPEPTm8e8%2BKJ1s4nxiDi4v%2FDqDUH%2FGbDAMtXM2JW%2BdEyQRYoLAzBvbs2np1TXja14Cn2iQI4psHmnZJeuSP9n9qV%2BPVe0TuB9EHI4ianO9EBRvuL%2FIpwCwniPXLWzZrXykOJSr0JCl1CyfZMnOT1mWABGu4Ib%2B0yeDAaRwUo9rEB1bgMviQwyLWdSvSGDEtJzpAlR5IvCaRucwGnGrPXWiuqgNihOAS%2Bq9u6CByZXsXkBlBXG6zxUy%2Frv75gejXqMlofR72DfKjdeUiBSodanjceoAMcxoFjNpcrFMEJgGEam3t3NNpmZDmcnDXTsJ1IMFO7O%2F05rhuGpJzFgbvNbv2TZ7atPqWF4aKs6dqQthfJ%2FYOC3MNtKARBivefKCxYHoRG%2FJnyuUseAQ4gRHDZIQ0tG6u2blVSKJB2%2BdR8zS1aknDP5kSKzWDOJzz4mEs22Z6cAJNThHubFAGXYSq0lAZ1bTgTWmLbxchPWTC1k%2B%2FMBjqkAVLpzuD19sx1raiWvRpeLf63kZs9brQqr1kbWpgIlzAXX44NlcBGJEFmkk%2Fy5aSjg6zYJyooPV5%2BGv%2FMjU1FK1EKY4i96KWuYqojLdpA%2FUf9bP%2B1%2BHf58JPEc4huUjiQJZB971q6XShB87PPOL1lGv9BCFezzkb9rlNjLHeIh5Omjspn%2BZM9AiOQvLXw2uq3bp6RyTngMHlwLm3JhWXg5%2BZvDnze&X-Amz-Signature=5c1aec84243a97821757e75a1080cc7f6178c421d6ea2069f0668ca2687d191a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


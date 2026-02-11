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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPUJJYF6%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAZu7MIfa2eAAd0FLIK2uwBVlB85WXW8%2BWzgN%2B8sUMUQIgfBVgqGjX2NewCyM8QjpP0cvQCLLHah3b4FkwOkug8QoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAzKXSWmwCWuEcna0CrcA9gDAx%2BoV2b15CYuC7do7eFajSf0EchTlsycbibVhiToVaKnK8sTwJykv%2F31Sgywc1Jl%2FtyQC318deh9c0UPSXZUem82R%2FjcgN3LFnHk1cGBGw1oGMr3sHQeTmp9L6smCQD2NcBaT2hIeFlw5uhO3u%2Fl2hZm3zE2nJoGgy0s%2BJgtG14kjqI%2Bnmd5S4np5cGyQrrhwr29fTMmYZ9xM6hmXIcjh8g%2F3dNzdhpYBWA5aSsxN1SFVNiLTjk1TFjCjZUY7IhGJ4fBZRDGsXbJsrJxsT%2Btj1dnUM983A7ooBYv9pw94EgOKe9Ac3mt3Pn%2F7lSA4WeC9Xn%2Bc%2BePpyjdACT%2F%2BVOjavleXFxbI2kPUhrPc3sTbg%2Fx%2F4gxCegLm4rd%2FO%2Bn%2Fe8JHBHNwTOxE9KeRCkwKjgwffAK5ZiO8rVNzKJVGiUxPLpNOt5Ac2oMN3lgRb22fQd6e4oAVpyeuPK7Jax1wtlPXnkc2thz1Kw8oO4yvje642CrAGBcfOpRSRkN6bI%2FSGJEpjweeZT%2BX%2BhtSFj%2B8gyKFL4hyKLD%2FnZVB1GYljjKJktr8SdO11ZEP8t2OkRNW3MKAKO7INI5mKO9Mi0OVM98q6BUhNAJM1H9hlKfk97G%2Bhvyg%2FOWAuxZd7YYMIHLr8wGOqUBcxIFsbXgJWg6AO41bkjNitfcFq4V%2FevEuIRjIR2zeEKGrAjqMeFYtrBJ%2F55z3Qq0uOeSCH1ZM%2FYbJO8UvLvY6ruRN%2B6QK%2Bsj22aW4GcHavyfmxHhG2nSJV9KTgK5txWcagNA53YN0RMPc2dna%2Bkde1VuQQ0852WNskppGq5%2B2pzqS4W%2F0EykSf%2F7zSQW8B5gqdd5%2FtHagxb0VJGBJYCXT%2BJh1Thd&X-Amz-Signature=48d73e3b436abefd5cc0b3a6cb1c0061a6007c61d66fc074b300f76d97b0996a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPUJJYF6%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAZu7MIfa2eAAd0FLIK2uwBVlB85WXW8%2BWzgN%2B8sUMUQIgfBVgqGjX2NewCyM8QjpP0cvQCLLHah3b4FkwOkug8QoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAzKXSWmwCWuEcna0CrcA9gDAx%2BoV2b15CYuC7do7eFajSf0EchTlsycbibVhiToVaKnK8sTwJykv%2F31Sgywc1Jl%2FtyQC318deh9c0UPSXZUem82R%2FjcgN3LFnHk1cGBGw1oGMr3sHQeTmp9L6smCQD2NcBaT2hIeFlw5uhO3u%2Fl2hZm3zE2nJoGgy0s%2BJgtG14kjqI%2Bnmd5S4np5cGyQrrhwr29fTMmYZ9xM6hmXIcjh8g%2F3dNzdhpYBWA5aSsxN1SFVNiLTjk1TFjCjZUY7IhGJ4fBZRDGsXbJsrJxsT%2Btj1dnUM983A7ooBYv9pw94EgOKe9Ac3mt3Pn%2F7lSA4WeC9Xn%2Bc%2BePpyjdACT%2F%2BVOjavleXFxbI2kPUhrPc3sTbg%2Fx%2F4gxCegLm4rd%2FO%2Bn%2Fe8JHBHNwTOxE9KeRCkwKjgwffAK5ZiO8rVNzKJVGiUxPLpNOt5Ac2oMN3lgRb22fQd6e4oAVpyeuPK7Jax1wtlPXnkc2thz1Kw8oO4yvje642CrAGBcfOpRSRkN6bI%2FSGJEpjweeZT%2BX%2BhtSFj%2B8gyKFL4hyKLD%2FnZVB1GYljjKJktr8SdO11ZEP8t2OkRNW3MKAKO7INI5mKO9Mi0OVM98q6BUhNAJM1H9hlKfk97G%2Bhvyg%2FOWAuxZd7YYMIHLr8wGOqUBcxIFsbXgJWg6AO41bkjNitfcFq4V%2FevEuIRjIR2zeEKGrAjqMeFYtrBJ%2F55z3Qq0uOeSCH1ZM%2FYbJO8UvLvY6ruRN%2B6QK%2Bsj22aW4GcHavyfmxHhG2nSJV9KTgK5txWcagNA53YN0RMPc2dna%2Bkde1VuQQ0852WNskppGq5%2B2pzqS4W%2F0EykSf%2F7zSQW8B5gqdd5%2FtHagxb0VJGBJYCXT%2BJh1Thd&X-Amz-Signature=a7661b4c97cb9f5a694a579b19a1f7c2af64d4204334a8690ffe643fda33d49e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY2CGHPA%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPDELfxAm4VMa2ESOadWwz3XYkm0ytoaID%2FPIyJubudAiEAkRfRp7tcra2BrXPtP7ABGLbZG2VQI%2BcFsNnyTVf0UjEq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDBsBxXEx3hy0svt0SyrcA5oesc24V60ns7%2BlzBwQCMRqS4Cq93oEBHRmatwWm5L176wv4PrBQzaKG4SbGft59lPFLJHAqxUVA126LYopeMfe5c5ejK3tG5prtqJ3L0%2Bg0YYyAeVoggu3XPxQYdjKSSQ%2F8teAt31E%2FXKE0sRvaaOOU67vYBBmVj5DbqWy3QTzJ91wev7fsJrrrinnUcr1Z8vU7No%2BhUmJ%2FhIJGGIkfNQLqiN3ri5fWaorzDYSHxUY1XEJ%2F0JnBwMVVWWchCTfFwHnNxOCKi3Of2nKddOwmClcQgKFGTJejQdMdu3Zl9LDnrAskRWgprSXBaXOEqdeg0B9mzBK8ujK9Oj4Fla1VbIaEC6EXZIHDwcHUIV8hXzbROcjx78kpdhLFEom7wiMHFKreeSi7O%2FSkJrriXQqdyGaIQ02rkF82qJdBRf1MX7wEf8zAW4sxlFkN7Z9ZKitpelFE%2FnfnbKAkZxR0WAap7M2kCIoWCQVvPVYv4jf2rzX1BpaZUnRxkSJjOBQQDTFaiu1I%2FoleIQEBO7hFxfQGSck6NtNVS%2BLfMeaGRyjjpm8nENPT3%2B9j4HhOpLiEykPf1H7W8z7lJMkfjjAp%2B%2BA0OLtlRGp3X4iQ1JTkLErC5DcOEjenD63foLLbFG5MPbRq8sGOqUBWIpmtfK%2F8pAsRoZcR7M1ND96qtAXrB6i8DjO0WaJrKSvwpw7uYCiBU%2BiAzjRIZjT1eO5%2FQcDEjTpnAquB9WvMAJTJi8ioBqfGZZrIjazy2jkatymWLrVy6SvuLeDPQrHnw7cYnf%2BfkzuUDUCwb03lMUvW0tvu013ErgWyVNGsh4Xg5mzB1tLpZFy3YIPvHdpOQJ%2BTVdMdSI7YnDIT3WW4BnDVJ1W&X-Amz-Signature=46797b75dfc2f695fd6f195b013dc6c9839f6ae5a601b9b48fd2c85feee53c27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY2CGHPA%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPDELfxAm4VMa2ESOadWwz3XYkm0ytoaID%2FPIyJubudAiEAkRfRp7tcra2BrXPtP7ABGLbZG2VQI%2BcFsNnyTVf0UjEq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDBsBxXEx3hy0svt0SyrcA5oesc24V60ns7%2BlzBwQCMRqS4Cq93oEBHRmatwWm5L176wv4PrBQzaKG4SbGft59lPFLJHAqxUVA126LYopeMfe5c5ejK3tG5prtqJ3L0%2Bg0YYyAeVoggu3XPxQYdjKSSQ%2F8teAt31E%2FXKE0sRvaaOOU67vYBBmVj5DbqWy3QTzJ91wev7fsJrrrinnUcr1Z8vU7No%2BhUmJ%2FhIJGGIkfNQLqiN3ri5fWaorzDYSHxUY1XEJ%2F0JnBwMVVWWchCTfFwHnNxOCKi3Of2nKddOwmClcQgKFGTJejQdMdu3Zl9LDnrAskRWgprSXBaXOEqdeg0B9mzBK8ujK9Oj4Fla1VbIaEC6EXZIHDwcHUIV8hXzbROcjx78kpdhLFEom7wiMHFKreeSi7O%2FSkJrriXQqdyGaIQ02rkF82qJdBRf1MX7wEf8zAW4sxlFkN7Z9ZKitpelFE%2FnfnbKAkZxR0WAap7M2kCIoWCQVvPVYv4jf2rzX1BpaZUnRxkSJjOBQQDTFaiu1I%2FoleIQEBO7hFxfQGSck6NtNVS%2BLfMeaGRyjjpm8nENPT3%2B9j4HhOpLiEykPf1H7W8z7lJMkfjjAp%2B%2BA0OLtlRGp3X4iQ1JTkLErC5DcOEjenD63foLLbFG5MPbRq8sGOqUBWIpmtfK%2F8pAsRoZcR7M1ND96qtAXrB6i8DjO0WaJrKSvwpw7uYCiBU%2BiAzjRIZjT1eO5%2FQcDEjTpnAquB9WvMAJTJi8ioBqfGZZrIjazy2jkatymWLrVy6SvuLeDPQrHnw7cYnf%2BfkzuUDUCwb03lMUvW0tvu013ErgWyVNGsh4Xg5mzB1tLpZFy3YIPvHdpOQJ%2BTVdMdSI7YnDIT3WW4BnDVJ1W&X-Amz-Signature=d6ed5cae4159a182dcea43cdf00c202312a1e9c761d0f758069dded6b7815755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


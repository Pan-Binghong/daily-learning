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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIEAWK7%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bio%2FIieKP2icRBPwYCvg3qD29fd4wZJfZ9Fl7LuyQNAiAl7hYxy85Re%2BmkS2p1GAf58TfGvB77k2H8AHDQIT8l5Cr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMZ1XGjs1J%2BKt8bZfuKtwDh0XUurRBOOMnulMLkt64JEYw%2BewUwnQexEIX%2BkLNl%2FpsliPMv8Z%2BarqqjyrzUxO245gsm8puTI9yZTmI8tAk6uSgMrJaZD1Xvet3epj6qPVBTLc9UmnLEfPxyowRdOt4Hd%2FyFz1XMORUaiN0IrH1fYX9AIy8%2B463cKFGqe4mj1d5cUT51njSEbFaVsUaOE1xIyG19P%2BNA2hk9O49WcHBr77ZcUTQ0iQI5p01mmHJYkUmJNfsCsT0N2ekMUsi7mSuygIBohVVXE3VVk%2BnZ0le%2FWHmrzjwW4N6twBtqI6PiG0met9bsFHXzZZiBP5EUDLxXQRnxWyx0d0vNffTXB0ESGIMvUponzideYDJN2H1UCFQyRPYoMJDrX3Il3zgJuAsa66nWlK%2BTRAN4BMdvwvwYr5tBChgsn5LUYn6MzjQ2gLKR1ok08ogeyBH72T93eMVBe2GAZkguUGG4uoB73nIUOeY6qqLIWzThcq8bmDlNAyLZXBP4HVeslsV2jLsYt9EI%2BHU369dN2LVJtiYpuV1D4wUNsUSsdrir181rZhsJZq%2Fp3Jt20Kl53vJFgN6814wShyxayzVNZyzWKE3%2BeHIyMMP8wRDf6a5RSVp76yZEnS5t4%2Fn5I%2BV5WXfcGswy4nayAY6pgGfmNmOG0gGuVcYTXRL7uIFw0wSXMW0xF%2B8ZQSZX8BSSCSR3NTmfSA4yuD44WQqDhdnnOZoUkQ%2FP%2BA%2FCSKwAkfvFVgkj1Qe6m3zS%2BcJ3jNdOheYzEUmncD97n6MQn9tZ0i8wKAZlQKLVbOksETmpseT9RPVdtqe5Qz6ndZslG%2F1coLqJzP4XPuD%2Flgb3FylFMsYM5vzjbKfyLSHO6pn3iCkwgYld1VQ&X-Amz-Signature=8e57bebc30fdaea6ccfc5ec9968c9943d76f0dc90c488fa385d3007367add1aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIEAWK7%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bio%2FIieKP2icRBPwYCvg3qD29fd4wZJfZ9Fl7LuyQNAiAl7hYxy85Re%2BmkS2p1GAf58TfGvB77k2H8AHDQIT8l5Cr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMZ1XGjs1J%2BKt8bZfuKtwDh0XUurRBOOMnulMLkt64JEYw%2BewUwnQexEIX%2BkLNl%2FpsliPMv8Z%2BarqqjyrzUxO245gsm8puTI9yZTmI8tAk6uSgMrJaZD1Xvet3epj6qPVBTLc9UmnLEfPxyowRdOt4Hd%2FyFz1XMORUaiN0IrH1fYX9AIy8%2B463cKFGqe4mj1d5cUT51njSEbFaVsUaOE1xIyG19P%2BNA2hk9O49WcHBr77ZcUTQ0iQI5p01mmHJYkUmJNfsCsT0N2ekMUsi7mSuygIBohVVXE3VVk%2BnZ0le%2FWHmrzjwW4N6twBtqI6PiG0met9bsFHXzZZiBP5EUDLxXQRnxWyx0d0vNffTXB0ESGIMvUponzideYDJN2H1UCFQyRPYoMJDrX3Il3zgJuAsa66nWlK%2BTRAN4BMdvwvwYr5tBChgsn5LUYn6MzjQ2gLKR1ok08ogeyBH72T93eMVBe2GAZkguUGG4uoB73nIUOeY6qqLIWzThcq8bmDlNAyLZXBP4HVeslsV2jLsYt9EI%2BHU369dN2LVJtiYpuV1D4wUNsUSsdrir181rZhsJZq%2Fp3Jt20Kl53vJFgN6814wShyxayzVNZyzWKE3%2BeHIyMMP8wRDf6a5RSVp76yZEnS5t4%2Fn5I%2BV5WXfcGswy4nayAY6pgGfmNmOG0gGuVcYTXRL7uIFw0wSXMW0xF%2B8ZQSZX8BSSCSR3NTmfSA4yuD44WQqDhdnnOZoUkQ%2FP%2BA%2FCSKwAkfvFVgkj1Qe6m3zS%2BcJ3jNdOheYzEUmncD97n6MQn9tZ0i8wKAZlQKLVbOksETmpseT9RPVdtqe5Qz6ndZslG%2F1coLqJzP4XPuD%2Flgb3FylFMsYM5vzjbKfyLSHO6pn3iCkwgYld1VQ&X-Amz-Signature=f849745c6a3c3922b16290d29701fd68c0ba1267402abc35eebf8aac0e388635&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


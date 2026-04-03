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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX6NVAZT%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZ8uyxeYjd6%2F21y0PrOwxzHuBXJtfqAYdUT3hHeoI19AiAxAm5obxsenRG%2BomkLhAeqmsjr1Fik4O5yc9bZyeqWBSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMn0aI%2BFJBkJQ36X1%2BKtwDRuTbKtin11TNymligVcF%2FHXphlqSRLy9t2JBzeoSIu7%2BEdXxBglKRR7NgZGXrA%2B%2BfTMhc7QOd5IDaF06L3qS3BUcWrLQiYQLKb5vTSmN64D0racoZ2Op0HOSNFtiAD3zYZdmihF5lDP2kT91osSaI77UYDXTAdlQDs2nh0HhkIEUsKdauz0cIvk8DaKR%2FdbZf5h2pFmrKdbCKCRYkrmL8ekGgx4gO2067srMx9lpYGxec2T4H%2B8tUAP%2BUoZ8BHnG7fKHn7%2BsW9I4L0eThZBQLESKqPO1TKX6f6cGcSb3xN8RYcfnCMqNCnie6Fk8vdZEc%2BOaYOAX2MQhidYmTsUcpHzREa%2BFjE2Tm2xn9VsPownHSvBy24Q03vM4%2B0Ec1ce5KFu%2FDyckiBryeQxSRIwmDROPyYzA%2Fjlf2qfkb88chtuUmQS4kHaXlxLc%2BPFTTCj4xhm3fWjcn3%2BYl58B316VZneb%2BQ0GNzM5lGPtFmv9O%2BclU%2Fa5TyFCf6KnicX23RS%2Ft8VnUTw1w8JhJdHLAFtt2jMY%2BxoznykGB16vjoTbzkYzxQ4N9FO1fmuxCUbgQjBvPwh7Ept1PFq8Sx%2BsksjH9IwwwM%2BqNhbHGN%2FbBBVmOF8aT2rH%2BhmK90qjnmQw8669zgY6pgHu5F%2BWKBg6%2F%2Bz0ISbxiMJwp3n%2BT6e%2F85mttQmbH91zRhRR7UHskMoz%2Bz9mWBRgCdBnX2McLc%2F%2BJfJ4G7sDX0tWDlNFH1wngxlPbffd9%2FZpYqOepctEc2VsfS3HiIlawmvtD%2BsfHRrWMya711ZrxhqJmjhNJUM1L8OBiuslwRRa18JShV%2F6MaTECe3HZzguNcuIkkNzUatqy4xwv%2FJd%2B6pVn2GfEsP9&X-Amz-Signature=dc4ee72594f17654b73e2dfdb03b057e7f698ce2bb263e1dfb348ed180149069&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX6NVAZT%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBZ8uyxeYjd6%2F21y0PrOwxzHuBXJtfqAYdUT3hHeoI19AiAxAm5obxsenRG%2BomkLhAeqmsjr1Fik4O5yc9bZyeqWBSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMn0aI%2BFJBkJQ36X1%2BKtwDRuTbKtin11TNymligVcF%2FHXphlqSRLy9t2JBzeoSIu7%2BEdXxBglKRR7NgZGXrA%2B%2BfTMhc7QOd5IDaF06L3qS3BUcWrLQiYQLKb5vTSmN64D0racoZ2Op0HOSNFtiAD3zYZdmihF5lDP2kT91osSaI77UYDXTAdlQDs2nh0HhkIEUsKdauz0cIvk8DaKR%2FdbZf5h2pFmrKdbCKCRYkrmL8ekGgx4gO2067srMx9lpYGxec2T4H%2B8tUAP%2BUoZ8BHnG7fKHn7%2BsW9I4L0eThZBQLESKqPO1TKX6f6cGcSb3xN8RYcfnCMqNCnie6Fk8vdZEc%2BOaYOAX2MQhidYmTsUcpHzREa%2BFjE2Tm2xn9VsPownHSvBy24Q03vM4%2B0Ec1ce5KFu%2FDyckiBryeQxSRIwmDROPyYzA%2Fjlf2qfkb88chtuUmQS4kHaXlxLc%2BPFTTCj4xhm3fWjcn3%2BYl58B316VZneb%2BQ0GNzM5lGPtFmv9O%2BclU%2Fa5TyFCf6KnicX23RS%2Ft8VnUTw1w8JhJdHLAFtt2jMY%2BxoznykGB16vjoTbzkYzxQ4N9FO1fmuxCUbgQjBvPwh7Ept1PFq8Sx%2BsksjH9IwwwM%2BqNhbHGN%2FbBBVmOF8aT2rH%2BhmK90qjnmQw8669zgY6pgHu5F%2BWKBg6%2F%2Bz0ISbxiMJwp3n%2BT6e%2F85mttQmbH91zRhRR7UHskMoz%2Bz9mWBRgCdBnX2McLc%2F%2BJfJ4G7sDX0tWDlNFH1wngxlPbffd9%2FZpYqOepctEc2VsfS3HiIlawmvtD%2BsfHRrWMya711ZrxhqJmjhNJUM1L8OBiuslwRRa18JShV%2F6MaTECe3HZzguNcuIkkNzUatqy4xwv%2FJd%2B6pVn2GfEsP9&X-Amz-Signature=e3f6645ee429350a8a9465256eb49cc0742326e32ffc107edf472d62db242874&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


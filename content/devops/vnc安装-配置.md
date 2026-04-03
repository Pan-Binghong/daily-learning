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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SOMZL65%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2FBQf6XQ%2Fz3WePmfKrFBW1%2BhKid3FeAo4UObp2e8ya7AiEAgdYPIPT%2B38BmO7iqJyCivBzWZfn%2FsQMWnclB9ljg7boqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsV6d8uLXno8ULtHyrcAwyDHhbPDhYmuW0jfNDADz%2FvGfwh6iCdeU84l4Y4FGiyHkkK9OJqsM%2BAR8PFcDLu3MvommAZWBYvzQVTHmBZY7tOungFy0DNBmkvDiRK7XvAMMMzK6uAkBYFdu3VxfpGFLiY%2BTYZzQuIW%2B8FN6KGp3pi8WiSKJ8X7qUE2JkSt5vaGCzEZPrU8%2BP%2Bea339t%2FMp4Zk3sz1xeCuZwNttt5r7oVfhd9QSrNmqpnNrN9hh4D0RCATY7i0k4%2Bn2Hln6Z3qHia9INRRcAQG6ocE2AEKTzBeblIq0MCGdD3QAxeTjF%2BzsS%2FwfAdIiXnrrTuL3Gt7Ag1YnEjDRd9OlVc8hN24u%2FWLMMJZARo0qF8iMTAwNbevKCYdI2PJ4lJFqBSuA5Rkk4NmhkB75U%2FxZkt%2FACffiDaRxbof5w4hMdV6FgkwQFCuhh4QNk1mstsalfbY25hIGdOK2%2FoJwudS%2FMR71C6qd2Mvfv1Ruv4%2F0L%2BGDpwA2AGU4GvaEIJFArnfiqClNVTGTn2%2F4OZnuR%2FfiekK9ViQPYUSoPeE7lFZ%2BuyUUgcSlxXvbkyMT%2BbgdzLbDiY86ieoGTOvvf8SkfMBXcHa%2FWdPaK84OiOEwTxVsyJb03MpwgemjtG9J%2F6Y0ucPcsYQMMDRvc4GOqUBAcKH12cSnif9h7YlV7e3GUCLf%2Bm0Era8j5%2BSljGIhUXMeul2SbeIXbkueMaoTXbimNGNDcMigx5tJSBBl5R4oB2v7CU5dJVZZ%2FHsN60OcZAdcxU8ja9%2FmkjI7fymm6tCAjVujesut9ZJVR%2Bfqy6J8O48oQS2Fy%2FRmZvpQ7xsoaErK0fiQ3IQU0F4x4tovkRYfIDxFfI8SR8O8WX1QWtQLfjuMRfa&X-Amz-Signature=a23c423c58d16e847eb7a5c76a870d68e495d962a5f0f059ae864e5ddaf1e200&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SOMZL65%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2FBQf6XQ%2Fz3WePmfKrFBW1%2BhKid3FeAo4UObp2e8ya7AiEAgdYPIPT%2B38BmO7iqJyCivBzWZfn%2FsQMWnclB9ljg7boqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAsV6d8uLXno8ULtHyrcAwyDHhbPDhYmuW0jfNDADz%2FvGfwh6iCdeU84l4Y4FGiyHkkK9OJqsM%2BAR8PFcDLu3MvommAZWBYvzQVTHmBZY7tOungFy0DNBmkvDiRK7XvAMMMzK6uAkBYFdu3VxfpGFLiY%2BTYZzQuIW%2B8FN6KGp3pi8WiSKJ8X7qUE2JkSt5vaGCzEZPrU8%2BP%2Bea339t%2FMp4Zk3sz1xeCuZwNttt5r7oVfhd9QSrNmqpnNrN9hh4D0RCATY7i0k4%2Bn2Hln6Z3qHia9INRRcAQG6ocE2AEKTzBeblIq0MCGdD3QAxeTjF%2BzsS%2FwfAdIiXnrrTuL3Gt7Ag1YnEjDRd9OlVc8hN24u%2FWLMMJZARo0qF8iMTAwNbevKCYdI2PJ4lJFqBSuA5Rkk4NmhkB75U%2FxZkt%2FACffiDaRxbof5w4hMdV6FgkwQFCuhh4QNk1mstsalfbY25hIGdOK2%2FoJwudS%2FMR71C6qd2Mvfv1Ruv4%2F0L%2BGDpwA2AGU4GvaEIJFArnfiqClNVTGTn2%2F4OZnuR%2FfiekK9ViQPYUSoPeE7lFZ%2BuyUUgcSlxXvbkyMT%2BbgdzLbDiY86ieoGTOvvf8SkfMBXcHa%2FWdPaK84OiOEwTxVsyJb03MpwgemjtG9J%2F6Y0ucPcsYQMMDRvc4GOqUBAcKH12cSnif9h7YlV7e3GUCLf%2Bm0Era8j5%2BSljGIhUXMeul2SbeIXbkueMaoTXbimNGNDcMigx5tJSBBl5R4oB2v7CU5dJVZZ%2FHsN60OcZAdcxU8ja9%2FmkjI7fymm6tCAjVujesut9ZJVR%2Bfqy6J8O48oQS2Fy%2FRmZvpQ7xsoaErK0fiQ3IQU0F4x4tovkRYfIDxFfI8SR8O8WX1QWtQLfjuMRfa&X-Amz-Signature=64551ccd78aafd313cb0935931dad732f8478f40647053650e9d6515abe41e86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


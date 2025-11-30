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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675H24A5G%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCICYQtaz9llKiB9TMlW%2BkI8XnPUBLK%2BOtPgZxBjrxEMgRAiEAvETGIUnp2HGGWJtFUVrsRVJ1NPf7xELnMxi7of8aYsEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIBCpxxN3tjLfdpo3SrcAzs%2BIq%2BT3q5pUDdPN4mXE1NGwYHk9NifmfHTnzOxUjCbIJlhyJg6XKSJFuAFGI4SyrQ%2BN9bgLKi5b%2BghJEEfcajC53uaTYfTl6okVq8QzdGeiAB%2FkFFoDv7XzlZ7sECtqPJVglsgstMHn4N5ZZqKUPebRPt5UZn3%2FNayPcYqzdaskLZY3i2ex64KcmlmSv127eO%2Fm1D2chJWWvRaBWWOLqQwahbyW26tC9n9xFzWJSo8rst%2Bu3mS24UjaS6fYUfdcZ%2BHzIozNACIlHoXezuE%2F%2F%2B4zWwQ4aqy02yJgKbLbDdx%2BDL297c6LOnQucCrotG1B2T0B5J8kJL8lNiGbAuFNhwkFKOhUaO5AyZsogoLPDH5sMMkdEAT7NurbeLGO%2BbIXaUSeWca25D89D58PYkxMUdTaPsgV7I4Ts5PhkoCldiZnssUPQPQ2eYLdzbE6IHYkJU35jQg0cofxhuPqpmyQfKBHIF9OYth%2Bw7hK%2Ft45xWQqtxkdWConBzxUJgyBjNkv70p3sK4lWGTiyFKJAnvris8%2BT%2FYUYeFpLngtcTcga3c%2FeyuxGBsTfRi80f4h6pgavPdIGnpw3glCdNyMTyZYbZlP%2BXZXhkL4JPdMfYt9aTkskuIkR5B1gyKHUK7MLrZrckGOqUBStPJjk70EYGOFy1Ic8L%2Fe2IPMALSiXpu4RstdvdiwGYVDfJAhgpLAC1Ha5yxQj%2BOtUk6hiqp5zP3r0yMGt1T7LcHAFr3%2BBjvMzmA77Dg1jN2V48B6niyyWGvRNX9uc15VvVbj2u39q3khQ2j4IVe%2FQSRQO5fqK9%2B0DmTfHvM9W5NlhtHYD%2BoTXIaz2zdtAkfFCXylovGTJHprknudF5D1Qjzkf88&X-Amz-Signature=43a07b0b1d78f85d7950ff43ac73ae6c57d06d0beea09548faa29de76224b274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675H24A5G%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCICYQtaz9llKiB9TMlW%2BkI8XnPUBLK%2BOtPgZxBjrxEMgRAiEAvETGIUnp2HGGWJtFUVrsRVJ1NPf7xELnMxi7of8aYsEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIBCpxxN3tjLfdpo3SrcAzs%2BIq%2BT3q5pUDdPN4mXE1NGwYHk9NifmfHTnzOxUjCbIJlhyJg6XKSJFuAFGI4SyrQ%2BN9bgLKi5b%2BghJEEfcajC53uaTYfTl6okVq8QzdGeiAB%2FkFFoDv7XzlZ7sECtqPJVglsgstMHn4N5ZZqKUPebRPt5UZn3%2FNayPcYqzdaskLZY3i2ex64KcmlmSv127eO%2Fm1D2chJWWvRaBWWOLqQwahbyW26tC9n9xFzWJSo8rst%2Bu3mS24UjaS6fYUfdcZ%2BHzIozNACIlHoXezuE%2F%2F%2B4zWwQ4aqy02yJgKbLbDdx%2BDL297c6LOnQucCrotG1B2T0B5J8kJL8lNiGbAuFNhwkFKOhUaO5AyZsogoLPDH5sMMkdEAT7NurbeLGO%2BbIXaUSeWca25D89D58PYkxMUdTaPsgV7I4Ts5PhkoCldiZnssUPQPQ2eYLdzbE6IHYkJU35jQg0cofxhuPqpmyQfKBHIF9OYth%2Bw7hK%2Ft45xWQqtxkdWConBzxUJgyBjNkv70p3sK4lWGTiyFKJAnvris8%2BT%2FYUYeFpLngtcTcga3c%2FeyuxGBsTfRi80f4h6pgavPdIGnpw3glCdNyMTyZYbZlP%2BXZXhkL4JPdMfYt9aTkskuIkR5B1gyKHUK7MLrZrckGOqUBStPJjk70EYGOFy1Ic8L%2Fe2IPMALSiXpu4RstdvdiwGYVDfJAhgpLAC1Ha5yxQj%2BOtUk6hiqp5zP3r0yMGt1T7LcHAFr3%2BBjvMzmA77Dg1jN2V48B6niyyWGvRNX9uc15VvVbj2u39q3khQ2j4IVe%2FQSRQO5fqK9%2B0DmTfHvM9W5NlhtHYD%2BoTXIaz2zdtAkfFCXylovGTJHprknudF5D1Qjzkf88&X-Amz-Signature=417b200b9f460858e22a8310c20fe80d54f9ea05e618f9764436b6473a5f057e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


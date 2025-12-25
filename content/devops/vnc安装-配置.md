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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H3TPZA2%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIE2jQ6ITjc01PlI0746x4PylIScI7j6SEMG%2FsOgexsS4AiEAzg2rn3vwIImt1ZYR1MD3DlouPrgPwKczzMdCPckW5dgq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCkUwWdwmOD%2FFOa60yrcA0Dhy6EGTMjT7anSTGxlgysFB0S65cE%2B5RcT%2BVUnVZbF3NSTkm4f7pCQuERtChP4A5yZcsdrZU1WDGpLEoyiP9Q2MBmi73DXvQIPFpWBoUFjGltmftw95pDTNdAQOll0SEnfk17qgpBujRB3dPGhRUKgyxGTm9AlaWMfv65So1EGT2lPkmkO4W3sJnsO%2BU%2BcIme4MaszlgCsk753B7%2BGBAdO4BH94B4KMH2ySCP09oqDdgeZSEnOXclYVZDjysdB9QDg5LjCISCJXoYmriQFhBTcxM05NQZ2LohrplN%2FveXZbTTybdXS11m5ssANNZtSD7NUnWhgwYXp%2FFa4CfZRU0bOvFi52KhzCPu3UwWPbH%2F4BJD%2BmfY%2Bs47WRdbgLOnLMQIki2DmKe9fcoPxhtTWhmRMA6CIJ9124wJoP9Gu38jTRsGfJnOOFv%2B2PnYNqvC2N5B%2BUZkuIOMufvy1RsviQYB6LIeBATxkqgPZGxKrVgh5kL%2Fw4sAxoN%2BBGRoiMlVUb8%2Fwo2E1U%2Bmx%2FQ1k4ARAWwq8j%2FMAV%2BjQhWRwdvD99bvmDfN%2BHk0garoXCZLudG8qJo9RJlrEm7ZQdZ5I51hfMKZ1bQFyXHmoRr3nzlx2Yz2t6BzRGc5y8%2FmjrIuXMOalssoGOqUB3VToYh8%2FmlESU6kzynyd1ZQQvIZk2c2t6ddQrYy7euo6Q81kjQv%2B2G1qYd5sT%2BSPw6PZkrFVGQWOUfUWCcFJFOOB9X73CMPFfiCH4tCLY%2FfRCltaXN3yYafS7T4wqi0nkjAkIX6I6BWGfOFPGjecZt0VhIzKR3efik8qI1SMgAXAAdwX0SI4V%2FoLyBWBacVWMu0ezl1MObjMBO6vbo1Kbv0SxbZ9&X-Amz-Signature=d4accc2e7910bd2b97100337e758cfdb7a1ed4430bd3a21710069fef4d0cb00d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H3TPZA2%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIE2jQ6ITjc01PlI0746x4PylIScI7j6SEMG%2FsOgexsS4AiEAzg2rn3vwIImt1ZYR1MD3DlouPrgPwKczzMdCPckW5dgq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCkUwWdwmOD%2FFOa60yrcA0Dhy6EGTMjT7anSTGxlgysFB0S65cE%2B5RcT%2BVUnVZbF3NSTkm4f7pCQuERtChP4A5yZcsdrZU1WDGpLEoyiP9Q2MBmi73DXvQIPFpWBoUFjGltmftw95pDTNdAQOll0SEnfk17qgpBujRB3dPGhRUKgyxGTm9AlaWMfv65So1EGT2lPkmkO4W3sJnsO%2BU%2BcIme4MaszlgCsk753B7%2BGBAdO4BH94B4KMH2ySCP09oqDdgeZSEnOXclYVZDjysdB9QDg5LjCISCJXoYmriQFhBTcxM05NQZ2LohrplN%2FveXZbTTybdXS11m5ssANNZtSD7NUnWhgwYXp%2FFa4CfZRU0bOvFi52KhzCPu3UwWPbH%2F4BJD%2BmfY%2Bs47WRdbgLOnLMQIki2DmKe9fcoPxhtTWhmRMA6CIJ9124wJoP9Gu38jTRsGfJnOOFv%2B2PnYNqvC2N5B%2BUZkuIOMufvy1RsviQYB6LIeBATxkqgPZGxKrVgh5kL%2Fw4sAxoN%2BBGRoiMlVUb8%2Fwo2E1U%2Bmx%2FQ1k4ARAWwq8j%2FMAV%2BjQhWRwdvD99bvmDfN%2BHk0garoXCZLudG8qJo9RJlrEm7ZQdZ5I51hfMKZ1bQFyXHmoRr3nzlx2Yz2t6BzRGc5y8%2FmjrIuXMOalssoGOqUB3VToYh8%2FmlESU6kzynyd1ZQQvIZk2c2t6ddQrYy7euo6Q81kjQv%2B2G1qYd5sT%2BSPw6PZkrFVGQWOUfUWCcFJFOOB9X73CMPFfiCH4tCLY%2FfRCltaXN3yYafS7T4wqi0nkjAkIX6I6BWGfOFPGjecZt0VhIzKR3efik8qI1SMgAXAAdwX0SI4V%2FoLyBWBacVWMu0ezl1MObjMBO6vbo1Kbv0SxbZ9&X-Amz-Signature=e37264701a85be1d80079eb1d46449a460671e717ca1d73776d30f32f4ad5910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6AWGPHO%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDyV6VeDOLeKounTDxJpUIilyGoGm5roICcHQEoyuBL5QIhAJpYb7bvKibKAYxZ8Ruo5%2Bs1gm0VezhguJp8WmYHsy2kKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3Jg96jfZ%2FVvedh40q3AMFNEW2Xp8aY31yi5qIC3HrEMltvA0%2BTv0DlymKJYP7qxeNQ78uhCFPDaq3rrkL5%2FgvAjo9Bewpj4CLw3EtF9UeucKQUdxO9lAA7Nkx0G%2FOVEyy%2BjRXaBi%2BOrW8%2BPTWs6CYeSkMl%2BCNGWlyxGtwvdE8eT7Nteu20wXYGa46WxVjVGlrDEOjC2w0cyhwI36qEr8NobEw1gfZEmwBJdoHBpKr933pZcSR4Hc%2BiYXcv9QGhKkOUyCGLpQ53ki%2FC6x4iAhzaRG3FbYjadImV83qzgP2J389v7PmB3vnRG5pV2%2BRhmitwnAjgb4w5O5hz3F0XAbtPlAXJP0jg60rhWXCGfJh64LqJykKE02GYwPYFJv%2BssBxhZevlH3%2FOC348G3GnjAkBmUPFWlvJ92vxuKgVHirbYXiy2BXVx94LUWLNxwPUP5RJjA0q5%2F3LRmhCisaW51plqKFUhjo8rgquyH8nGysV8y%2F4UiIa5c%2B3LOZR3EJ15XF9E4PT3esDAx0Ya1dgunM9JNgQ422h3%2BxVWFVrfN4p8e61qkfg%2BdX40BfHkIEpCACvk4cZtDJiiRLhD7NdJv3kS1JLWSLM4e%2Fh5I%2BIZs0fr4sV%2FpKCliWlVDEb%2BG0YUdpNN9FS2rjklFpYTC43JDPBjqkAZtj918L7d4%2BeB29raHnsPscSVjuUb62EzrFSPRDz9bzOTMyKTJUGYAcDazO325eBbcdfWwZ91Hqn%2FIPrm0RoMqIW1GiLln%2BYl1XDBUuOa6v6gabg%2FRxwI7zEZirPs7GYwgbNfo5Iw%2BdQaJR8pPSwYPJnZPFb7xUrBhZzmrBMxgrgU3M1wpKsm5bZ3%2FOy%2BcuIs4Z6QO5ENOA%2Bz%2BcrvozdFqW%2FA9Y&X-Amz-Signature=1c0014e51377e8a9f820b5f6dae79da48ebc95a8382424f95776c58a98d2164d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6AWGPHO%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDyV6VeDOLeKounTDxJpUIilyGoGm5roICcHQEoyuBL5QIhAJpYb7bvKibKAYxZ8Ruo5%2Bs1gm0VezhguJp8WmYHsy2kKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3Jg96jfZ%2FVvedh40q3AMFNEW2Xp8aY31yi5qIC3HrEMltvA0%2BTv0DlymKJYP7qxeNQ78uhCFPDaq3rrkL5%2FgvAjo9Bewpj4CLw3EtF9UeucKQUdxO9lAA7Nkx0G%2FOVEyy%2BjRXaBi%2BOrW8%2BPTWs6CYeSkMl%2BCNGWlyxGtwvdE8eT7Nteu20wXYGa46WxVjVGlrDEOjC2w0cyhwI36qEr8NobEw1gfZEmwBJdoHBpKr933pZcSR4Hc%2BiYXcv9QGhKkOUyCGLpQ53ki%2FC6x4iAhzaRG3FbYjadImV83qzgP2J389v7PmB3vnRG5pV2%2BRhmitwnAjgb4w5O5hz3F0XAbtPlAXJP0jg60rhWXCGfJh64LqJykKE02GYwPYFJv%2BssBxhZevlH3%2FOC348G3GnjAkBmUPFWlvJ92vxuKgVHirbYXiy2BXVx94LUWLNxwPUP5RJjA0q5%2F3LRmhCisaW51plqKFUhjo8rgquyH8nGysV8y%2F4UiIa5c%2B3LOZR3EJ15XF9E4PT3esDAx0Ya1dgunM9JNgQ422h3%2BxVWFVrfN4p8e61qkfg%2BdX40BfHkIEpCACvk4cZtDJiiRLhD7NdJv3kS1JLWSLM4e%2Fh5I%2BIZs0fr4sV%2FpKCliWlVDEb%2BG0YUdpNN9FS2rjklFpYTC43JDPBjqkAZtj918L7d4%2BeB29raHnsPscSVjuUb62EzrFSPRDz9bzOTMyKTJUGYAcDazO325eBbcdfWwZ91Hqn%2FIPrm0RoMqIW1GiLln%2BYl1XDBUuOa6v6gabg%2FRxwI7zEZirPs7GYwgbNfo5Iw%2BdQaJR8pPSwYPJnZPFb7xUrBhZzmrBMxgrgU3M1wpKsm5bZ3%2FOy%2BcuIs4Z6QO5ENOA%2Bz%2BcrvozdFqW%2FA9Y&X-Amz-Signature=b74695ed4c4091ef75967462b59163dfb84093a50d69587d76f6e496d015752a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


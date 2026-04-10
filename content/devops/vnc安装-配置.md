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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXUEFHVM%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIC4CAEiYjjdbti7GFvFZiHm9SJRqksJf%2B7jGaI7Xs1MTAiAoyL2cJZjBAeZdCGzKG4CYzhjmKLx%2BLhMA0Q7f1z%2B6FSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMWCtmpZcMsU8nbCceKtwDPG7UtRJi0bGdN0Cj8rmPUeJCmmmJiZRWyh5UErR1GOIwVJ%2Fj0o0dtZWLcibIMGy%2BCb%2BitIvqQUtLlg03wDsBx5UWC%2F06hLtFruoIckgfIhnUnoD1nQ5rafIOwItFGdn9P4Bbakm4tdhGe1YGlaGGsMT%2BcE2WKN4VxIXrGmbuCGDtLfa%2FE%2Fc5Gl%2BKvY4mujTIyn9FO0XVA4ogFVT1Yfbvl1oAca0nGtaScMhu9zSA86e8%2FCBFpoExA4jCp4vKDYA9OmPpinF6ve8JQ5%2FZRdDCF0cAME8mm%2BuIeYzR1DH%2FRwXSCQXxi%2F%2BI8mx4fHwq%2BFToEdEeHeEZvWpphZM8jz4%2FcbCcyeb2DaOhnxGnYwzm7QABnoK6rC2C41IbLAhVaFwvp%2Bo0O%2FgG7SmUWXW2m3ajOTIayQ1wE4zXa77znfPRF%2BiAQJigs48rNifPAZ%2Fzzfk4M2dMwanqbcSUayLjaUazip3KNwRg8QiLMtPWoz0SR12QXk18f1LP6%2BlzubmYJeHkm9mQRqgj1HA8Po5FJJjNiLYh93S5imCpiLgUN7DwX3rxilWSeaPUeYMc9hw%2BsTDZu5bOdRoE4HzfOAwaOzIlWVGXIuU7ysGXd3kU1MW13fB0LGO%2BQB4yPCBlBtcw%2BcPhzgY6pgHi1fIZe2FSmH8na5DJ60gTmkMHYd988UvSDFMwC2hIbMb6JPwjct8SYry53DFC1eFVMBbR1xiGCiAq21BJjYfkHkzScFg7yrotdjx4nOqigayFrASjZrCiy%2FwPiBaNsbOgI5kvBRYAVIqWPX%2BwXrQboItWO9VoieSq8h5wLbjPFqA2ENA4z%2BTn9kV7ClI0MH5IUCqIWUvHGyzzzmjzydY%2FMlum0i51&X-Amz-Signature=05bdc391f6d6f556fc14cbebbe835586792167df3c9f7c040bc192128ecf6633&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXUEFHVM%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIC4CAEiYjjdbti7GFvFZiHm9SJRqksJf%2B7jGaI7Xs1MTAiAoyL2cJZjBAeZdCGzKG4CYzhjmKLx%2BLhMA0Q7f1z%2B6FSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMWCtmpZcMsU8nbCceKtwDPG7UtRJi0bGdN0Cj8rmPUeJCmmmJiZRWyh5UErR1GOIwVJ%2Fj0o0dtZWLcibIMGy%2BCb%2BitIvqQUtLlg03wDsBx5UWC%2F06hLtFruoIckgfIhnUnoD1nQ5rafIOwItFGdn9P4Bbakm4tdhGe1YGlaGGsMT%2BcE2WKN4VxIXrGmbuCGDtLfa%2FE%2Fc5Gl%2BKvY4mujTIyn9FO0XVA4ogFVT1Yfbvl1oAca0nGtaScMhu9zSA86e8%2FCBFpoExA4jCp4vKDYA9OmPpinF6ve8JQ5%2FZRdDCF0cAME8mm%2BuIeYzR1DH%2FRwXSCQXxi%2F%2BI8mx4fHwq%2BFToEdEeHeEZvWpphZM8jz4%2FcbCcyeb2DaOhnxGnYwzm7QABnoK6rC2C41IbLAhVaFwvp%2Bo0O%2FgG7SmUWXW2m3ajOTIayQ1wE4zXa77znfPRF%2BiAQJigs48rNifPAZ%2Fzzfk4M2dMwanqbcSUayLjaUazip3KNwRg8QiLMtPWoz0SR12QXk18f1LP6%2BlzubmYJeHkm9mQRqgj1HA8Po5FJJjNiLYh93S5imCpiLgUN7DwX3rxilWSeaPUeYMc9hw%2BsTDZu5bOdRoE4HzfOAwaOzIlWVGXIuU7ysGXd3kU1MW13fB0LGO%2BQB4yPCBlBtcw%2BcPhzgY6pgHi1fIZe2FSmH8na5DJ60gTmkMHYd988UvSDFMwC2hIbMb6JPwjct8SYry53DFC1eFVMBbR1xiGCiAq21BJjYfkHkzScFg7yrotdjx4nOqigayFrASjZrCiy%2FwPiBaNsbOgI5kvBRYAVIqWPX%2BwXrQboItWO9VoieSq8h5wLbjPFqA2ENA4z%2BTn9kV7ClI0MH5IUCqIWUvHGyzzzmjzydY%2FMlum0i51&X-Amz-Signature=e3e2f796cb517fc4bfc3096b3e979a97fac6d9f2f41c44e4452917ec589c0060&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCB7LMTR%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEo4hWPirn1gdRabn9ZIIEXu6kO7oqUUN4BuZ5BO19%2FTAiANPk4fDXYc%2F9J%2FOfT9m5u4A3ITxplgER5Jn9NW39mKhCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIML%2FgkCoiX33cdWodyKtwDfHAEtmxCu%2BBIksT3M39M6KqFlIcE1gtHohLT0S8ifa0lCTWgEm0EFrn%2BgsgmZ8rAInyyrPI5OcpNlYkHaWy4SpQdzwKxoqEwLy%2BF1CGQ4KYqpweUHnpKCJn%2BXzNoKU5Ri1wVTqNW589gC8XMq2aU2NYCi1sC3N6Tpte1ZIDdR9bUs4suaxn8SOzXEQFgZF3Fjx%2Bso2uFH88f2y3mSuxjDgRC0zcXH5dozd%2FKbm8immwsvheoWPZMBK23hhV66UhwAHkQyO7rfwEEGP%2FA0KXE8IxUd6frK2AHvP70lPjDYjoC0WffcLW2MelSc2Cwcb2M1bEjdFHEat2ore5h3kBu9pwQpqjQQpeKPkdIe8M3uRHxtINXPjCZue1A44OlNrTyAmQrILv%2BsfxpPQR3nIhOHBHpZjGTF%2B3PCFmO7veA4J72pvlXFDXMCcsNrqA%2BbmU4MHyx927ah1dbK%2FPhaWTlXI6%2BtKbOIV3U%2FR7QqbEAjGnMG9Ty92NB2JP48cDOUb%2FIcqEdC8msNfje2C4A3NpjqnMOawq81rzZzlkHjiC4Z6FuXQDTVnp4fJEX2aCmXEX%2BJhzGAz%2FtXq1QCIaWBp1JG3rU6zAsMDdVItDs25saNLIAzVPDlcqto5l%2FL1Yw0NulzwY6pgH3WXdqNnvzOIp46WjPWtgPwtx%2BQZfv2Me9HToxvk0eYrsubo5%2BPlJaTkOsaORxZdFbB%2BMTmueosYiYpC%2Bvgwv1ikQAVfQut%2FMGpVD78xTZSBplqrsycKr9sMkXmimBofZ1vu9avXNILHMhMnEINryLCKbQlLjwz7enCJHphOhdCNrHSy9tQc2t1ua%2BpdfPbp1kG4wA%2FAUypNWJq3wmTUG4hNk0frdc&X-Amz-Signature=d3da25da50613d282b90be6d87385a054009ff76181a1d13b3d4eaa296fb6793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCB7LMTR%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEo4hWPirn1gdRabn9ZIIEXu6kO7oqUUN4BuZ5BO19%2FTAiANPk4fDXYc%2F9J%2FOfT9m5u4A3ITxplgER5Jn9NW39mKhCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIML%2FgkCoiX33cdWodyKtwDfHAEtmxCu%2BBIksT3M39M6KqFlIcE1gtHohLT0S8ifa0lCTWgEm0EFrn%2BgsgmZ8rAInyyrPI5OcpNlYkHaWy4SpQdzwKxoqEwLy%2BF1CGQ4KYqpweUHnpKCJn%2BXzNoKU5Ri1wVTqNW589gC8XMq2aU2NYCi1sC3N6Tpte1ZIDdR9bUs4suaxn8SOzXEQFgZF3Fjx%2Bso2uFH88f2y3mSuxjDgRC0zcXH5dozd%2FKbm8immwsvheoWPZMBK23hhV66UhwAHkQyO7rfwEEGP%2FA0KXE8IxUd6frK2AHvP70lPjDYjoC0WffcLW2MelSc2Cwcb2M1bEjdFHEat2ore5h3kBu9pwQpqjQQpeKPkdIe8M3uRHxtINXPjCZue1A44OlNrTyAmQrILv%2BsfxpPQR3nIhOHBHpZjGTF%2B3PCFmO7veA4J72pvlXFDXMCcsNrqA%2BbmU4MHyx927ah1dbK%2FPhaWTlXI6%2BtKbOIV3U%2FR7QqbEAjGnMG9Ty92NB2JP48cDOUb%2FIcqEdC8msNfje2C4A3NpjqnMOawq81rzZzlkHjiC4Z6FuXQDTVnp4fJEX2aCmXEX%2BJhzGAz%2FtXq1QCIaWBp1JG3rU6zAsMDdVItDs25saNLIAzVPDlcqto5l%2FL1Yw0NulzwY6pgH3WXdqNnvzOIp46WjPWtgPwtx%2BQZfv2Me9HToxvk0eYrsubo5%2BPlJaTkOsaORxZdFbB%2BMTmueosYiYpC%2Bvgwv1ikQAVfQut%2FMGpVD78xTZSBplqrsycKr9sMkXmimBofZ1vu9avXNILHMhMnEINryLCKbQlLjwz7enCJHphOhdCNrHSy9tQc2t1ua%2BpdfPbp1kG4wA%2FAUypNWJq3wmTUG4hNk0frdc&X-Amz-Signature=3ae03afb2a5427c69fed7e9c6c96921f6de2f5d0219c44445a53dd107775057b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJEZ6SOJ%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIBxKKOV0bZug9CdUs0jJVbf7m3V8jMaE1Sf1izG375jsAiAjSRIGIb3NdwTLXZVIK29d69kzTO%2FyrErlU2W4ONfZ2Sr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIM1Eozxzi%2B%2F1cgNQW0KtwDc3INPEPZ9inkCvAZKPV%2FuTgrIntB0uZ82EsjohMS09YQAcu0ePDKJJvVOqmSfS2PgIRbWCLgbm8pLDK%2Fk8f38C4Tx8RmeB%2FPVfx4YT1AxSyWMv6UZwqCGtYv7AKHy%2BwRGitUezSYhZu7WjBOodSZIkvSw5soo3lebcT3I%2B4epDQeXhMGvxB3pxhGVDTDNmxMMP8GimgPZdhKbUGKoGqKjEwA4osKIsrQH0%2FSMVDPV8zXsCmDD9iOxYFMkbfJI5MAqEsRkpPuD%2BSphiwwEC%2FBV9naKqeU1ek8Sfo5d8N4LPB8mWeWUf7Z1840yuDknwOFsi8o7T54YWmWo2Luu1VXKhBgn2AHCh0EryI59cJJ85mF%2F7SfKM134C8av9NbrNOoNP%2BxY3wdm41QxV1xzgwiVVfWhsuCBFz2LJpTT%2Bk0yxhezyml%2Fzyk31Xl%2BawfwszbdejcZZ1SlMrEjiFjdd67vrxUOYXzgOf6Qgk%2Bb7LCkme3okgLbhr4J8E%2BSUDq6KVPPxnU%2FYRVOBoNMwW8X3g%2BwaCbaTHFn8Hy7bTvtciIlwWfF%2F8GGNjsZCTzvq23sEzVKdRIAdBPGsQmCSiMdXvk3ZUuxNYJDjNjSX8ugMom7fwckB6XBVn%2F%2BKcAsocwpIT5zAY6pgHEoxQ92GirVbSr4obuFKHkYmynzrWrA1RKEZXeFHflPbpmE7ko5laWSYrMeGYuNcAxu1HLVRkD%2FyWjzzynBiU%2Fe%2FQeBdqOdxGLDeEXi%2B9qBsJCsAw60KrBuSX4oPnlSdYA2X4DXZFn9%2FovlwmGZDaSUc4%2FaP4gVIGh8s8tClHX3zpPpKqb%2FHaUBz21LixyTzdXKkw3jjMfvuQbF5fUFrgQe1IH9zRc&X-Amz-Signature=1755a94a90f54d9dcfc9ae2c69d59cf84c3e03ad51e67ee65f6054027b0c8f8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJEZ6SOJ%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIBxKKOV0bZug9CdUs0jJVbf7m3V8jMaE1Sf1izG375jsAiAjSRIGIb3NdwTLXZVIK29d69kzTO%2FyrErlU2W4ONfZ2Sr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIM1Eozxzi%2B%2F1cgNQW0KtwDc3INPEPZ9inkCvAZKPV%2FuTgrIntB0uZ82EsjohMS09YQAcu0ePDKJJvVOqmSfS2PgIRbWCLgbm8pLDK%2Fk8f38C4Tx8RmeB%2FPVfx4YT1AxSyWMv6UZwqCGtYv7AKHy%2BwRGitUezSYhZu7WjBOodSZIkvSw5soo3lebcT3I%2B4epDQeXhMGvxB3pxhGVDTDNmxMMP8GimgPZdhKbUGKoGqKjEwA4osKIsrQH0%2FSMVDPV8zXsCmDD9iOxYFMkbfJI5MAqEsRkpPuD%2BSphiwwEC%2FBV9naKqeU1ek8Sfo5d8N4LPB8mWeWUf7Z1840yuDknwOFsi8o7T54YWmWo2Luu1VXKhBgn2AHCh0EryI59cJJ85mF%2F7SfKM134C8av9NbrNOoNP%2BxY3wdm41QxV1xzgwiVVfWhsuCBFz2LJpTT%2Bk0yxhezyml%2Fzyk31Xl%2BawfwszbdejcZZ1SlMrEjiFjdd67vrxUOYXzgOf6Qgk%2Bb7LCkme3okgLbhr4J8E%2BSUDq6KVPPxnU%2FYRVOBoNMwW8X3g%2BwaCbaTHFn8Hy7bTvtciIlwWfF%2F8GGNjsZCTzvq23sEzVKdRIAdBPGsQmCSiMdXvk3ZUuxNYJDjNjSX8ugMom7fwckB6XBVn%2F%2BKcAsocwpIT5zAY6pgHEoxQ92GirVbSr4obuFKHkYmynzrWrA1RKEZXeFHflPbpmE7ko5laWSYrMeGYuNcAxu1HLVRkD%2FyWjzzynBiU%2Fe%2FQeBdqOdxGLDeEXi%2B9qBsJCsAw60KrBuSX4oPnlSdYA2X4DXZFn9%2FovlwmGZDaSUc4%2FaP4gVIGh8s8tClHX3zpPpKqb%2FHaUBz21LixyTzdXKkw3jjMfvuQbF5fUFrgQe1IH9zRc&X-Amz-Signature=546391371d792f37e87ccecc845904dea234a3d2a82b3698af4533290e72494f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


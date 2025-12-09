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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCG7QGIB%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoE6MY5cLJYAasYmV7o3YaE8tdNEcIIZ%2Fh%2FByuvazIcAiEA2RPQZUNV%2FyX03LALK9NgX4faXQiv8iuE5z2dNmT8r7MqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD29TgpyFALmpHkGgircA8NTdcXY9C1CihhscmtQ8qqbFSiu7Ay17CXuFBV3UXktfEXPRQcOBHQBiU72EWTEZ0bj%2BnHyuXqUD7VtBWMP7X8E1BUNT40vWVchqI2c26VA11t9Gnyiod75WWQTEWmb5UDHFd6nUH31%2BaBh1bzq3k2AuF6cLFqrw3i005orxWNGeZswwZtQLKQVMVN23sERGh7CmAjqb4UwNDQYFpMDaPiTP%2BUvXRpyEnOzrcWgubteXdcKqdmviiWQx4xCgMatbUgXL3eV89sXabSnRMgm12WLbTYwf2gNfw4km%2FuXL0HX%2FQ%2FaGOOeOwzokO%2BZol2rGEAuqy7C%2BiNX%2FiDx2%2FLI18jZFEnSe0GS%2FbBtXokYj4f9X5aeabs9G%2B%2BCcQtvXsPRSwRqMWg0XFlnEzCMv72%2F8hHO5dFsX27ExkIqmUlBVxT%2F%2F%2FvuOJAt1RMICvIzG3MvcaiRPNTHMM%2FEGl1AV4jo1V%2FK9aSZ2o66sOhV9VWVokMC2aQYC2PsIdc6XUTCFrGzIIjRKx4FIDaIY9f9UJtFC6VRcrRRZy2Y7nf4sryAVAWq2oPNYpX6%2B0GuDnPaxhnkf5SAQl7GBxpHwXKH3f8JZsLzlAd3o0VuF6sskToDTn394GeEXi3I6l%2FdmOhqMP%2BO3skGOqUBqrg356DmBaK11%2BMk6GbXg4fFktcJRnPXWQvVAS6x2rxtVkLOXMh7n7RdpGZfB%2FpLGBmRyYDZ6payVpnjjr3N0GFtCBGumw4uZC6Ey2Y4JgosgCD0OG1q86sUs%2Fu6%2BhmUofoTqrQyG8qdXB5yPJ%2B85EtufYEWrp319FLg1zTXreV1vbkqm10f128Odgva98%2BQ7OyIdER4B14FIErepyn7ni%2BF%2Buze&X-Amz-Signature=6042b89ba50ed9082680f307a563d100dca99ec1fa99710534dd98fc63adb056&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCG7QGIB%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoE6MY5cLJYAasYmV7o3YaE8tdNEcIIZ%2Fh%2FByuvazIcAiEA2RPQZUNV%2FyX03LALK9NgX4faXQiv8iuE5z2dNmT8r7MqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD29TgpyFALmpHkGgircA8NTdcXY9C1CihhscmtQ8qqbFSiu7Ay17CXuFBV3UXktfEXPRQcOBHQBiU72EWTEZ0bj%2BnHyuXqUD7VtBWMP7X8E1BUNT40vWVchqI2c26VA11t9Gnyiod75WWQTEWmb5UDHFd6nUH31%2BaBh1bzq3k2AuF6cLFqrw3i005orxWNGeZswwZtQLKQVMVN23sERGh7CmAjqb4UwNDQYFpMDaPiTP%2BUvXRpyEnOzrcWgubteXdcKqdmviiWQx4xCgMatbUgXL3eV89sXabSnRMgm12WLbTYwf2gNfw4km%2FuXL0HX%2FQ%2FaGOOeOwzokO%2BZol2rGEAuqy7C%2BiNX%2FiDx2%2FLI18jZFEnSe0GS%2FbBtXokYj4f9X5aeabs9G%2B%2BCcQtvXsPRSwRqMWg0XFlnEzCMv72%2F8hHO5dFsX27ExkIqmUlBVxT%2F%2F%2FvuOJAt1RMICvIzG3MvcaiRPNTHMM%2FEGl1AV4jo1V%2FK9aSZ2o66sOhV9VWVokMC2aQYC2PsIdc6XUTCFrGzIIjRKx4FIDaIY9f9UJtFC6VRcrRRZy2Y7nf4sryAVAWq2oPNYpX6%2B0GuDnPaxhnkf5SAQl7GBxpHwXKH3f8JZsLzlAd3o0VuF6sskToDTn394GeEXi3I6l%2FdmOhqMP%2BO3skGOqUBqrg356DmBaK11%2BMk6GbXg4fFktcJRnPXWQvVAS6x2rxtVkLOXMh7n7RdpGZfB%2FpLGBmRyYDZ6payVpnjjr3N0GFtCBGumw4uZC6Ey2Y4JgosgCD0OG1q86sUs%2Fu6%2BhmUofoTqrQyG8qdXB5yPJ%2B85EtufYEWrp319FLg1zTXreV1vbkqm10f128Odgva98%2BQ7OyIdER4B14FIErepyn7ni%2BF%2Buze&X-Amz-Signature=3e39b348f5e3443ab6da11a02e66d166a1d54a2aa67b799bf50ab291112a1300&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


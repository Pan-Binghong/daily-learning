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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBI47KWG%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIE6gvabaPLBnwzGosRWL7axaObs40VJVP4%2FRMV2oEi3%2FAiEAmmXQGT9CKXA4G2Zoic%2Bd0aluv8YRp7AIGJdO3PzJZ3sqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMrJNPNoI4Ex6oDUcCrcAwrrN%2Bbv0mH7qZbKcxNOoJ%2By8HO2Pp5TG9nn5PiWvJqFU4T33mhuHxCa5yvwvs%2B9gj485x23dys%2FZekx8YKrfgSoSZVPIKjTT1SLSz3yVJkE%2BM3bcr49SMevfxO3kI8HIzPdfvvddjgsO%2FV7U2GfpuiBAyRP9MA3mtI37ITtZzwD2UA13DClrtlJHRHPMecmrSYLtNllxxGUZGjtah%2BxJ%2Ft8GMjeb0V9wgnqlPSdHFl5h8BgZIdW2YDtBpEgVaoQtuiBGiGGqVvCWfVTCm%2FxK%2F9EgPt%2FJiw5KeWVJPrdPq3i%2BtCXB%2BbDX%2BpSF5nmIAtGtlPQu7Dpv0SXdWF10qeaH8FroaPVLchDhQXX3zbPATyOcFAJbVbQWr2pHhzSe1%2FBt%2B9zASjinhNtwO%2FknhgTB4p%2F3Ef0c2N825rc6JQRqNmXK5lRqzOKU28ZcJjJ2qWe1dRKmfvsgAzang1JSw50nKBWkVdn5Hs2rWxqgBRoZAjX7wl8IAD1sAOxmc9AX9aXiwAB5sdmufC4O8oruLwPh2nx0BvkVuR9Dhuvv9PyzwAkmRAxx2JGayETIukkO7ZKkSd8LtFBrFCvYhkIXoyRdEIY8usXRXBEpxC5DOzA8mYekwz1%2FKkkGibGQT%2FCMNb00c4GOqUB%2B8pBlIsd29jysRWNkSoEOlNjyUy%2BrlI%2FhcTCAfgP7buFn1ybku2BZYXHiT3Kh6TDpFKIRWGkPyFAFlhAvh2Boy0OFw4Xf5DZNnJLmEBKJrTjgAeRNjZTBiZWtoJjLROm%2Bqu3XA8L2r3FWfowvMoSORtyCMgeEbcoS7unQYaBl03eMuX4E6mCKDOyKDuyI9546vN%2BIN434gQ2xzRPKQ9utNsiRMVw&X-Amz-Signature=660aac2c323f38522559b3de642e8af01f7861f5abdc5eef859be4e8d670332b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBI47KWG%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIE6gvabaPLBnwzGosRWL7axaObs40VJVP4%2FRMV2oEi3%2FAiEAmmXQGT9CKXA4G2Zoic%2Bd0aluv8YRp7AIGJdO3PzJZ3sqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMrJNPNoI4Ex6oDUcCrcAwrrN%2Bbv0mH7qZbKcxNOoJ%2By8HO2Pp5TG9nn5PiWvJqFU4T33mhuHxCa5yvwvs%2B9gj485x23dys%2FZekx8YKrfgSoSZVPIKjTT1SLSz3yVJkE%2BM3bcr49SMevfxO3kI8HIzPdfvvddjgsO%2FV7U2GfpuiBAyRP9MA3mtI37ITtZzwD2UA13DClrtlJHRHPMecmrSYLtNllxxGUZGjtah%2BxJ%2Ft8GMjeb0V9wgnqlPSdHFl5h8BgZIdW2YDtBpEgVaoQtuiBGiGGqVvCWfVTCm%2FxK%2F9EgPt%2FJiw5KeWVJPrdPq3i%2BtCXB%2BbDX%2BpSF5nmIAtGtlPQu7Dpv0SXdWF10qeaH8FroaPVLchDhQXX3zbPATyOcFAJbVbQWr2pHhzSe1%2FBt%2B9zASjinhNtwO%2FknhgTB4p%2F3Ef0c2N825rc6JQRqNmXK5lRqzOKU28ZcJjJ2qWe1dRKmfvsgAzang1JSw50nKBWkVdn5Hs2rWxqgBRoZAjX7wl8IAD1sAOxmc9AX9aXiwAB5sdmufC4O8oruLwPh2nx0BvkVuR9Dhuvv9PyzwAkmRAxx2JGayETIukkO7ZKkSd8LtFBrFCvYhkIXoyRdEIY8usXRXBEpxC5DOzA8mYekwz1%2FKkkGibGQT%2FCMNb00c4GOqUB%2B8pBlIsd29jysRWNkSoEOlNjyUy%2BrlI%2FhcTCAfgP7buFn1ybku2BZYXHiT3Kh6TDpFKIRWGkPyFAFlhAvh2Boy0OFw4Xf5DZNnJLmEBKJrTjgAeRNjZTBiZWtoJjLROm%2Bqu3XA8L2r3FWfowvMoSORtyCMgeEbcoS7unQYaBl03eMuX4E6mCKDOyKDuyI9546vN%2BIN434gQ2xzRPKQ9utNsiRMVw&X-Amz-Signature=0e0387ab5d6e4afe55bf811d60ec43ac935c4c6421faddf89d07158eec761cb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


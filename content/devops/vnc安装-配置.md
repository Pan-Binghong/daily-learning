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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKZEVZRQ%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPT0d1ru5z%2FswY9XjUjeHmmtgKBuWQP6ZX%2Fhvg7CCl6wIgZpqyiZYvwynwYKTBRMNe%2FFRFsCtCjUQieA6y0MQt1dcqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIU8ZJsIt5WnIWtAircA5oAiyXZhvS47mbAJEW%2B%2Byn%2Fjfq%2B9Q43oOfVoFbqgNYog8tDOL4xH%2Fh8gGkxxw6i19%2Fz9scXvZChx5ey4FgrAq%2BHMwfCOPYGyroDQbLxAqE%2FhN7dygUPnNCluiCld7VzRaeToBXrcmj%2BFdaSFgF%2BXx8UOoJH096Hi2trvN%2FA6BO1DWsQ1VzFf7eBiYxAqeSOFxlaYaGir5i1zRHt3oFaVdGqZSBq2zirhFk54EOWn%2F6%2BVVAacCuIuk40idx0TUQIqBgeQB2liPhOw5SLoZLeX2CKCICwP8jdI5VLsNXe9rdfwCWCLrb%2BafHWvJkf5PpDuxPdBth4YHGI1jZhSn7Zqxlq3UIau5ImWBqmOngyoGpU0TH9Axi9XLebdbrtets7hl4KPFxOaxTK62yO%2BF9ola9btq6z%2FI8zwpzjU7W1vF%2BP9yP6eK%2FkqAC4eEEJp7nZ37pYkcDUPPlJ4a0gapAx7TiTb0Yv4H8cG0ZCY0onsx2%2BRTy09FAgmGFocsWYcxXb02J7frab8apkFFJetwB8zH87Y5%2BZPaAxeJRsXau3OIV3aA9Mp15PNG23NqcGuIrGUpCRrmSyIxrQtfuio3kynx81WoF80Y%2BsBiBuivqz1T5U%2Bu3dVCkpwEobnc4yMK%2BV%2FM4GOqUBNlhWBeWTtdmU19O47KmW93u1bs9cL6BSukWM1Chi7IVNkGlUH9ryx%2Fa7HlH%2FqPpFKgZILJBtyaMTwam9T0%2FyKez340G0%2Bv2wyWgy5ObUSTKlvZDhTJs4CiP7LcvDR1ANWRq3r%2Bb%2Fv684L3D%2FHJcHctCxehX5vbK%2FsoRU2tRBhSGp2OuFTEnTPMDYOpcff7WunXUpG4jLlmEv%2FaH3HzeGaikK%2FH9q&X-Amz-Signature=dc26b1a1a6d72eb5f9e36bcbc66a0bc3f77548e8946ddd75036f3498c12685a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKZEVZRQ%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPT0d1ru5z%2FswY9XjUjeHmmtgKBuWQP6ZX%2Fhvg7CCl6wIgZpqyiZYvwynwYKTBRMNe%2FFRFsCtCjUQieA6y0MQt1dcqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIU8ZJsIt5WnIWtAircA5oAiyXZhvS47mbAJEW%2B%2Byn%2Fjfq%2B9Q43oOfVoFbqgNYog8tDOL4xH%2Fh8gGkxxw6i19%2Fz9scXvZChx5ey4FgrAq%2BHMwfCOPYGyroDQbLxAqE%2FhN7dygUPnNCluiCld7VzRaeToBXrcmj%2BFdaSFgF%2BXx8UOoJH096Hi2trvN%2FA6BO1DWsQ1VzFf7eBiYxAqeSOFxlaYaGir5i1zRHt3oFaVdGqZSBq2zirhFk54EOWn%2F6%2BVVAacCuIuk40idx0TUQIqBgeQB2liPhOw5SLoZLeX2CKCICwP8jdI5VLsNXe9rdfwCWCLrb%2BafHWvJkf5PpDuxPdBth4YHGI1jZhSn7Zqxlq3UIau5ImWBqmOngyoGpU0TH9Axi9XLebdbrtets7hl4KPFxOaxTK62yO%2BF9ola9btq6z%2FI8zwpzjU7W1vF%2BP9yP6eK%2FkqAC4eEEJp7nZ37pYkcDUPPlJ4a0gapAx7TiTb0Yv4H8cG0ZCY0onsx2%2BRTy09FAgmGFocsWYcxXb02J7frab8apkFFJetwB8zH87Y5%2BZPaAxeJRsXau3OIV3aA9Mp15PNG23NqcGuIrGUpCRrmSyIxrQtfuio3kynx81WoF80Y%2BsBiBuivqz1T5U%2Bu3dVCkpwEobnc4yMK%2BV%2FM4GOqUBNlhWBeWTtdmU19O47KmW93u1bs9cL6BSukWM1Chi7IVNkGlUH9ryx%2Fa7HlH%2FqPpFKgZILJBtyaMTwam9T0%2FyKez340G0%2Bv2wyWgy5ObUSTKlvZDhTJs4CiP7LcvDR1ANWRq3r%2Bb%2Fv684L3D%2FHJcHctCxehX5vbK%2FsoRU2tRBhSGp2OuFTEnTPMDYOpcff7WunXUpG4jLlmEv%2FaH3HzeGaikK%2FH9q&X-Amz-Signature=93e62e95b6e4b748e2b572d861110945fee0947c1b740cec0dc64e20af98e653&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


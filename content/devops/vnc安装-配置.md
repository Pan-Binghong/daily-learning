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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626VF3GE4%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCICTZi3GbVy6Siz1tycU7ukxwmZweKXAMKFNGdUH8r9NmAiEAtgSawYSoeqSVjRZv9%2BCFEyw8RRVk3sKX2yaZolaw17YqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDACR1Wd4JSkdrT7QUCrcA%2FlldDVkRjqPEx75DzMN2pmLygmzA8TbdJaYc2%2B2FBl2kExjj15eVvAkwSzl7eAzzyuHE4SoY%2BBuo4yD7xTatXCsc5hP133%2BkG0iHx0TVy%2B%2FUXP%2Fh9elSgCT96dAauKlY2RGS7lgbpIj9rTuVyNuDmhxmkbbbJadoikyl9zY3itXmJqKU5zGAEOFCQS%2B50qyq65jkFMol6tUBxQyV9bKo7X69gggUNmXFbMfw70gpfcxsz7oh1nLDHACdq5UA50s9gIi0QmjOg2L6kg%2BMqO4oEY4YHQTGLFUXJDXwgy4IIbV0oy6gdshojxLuT0d%2BiOsEhJOxNbODKCHTOfER1eOIrnitWs1hwDL5zczqG%2BUJ3bHABDM%2BEtO8vpeSlc7rVHa9EBH3685Ecw2PqhVCwD%2FJRisqHrVX6gCQRAznDVJ%2B9PBfb93tTu0HQGisosIwUMmsdqaieC2aYIbE8Np%2BUoGf6dEDnRPvHwKdGGfXaxTVPGFypDLkvk%2BF%2BVsVoS7BQsX944q8DpS%2FSPr5zE8%2FHODYn4iu3pQMlAYfG9c6wTV4Jn2Qk2HTwKJKwMQB6Cd%2BzxfQgWpFO5Nwsa%2FijZCYirp1EYDUUiMwPVQ9yiTkQR1qn6%2BD%2BWlAtled2ffyFd7MNbYhcwGOqUBH0dLPFrFi%2F3yNvq30rt%2Bk2MoOopQysGPaoI9i0ZT6Z8Ya9PZEJKuKR%2Bs9fsjosyOW%2FyhY2uTLCfLDgrRbQxYP39OYEft%2FNig0Al99las5jsE2C6SDCtoE0vxsVEYw5lkXmDamqvJPvC2xcYh%2BwPrNUXYMBfHghZV8IZHSIRxEBgmZJ5HqAEMLreP732%2Fni1%2FuceGN9LFfrpV2VCyasweCRSyr2Jc&X-Amz-Signature=ec65635108ec928f65e415efcc3f80a30ae7a76b938ffa12a1f3fa093b2ca8a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626VF3GE4%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCICTZi3GbVy6Siz1tycU7ukxwmZweKXAMKFNGdUH8r9NmAiEAtgSawYSoeqSVjRZv9%2BCFEyw8RRVk3sKX2yaZolaw17YqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDACR1Wd4JSkdrT7QUCrcA%2FlldDVkRjqPEx75DzMN2pmLygmzA8TbdJaYc2%2B2FBl2kExjj15eVvAkwSzl7eAzzyuHE4SoY%2BBuo4yD7xTatXCsc5hP133%2BkG0iHx0TVy%2B%2FUXP%2Fh9elSgCT96dAauKlY2RGS7lgbpIj9rTuVyNuDmhxmkbbbJadoikyl9zY3itXmJqKU5zGAEOFCQS%2B50qyq65jkFMol6tUBxQyV9bKo7X69gggUNmXFbMfw70gpfcxsz7oh1nLDHACdq5UA50s9gIi0QmjOg2L6kg%2BMqO4oEY4YHQTGLFUXJDXwgy4IIbV0oy6gdshojxLuT0d%2BiOsEhJOxNbODKCHTOfER1eOIrnitWs1hwDL5zczqG%2BUJ3bHABDM%2BEtO8vpeSlc7rVHa9EBH3685Ecw2PqhVCwD%2FJRisqHrVX6gCQRAznDVJ%2B9PBfb93tTu0HQGisosIwUMmsdqaieC2aYIbE8Np%2BUoGf6dEDnRPvHwKdGGfXaxTVPGFypDLkvk%2BF%2BVsVoS7BQsX944q8DpS%2FSPr5zE8%2FHODYn4iu3pQMlAYfG9c6wTV4Jn2Qk2HTwKJKwMQB6Cd%2BzxfQgWpFO5Nwsa%2FijZCYirp1EYDUUiMwPVQ9yiTkQR1qn6%2BD%2BWlAtled2ffyFd7MNbYhcwGOqUBH0dLPFrFi%2F3yNvq30rt%2Bk2MoOopQysGPaoI9i0ZT6Z8Ya9PZEJKuKR%2Bs9fsjosyOW%2FyhY2uTLCfLDgrRbQxYP39OYEft%2FNig0Al99las5jsE2C6SDCtoE0vxsVEYw5lkXmDamqvJPvC2xcYh%2BwPrNUXYMBfHghZV8IZHSIRxEBgmZJ5HqAEMLreP732%2Fni1%2FuceGN9LFfrpV2VCyasweCRSyr2Jc&X-Amz-Signature=c10ac5b73de19ab4279474ac69ba0ebbc24ae4bd5578e11ad2cbbd70734cb558&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


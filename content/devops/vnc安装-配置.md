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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QWTA72K%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIEWiHhWVgXbWWiURqGAweRmElX5wS3GabrHp%2FwZze7nOAiEAxj10U7ywQyhfzpDenBZDH9TSYcKgPAaUl1Bkc7QGH2UqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3Nu9F1uYBrOpD2KSrcAyIpYVFod11lpyVGWV%2BP6SpFGSUgmb%2FuNs4kJoG%2FkEoV8NprRajxNOMWW%2BsP7vVdHBzwybo%2FLw6nA291JTFUBuWs%2BgYVAgQV8v0dhsWugxoLDgS%2Bx9E4CMBPS4iUrWDtf%2FZSLT24Oe5EmEabgD%2BqmugZ36OplBIslwIOuRH8cJRSYbL%2Bg5q0v4zciHGXMC5OTFb%2B27wufuUUmHzzIV3EmG12KpCS8CDVfCZdDFd1iZdCVT%2BD%2Fd531JJHpTMW3DcuK%2F3vJajfkBS40QkDb5i3ytse1gT5sWNUGE6yIxVN8slSweI9NFCdjYNoQy19g5FxzXOkzPIbtO8WlAPcmyWYbDenKmjxkh0%2Bf7yc3ogwbXTMOqIIRMQrlUvOaM72AdqLr2t7M48aKvbuqJlldKw3ZKAHS3il97MK%2BQ8ygmJLIl48Wqpa77eplI4xhuW56BZOhfVGXVc7g246iPVzB3k743Bkg4565dzonxzb9PfGdAj3s6inw%2BOGBWM65U8%2FWWHUZhItsCLhdU6xCwOk%2BhmyGkRtoQW5ea422WkQfZyrufbU3pGfTwORpWRYabtHlNHxwq6skOwkABAMj5ajSLX2VSJUOT3on%2FsQUcgiYY9lbMmq313wqjwueWExN54kMOGy3MoGOqUBUL2jlNGR2nSijjtGIpAG%2FVrhwLojsb7vyb4WFbXK%2B1AB9Rq2WMpDuRbSnJ%2BbMM55xbcKeGJI%2FlJXsMIe0T2T9UY9VVZfa6tWxDArGWAC9hN0LBuyRb2LupXxBU6PShAcdVQyI5GpBDuSLqwYs51LYGSbJQL7c3rp8c1%2BoDPq7ORri7u7HVLKNgk%2BBWZMMEJZVH6g4W%2FzaIEWIRiyj94oSn5wOBZG&X-Amz-Signature=c7bbf20bf0a34f821b1d1d13a3477485d742e3361e6dc9af4b62c60fefcc3dc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QWTA72K%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIEWiHhWVgXbWWiURqGAweRmElX5wS3GabrHp%2FwZze7nOAiEAxj10U7ywQyhfzpDenBZDH9TSYcKgPAaUl1Bkc7QGH2UqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3Nu9F1uYBrOpD2KSrcAyIpYVFod11lpyVGWV%2BP6SpFGSUgmb%2FuNs4kJoG%2FkEoV8NprRajxNOMWW%2BsP7vVdHBzwybo%2FLw6nA291JTFUBuWs%2BgYVAgQV8v0dhsWugxoLDgS%2Bx9E4CMBPS4iUrWDtf%2FZSLT24Oe5EmEabgD%2BqmugZ36OplBIslwIOuRH8cJRSYbL%2Bg5q0v4zciHGXMC5OTFb%2B27wufuUUmHzzIV3EmG12KpCS8CDVfCZdDFd1iZdCVT%2BD%2Fd531JJHpTMW3DcuK%2F3vJajfkBS40QkDb5i3ytse1gT5sWNUGE6yIxVN8slSweI9NFCdjYNoQy19g5FxzXOkzPIbtO8WlAPcmyWYbDenKmjxkh0%2Bf7yc3ogwbXTMOqIIRMQrlUvOaM72AdqLr2t7M48aKvbuqJlldKw3ZKAHS3il97MK%2BQ8ygmJLIl48Wqpa77eplI4xhuW56BZOhfVGXVc7g246iPVzB3k743Bkg4565dzonxzb9PfGdAj3s6inw%2BOGBWM65U8%2FWWHUZhItsCLhdU6xCwOk%2BhmyGkRtoQW5ea422WkQfZyrufbU3pGfTwORpWRYabtHlNHxwq6skOwkABAMj5ajSLX2VSJUOT3on%2FsQUcgiYY9lbMmq313wqjwueWExN54kMOGy3MoGOqUBUL2jlNGR2nSijjtGIpAG%2FVrhwLojsb7vyb4WFbXK%2B1AB9Rq2WMpDuRbSnJ%2BbMM55xbcKeGJI%2FlJXsMIe0T2T9UY9VVZfa6tWxDArGWAC9hN0LBuyRb2LupXxBU6PShAcdVQyI5GpBDuSLqwYs51LYGSbJQL7c3rp8c1%2BoDPq7ORri7u7HVLKNgk%2BBWZMMEJZVH6g4W%2FzaIEWIRiyj94oSn5wOBZG&X-Amz-Signature=af6ebd2cc77915960955a52125074b214c318d154b750186109235fe6e588c61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


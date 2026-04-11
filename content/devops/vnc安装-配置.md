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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663JTMTKQ%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2BLPwtmtCaBqj1lcGYZrFs12mx6ddaQW1UkOe%2BhBPJQIgHvzI3P%2FfA%2Fm%2BOnD8ZbF5yBGGGIJshS860dHdvXkbU0Iq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDDrfxZSue%2Bk4mJK%2FrircA8jS4K0Yl9%2FowBRSs5fNsbpQP40CbA8Vs5mIRcN9iUhS23HPDyOm4m3x2lm%2BUuEkg1S7XQpP3lIGG0tEVff0%2Bukh2geUELzkkaJsirC3VdgsTUM%2F89zsxh5TUCGy707WF8Y%2FrUG25%2FKLnzsr2ZAwdoEdQXSY0EpBDZzDazpbXSygrmDa6UPHa0qroE5ymhW3G%2B7USwrult2d2EEl13QFt%2BeZfYkLZi8NGbRnR9yS6NCFftXPyZfTIIQwy0Jemrkujj3mzuzWvGXlKJaAwxsaqy2mMSxdZ1iIOfmgvE%2BAM8iWB4ev5L0gF6G%2FOE1aXrc1mZhU6uCFz6yCk0m4IP5x3UIfjRyVyA%2B6uLmMFq1L6a%2BG01wdxx7cUzFpYBiSSXv%2Fe3YF5hkXW46tfQdiwdpUC%2BZldwoaf9l2uXI0f5i11tn5o6qib0tmf9h1Xs0VpcoWDdjf21NZ7HaaIQeRvYr5fL3yN0rcJa8%2Fq8i9XbK0D3R3IjHeFQvLe8ls2w50pXNR1aVevI4VddOi8a43N3r0maHjuciOLfEEjLgeax%2F62zF%2F3q5KwJgJS0CE7IOvyUJtrNIPNiXUhFtWEqrY%2BBUX8ZJJwYWSuR%2FhqPPyPMdEplU7144vSXMNNeU6x4L6MM7p5s4GOqUBzQAspVjRWnbFSpwXwxTci3uOHQ14fr5ZwNRfqCCuIsKI8ONi3WCDBfCaxghPCaDkpWaym031B0iNzQlLvFW0P7Hy6zrZVfPOr4FRhTtFLHMCk%2BRA2OnD9CpHtk%2FiknzEcd6ftopGsl%2B1PzL6KykRfOwDmtDpZmvUfcWkaGZF8GJy1GnKYOxK5iZZH93ZrIil4ILYJAPLfjQ25KlF0%2FSJlWxPoc2l&X-Amz-Signature=95e16a765374022b92994b5da4190cd7e35811634dd12cade122072d63ac926f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663JTMTKQ%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQC%2B%2BLPwtmtCaBqj1lcGYZrFs12mx6ddaQW1UkOe%2BhBPJQIgHvzI3P%2FfA%2Fm%2BOnD8ZbF5yBGGGIJshS860dHdvXkbU0Iq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDDrfxZSue%2Bk4mJK%2FrircA8jS4K0Yl9%2FowBRSs5fNsbpQP40CbA8Vs5mIRcN9iUhS23HPDyOm4m3x2lm%2BUuEkg1S7XQpP3lIGG0tEVff0%2Bukh2geUELzkkaJsirC3VdgsTUM%2F89zsxh5TUCGy707WF8Y%2FrUG25%2FKLnzsr2ZAwdoEdQXSY0EpBDZzDazpbXSygrmDa6UPHa0qroE5ymhW3G%2B7USwrult2d2EEl13QFt%2BeZfYkLZi8NGbRnR9yS6NCFftXPyZfTIIQwy0Jemrkujj3mzuzWvGXlKJaAwxsaqy2mMSxdZ1iIOfmgvE%2BAM8iWB4ev5L0gF6G%2FOE1aXrc1mZhU6uCFz6yCk0m4IP5x3UIfjRyVyA%2B6uLmMFq1L6a%2BG01wdxx7cUzFpYBiSSXv%2Fe3YF5hkXW46tfQdiwdpUC%2BZldwoaf9l2uXI0f5i11tn5o6qib0tmf9h1Xs0VpcoWDdjf21NZ7HaaIQeRvYr5fL3yN0rcJa8%2Fq8i9XbK0D3R3IjHeFQvLe8ls2w50pXNR1aVevI4VddOi8a43N3r0maHjuciOLfEEjLgeax%2F62zF%2F3q5KwJgJS0CE7IOvyUJtrNIPNiXUhFtWEqrY%2BBUX8ZJJwYWSuR%2FhqPPyPMdEplU7144vSXMNNeU6x4L6MM7p5s4GOqUBzQAspVjRWnbFSpwXwxTci3uOHQ14fr5ZwNRfqCCuIsKI8ONi3WCDBfCaxghPCaDkpWaym031B0iNzQlLvFW0P7Hy6zrZVfPOr4FRhTtFLHMCk%2BRA2OnD9CpHtk%2FiknzEcd6ftopGsl%2B1PzL6KykRfOwDmtDpZmvUfcWkaGZF8GJy1GnKYOxK5iZZH93ZrIil4ILYJAPLfjQ25KlF0%2FSJlWxPoc2l&X-Amz-Signature=bf548152325c0737ff20430bedf72853773520366b10824766daa058149dd2e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


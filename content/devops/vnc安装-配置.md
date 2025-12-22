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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SSOLM3B%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIBIw9bEAFXmP4zcuMCdmsBqQ%2Fi%2FZiNRcR9FFecbH3CgGAiABrHT6xK3iclAHyxaqAJVVDj%2BIzOsPVm0%2BclsEjAsiyyqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMie5GALFE%2B%2B9Qk6arKtwDprqWnRyychHvG9ofT4UOY9ZUaH8GEfzhpZmenPc3s%2B4A99vIa5xCAxhKTvo5t1bU4UZxcFw9RPXOETdv16XjI0UJ3ONE4iNoQ3FR1Wx8Z%2Bs%2BvTBG3g5H5xgw7QvA76oBz5C1DXJIv9XKdACvgeziWPgSvgjgc1buYUXzBEwo8oJg5091YBlBSAQTjZoiqBJXqU50qrDbwmLC9dmcyBqwSVcXll1%2FMMmOAsm4DurUF6KNGxWamj2kbIKbt3GT2nASZmnu9ySmn9T%2BKn48qG66UpDw53ZQJQvf9Kzr7TW5%2B6qFSJUIPElEcAfEFAMSw6R3Gdx4H4okty4qOPfk%2FQgAvwiUnikOLeRuQrsGsvMD7vUadtJCUJELFR%2BVgilhGHR0uNUEfCIFetkSzhEuWC5eEIj4VkcVyouxoOzeoI%2FZG7JOUhn4YrXmIb5mNlRe3NyOedGekEfem6qU3KwEFM6y41WtVdbGu46Sj1RK9IIjfc74qRZ2qRs0KpZwoH0%2F%2BM22UYoInJmVX0S9RF7h7dk%2Bzx6yOFc3AJmhbxdESUKvQTtBo26StoADcItBC9k75dzNeVbo6aiA2JG5hyj6PLTKfIdkj7fdVWNmtEMFnJvbFe%2F5YBroH3sg6kUKlLQw3eWiygY6pgHAc0gegy8JDt7w123kfIuxko14MRNeJObO45d7QnozKVh9%2FijXgVMkmdtbkd%2B%2FG9NWmuil1jmJfnG%2BIC2m36WNkH6KaKwvibJIrMNk3k75omehJI7MvdUudIQuLtsRGhHALS1WBCdqOW0aVhS1shWii%2F6vxr%2BrmnOw9%2FdtZxuyLz7mz6DmaTic8PvYpSVQtceYXF1nTCE7fB5b%2FXGytyoRb%2BGLLpii&X-Amz-Signature=1dae461867816ccf17bc5a73e9433c2576c3eb5d767064d6475ece7471e83aa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SSOLM3B%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIBIw9bEAFXmP4zcuMCdmsBqQ%2Fi%2FZiNRcR9FFecbH3CgGAiABrHT6xK3iclAHyxaqAJVVDj%2BIzOsPVm0%2BclsEjAsiyyqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMie5GALFE%2B%2B9Qk6arKtwDprqWnRyychHvG9ofT4UOY9ZUaH8GEfzhpZmenPc3s%2B4A99vIa5xCAxhKTvo5t1bU4UZxcFw9RPXOETdv16XjI0UJ3ONE4iNoQ3FR1Wx8Z%2Bs%2BvTBG3g5H5xgw7QvA76oBz5C1DXJIv9XKdACvgeziWPgSvgjgc1buYUXzBEwo8oJg5091YBlBSAQTjZoiqBJXqU50qrDbwmLC9dmcyBqwSVcXll1%2FMMmOAsm4DurUF6KNGxWamj2kbIKbt3GT2nASZmnu9ySmn9T%2BKn48qG66UpDw53ZQJQvf9Kzr7TW5%2B6qFSJUIPElEcAfEFAMSw6R3Gdx4H4okty4qOPfk%2FQgAvwiUnikOLeRuQrsGsvMD7vUadtJCUJELFR%2BVgilhGHR0uNUEfCIFetkSzhEuWC5eEIj4VkcVyouxoOzeoI%2FZG7JOUhn4YrXmIb5mNlRe3NyOedGekEfem6qU3KwEFM6y41WtVdbGu46Sj1RK9IIjfc74qRZ2qRs0KpZwoH0%2F%2BM22UYoInJmVX0S9RF7h7dk%2Bzx6yOFc3AJmhbxdESUKvQTtBo26StoADcItBC9k75dzNeVbo6aiA2JG5hyj6PLTKfIdkj7fdVWNmtEMFnJvbFe%2F5YBroH3sg6kUKlLQw3eWiygY6pgHAc0gegy8JDt7w123kfIuxko14MRNeJObO45d7QnozKVh9%2FijXgVMkmdtbkd%2B%2FG9NWmuil1jmJfnG%2BIC2m36WNkH6KaKwvibJIrMNk3k75omehJI7MvdUudIQuLtsRGhHALS1WBCdqOW0aVhS1shWii%2F6vxr%2BrmnOw9%2FdtZxuyLz7mz6DmaTic8PvYpSVQtceYXF1nTCE7fB5b%2FXGytyoRb%2BGLLpii&X-Amz-Signature=05c3a966644e3bd3ab111ca096a0fb684bf39a4ea16ea6abf3ac255e2ab67552&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


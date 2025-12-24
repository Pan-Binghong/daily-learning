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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5FYBBNN%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHU3M9uoANZKhrEcktR0kCfmZimFfpEc01GtnvubNVuVAiAWDeIpMuZlgCs6PtI9rf%2F7%2F8j8KQo8KZ6GwZTYGOwRjSr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIM6uaPlJJY6oha%2FYRDKtwD7Rv6PAosGiSPQ2kjhLCVhZvD8eJeCBrT91VDg6GAoKDalKfVL%2BE%2FmyP8GlI%2BVXI6sAW8fPY23FcBD9jiiLuZzHEpmb%2BKHwyUgMZnwcK0LqBlkR3A0PkP%2FpwaQblgcoNLiQ5C0Ic1ON7qUZlc2rt%2BYPxWDXrtd1B%2F11B6UBhd8CFa4cKgUDk057qZpsNDpQUpHL%2F0pbvonW2%2BxsjTbMRZo7VBZc%2BMUUzLhOrapPVCQPQNaMa8nrx4ULUl96BXESf7aQSUkHWaPh4ONZxSKYgVXA7AmkE%2FW4Z5XUvhQ96tF8SvJuZPuFrj4WUKFvErRekGz4W0Nb8oywsl4rNfUg7sGD5eIQL5TIliW4bQr6fm2YihCP4X8IVMX3bQh0C0GmQqSryOHsgh9VIvGZ9Rs3NrWsmnx9zP4x8%2BU0EfKruBQWGQwTO39OdiIeDyIk%2B3qK0sabstxaVWLOkU0rqVkulBx80WWtHbB39ovkd4jqgMbxTs5HBP4pDyFlf%2B6D5s5T1sNAgzuMkIa9wU7SNlsjooK%2F0hXcM14zv6iDOVrLhwotnb%2BQsYGJJiO9Okm%2Fg7Z9RVo9GAUCNq%2Bbf%2BB2RF7NKXdaybG3PPF1ZTWHcgK%2BDf85gg8SsHa2ZEuwffEk8wreGsygY6pgF8%2FRu6nKtc4VzkKOwQU%2F6UHdE18CdLL29GM8dQ5%2BFgKn%2BTjfxnQq1EwJPZNpDC3NmvJzr3A2HqcSQ9cCCQnz9o7%2BtUYq8vA25vKJdcKA9ks8V%2BUwzR0J0%2FUOwK5TnVGnZPC7L8t3Ta3affNChH8SQR7GSKGGs4UiN%2FpKd5ISYwWBbTQpaZaIEFp3DxZO%2BwZ9gEL5xlPi2vMnoXV5fIU64EiVm5fdoP&X-Amz-Signature=ad85a551f3c36a18fde9e96df21f85b1b56e04ab5a589abcb0839f512a660f00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5FYBBNN%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHU3M9uoANZKhrEcktR0kCfmZimFfpEc01GtnvubNVuVAiAWDeIpMuZlgCs6PtI9rf%2F7%2F8j8KQo8KZ6GwZTYGOwRjSr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIM6uaPlJJY6oha%2FYRDKtwD7Rv6PAosGiSPQ2kjhLCVhZvD8eJeCBrT91VDg6GAoKDalKfVL%2BE%2FmyP8GlI%2BVXI6sAW8fPY23FcBD9jiiLuZzHEpmb%2BKHwyUgMZnwcK0LqBlkR3A0PkP%2FpwaQblgcoNLiQ5C0Ic1ON7qUZlc2rt%2BYPxWDXrtd1B%2F11B6UBhd8CFa4cKgUDk057qZpsNDpQUpHL%2F0pbvonW2%2BxsjTbMRZo7VBZc%2BMUUzLhOrapPVCQPQNaMa8nrx4ULUl96BXESf7aQSUkHWaPh4ONZxSKYgVXA7AmkE%2FW4Z5XUvhQ96tF8SvJuZPuFrj4WUKFvErRekGz4W0Nb8oywsl4rNfUg7sGD5eIQL5TIliW4bQr6fm2YihCP4X8IVMX3bQh0C0GmQqSryOHsgh9VIvGZ9Rs3NrWsmnx9zP4x8%2BU0EfKruBQWGQwTO39OdiIeDyIk%2B3qK0sabstxaVWLOkU0rqVkulBx80WWtHbB39ovkd4jqgMbxTs5HBP4pDyFlf%2B6D5s5T1sNAgzuMkIa9wU7SNlsjooK%2F0hXcM14zv6iDOVrLhwotnb%2BQsYGJJiO9Okm%2Fg7Z9RVo9GAUCNq%2Bbf%2BB2RF7NKXdaybG3PPF1ZTWHcgK%2BDf85gg8SsHa2ZEuwffEk8wreGsygY6pgF8%2FRu6nKtc4VzkKOwQU%2F6UHdE18CdLL29GM8dQ5%2BFgKn%2BTjfxnQq1EwJPZNpDC3NmvJzr3A2HqcSQ9cCCQnz9o7%2BtUYq8vA25vKJdcKA9ks8V%2BUwzR0J0%2FUOwK5TnVGnZPC7L8t3Ta3affNChH8SQR7GSKGGs4UiN%2FpKd5ISYwWBbTQpaZaIEFp3DxZO%2BwZ9gEL5xlPi2vMnoXV5fIU64EiVm5fdoP&X-Amz-Signature=54e3bd4f4e96ddbceed62e1d7c549330f2e63745872fb66bbc21e3e87b2be640&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


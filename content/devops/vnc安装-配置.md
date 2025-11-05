---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
标签:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNPMBWZ4%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB6or0cyJgFV%2FcKDRL4JrOBph5EEjona8jx11IutX9FwAiA7QORmUHRFw5IskngqmOBmgeCWBM63hkZevoE%2BuwXofCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3Zw%2FC3Ad47ZoGbj1KtwD3D1E2NdGZoZBRaaA0u%2BDIZrDHCrt7WTYSr6nnJhlHpJEBdIlK%2FNeSp9tvNhrPV4r%2FUE9%2FXzyJvP6Z23uQkn04Fj2SNSYNOch%2FBHcmaC7TWKlsiFHOmIZOI6TxsWLttWD%2BIDKYPLoGyztGN3DhXg182deWOhH4S5l30BEEqHMVDQlSM4T%2BuhpzLSUaXf3G%2BWMviG4fe%2FgdVsYkqbleyYX2nnGU8HTUnX2fw0AWio7YPc6cFFw7OV6ra0iSOYcyQtWbywAIeR4aXUigcczuuanDAr2PhGHcgs5kteni87LYrYrhxiMy7UvHi4N7sruafXXuetcsF4FnYrLOT5d5JKufTBStThgfRkIsfHY5MUWZx%2FH%2BlMicofqWu5kkBaisKnvWu9jnMBoYBG%2BRDtl5%2FGhMuUm9ysGHJZxe2CiVqJxiFPLSxLqTlMQoV3hZ1Yyltg59udBcYY2qjbYKNaJtVaC6Xp3SfwB3%2FSwYNPgGq%2B0qA3RGPTCEpKe9nEB128me8fLCdmeJhr3cO1VZACZlA%2Fc6XhFwdMDPkFzb1l%2FMWc%2FOTri3%2FOpInj0fgE7pb0nqYArrFaA1bh9NH3Ww6n7%2FcTifzI3P1TGgyf93Cnkt%2FqDxQDsp2hXvBf5xH7Y65gwrqKsyAY6pgF3JpDuBLl7ZkC72I%2FEXcXindsLAcVNcFD31A13%2FeTHXO24R6CtYX%2B%2B7VTZBYgD5tTD1doWI96IgsoR3vqI2kKrRlhDRcJNbYMKsQiYIiw3H%2B2EELisgzbbsUzPaIrFi2fODMrdaHuLbaZ9FiZ2n0YGIbOmZbnvXaBYk9kkduMm%2BLTE76cv09qwhwuDD0yqC%2FEeOPn%2FMH4HyKqj7Mlcq25tJXZ3Q6sF&X-Amz-Signature=ee1e53efa491314baf1512b2a4da8f41858350a74e4cdbc736c3d9549dc90492&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNPMBWZ4%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB6or0cyJgFV%2FcKDRL4JrOBph5EEjona8jx11IutX9FwAiA7QORmUHRFw5IskngqmOBmgeCWBM63hkZevoE%2BuwXofCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3Zw%2FC3Ad47ZoGbj1KtwD3D1E2NdGZoZBRaaA0u%2BDIZrDHCrt7WTYSr6nnJhlHpJEBdIlK%2FNeSp9tvNhrPV4r%2FUE9%2FXzyJvP6Z23uQkn04Fj2SNSYNOch%2FBHcmaC7TWKlsiFHOmIZOI6TxsWLttWD%2BIDKYPLoGyztGN3DhXg182deWOhH4S5l30BEEqHMVDQlSM4T%2BuhpzLSUaXf3G%2BWMviG4fe%2FgdVsYkqbleyYX2nnGU8HTUnX2fw0AWio7YPc6cFFw7OV6ra0iSOYcyQtWbywAIeR4aXUigcczuuanDAr2PhGHcgs5kteni87LYrYrhxiMy7UvHi4N7sruafXXuetcsF4FnYrLOT5d5JKufTBStThgfRkIsfHY5MUWZx%2FH%2BlMicofqWu5kkBaisKnvWu9jnMBoYBG%2BRDtl5%2FGhMuUm9ysGHJZxe2CiVqJxiFPLSxLqTlMQoV3hZ1Yyltg59udBcYY2qjbYKNaJtVaC6Xp3SfwB3%2FSwYNPgGq%2B0qA3RGPTCEpKe9nEB128me8fLCdmeJhr3cO1VZACZlA%2Fc6XhFwdMDPkFzb1l%2FMWc%2FOTri3%2FOpInj0fgE7pb0nqYArrFaA1bh9NH3Ww6n7%2FcTifzI3P1TGgyf93Cnkt%2FqDxQDsp2hXvBf5xH7Y65gwrqKsyAY6pgF3JpDuBLl7ZkC72I%2FEXcXindsLAcVNcFD31A13%2FeTHXO24R6CtYX%2B%2B7VTZBYgD5tTD1doWI96IgsoR3vqI2kKrRlhDRcJNbYMKsQiYIiw3H%2B2EELisgzbbsUzPaIrFi2fODMrdaHuLbaZ9FiZ2n0YGIbOmZbnvXaBYk9kkduMm%2BLTE76cv09qwhwuDD0yqC%2FEeOPn%2FMH4HyKqj7Mlcq25tJXZ3Q6sF&X-Amz-Signature=d664c57c6c4dd1a9523f33dbbc8732a148fc1a996eb21bb5de2ede3e8035dc6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


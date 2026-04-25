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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RGFU5AE%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIASrrA%2B2ydITJpgE6neKB%2FK7tLhp3HmDQANTNItmlZaKAiArw3od7AD2kAQ46Hfr%2FN6ZpfvydDJoP95hxhHBBDMngyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUz49J6p0luauxFbUKtwDzUFACPJLA79YsDSaPbS7ZGJVvqXhXCv3PvtmFhbyTdUJ6%2B8AFom86ZnoEp2ymiJppD6CVZ7hsOwCcbo1Z9DASA5aeJhrs1tTdNbr8LeOvcRiZrNmi2gRZS5AE68naIEtFXe0iV%2Flw%2BAsNOQl5evNh%2B1iJ%2Biz77rJmTfIbNqqDk7MDgUR1QW5L0j21M4RPH%2B7BgMbsyNajb%2BRqwnSfd%2BGCfNyRb%2BS3aXBMVC9krZ63Za%2FB14lTudGoNsEbTnrsLldxY1p%2FNerO%2F4SwryEWicTXlc266SV2Hj4YdfXqt5SkoGSWe%2BXYKId7crAyvsudCBrHU%2Bt3hbO6wEsX4tdOicUbGHqBfD48UEoRbf3L83ipxtUH7ge2AgCypJErY3h6DVGIsj9prfoNAMFDnY5Hr6Y%2FoAf6%2FNNUtkcYaQu7HNX25AXtkgRSvAyZEDzrdES3YPlThqctFt5XevKwdeWZlOUPovoYGg22wuzUyczSKSisEAN%2BmRrTkcfNrIeuYZKHIF4AqFzs5dhCXnYjptnJrbSOzc6SA3WOMa1uwZPShjXHvPEEH2QLuxiNMgOggobNxdFRTgLN3WY9nNkD6gFQXVtr%2FY6qP4uwx49AdMh6%2FfCuq189CF3onYnwaZiD5kwtvGwzwY6pgHKN7VedFu8FDlkjotN%2FsF6O1FbyMduzrzUWGtiK0p8NmG6hDSzBzWRH5xeZcIdImDmPQPSSvK3TwsjRfB%2BeGJr3bLZ%2BJ1J6wFTC76kmnxp4a4n9DcdFySbJycDr9POjXmI%2BvV03ecPRgVXL6XhiO1d7a%2BEmc04PXg5fYmQak5RCuMAS2JJ3FKKs6l4lHDXiL%2FSuFuHlCZwv3MXWyVKKZY3Y2LLAkiu&X-Amz-Signature=5cb1ab2b80125ecb5e1a62bb71ca6f1c2b260e464ad650c3f16a8316839a5a1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RGFU5AE%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIASrrA%2B2ydITJpgE6neKB%2FK7tLhp3HmDQANTNItmlZaKAiArw3od7AD2kAQ46Hfr%2FN6ZpfvydDJoP95hxhHBBDMngyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUz49J6p0luauxFbUKtwDzUFACPJLA79YsDSaPbS7ZGJVvqXhXCv3PvtmFhbyTdUJ6%2B8AFom86ZnoEp2ymiJppD6CVZ7hsOwCcbo1Z9DASA5aeJhrs1tTdNbr8LeOvcRiZrNmi2gRZS5AE68naIEtFXe0iV%2Flw%2BAsNOQl5evNh%2B1iJ%2Biz77rJmTfIbNqqDk7MDgUR1QW5L0j21M4RPH%2B7BgMbsyNajb%2BRqwnSfd%2BGCfNyRb%2BS3aXBMVC9krZ63Za%2FB14lTudGoNsEbTnrsLldxY1p%2FNerO%2F4SwryEWicTXlc266SV2Hj4YdfXqt5SkoGSWe%2BXYKId7crAyvsudCBrHU%2Bt3hbO6wEsX4tdOicUbGHqBfD48UEoRbf3L83ipxtUH7ge2AgCypJErY3h6DVGIsj9prfoNAMFDnY5Hr6Y%2FoAf6%2FNNUtkcYaQu7HNX25AXtkgRSvAyZEDzrdES3YPlThqctFt5XevKwdeWZlOUPovoYGg22wuzUyczSKSisEAN%2BmRrTkcfNrIeuYZKHIF4AqFzs5dhCXnYjptnJrbSOzc6SA3WOMa1uwZPShjXHvPEEH2QLuxiNMgOggobNxdFRTgLN3WY9nNkD6gFQXVtr%2FY6qP4uwx49AdMh6%2FfCuq189CF3onYnwaZiD5kwtvGwzwY6pgHKN7VedFu8FDlkjotN%2FsF6O1FbyMduzrzUWGtiK0p8NmG6hDSzBzWRH5xeZcIdImDmPQPSSvK3TwsjRfB%2BeGJr3bLZ%2BJ1J6wFTC76kmnxp4a4n9DcdFySbJycDr9POjXmI%2BvV03ecPRgVXL6XhiO1d7a%2BEmc04PXg5fYmQak5RCuMAS2JJ3FKKs6l4lHDXiL%2FSuFuHlCZwv3MXWyVKKZY3Y2LLAkiu&X-Amz-Signature=f0c7aa1e5efd04a028a2d5b565348ab7fc23ca977a9abab0a524bb230db47e22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


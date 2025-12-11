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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBSH4JEE%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCrgZVrEG3GFN%2Ba1Sdl10r%2F9WkcjkDfHudvK%2Bb6LEO0bwIgIJYLqpNcyKgNc27cA1mKmnUtePkWh0N%2BZJaUdHGcm1MqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7%2B7sI0TvMp4N7b0CrcA%2FvrUVS%2BHR0Xw2hK5S1PVZqVHZu4DUR%2BnalDrqVh1mmQj1y9l6PRTp5651YfvX1XFKZrr9PVQArb9pEUXMFFBDWMdShFermq33VsC8%2Bp7MVSMCo1AWnOqiSkWTt22E71%2F0N8tJ0Fz71SpiQIMK9m4%2BrKiLueP4HcZxyCNp%2FgceemuGpaTqzwMg0wdSmzYT9IpcyA3GKSPwf49WI4yWfe8upWDvRzBzNMU6hGhMN7c5VxfHrHgsWxytXPYzniNbl30BnnoFjhiMSGMmTrUl8aVS1RcVBJptW1nZR5gcOdLa2vvpsQLqg3BLZezGLS6tcoV7zR9Gu%2Bn15Egoos8a6AEW4OvXXAXk2bu2HlyarquT87ld25VfF6EPqJD5Evt45JHaKw4%2F6IJOZB9lPeKcLrMkfoZyW2Nuzf99mEVlkMUuphRJIaqv2Ub1AGKQ%2BaluDD5alO1JVgyHVk3uz4IpwCCt9ay2TrRBqq1ca3qNLPW3h4n%2FRNLKRHWIaJoI%2F%2FGUVvzdMq%2F4zgIHfL6Dir83LU%2BKdGR%2FZNyfZx6NrQ13PniuBsa8YEeu1jgoTq4sItB%2FO5DXns%2BDzgJyFtbzuOqrxVN3mNpY7qNnc5zcz7GqJWrB1uxoIPHE7jS5s4mVU%2BMOa16MkGOqUBclzlyLPQ46aBgZ%2Bujr74ydy1UGE6%2FUooVomOoYwoewYjksIAlUtnDAwIf1921%2Bwr9KUmgzLVG36l%2FtVp10jHOgJcEDNdfhY1Pa%2FPeY5Bwlff%2Fb8iIQcLS42B7d19FRiQVrjanaV9jV7tp4F%2BKE%2F5Tf3t9kNE4vJ6zTxCn0iP8b7P9BU0C5Qo%2BPvHKckxSFTthqywXgLb78GAwUF%2BY1Nf67%2FZHaeZ&X-Amz-Signature=4cf03636e1ac063fe48d9dc8337d3c6629535fd1dcd4051f5e959e294fe2d392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBSH4JEE%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCrgZVrEG3GFN%2Ba1Sdl10r%2F9WkcjkDfHudvK%2Bb6LEO0bwIgIJYLqpNcyKgNc27cA1mKmnUtePkWh0N%2BZJaUdHGcm1MqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7%2B7sI0TvMp4N7b0CrcA%2FvrUVS%2BHR0Xw2hK5S1PVZqVHZu4DUR%2BnalDrqVh1mmQj1y9l6PRTp5651YfvX1XFKZrr9PVQArb9pEUXMFFBDWMdShFermq33VsC8%2Bp7MVSMCo1AWnOqiSkWTt22E71%2F0N8tJ0Fz71SpiQIMK9m4%2BrKiLueP4HcZxyCNp%2FgceemuGpaTqzwMg0wdSmzYT9IpcyA3GKSPwf49WI4yWfe8upWDvRzBzNMU6hGhMN7c5VxfHrHgsWxytXPYzniNbl30BnnoFjhiMSGMmTrUl8aVS1RcVBJptW1nZR5gcOdLa2vvpsQLqg3BLZezGLS6tcoV7zR9Gu%2Bn15Egoos8a6AEW4OvXXAXk2bu2HlyarquT87ld25VfF6EPqJD5Evt45JHaKw4%2F6IJOZB9lPeKcLrMkfoZyW2Nuzf99mEVlkMUuphRJIaqv2Ub1AGKQ%2BaluDD5alO1JVgyHVk3uz4IpwCCt9ay2TrRBqq1ca3qNLPW3h4n%2FRNLKRHWIaJoI%2F%2FGUVvzdMq%2F4zgIHfL6Dir83LU%2BKdGR%2FZNyfZx6NrQ13PniuBsa8YEeu1jgoTq4sItB%2FO5DXns%2BDzgJyFtbzuOqrxVN3mNpY7qNnc5zcz7GqJWrB1uxoIPHE7jS5s4mVU%2BMOa16MkGOqUBclzlyLPQ46aBgZ%2Bujr74ydy1UGE6%2FUooVomOoYwoewYjksIAlUtnDAwIf1921%2Bwr9KUmgzLVG36l%2FtVp10jHOgJcEDNdfhY1Pa%2FPeY5Bwlff%2Fb8iIQcLS42B7d19FRiQVrjanaV9jV7tp4F%2BKE%2F5Tf3t9kNE4vJ6zTxCn0iP8b7P9BU0C5Qo%2BPvHKckxSFTthqywXgLb78GAwUF%2BY1Nf67%2FZHaeZ&X-Amz-Signature=05b1829e79988f6d45d506304cff594d31adf6fe54cd3faefb5f2b907ea934e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


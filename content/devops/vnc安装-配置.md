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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXINFFR%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIA2ItLXXcPeBw0Ivx7s99IgEkxCtle%2B52tw5enhhFdehAiBkt%2BBm6csZlzHiQU%2FTnJQ9zJsayC9ESxv5hsuGv4m6riqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZdBSs1Ny9PZ%2B7sUIKtwDZZXJbWpzM6TXr0st7ZH1p1j2EOJkStwZGL6BYyGEV0U9tIeXFGuZXkl4U19SKA8lJ184NKyUEcSzMf4ttEafterDwmD%2BQC3HV20gzzbT76CoC4HWzFNrjjZ%2Fa6TQNW%2B%2FJZS%2FGW7xcH2hKPnBeWY0HTjDiAgxOTR5MasgIjr8KAO2csrf3lUNhLLesmQJOMPFL2dCK5Y8XPRQpw94Ldskr%2BP3TWMH%2FSlxR0mciOSLv1lcwsmoT6YY0mTIpBPbF4Zci9vVp%2FH29urtAiMsG%2BLvosJrGyfHy7XgCslyOb80DfDqn2IZVR%2BpCjVchjMnQiy9NIYmvLd9wLcZUTMYk4B%2BXeKHT5EHpJBqGVYpHv1y2%2BPWhU7gV41Z6JRaVcJXR2c5uIyMuR7kDKY%2Ff7bheejRwoBwTJj2YI%2BbLums4sfd0tyj91ZnxXtpuct4sEq%2FJMLyIIBVkVc9mTmdgHIffc%2BvjAAwtQsPd%2FRA%2FAr9LebyH4EwF2AB4NC%2B%2B%2B2q%2Fl%2F8OqQQWCOL%2FNjfl%2BiJzOfNiQh0%2BnaJYcGYKepHBmuUDQ%2FYimWvSEoWH0NxG8yqBeYWRra1Q6uLPzJ7ji2%2BPWn9r8jpIfp355WPqSyESTSN9vkDcwW1OlL0%2FRbRR%2BqL%2F70wzLm6zAY6pgHYRTPumxu1LbP8lHFCjQOKn7TtGQHsHKY6nWBEB5AK5vz577x1dqNRU2JEp4vUd81QsPQduo2n0MQbe%2FvrYys7qeP6JbNOV%2BK%2BAp4fzQPwgbq7hfedNEAhIPs%2B9wm5lsIX69I21a4oiMGltJlfqg65WXUW7ghZqGUAnDKrl2uNMsOYfgVlKH1yVXE5ZeNMPlh%2B6N3PRvZZeuDgZbK87SVehlDwwAkh&X-Amz-Signature=8126575213e74add20bc25e4c020222629960a072d3a746eb9046c3d74d4b686&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MXINFFR%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIA2ItLXXcPeBw0Ivx7s99IgEkxCtle%2B52tw5enhhFdehAiBkt%2BBm6csZlzHiQU%2FTnJQ9zJsayC9ESxv5hsuGv4m6riqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZdBSs1Ny9PZ%2B7sUIKtwDZZXJbWpzM6TXr0st7ZH1p1j2EOJkStwZGL6BYyGEV0U9tIeXFGuZXkl4U19SKA8lJ184NKyUEcSzMf4ttEafterDwmD%2BQC3HV20gzzbT76CoC4HWzFNrjjZ%2Fa6TQNW%2B%2FJZS%2FGW7xcH2hKPnBeWY0HTjDiAgxOTR5MasgIjr8KAO2csrf3lUNhLLesmQJOMPFL2dCK5Y8XPRQpw94Ldskr%2BP3TWMH%2FSlxR0mciOSLv1lcwsmoT6YY0mTIpBPbF4Zci9vVp%2FH29urtAiMsG%2BLvosJrGyfHy7XgCslyOb80DfDqn2IZVR%2BpCjVchjMnQiy9NIYmvLd9wLcZUTMYk4B%2BXeKHT5EHpJBqGVYpHv1y2%2BPWhU7gV41Z6JRaVcJXR2c5uIyMuR7kDKY%2Ff7bheejRwoBwTJj2YI%2BbLums4sfd0tyj91ZnxXtpuct4sEq%2FJMLyIIBVkVc9mTmdgHIffc%2BvjAAwtQsPd%2FRA%2FAr9LebyH4EwF2AB4NC%2B%2B%2B2q%2Fl%2F8OqQQWCOL%2FNjfl%2BiJzOfNiQh0%2BnaJYcGYKepHBmuUDQ%2FYimWvSEoWH0NxG8yqBeYWRra1Q6uLPzJ7ji2%2BPWn9r8jpIfp355WPqSyESTSN9vkDcwW1OlL0%2FRbRR%2BqL%2F70wzLm6zAY6pgHYRTPumxu1LbP8lHFCjQOKn7TtGQHsHKY6nWBEB5AK5vz577x1dqNRU2JEp4vUd81QsPQduo2n0MQbe%2FvrYys7qeP6JbNOV%2BK%2BAp4fzQPwgbq7hfedNEAhIPs%2B9wm5lsIX69I21a4oiMGltJlfqg65WXUW7ghZqGUAnDKrl2uNMsOYfgVlKH1yVXE5ZeNMPlh%2B6N3PRvZZeuDgZbK87SVehlDwwAkh&X-Amz-Signature=5f1c74a410abfb05a59a13d1f6c4382d105930ecf002c6e3bfe9db65b170930d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


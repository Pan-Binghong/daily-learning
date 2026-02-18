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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG4B2GBZ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOm239yU11NgfnfEzPWNHY8V3e5Z44QbLerZzY7Cye0AiEAqW3lQeDWhzn%2FHEpku%2ByHp77fRwTFe3VSwH5ysEJ5SwMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHV12V%2FQjyqaCp20%2FyrcA4GzUleMbdigNIpZZNatww6WI%2BLLT6vYVkuVRKcS54zh6egKizUqAgKJlC5D2EOXnNJK4ucSR9ZXUxMKIbWnRTolXOxnFNia77Zz9scRUZOEHtNPR27dGI4ZpvcMU1lNiRlHyJpqVB4G%2BpbV0jF3oPJ5Onf157eX54KyHiN2iFr9%2Bn6zaO5WMsM%2FpBx1FAtV2%2BqoRR%2BRjVUH8GCB5GNcnWjjzBWnbaqKr6cCGPCjezuRD6EW%2FAR4zPvf83Ek0HRoJOLh0NM9W7cyl2Cqb7yyz3nNU0geRkhQMm3bJY6bsAAWOO2WqRqLfSSXWhCbsMUQMBNC6bRJ77HoNkjmNd6rc3cq7drL2YcDvPmqnhp4JDAiURQhALG9Pv4sv4xwkyr4LHtXIMusyAlmxnVTMBk7P%2BxveH9gy3bnIylE1t%2BVnklEf5O4x%2FAZsWmwfddh%2FQ77jJ%2FQ%2F97%2BkfrWxRkoqMeTfws%2FJXnDI48wJlov6BdCGdN3%2FAAHHcGXzLHOvMszLdk1aSrVXTkWJZ0HhjKPHPe8TdB8tL80exQd1P2QsoyhKIc7UA6SPzfzosEkHdwIRA4ooYpdExE1hjg2jzT6Hlh74oSD2U0MxO0HHcTCs9pLqheZvJXXixGQ2jM07w3AMPGf1MwGOqUBWj4JTRh8JwG%2FAeHqc3KQEbBr5nqrh9gljgfYOvO%2Bbx7uMLox%2BovU1keBcCxJELSFQCiSglNOlKBhFhKd5mtd4XSdtDYbWSJdZ251h87RT%2FSpO3HNGHa6Z6dXAUoy1Xmh0dmWhGt0Q%2F7pqXexWI1%2FSqf52ZdrvSVhvRuZJxsclUEE4pT5GtTyuGdI4GYv%2F1HyAi%2FF%2FfdLIg%2FvU7VAA8n%2BOik8%2Bt6S&X-Amz-Signature=2a4c4985bf3472181627fd515627c7c5742f22258bac5c3e4a183138cb20902a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG4B2GBZ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOm239yU11NgfnfEzPWNHY8V3e5Z44QbLerZzY7Cye0AiEAqW3lQeDWhzn%2FHEpku%2ByHp77fRwTFe3VSwH5ysEJ5SwMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHV12V%2FQjyqaCp20%2FyrcA4GzUleMbdigNIpZZNatww6WI%2BLLT6vYVkuVRKcS54zh6egKizUqAgKJlC5D2EOXnNJK4ucSR9ZXUxMKIbWnRTolXOxnFNia77Zz9scRUZOEHtNPR27dGI4ZpvcMU1lNiRlHyJpqVB4G%2BpbV0jF3oPJ5Onf157eX54KyHiN2iFr9%2Bn6zaO5WMsM%2FpBx1FAtV2%2BqoRR%2BRjVUH8GCB5GNcnWjjzBWnbaqKr6cCGPCjezuRD6EW%2FAR4zPvf83Ek0HRoJOLh0NM9W7cyl2Cqb7yyz3nNU0geRkhQMm3bJY6bsAAWOO2WqRqLfSSXWhCbsMUQMBNC6bRJ77HoNkjmNd6rc3cq7drL2YcDvPmqnhp4JDAiURQhALG9Pv4sv4xwkyr4LHtXIMusyAlmxnVTMBk7P%2BxveH9gy3bnIylE1t%2BVnklEf5O4x%2FAZsWmwfddh%2FQ77jJ%2FQ%2F97%2BkfrWxRkoqMeTfws%2FJXnDI48wJlov6BdCGdN3%2FAAHHcGXzLHOvMszLdk1aSrVXTkWJZ0HhjKPHPe8TdB8tL80exQd1P2QsoyhKIc7UA6SPzfzosEkHdwIRA4ooYpdExE1hjg2jzT6Hlh74oSD2U0MxO0HHcTCs9pLqheZvJXXixGQ2jM07w3AMPGf1MwGOqUBWj4JTRh8JwG%2FAeHqc3KQEbBr5nqrh9gljgfYOvO%2Bbx7uMLox%2BovU1keBcCxJELSFQCiSglNOlKBhFhKd5mtd4XSdtDYbWSJdZ251h87RT%2FSpO3HNGHa6Z6dXAUoy1Xmh0dmWhGt0Q%2F7pqXexWI1%2FSqf52ZdrvSVhvRuZJxsclUEE4pT5GtTyuGdI4GYv%2F1HyAi%2FF%2FfdLIg%2FvU7VAA8n%2BOik8%2Bt6S&X-Amz-Signature=8da3b6f5188cb173cb52848c152532f66368e1110701101dad225386ea6d530d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


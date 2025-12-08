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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXI45PSB%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBfLodkS28mevWrswTUoEUmxUUkC7t0VLlp0BJOW9dfQIgWYdKQZNB6QLMgnp46SNeM0mMxtkZnFZhTm5pr%2Fh44aIqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNAVgXWJWCnwTZz0ISrcA229FE%2BCLH131UBrRku9hp0U%2FOPv8z5VTLU3svG%2BYQT69Fl1E8mzm6HpZTQF7Q0rayeENZi5YD8p95cOmgfO46lx9UpdGmUWlawFkdeXVFCElbeaaWzGDPF2EGIS6STqmAwhvjFd95H0y%2BUoKx4QxdoJEya2MUmVK6zmQ66QUxa2%2F%2B0EsH6dVLq18BK4L45OwhQfun9j7y8uc8FxDllYc3hNvA8%2FOW2qe27sSIlwaC8VdQrqrbsAMPiPLdBen1J9f0mmXC1aTH%2Fo1CDGjNC6DYLR7ET4W%2FNBCFEL2b2B7PpUzye%2FIVRezMFN7D%2BQI3LQwfCh%2BXpMKlrE0lzNqjkWhvfB4JjJoZPptn58MSQo%2Fx%2B%2F0CqWqXYgO6ylciGOb%2BpgdIApZNCO9L4XvQ7%2BU4%2BskCO7BuEJQfSi5mh4WAdYCGmietQI3TqVmLqbOMvdHvQyaSguHZdd0nZ8qUBn9nkj6K02TGGkg%2FhzxmuZRZDdiyeXVpd0HDQyVzQP%2FoGSd5wbpqgkYeox8eRB3Jt75YoCtRXO0xxar6f28siUN9YbO%2FoqbXB10dCa%2B9ijOp%2FRRGuG%2BXa8EDQ%2B2yIPYqkYWAbQ84WlnQMIyM6vTrsKyvjREz8oumO5RwWmvnyLnWRKMP3u2MkGOqUBJUR1DpTmhO7XUiAg5DNm6BhOjgI1jlaxNyNy6qjdaVd1aChzBCc%2Bk%2Bahbb6iMTTj5nMjRrHI1xKPQM9obN6S0sDEc4wdgLP4LIDwhXIrs6UbC6YTrGF3kPRhWsOwZ5o4puaC44NkA4clUl95vgyR7sCnUgV7gkd3gt07%2B%2Bqgliy7lScZoaVM5lNnwzzvp6Vmr9L7XeHwZbkTFX1e%2BPJQrzAid9og&X-Amz-Signature=b1068b0f2ff1f1ef05fb70d050684a13b925b31a717cf948ea070edc5d500586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXI45PSB%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBfLodkS28mevWrswTUoEUmxUUkC7t0VLlp0BJOW9dfQIgWYdKQZNB6QLMgnp46SNeM0mMxtkZnFZhTm5pr%2Fh44aIqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNAVgXWJWCnwTZz0ISrcA229FE%2BCLH131UBrRku9hp0U%2FOPv8z5VTLU3svG%2BYQT69Fl1E8mzm6HpZTQF7Q0rayeENZi5YD8p95cOmgfO46lx9UpdGmUWlawFkdeXVFCElbeaaWzGDPF2EGIS6STqmAwhvjFd95H0y%2BUoKx4QxdoJEya2MUmVK6zmQ66QUxa2%2F%2B0EsH6dVLq18BK4L45OwhQfun9j7y8uc8FxDllYc3hNvA8%2FOW2qe27sSIlwaC8VdQrqrbsAMPiPLdBen1J9f0mmXC1aTH%2Fo1CDGjNC6DYLR7ET4W%2FNBCFEL2b2B7PpUzye%2FIVRezMFN7D%2BQI3LQwfCh%2BXpMKlrE0lzNqjkWhvfB4JjJoZPptn58MSQo%2Fx%2B%2F0CqWqXYgO6ylciGOb%2BpgdIApZNCO9L4XvQ7%2BU4%2BskCO7BuEJQfSi5mh4WAdYCGmietQI3TqVmLqbOMvdHvQyaSguHZdd0nZ8qUBn9nkj6K02TGGkg%2FhzxmuZRZDdiyeXVpd0HDQyVzQP%2FoGSd5wbpqgkYeox8eRB3Jt75YoCtRXO0xxar6f28siUN9YbO%2FoqbXB10dCa%2B9ijOp%2FRRGuG%2BXa8EDQ%2B2yIPYqkYWAbQ84WlnQMIyM6vTrsKyvjREz8oumO5RwWmvnyLnWRKMP3u2MkGOqUBJUR1DpTmhO7XUiAg5DNm6BhOjgI1jlaxNyNy6qjdaVd1aChzBCc%2Bk%2Bahbb6iMTTj5nMjRrHI1xKPQM9obN6S0sDEc4wdgLP4LIDwhXIrs6UbC6YTrGF3kPRhWsOwZ5o4puaC44NkA4clUl95vgyR7sCnUgV7gkd3gt07%2B%2Bqgliy7lScZoaVM5lNnwzzvp6Vmr9L7XeHwZbkTFX1e%2BPJQrzAid9og&X-Amz-Signature=16bf377a9c1bf4a7f6379c5c24cd2b74524ffe8e77bca4f9f95579907fcea270&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


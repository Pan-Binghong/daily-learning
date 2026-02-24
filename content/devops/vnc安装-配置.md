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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEATHZTY%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIH5bmRxfRKm%2F2C%2FU%2BUxKv8dO6o91HEiIGhXB36wluqJkAiEA0awl8qSPegguUj3fiUeYypjmhA1eZbbVBYQXSS8vGdMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClyneJvnIuNML64uSrcA9mqfkKEK%2FOz2DPf1PrGl%2BmGrMvXSDGnyzXSl%2BKpC5hv4xuzNy%2BTG0eTb894TXcN9DwIb36PCMf9Arq32Ps8L2ap6s%2BG061My9%2Fza53gdYn0sNBaKMbXf1ufkQRp9ebXO%2FIdIadQZVLgFII3vzJNUgKtOsi%2BsPuh8GzOOVh3GN6Y7NHNaPjE6qYy85CXTIiaLtV2PBv%2Bphg0i%2BOiFAQORt9vaKkx64CfkkOe%2FCH%2BpBqg4k%2BLufuqEMRa3GI0eZWfMTlDgkNLqlNiy92BRYRTYymTMkgORdd7Kr4TH178noy%2FOB6o7f54HrwgAT%2BNYcI1Cu5BlY4jgPhigprDJUqy49PKS5B%2BQLTjJi%2BFfa1uBc7Xqx%2F%2Br2Hp7e8iPkv2WI%2F%2BbUvTARv1W3BgVlfZMw0o3KlLoxzpTiaUuYYjbGTvSNXl8s9jeKP2uKJGVszcC9%2FAxX2yXYkjjONA6QrEZvvUWWSrFU47UOjbB4%2FcrasAQdV9cvqCHDLpWkO7KK6Ry%2FMvMVBz62hs5qw4NxEmd4FyoQ%2FpaLFGxzQG5CAwRXT7%2BuUbLhid4SPlhVcd0k2DvyI5U8nU2vOB4rvviLQuZV%2Fa%2FcLMoVKe1aO0wkjakKrDhv9yJ2voWH%2FCflrcI7T0MOa19MwGOqUBwCoL1TPb2vmjhZNLe47gLFtyU2PGKoIhkivUbwSvSfVGSp6AcK888bUdhwZctaJwTR82P3abSImLvTgjGTuLtbRZC5R5ykWpDrpz1AWk2qRDpaVpssDiTcgLyTNxZUepIiKDwpe5C2wQszHyZ9zEBa2c9JgOgRwpgt49kRWl1ClMkDFTmTbAClVBmzv4sXwHwZ%2BpwatlOB3ff2xCfNOlTwNCxodK&X-Amz-Signature=e75321eb14cebf069f3384192498dfea2998d450b1134067f05cbbd49d49874d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEATHZTY%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIH5bmRxfRKm%2F2C%2FU%2BUxKv8dO6o91HEiIGhXB36wluqJkAiEA0awl8qSPegguUj3fiUeYypjmhA1eZbbVBYQXSS8vGdMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClyneJvnIuNML64uSrcA9mqfkKEK%2FOz2DPf1PrGl%2BmGrMvXSDGnyzXSl%2BKpC5hv4xuzNy%2BTG0eTb894TXcN9DwIb36PCMf9Arq32Ps8L2ap6s%2BG061My9%2Fza53gdYn0sNBaKMbXf1ufkQRp9ebXO%2FIdIadQZVLgFII3vzJNUgKtOsi%2BsPuh8GzOOVh3GN6Y7NHNaPjE6qYy85CXTIiaLtV2PBv%2Bphg0i%2BOiFAQORt9vaKkx64CfkkOe%2FCH%2BpBqg4k%2BLufuqEMRa3GI0eZWfMTlDgkNLqlNiy92BRYRTYymTMkgORdd7Kr4TH178noy%2FOB6o7f54HrwgAT%2BNYcI1Cu5BlY4jgPhigprDJUqy49PKS5B%2BQLTjJi%2BFfa1uBc7Xqx%2F%2Br2Hp7e8iPkv2WI%2F%2BbUvTARv1W3BgVlfZMw0o3KlLoxzpTiaUuYYjbGTvSNXl8s9jeKP2uKJGVszcC9%2FAxX2yXYkjjONA6QrEZvvUWWSrFU47UOjbB4%2FcrasAQdV9cvqCHDLpWkO7KK6Ry%2FMvMVBz62hs5qw4NxEmd4FyoQ%2FpaLFGxzQG5CAwRXT7%2BuUbLhid4SPlhVcd0k2DvyI5U8nU2vOB4rvviLQuZV%2Fa%2FcLMoVKe1aO0wkjakKrDhv9yJ2voWH%2FCflrcI7T0MOa19MwGOqUBwCoL1TPb2vmjhZNLe47gLFtyU2PGKoIhkivUbwSvSfVGSp6AcK888bUdhwZctaJwTR82P3abSImLvTgjGTuLtbRZC5R5ykWpDrpz1AWk2qRDpaVpssDiTcgLyTNxZUepIiKDwpe5C2wQszHyZ9zEBa2c9JgOgRwpgt49kRWl1ClMkDFTmTbAClVBmzv4sXwHwZ%2BpwatlOB3ff2xCfNOlTwNCxodK&X-Amz-Signature=8ab58da1105fc9818027a101ee5aba61598bd50d136c1d0845f820f86ec4bece&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


---
title: Ngrok安装 | 运行方法
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-29T12:21:00.000Z'
draft: false
tags:
- Ngrok
categories:
- DevOps
---

> 💡 前几天帮人微调模型的时候，使用的LlamaFactory的WebUI，由于服务部署到他的内网环境内，做了内网穿透使得可以让多人访问。刚好想着了解一下，在此背景下，撰写了本文章。

## 内网穿透

### 原理

又称为NAT穿透。NAT穿透技术是让NAT背后的设备，先访问指定的外网服务器，由指定的外网服务器搭建桥梁，打通内、外网设备的访问通道，最终实现外网设备访问到内网设备。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV2F5HQB%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHtoMk6ukLCzlZ9kwZmXzEjgnjWG02nRdLSidhsvMAjpAiBSPeDXuOOVdD6zOCrXDHFKVC0%2Bodd1OslnBWOj98GYgir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM0HzcykWJBaJT%2BKt4KtwDPYQJyE9zEZbRFFohLkWhgliwe%2Bi7SjVUD9vI4zH%2FEc8bDHhdFcVYDMh7ubstLZj4uKPxUHlfr1lq9cBTKWHygNh7pBGSygXOT45B2j3JDiedT2XWi2cIdUowVN%2BjzceF88zop1CYVsP3tL%2Fb9LqAjRMxD%2BCb9JSQZQKuKCfjPfPRuMmjiU9lig%2Fm5iqFXE3Cho7tQAq6RT%2FAX3qx8GsF2RUlKZhsD19Gfm67S819%2FidN7N8LEEtx9yLK6vA3EfAv9fGolHnnevRWVzPWb860SBcozudkTzJbUSBdcQOnsoeIzW5HDO8zGzVYJdKJTdtStaKc8YuzGAtGzJKulHr5cVEv38SRaO19zVLxzVwHBNkEphtfCwFYku7SxETUgJctAxcpf2FwpmaWMHitEmj3YnGwxFlhG05SJfkkmQ3gAI%2FWN63peSj3BSxLDdNyLnNVXkjcqjeK26BoxBrxxQq2qEzfveNYReh%2FPTv2Y5B5FpCEb6Xz62ZWjbAhBW%2B32iOObrYXKn4HEbY%2BAKoFkObwXI4Ghxt1xG5GmTu2Hd8DeqbexEtATnUiPQzc7Eid1b8HrKyKIyCMUb8TicBpatlfq4%2Bm6kmep%2B3YkUdl%2Fbg8L14zQDJRGmy7mHbcAKQwqJS%2ByQY6pgEuRaP9YOU%2F8PAHrpCcK9H9mQmwIJLbn1hv0sEtAH6cHaewGBXRxhzGnOJDtBdjlAUx%2BTbqS7XLIPowP7os8fBrUXdK9%2FSGSN4xTJMpuhbYwYEx8dg0OdJdVRJo4U6Enpy5GPIBV7g638tm6Z2EpRt1povbUTJ6dsQnG9B1ZAd3nhY3ChQ2%2BSWjk8F3hMBmAzLT3EcMMGPx3HxhK6rAouY3j5bS5HWJ&X-Amz-Signature=37354d6bff6ab77081b1d973229c535c852f6ae774850ac5e08e202bbcd6c2b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 常用工具

参考各大论坛关于内网穿透工具的评论区。

- Ngrok
- frp
- 花生壳
- ZEROTIER
- 樱花FRP
## Ngrok

ngrok的极其简单，官网写的很清楚，下面是官方的安装教程。为了加深记忆，我就复制一下吧。

[https://dashboard.ngrok.com/get-started/setup/windows](https://dashboard.ngrok.com/get-started/setup/windows)

### 安装

安装前需要在该网站进行账号的注册，用于登陆。

1. 根据自身情况，选择合适的安装方式。
1. 假设选择是在Windows内安装，打开终端，输入：
---

### 使用

在终端输入：

```json
ngrok http http://localhost:80
```

> 表示将本地的80端口映射到ngrok的服务器内。

---

> Reference


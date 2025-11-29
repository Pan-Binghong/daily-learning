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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O57HWCD%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfmmrCUBDrZnnUj%2FhMAf5k%2BJpxlIMHq6ycsbcUfvPv2wIgBk%2FSwGXmYvPG1l4Gb%2BB4a57rnrUYfzgOOONdDjgzHPcqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqaBHl0yzc5YltlpCrcAxz6e%2BblgusbJMGhDwvMhHYqgJQKrJs%2FhkmnYFZ104EPT9J78y%2Bg8U1%2BUri%2FGhKiufG8dmR6StpFd7VZzfP4qFdMrARONUp1gDnenzE3NGLSifKt7R55nQULcAj0XbsXnvoTnTgnuAXe%2B2IqtDsHjRA8wSGPg8bdFC6FDAADPaaVzAIPGk1YSqqvBtXFCEAN%2B1ePB4eF6FjbLv6DaTECT8gee%2FrXoz72Jjw9Fvpk1Nnc3JgrWL%2BZFdjZl9MeK9f1GBULEz3hVcOiGj8WWjvyczhgo9yyicFliG7cTHLZ4l5wNAaxdrxBdYSa73wsyVRCodsZ9HZ0Uie095tp7QaEA5%2BA%2B6V9OQx%2Fml%2BdRNtBzNoocEcIXllYbXxs8NkKhjlmXIV8VANNG9b%2BV7Xgp1YQ9Wb8wFM8MFyjsgCq4FgBk%2Blhj88rvaiMg5spkpdCmsqij6wkD%2F9a%2Fzc3X0veK%2Fj3gPL3gC6r7t0Q5z0MohPFHYD8DUwJkAnNC2i0If32C5oh4%2B%2BvhuikUaRIzd8fzV18EAN2jRyF8SVnRlWncwfMtFXqNfbt46lF6LSRd%2BaXEUITLJaZ%2FmTbzIssCE0AaMTaD3%2BqaKYCAoepzTVBVQvtXLWSkE4Xaf4EHcZuw%2FwBMJeXqckGOqUBFcj93rNGosVvwQH3B%2BlTgA1JyR4%2FO7C3TyVHMxhVIoLKqAYVzeM6QZIfmiCX7ZpU0hd1TOkEEfAkR%2BlR86hq%2BXPv7EVn29gMXq3r2rNIYE%2B2lrKRxU0hBR0yupTMhfDziC2TmqMKhdQx%2BCeVhQzvA4c0LRw1R5ZMAFNzcpXJGGrzRAFQlNEfn6J21PekO4dx10NKA6TVD0SdmCRK6zmb9dki1cyd&X-Amz-Signature=5fa317c388c5d2359ae4d2958993f2e7ba3d6ca5d2adfcf3888edce10cdda8df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


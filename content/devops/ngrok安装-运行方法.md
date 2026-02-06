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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIXXZN3K%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCN2Lnr0K3vDETd%2FxnHrhfvMU9VH2YpfRAL6sS%2FZ6OcdwIhAOF3wHtPZBlDndlYzrhUP7LkLVOzsSaLKSqFCftbYHUkKv8DCDwQABoMNjM3NDIzMTgzODA1IgyvgdJtWPf4KAY1vr8q3APirrvUak3Dq%2BhHxU9HloyKBw9fpCZ54B6hDs7eHqC7iSHoRnWt2%2F4FNqAxkuxzALVRCB62Hxelv5hnnF5xWgnQp%2BiTfT8bmgVMzwBNrNSWxcXWgBoB%2BQOFd9%2FxVKoFtDs37IofpoOK0M8Pq0zVJ3Hzn6BxrMo74P7tMKOqattynY8zwHu%2F2MqXkOMOacv0PyNjoB1Feezxl5h0Xyf2coUqZCfNg8KIy9I7UMHFTZJiV7W3lLeKlCqbgYoPJAmtEySeWZzsGsjZpfSKYHiFJ4GXvHxuaqyEfFE%2BV8yWz5PppHHU4JTQW2anR0JP8vjM5ihcaCZTprAwbhxwyFKhi9dZX9vd%2FJ7GBQPwmt7vMWkz8TjxgKBjRtUg%2F0hUyugAgVZPaSO3ztpxmdRJQEpU%2FOEKwkFQvIPlaRKN1quWo7NYRQTsfPhWrZzru0z5unwB6Q%2F39I0WlaTd5mIJrt6o70E%2B3vgeOAKXEBkkT%2Br7wnyL02WqMsACDy0Ud%2FR4qNIkNCt7OWdM7Ry35XwhuPpa65cmAPLeUUiBqHJRZIa51UVnr3rJsOfeR%2FG%2ByWyd%2F8TvtKg%2FkMbZ2qc%2FIztVPPm0FIY%2BLnvTz2RiYeo%2FZWX176zFNRTolaxYSvLI55NjdDC%2BuZXMBjqkAYVp4%2FwAG9wvHr%2FS1f1cSgF1qazzk7uXcD6mQnHOsEB2WPfeHCNCMS7n2DReJ%2B0dUnHupjCvYO4BNOwtVVKGdZdExbRM0wL6Mfs0o7hp0LBkmrvO8VjLNSpTP2qBPaPslEjueUhJx7wHWF823xnpOgQQ2ZsU3iZyvJKVlRtiYyHNvI1U753Lug1DnQ8YSym5vxCv4ceCdVwZV%2BMce3KJ50EpbZAz&X-Amz-Signature=a49956eedf5d87f73cd56437f83dc14f61b67d47a7db0dbc51e724ace36dfb0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


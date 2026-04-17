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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U5JZBKJ%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHqDtFEiA6BSInxcq6iMT4k1YMJcJPb7nQptEp1sUzxDAiEAgWAZlduquydq0r2HpR2JBcQZojpLSopqZzR%2FMgkk%2FZ8qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYiZPxUsjAlVy3oKircA2OiSqisI8kLMhqq9Fy%2BTN%2B37J4hI8im%2FI9WmgV%2BsAXcqJuMhlxU2pDrb83DvITYdvezPTJTOYZ3u%2FZjIt3jCfmnfTHnXTTuuM9vI8nUZtr4wKeSEpLRtIgvRTjFht5wdn2kZgnrw7%2F4w6Q%2FT3MVIdpzMZ46ZN90812S%2FK7kX%2Bv5MKEKLj%2BtQ3ruix7rmZpYBVILijyuVpqRZXqoVjmevf60TkooPPBwkJ%2FiksgaxE3Oe1Xpp20D5a5Fsed51SoKYhy0cCTwbPEmUAyt14sUgXZtq%2BgGpbLFzksMw0xc0gQDjrl8b%2FASILl0x50O9Vx0A0v6BJMYxA1vy2Q4FANpX7M9mccsTVeSnB3eQdv5Jro4XxlB1ROaK50noB1ZbZXdCE%2BS6mHRiSSoCii9DcsJFDaZB9pYFicd6gaCii2aEiECnfB0GNviIv9%2FJ2uIg6j19voX0bGY19rcTCGSNsFs%2B1H%2Ber1DMwPkGJzpzY0FHxe9AaWkWszZkA70PJSZlENEC4Ecxg1H8USvRT4BtT6FeVw9lydBOcilkrXfFs0w4gmjZeQhifBP61Fm%2BXr2DhEypowmNlLnY%2BafRLfOsRZ9UycVgoLoS%2BLWJh0gr%2F3MzddHE1RkCjPxGyBMXeBpMO67hs8GOqUBamgFnbtIJlAd0qWT0QQcUtfV3YMyiQxzUKhg4Rjxf0DqPtiYGjREwqjqe6YozehoAeHFaxdrbXQGEv3UxhUbjRViWzlRoWmpMOgNE82Sn6eb%2FgaLG7P%2FvY3dSkuC9cf%2FHypbr%2B9Gc7jToOlootZWXTLasvFoGaIO%2FIQlKKUf2nPCv0LkzheCheOOcVVfElSuoKhcF6sDo%2FrcqYiqpIxCYLrqI9tM&X-Amz-Signature=0effe390f129e7da60412af84ffae068a25d9e0cf6afd0c517e5c624414f1faa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


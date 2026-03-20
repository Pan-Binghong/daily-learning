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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TASHMK2Z%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCH1dNTrQtBSvFRZEvuH7JoQX7fMuYlwH6mzozSoawHYoCIQC5n3Cg%2BIITzwfqcrKawFk%2FwobhNxBadPIgWXwDLIeXFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMfNs0sMha7B6i1JBTKtwD23BS48T%2ByzLDPrph1%2BoHA6Y7UCx%2FAb6HWN4T%2FHcn0xCXl2Nr3uENCoEKVaApKDVXsHmDpbZ3giLFzDXLPwM2Pmv2Gm4UzESbatA4gH%2F7mmZzrmkoFz9Sie8C6KD4JQ7r94RlaJw6%2FsR%2FPzm9OPforzcfgOYgfKWnp3NULakWaR7sLheXZtACUDO31QUWuRLlEaBnpaHZGaiCmj7ISHqJP917K1vPgJ7kGKzwu16gFIm0BuQSpCLwjzcbC37zTovsMBnpqJnZI6LvAt7Tb0Bo9rUDSJhTl5IhY11HQ3cleIpnMSYM0hS%2FKNxD9LzTx16eUEdH8MDv0Wi4%2Bu71dX16ffxv1yeuENJfWG05QX28LjSd%2Brb4foHdfbApXtAK1BNWTjAcHE3Is2qZTkcM4%2BP1BYvacH7F1RNzSOorDM1Vn0THOJegzIvTp1Fbkf9HNbeByThbgjuSvwRfKAUBnIn5UeXlZecrcJ5PjmyqOAq0hNceWB2FsZ6SM6f1dzBD7x5Rk%2F6B4JuGDrESkZ49jaAPuIWdJFaMYEM8EFvk8D1xJ3zuYG6FYLOicIRml%2BJ3K0Qyc1o99yJlhjIAUTcz2nRmh8AWL3lQz9cqvxdtFav0CPbYSTGwDpy3ndbB7mowprfyzQY6pgEbcoLgyeh4KNGLG5E1BjeMDuOTsAwhZDvKSzgoC488sLZQA77%2Bfk95NKqcMg3uhOnmnTs2U0KrlbXVoucYUjOdL%2BOITAY3ZA9yTnJIuO8KGexjIT29TLtATQm7LJ%2BGBeERDMrDN3kft2HLu0xelqAbAlSbsEAS7FZLUMNrERRXSuMUzQhh65A79Vc8Bz950GxShkmpX7X0%2BPBWyph1n596Ta01QLiw&X-Amz-Signature=5c7742ad4aa7bde8fab7beef75058031b0bc52f9d55118ccce0b89f5b9e91969&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


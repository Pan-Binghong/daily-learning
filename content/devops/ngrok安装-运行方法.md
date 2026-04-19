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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJIVFBGM%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDrXP4KHNXEZZ9PK2yolGfeF80%2FdvrFvBKK41%2FwuQdVeQIgN5fGz4UQwImHFK8WOBKUCrmfQ1QfQz8WgRVZYz507NcqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYdxcmRi6SwKNjxhCrcA0aS2n1%2Bzpy36uNdjmNbhPe2ng7XHTovPECynOn7RWGvjLtiZwcLHWvSOhzP58ag98D%2BuzDQ6VKYafKeX%2B9Umb8YBDuwpNumAK2Mf%2B6WtgOlnGNJZalkOS0kKdJCNwKd0S5vGW09bB2Zn1TYWHvbX4mQ5LaiamaOk%2F92466R316qpUqD0OWvsmAz3KAVP5yplGpJOf%2BH91ufmMd3riKXptBb9liSxqrMT93DVtV3xLNF%2FUszbTePeABl9pgaMJLPdM6M8S1DWeCDr9j40da5k2ZFo7UHxZc5db0WzSL4H2Qo7MslGo4t4J0eQeORhSTHKdxgFXeB6dgK4i6C8nu6xOlLUkMM85ydTGrnb5Vw3wmn808kwXiECNme1NFGXh9z71bx8eWUDDPO6N2HNjjDnNlLCC64pK%2BAPKWSongoR77NchhiHjx85W0ipamB%2Fkb6zvFhIK5Sr8iTX16%2BnETOMv2rRCtzpCk483BO3xePfOcyzJlhb0dLV7SXJQUEvQsLFAf6ulF2kExgloPhTcGXndzad5nfKo6X5Vmp5FFWb4KEbrQUw4GYsuLIOTQWnBR3TDgqMScpL%2Bilk1y8dYRnYao%2F34e9%2BVtx3IzJygPAIfx8wEnF%2Bp78IFGukzd5MJzckM8GOqUBg7D2McZIb2bbun6f0zvnNvgxcRbOvT%2B15CKW8VP32hjkq9eg8%2FyOBK3lqfIGOsgi%2BqJPDss64%2F08dTCGbjoFLmXNULBRwKuNg%2BZ5M3ACB4lbtE5Ykr4oytuD6uvldNAH%2FoGLqh9Qf42GvbezN7rTtqc2nfKzG43MxrJc1ZSuC6Qt%2BP0QJ%2BJCgLsQGy1OuOkZigaAcztm%2FRuuhjcCnFr3%2FXinUWNy&X-Amz-Signature=75221cc6f07ae42655493ee83496c0572d919255bc559b6c0b3aa1b8d4039ee3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


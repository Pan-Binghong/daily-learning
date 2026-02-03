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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XIXVUQ7%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIECK%2BPHuL3ZUeS9D4zUQIo10moGVA%2BTWCNEfYCOaGor%2BAiBo%2BCDnkecN2jtbRKePsRGlIitOEcMMnGe6uWr%2Fot%2F4OSqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYXN5G3aME%2FkTyw09KtwDxgATwdUo67yl7iKYi0n%2F7FI9rBk%2BmWU7v5hflEBr1HwaFkqDYYNQzVG8pnTzKD8nlrq6XtQZH2k9ZXJa2izvZ%2FmAZPzTfi2hL5g8uDD6G0g%2FIpnIU2fUrQg%2FMZmJEu4rEm31ocHkMMypu%2BOF1V1SwXO0OY%2BOKPI9Df73mw3FiwRPfOCnbptN49KwmQkL%2BUYtWFKSqGZM9TEWg%2Bs10eauihe1zuOfQpbT%2BFVijsssTykSzRFVTA4BZbEjlEyUpEvr5pRWUC5IalCpRcei3GXKmShoz5Phd6VEutbVb9dd7G%2F2k%2B4YrZ4n8qBISc%2BCUzI57kkGJR7oMCKukIg9jpkWzaMQso5tXlj54YnF9GAQHLsnobgy6GOzHC6D43EL24nMAZb0dm3%2FWHMVApM3o0io6nXtOoFJIJuiLjvdUVknCw%2FdKm3NYu41OuXopwiDRTXQXXmlftlEoEF%2Bd5UsJB%2FtEb4iRoRm9togCj6se1IWlpIdlr3uol3Yu0CMObAg%2F30w%2BQHiybE6LnFtFgtvxvWmJNy3UYnG6WcgUwln%2B0PvHuV33cpy%2FzGHa3h8ALCdN0%2BWN8aPe3qJf4O1ASJcFN1ulr6eJkHw3dEMMk%2F14%2BwKHe3vB7h6pbYlphP2XKEwrdiFzAY6pgF2l6HifzUAqbJQtR9kjg8aKEIeYnm%2FOBZd9C%2BUlkJINXGhHnybshhh3nL%2B5tf5oTquTwTTYI2J1yG8%2B939lvuX1UaILmd30GzchQbwb%2FpL4iU2EcsL5Hh6heS3dIqgqnZj3J1FGQxzc1WI2ELfBTYdfj%2FmUdM3WN%2FEZIgar3toCIYt823RkXPeDsj8ljsbH4wNOyaTrPvdmMf4TMLb9N0RfecizQba&X-Amz-Signature=e7c2b9cb57b8e4a3fb27da8c0c6b023a991e7078c68e97baf1bff0c6b3e3ae22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGVQLH47%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQD1Zx6Ov3W18ThgGXoE3xhWHUtGTHAnZC2qFErCCHd%2BwwIhAJi6nZOI6AACePOn4E7vVn52SbOX847PRIdv4O4qRM4DKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6DBQgDkKloz6Q4u0q3APHolUjwY6SmUXlJjmXNRu2FfBumVy4wZvX4jfEGAFjAPqZTLdc%2B9%2Fo9r32JiZPoi4MxqkikEBNLcdXijvk5vpQE299h0nbZSgZtBBEXS%2B4irT1bkxOvHSnu1NNgrMr0EtSJyHp%2Ffc3u2w8UwNJ6fYdEptMRfxyAxstESOFACGhR1kkg9gD5th8smT5AQQ4QqRSUOghx31OMugvJg5GvBcku8uNCpJBMo6%2B5lI2L0%2F0fmVblq8T9yGPcc0JZUwr0Jn33y0k3rxV2z976P8JWXoSb8gXmG38t%2Fhg4lDQIWeueRGyqBqT4pVzEVjCdLEBkhCvfk8fQOePjDfS%2Ff6P4zWMt8qjoyhBVSBtb5Vul74sbTX7gbH1DJiIRKx0XNtWYe9Z5pve6dlKIHDu6YA6%2F3JcbxFBJhFEUvX2O8t9zKy63q8rrZblSSoWxXBlnSijA4dlBhijrZ9wYG9Y0LU99ax%2FAULAt23vLvhjCx03IikIcdE6CjFD9v38kRGAfPA7Er0A6NzgscULEudw5BeQB9dkJJj0i4NcFXhad3CuPdcREYomC5Rwo6FA8g57fyvkqG%2FbNAayLWnBMw7V1JhvlzUAdDKrVGpUhTEPb42VXGDQs2sV0JeAvasr%2BggWCDCu5pbLBjqkAQHIv3AwFqQfdlDaG%2FJxIIxnBovvBuCQJQbXcFEizOjCy6w%2BXNrG6QCRhcXj%2BLZZlwfsCGuGVhpz8OK8xgxy%2FQApJe7r%2FalsLeOb4uXTax1BLiIEsU%2FL3NvL5a1%2B5Vew4YNdf8rYVV7K54EauzHs93Tq88htA05fuzFImiWS7qjCFY0eNWhWq%2B2ElBfsBqjE1Y6PWYHHU%2BzKGc3nZfkUT12YtLsw&X-Amz-Signature=5a9674561aa0f119bb54b7f915b8aa7db1744620e00a3ac007dbf1cc6e1fa096&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


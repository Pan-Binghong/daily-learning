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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LKTK5ZT%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHMQKgXTlH6NnjgX5LqEaDEBeULi9lqoilK75IaRTRhDAiEAyHDCrPRTEFwWNMPNlmLbF6KtF3nJ4HpxYix1bpbLOC0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNM9TnvAyWvhCBxtyrcA9BFUq5jv%2FizdVVjKr7fHk1nmWiFygONRNCtuC8wLu9%2F%2FhNoziB%2B1rpeccn3GgQe9gBx3qfz0LpSTGeD%2BXbTSIhvgzZL867SqZrqz3RoIA%2FZjBM9FvcX7DBT4d%2BfNtEsps5p3h8UVbPqW53jYgYrGH87r7ewsEtQHF0EELNE9a5bR4YinpnF%2BVWBGO3AN%2BvESVjXoD4UdLi4SaO8RWFxSKh03cD0VOXLLYU98H%2B0Py6v%2BDR9H0j2X6NMTg6%2F906J39yVf2%2B4J65O2Bv1JZjQTvDnyscFxQvoANO2DKeQHAPXF916aUB5n90HHBvOHoQLeMeYvcfTUb1lICvAcboQocCMdoa33LUiinRollsKoKViFJgTsmbuQb8rfxNAH%2Fvz%2FzSTYtlZHZW8GQ4SejfT0vleobBJfid1HS1PPf%2FWno5WON%2BbL93m0%2B7%2FBp3qyZYqj6eWoc%2Ff6%2F%2FdYXQz8lRDpVyMkyIJncCLm8Fo19moEayEsloA%2B82Ox5QlKDBEPbel6oS0pMz4K7T3Qwg9qRa3R0q7%2F2J1fMlAvKJafYkwJnxJolC7cf4BUrlfDVGDP0jECXce2l7ZBFpQ4j%2Fnpf1dtURMOr8Gsvl%2Fkqt3EVYKCMVGC5Tg6nZQR%2BmDD7AnMLzyh84GOqUBIu02tPmOXpeqXdc570AWpSmvC0TbyDDJF50APZM0c0Q1yW6hjyEQtbkM5cy8YK6mRTO8LAHKz7DjL29Q52nCH319Skz%2FE5XY6EWl16FTDFDQ2967LgS%2BAzK%2BtEdrwC5FUtZKWRjhDHz2leNY7e94LszIoDw2jWrTi%2FjgpCZIX3DsxUQsLzaoX9LbMT58C%2B%2Bu2RZbWgAuunXyOP6E7NC7dQLOL9wF&X-Amz-Signature=eac9d11298a31601203bf38fcb6749c5dee7338f67a3cf77750c588292d45e16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


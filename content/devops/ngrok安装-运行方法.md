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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656J6UDX6%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEFy8iUnlXqB%2FCFmQToydjHkjBa6kZpiXCXU2Q%2BcHXZBAiEAtTcEuf2D67tg4rZ2VizjK1uKG0KmhYYB%2Bsnh7H8j8jwqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC0z5pR2mu%2FgD9qgVyrcA6%2F6zFUqFWFRSnW%2BjQQIO3qrnq0yI%2FdWhQovVdChrqfXCY15GzyxUQPWuzfB9%2BXOuMJAYEL8oenCUmnAz64FhZPS6sPEN2qIRRZEE%2FEAWGqmCvRv%2BpJj5lWaFz6tyB6JdnUvbPPfD94mGHRmdJlyrIVKFVxBAh1xIKbLo6erHphdWjZ0NCZlGfxmTnnf%2FCvWc1ZXnT3ZUm2gC7WM82LFY7%2BDUMmUvM89f8sOpQMhcROU5rqIoOKTL7d2p9TQ9pfoYr2uRpC%2BF7%2B%2BdyJCB3TEBsmz6mwqyc5jB%2BnAwOzqQXkbzBXAbgDuFESoz3ZQI2lzLbjkLglo09Jd%2BS%2Bk6kGJB0L52NYxXlA6lSOnsSNxsRWaYIWV2X7w48E%2Bp1A%2FSajdRES%2BP6uQyy3cTV7mM0WqQcwxIMamTyvU4xFuxuNcbA%2BML3clg9iCJZeF4RCqGFYkrf4HfYKP7mP34MRgXRk33bXgDcHb2EmIAann4XpCAHUwc1LS2Ma9l1qE72dkXilWTei%2B5hpiLtsbkfJZtTR%2FhtLQOsGOZyjqQIRGn7iCfKI9Uk7kN%2FoWVAiSM7jG2AM015WXwEmxkmvQ0lP6XArup0MZGt%2B5jxw8VeB7tbWShKCABFUW%2BghhoiijAyrrMKGti88GOqUBqQbJtzOJ%2BvZ4y1ySlK7uVQ%2ByvfWFl8WZJGP8ZuaZKQQ43fpGxfhjPQp6a7R6GZO0AXaP5r4O4uGqeIhk99iu7xCHK1hKLOUmwr0io0dIn7Mso38Q1pwE2DmTOT0OR92tVT0DYWVI8bt8YqOw1mQ7sxF%2FW%2Ffis2bJQiKF4oTy0cKviK2JHri6Z6eeO9DLmqma09LbvyxFsTugyt6FdJigLapk6T3X&X-Amz-Signature=c1720869762d10dc310f38517d90cdf02b4441975f66ddd77ff2473fa0eaf386&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


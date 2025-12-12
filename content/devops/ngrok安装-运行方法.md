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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQDQL5PQ%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIA1fSZMAcpPzlr%2BKVeP85esYDISWP7tVE2y%2F2n254WpAAiEAtSdPow0xWwJ6umZRdxojrq6zcvq4cs%2B6ogbSImhLiicqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1srsB447pYIH3A5SrcAwBbYDWRFATokwhNI48L3BHKJh3Odwc3%2FnoI8aBqxYlDVEM6hQfcmKj1UWtcWQq6BY%2BLkyPCNHEUMBJ4NV0hOGVUeygITRVti%2B1jQx1OL38Zb%2BG7tgMUawdqWsecnN0pR9bpcq4V%2B0NobC7DFfvYZ5i7b7jYZZu8CWz%2B9LJ3PFmJjmNaX6m82VhK8ZtCsk%2FSENhf8QJ9%2BxI%2FRhJ15kthvZujXwdBA2VhVM6asJ8%2FWX0AczjrEHJQ1y1fGkyWEWYJV2OnGnMelNQmh0Gu7Zb4nMl9XonZqC13%2F870QRZhDZxagvgEb8Y1hqFvSxJQEQ4DjCwcCZD9BEOHaJhqDljaZJDt9%2BSEwF6yGjxee9lh7vRvlf3FiGvf0%2FHadc8sxPHk186r6WtDBtCyCCwc7wLFEpaiQyKF2mQsEYxycKh4dAaz5T9l3vwtPkDbAq2Hl2Pux8xUaeFTQ4Q7GXro7JxnoFVBMYk30KFF1BEWj6WgagrZYu%2FMan0RJiYDZ%2BQ9DY6xVs1i1tWtFcSlMkaB0aR%2F2yFAwqhw5YyFyTJtNue9OVlxJCTm2h5ZZQ%2BbHO%2Fcj3Qvsn34qkSFknawJAH%2FUs29XLJybJ5n%2FcA5zh1ff47hWIGpcB9Oo%2B3cynQp2J%2FoMMPU7ckGOqUBsp0v9Txv9%2Bs7QTVd2Q8EGJn3Q7ngyWxK0JQlxonDmDzOx1vwPPKwSgg6oEugQF9MCOpmBGFB5YaiTraoCAGvBs5xbc%2BcCFKgHrprxRhzaTV0xn1ETtfpofYnWwP9alZTdRwraWz7ANB3V2JSX8lyiCe5Lju9VBHfFt5ROjTG5MX%2BRsYr62lmXCRAxDehk7b9KHKQrYflB9EijEKU0iTeMhtIsmw4&X-Amz-Signature=e74dbc66897a2e50730133b701b7d5f0e53c67ec1471c86aab8e8b0247e4baae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


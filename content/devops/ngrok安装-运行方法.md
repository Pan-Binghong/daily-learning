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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I57KHHS%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIHxyUn9HOS8iRTzdtYLG%2Fiias7WzcDsFEmgyyok8q%2Ft6AiEAw6aO4vGOPs2dZaBzQTI22Sb8DQ2nCcg3nvAmCV%2FhrNMqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNmTwQdYR0chDt74NyrcA5GGVRP3wO%2Fjf%2F7O2ScDaFvZmF6fD468bYrnnUlUS9uqQY2xqCQeNYzUyKPGepjQHx9KRH07Xqi%2FiXcqxtzdiq4ZFuUZLGPe1r%2FjhPPQGeYtLT5IhksxL%2Fdh7OqUd%2FxlM5B3eQGvClZgBK68rVJ8Pp6%2BZA4gyLV8fqBFNRuZM900r9NXU5XtnJOYdnzHVEgzhT%2BWn9Q59W2xGtsfkp4lgwQfspus3XJOab2KKI5pkEY5%2BE8NOk5VRkS7ChwllPzjmJdjn4LNO%2Bnkorct7lAnH3p%2FfAUMB%2F98J0GpYOIplC46rZAf%2B%2BZ3INI7rMBtCeuNp2H%2FQ8WbEWIp2jZDICNQW%2B5X%2FlkPxbDpuNDnjKgjoYfSXsmdLjX9Feyi66fhYi%2Bt1n9AV2CPOW5LtJ4JtshN7p%2FqNwXMKktGTXNyziWAZO1Ey%2BghPE%2FfvkFe8ywmuGd3HbIN3JErETvvKvpl489wZOOPOOmHpjjPz9%2BOzXGRzDfrCdJB9g3ZJC3mqA1QtX8p0SOHoZbkx3FpZUwzsfyaOuOEzyuKFsTbLBdCTDFaHVeDkF5snNXOl1GRhwkAqbnlIIcPeovr6IdkdyZ8JjODRxfmzV7DE%2BVDanqrb2yFFZjFk5Dz%2BXg7Llr%2BKfthMK3q%2BcgGOqUBexFitW%2BGHrdJuJ1%2Btw2GgKiqVndY1PthXY2EOmb0MMeivq%2ByiduPegedD8ERMj%2B64KS7cL79F9zIy9J4W7GR6WG6gwFRnukUuzvL1zdJiScz%2B0bjP6UPKTFCcYQf9JfszFlcZij023DPwAXb7tf9IyMKz0FpOdxy6a5xlhX593yyg8%2BVYrVszLD%2B7qR1Q8k4BAD7%2FWwB9Pi664lcGSrB%2FAyN89gi&X-Amz-Signature=958c979811b639b59415a3f0d6b56de54c6e2adaa4c3868f900d2f1ce8a2bd98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4RPJK4T%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCASaQDRqXc67ofmwqaKjcM%2F9LnHek4zwkuBXqa%2B4w%2BUgIgBdsWhagza9ESIfwvalM%2BjZK7Kror4X3FABf%2BEIwp1PgqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQzHFEZS5y0LGeBqCrcA22b%2FDIdaJ7uPjWBjYafg%2FZGBOlGPlUd0CnFftdq4pfu4btIUXsl%2FD5C6m%2B3oSpLyJugfcVJKpLMJNcOGI13O6dzTD3fmqI53lo5ct0Jup2GD26uWp3L6fxYvtfGqhubbcR8NaMk6AfY%2F2hHW7MUouXkr%2BdA%2FNuY%2B2%2By9uvG3Pf4eqgARhYZ2NElCyNSWxbaiy4FKOirXsQoAKlsz13xLD9pcDjl5coIhvX3X%2FdemARP9ylZfwWjNhTHhsgkJtLFQDUe7ZVlTeNFDvmmRDZO2q68e535SVI6B8o0CnrcNNXByx9Wug5kwhUYColOcE8u1b9cyPwufYYdCCfr73NE1LJ8A53jRgmHNWnhlKYJY7FdJf2DUzYp9WE8oV%2Ff7QpvbO91Y0EP2NxxyuOL7jyGr4vxhdQpQiDGLSP7XdZg1kQZxIdX%2B7A0PAE7gJAS5mFb7qMYSdEZgpP9k0245hn2T0mtKogpIyd7%2BzHNlAYxOmShoA93UdQVMk5OBBkQPPFKbXGHbkDQ9zGSoUDjeodaAGfby8aAXKxqqGyr%2BD2rjHVE8kIXqPjEX691aQTJJknnvHRar2Un8eO1ph%2F2fUFUR8UNYQo6Mhnbn7%2BpjaaJnU%2F45DHV7Nr5%2BX0kSnJfMIDK9MgGOqUBpRNVZndHmpys9aYBRBE9GYB%2B5NKvFdynFlIY88dzoPkddptUKWuDck7HXiz8JcfrsKhet27ydldzsfB4cSW%2BkEiOESBbDBkmOPEjMI87lZBULN1mGXCROvjhmbGnWUIyl33WkiSRHVq4caz%2F%2F4loNIF9RpEUlhpjlqXvNq3r1XxBdyM8sQAcnRrI7HRA5tPcju%2FP5mM40fAXg68%2F3xMYa18nsl95&X-Amz-Signature=bed80aa56b43f551841e0ceca131cda0d701292bfc711ec069a4991576332ebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


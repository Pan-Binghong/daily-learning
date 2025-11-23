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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBUA2GUF%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIDlmNP5d2ilVxc4swCNaGjuMs5wu1KH7xEedaLa6HOcjAiAAnDoKgc6c5TZRfcUzQ0bTGzfkvJXGeadQkaJhjhIjySr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMgos7oHo6IBN3sry8KtwD5voWQvIJQeTAXXBWH%2BtXVtPcowDz437QQqR9EKnBa7%2BV9UGP1YtvCpiFdtUt3cBMU9dZQX%2BmxFp5pBORoREQy2RPnYuS5znHy14ryIndOeV8%2B4go0h2IW0xLz%2BOgpmyohqCnTipgWOggc2Q%2B9yQGuRaZLsuN8vxJDjuYo1G%2FsL5W7vcttZfucDIdhKl6RT1si6lgr%2B8sVT4EKKazjkEsXlv2OoO%2BYqae9r0PVzfyMvcVgESuJWaGWN1MAJV8KfCEAVihcTdHbseI6T9LN6RQyJiWq%2BIASbr4un5FSUGapxOQYLp0WZH0o7uhLjmplDCPSw4LRZTzt9SviyLuJqsFwowhn9KCCQuynJWN5YwGGqoMcLN3juy%2BAyldOS0adPfquC3cD6wigJXAeRSqyCTloeaiwFoFnW5vHcrG63KxmRDSZOg%2FhgPdLRkRk1g%2F7zJnTJwRbiuGQhITcpOtYu0OLeTysZ6mFkCky6hpP8CVyA6TijVw%2Frxt%2BnM998dNEC255R6xL6VUgwu%2FEQ9zu5oZiopswzUzgy5sIETFtDoQxbCaramEUdI6rph3okRG6su%2BlcmkpbdbkHObT%2BA53UhRVJqtwfVk%2B%2FHJAFfuZ3PNLdUN1jrBahBbchXBbncwjrGJyQY6pgEY7gFE704a8jmHStMPUcnSCygAe3kbLxxlSsyrYBjSFxIrXFR0nYS2gXGFsx572MzzK7di5arUY%2B7p6SujwSBZd3QVkiCB305gUvG%2BEgwD6BX4FCnFa7t%2FnLkxUYhI1GcZ7v%2BqEAqZVMMqFwkKBL9KS4I6AeI4eDkhFiQi%2Fl5RQrSlYB%2FjZWW9O7%2FTQ1Pnt%2F%2F0%2Fmae9MicN0%2Fpnhb1UWOvUQ8QXAGj&X-Amz-Signature=0fe503637d9b4887db98ffb3797cd1b8e5ecb50456e70f734ee6186355549729&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


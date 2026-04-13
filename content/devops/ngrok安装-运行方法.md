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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667DHKA3W%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2BtFLhHIN%2FHlE%2BpinJJMTyq3HfK4vwqNezMS8tjGLpAIgWF%2BTJGQQPHyuiLvf%2BwyOznqH1mG%2FTSyz%2F2rsqDga8xIq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDLs85Kf0qjKKHYEyRSrcAzm2n7mWXDoD7UFBql1QiPOlzQ%2Fib3IciJo9oOR8EY56jLvmnR8cnL5oUtZiuYX5YPTc6tMVPpmtZ5eor7NUyTs9%2BnPq0EN23QyEeH3rgYDZUtOAPvuGX%2BpYJZ1smw8PBsCSDdVcujQpkpZ0w1ioH2FkmHMZ4BdMS%2FzqddgB5LvtDKZcPRvnvGtsFexfF%2BD%2Buz4q0VYmk3MoGGjyZMdWzVY3fIR2ZfMQTDKoCtseKd8CPVzpaXpAcMoYp1mo21lnbjkczpgYe%2BKyVDN%2BSCOjp75GmnId03i2sUsrkaj6H9HXAUU%2FGLCk%2FnaZGErqEi7kBRBQ090nv1NS1kIEfkmBUrQyeVluMwx8U3vaNP%2FIOjuL%2BqUeom%2B0XHtFGXOXgh9nMDyIdno%2BN8C9o2Iq3LtA7%2F3MW9%2BodVsSaBoVO%2BZRqN8dIWE8v0WPZmn9LNsSqodNYHeZklH%2F5ZW6Q3nLfuBPsPY0FHVv9g%2FZ4HA6SCA84NdzfY5jJ9NMvUEXKJEloUhBi%2FfInkCOxRaJrDLV3f8FrsNpQy6KwwXOHBqvYPpAmgAHT9yC4s835hbn4ckl%2BGeCsgFi%2FhdIrSibziBbJKyPo8%2FiCS9tic9N3oHFUjMkMIoRVzfQz6l9KWBPOQB0MPKw8c4GOqUBbI0HgVsrr%2BjYXMyjbWepFSaVJzox5f1TMB6cnpm%2BKGQQmso2RB46bO0iuiko6Py9OOMrQGl3Qqmfn5ql0vKqOcWj0eMh6yJTvBgVfKDNh%2FUp5i8omfppTNQkZf0KuU6sdUGOPKj2InfP5rmIOxOIb8FnrV4nKwgMbnZOwDWkCGGgJL8IC8xIEsUvv1t4dti30fir7%2BLK%2B4YScJE5G9%2B6FiGTTww8&X-Amz-Signature=8b3ba366872f36d1f657169c5f69a038b408fec1cb728de8f939af0c5d436c45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


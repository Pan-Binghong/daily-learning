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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDJJGKU%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTWaaHE1y3JTJfds9WGjICoKE5QiCAsuisHElnd%2B7dmwIgIiHYOZpATgsdOS7ktLQrwIV3KL%2Ffmb1szFV%2FwuqbOwcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfNmcalaRKD90lntCrcAzIQsAEUxxBD391QZXH172%2BUH00FEKBluEnjFc2rJzwzk6Oco8qFtmAFDFwj38QTQ8nOw4b4bv4zxdtKtGX6bPeZdBkbPLYO20UOK1bLgSQd8Cs%2FI25O5VVy0LmFt2UFicCjaD%2FeQydZaBzVrhMq7ZtxfG7DCV7gZnqEioJsfXe9cDgDOnHU9FXOE7mmXHH7DIemrtNoTCNHInFDZwta2O1fruMbpvY5qLZbUGGV%2BH718Wsrj4POTbNzVzbRNYbKToPFbhhTxEjG7iOKlVnAzKx5MiFhfiOW4748764M%2BZZGNdvtJLghBfu%2Ba9lxpBMDXUNZzVkRFLPcQGEKmRegPifGkY%2BdjUdtSsqSZKqLw3TlkXIJYDUO0mvmya98wllW55Op%2Fe55z1aqLhBcpwvGtK3N8gVdpfAYtmmIFDvj0CMHOgcqlea7%2FVf%2FB1bJ7yeOGSMrEL7SJ%2BvRsD0HWMaf36xLlz0uz2Vm3WSv1Vt2Kqkr%2FcKQrupRExKbafNH9zPjKyASCFEMEISkcvLw9WMhspWRCwCy1K0%2F9X6knrOGXiGrzQjRXEytflJm9ObF4e6ksOG%2Bh1xPsvpOB45Z37J5c6YdoTr8BtC6u4c8jI8eEKWe%2FWSUuMYGJgxChZUMMPHCqswGOqUBq%2BTT06ZfM7SC7YbUzWRu0LfjdYV8kuV2n29RvqYBuAgWlh3NJBRdR1%2Bg6LOPPjkj1ZivaNbSAVv7Mj0FkDuRGRAPMP2DgRE5dGq%2FxWwMgD27vwffVuX2z9y9gHj4AEvGjDee0bGIg%2BJyvPdFMUvmag2T%2BDDG57TtEHjPxn45vbB8OgzFwWeqeohduJB4hCBX%2BjUS2URBXGqo5YhVi8zaTLE6V2%2Bv&X-Amz-Signature=42294997888a4452fc513fb43c7c5c8570e7afda1d993e9ee544be4b395dc58c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


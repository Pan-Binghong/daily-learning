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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GO3Q6I5%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIH%2B%2F9biXR497AM2l0L%2BKIo0RN2GauWPyQS0t1Tj4SxWZAiEA0q%2FH84YPAy%2Fjs5SUsCXwsJPEh1R%2FjXstmbHB5yawDL4q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDFcWPa25xkne4gOdMyrcA7vXZ5QpgAu67%2BOJ4MxJ6%2FGD54DtfcrMuI4reTU%2B1b9IRRsZ0bcjOpqC2jzMej%2BsgMZFquSHXr218o01iwvH%2BGo8Mi7CaIKBo1W0NFndyaFfYz4eHCTawZFTN9JlRMhIaUIx2rNbivQaXUcYLJfRMVIIwVlD25aa0bOTpbr%2B8lzGvVijTUqzOztzm%2BYgtzYpS7KHmQjNGJRWXuJZZBbYDJeyWLNEOjCBSZbspwG9orRm9ngFPhRuzqAKeaOxwYObFRruhkeQJa3GkqosrOsZZTzgB9SV859XZnp2GqqCftFlnA8y2D5t%2FdTkh8vlXr3AMnFmkQReMkaOkOibbktq%2BSTkr65jCRr14xG%2BmJ9HwCpoplJEH8cPYsxe0OGAVNR4ubarBufmd1O3O6PtrmyJNWyYKhtZmwH%2B0aDcYLldR9hQ5Q6wDGhfMqPTHYjhlcSpfNnYQ5geGp0F7lwCz95zwmC3jVRZz9CQXAcrDRScXIG4moLHGZNwUTZ0OQy37NVPCOpR5gZQv9vf%2BFYCqmsfkvjhwT%2FiUUBEW7fqxm9PBUwlG9JkEhtoFv6IBB%2B4jyqfMsh%2BG3Iz0VnTHD9kVRqgpIdSBU10NAYxmoyw4691vchaEpSduZCBDostV91cMP%2B%2Fz8wGOqUBWuZZxRKdDNrhv057t05eG1AZnpMl98i2IjBkUwRYLOEEGMf1GaFgih9oR0JzGVFBIg2GLOEpmLklpVFnaqN%2F%2Fzssk28RlmZo6YChGBvyYixsEIrqpgpSA8UGY88yPb7s17nvoWrcdGkw%2FTKNeLrcfIojyLr1hO9njYTUlxy38oBOhJeSum6cIspG%2Fl5ZPOTYQVn3I52FAthr5JpKCVxZrzYBo4Yy&X-Amz-Signature=1d8a8080c519a45f796d01aa052bc3b45b68949f0d0cc9054011520e9856e9bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


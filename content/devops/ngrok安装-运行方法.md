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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOGMCZL3%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIFPGyfS0dJFxz5fQ3KPlgHDucuMkOevzAbjCKOmbWmjJAiEAou%2BY3sx1um47JZdgsq1xsf74H3mSlYmZYyWE89X9%2FfUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDD7ZQMTkEhqHUh9z9CrcAzAfDtFxcwTc8dVV3iuQ3Lqoa9lrxKViOHA5QRVJnBFgFGZGPX0fmyCpMAb9KLGA3UX4Y1yfNkSFknq1YisVsMZFy%2FSqYf0q%2F9M8uRDxw1wE9dmPyjyUM1C68551xdvUZcK8qfwqohHjj6TbkURzH4Z%2F0iJFaunpaTeyvLXd0IAhtLAzGrj9mxx568xlxeu%2BzZ7LomP3OoAfqy2Jc5D%2B2dDC2zWCFAYIskxYEEMq13qLUKLba9c9HIezrXUixoIG9j5aFjO2ikNiOu5RnbeTRxTDxvi%2F922ci8S8lg7SD6yiqnwJROxVz1AlkH3YIID2cijk5IGkylrs9OcT3Q6Ks0wBmAiJrvvJCVQ1bjk52IXX%2BVO4X4mcOwLhVS%2B3Z7mTs2OgcJ9FNeucNXef6X61NYSvqNRudqS%2BFQ7PsC1gtYZ2LeDFNeIGLmADykzJyzr305dFh7ZET8NuNo3q%2FIcyGjEeP5Mk90mH1gVulTlVwjDwAumNRX7it1tzRxSn6huJ4n5x20gYDF3e%2BSs4Zuq2HrLN8UGZxwRS6NtpF6OFQRXiiJHGM6%2F0ODQl5wmkqTtoa5DZHnSW8NgrKH57zamEPsoRFqCVb7uzMR8TOmKabxPB1Sf%2FWofcPeqyWvtLMOXH7c0GOqUBm7t50dYW0hZL0KbOipH0pgbdoDLe3Mavcpk%2Fv8D5qOEILpv9370%2Bm%2BtuKLYjai%2BZpJRFlA9o%2BwmdW%2Fzkq72qnWktVmGsHZuQWn2r685uS8EVmMKQhiwJ9hN1D7oTlvGML%2FkYYiGJ%2FOz4E0vZsT2%2BzbZvHbguqgKTtVS0q0dVFdTiQyrWv9mPnazfqkK4tWDeQIZboo1DEYs7CUBACnLMWXPNsybn&X-Amz-Signature=d243aef300ca1524e92e4625fe9ce2153c52f84e78353104aacd0ecc021a37ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


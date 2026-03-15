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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NI4JOMO%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCzH2lKts0p99eYRulmnnFT2h9bAsYuYCMcvovUWJtAQIgRZN9mdZCEPaHYTLV8Xi3MpvrvMtvxaDkQoW5BIHQ3yoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD4CeOCIQ2kazxU2circA458hhIeoFojarlPDwfN7uYqFSft909sak0HSYPyH%2Blh9J1PUobNrDLwSs9IR3KLJaW%2FolKVKTif3a3MtfelrONyx2jdFnB9%2B5lB29hGj9elvWI%2BCbS1J%2BEVFmnxULWvfvwtI6YiXfk4NOTQ2qFkk5jnx5%2FSpXJM%2BuuX77IpuYAg%2Fgtf9tyhgnryvnbrzcpSu81fv%2FznSuvbvvyB3dFxF%2F17kMF0SPLl1P1WmTjik0xBIeGDKqZ%2Fm1ioCoHfWLKqBfOFF8dBAkcGGftMpHACGwktUw0ezn68MvCFAbJD82UQ9EafL0Y954gXwk4mPKS%2FEyNEEjwwgf2ycZJ2ZP%2B86%2BZRST7qKjsSfWP%2BTvWTnBMXMW05k4qUTUHHnFcopyOUYUwLGA49RLFfiyHxkHDArMbuojLleyOU5Fwohn9H7kW7JZ3fzsBKE0X2UcGyyc00itb1smT8%2FVt1j7l7QiZlYS6P1ILnDdWoyPeDHYTbcUCa2k%2FIP0QXpYI7ncpL2gWU5K77L8%2FRRcjQa0w87HA%2BAWul%2FNdNHfnc7kgiorUvgUMSlgPRjE54LvBuHLbsGmlb469Ecp%2BompUZeU5oKqHQ5lskhhklzU9AwHNU87JLSRMm%2FD4Ir4hPMwHi3XC%2BMJuQ2M0GOqUBbdguDieMsQ7iUTSMtM45wsMf57r0Dtq9nZ0SsjBsYcD%2FW7yxgKy5jfrD7FicJowbqJHU%2F2kmPdony5IKru9Qkd0Tj6KxdnPzIa%2F8MN3mEo3dq9lacQX0kt4fVYZ0%2Fnh%2F%2BUeh5mZjGkKAXu3kCbovUveSXg0I81RJqdqwInjBpza8pgCDyh2yoU%2FXRlEAdTc4w2ZS2D%2FewPq1HbCj8BA9RC8ayS%2F6&X-Amz-Signature=a348f389b9f00359cfb9a2141e5a93cca2c1478d7f88094f247b45a9d706fc90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


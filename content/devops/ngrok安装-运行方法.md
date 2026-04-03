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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RCPM43D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVL9KjQoTRGdn7%2Bx3Iphr2sOUE%2FVP1ScZ1xj0bUEMArwIhAK7el13ItRXbFnOddPGEynTvNzaPpFMakbmxGCJc%2BPqZKv8DCH8QABoMNjM3NDIzMTgzODA1IgypcnOXmljpfRUAmTMq3AMFBWATMut9U0cwdHci8P0ctkpnBDBqimjnywn8XpBzTTkNrHX7i0mhUrCedRwyAk6R8D8IH9T1bkPiWpz0%2BFo9L2%2FMk%2Bg40gsLCBx1YqO5PxHoVQ4XdY2AWcz%2B%2BPDaqVgs%2FqXKQR2UeEUa%2FMrRRVrrTmlDJFLQSOoRByeimiclBqfkozPKJYU0PVhprAyIAfTJKzkRXC%2FJac4wL7p15%2BC8himLFnaCm%2By0Q6wdA%2Fb2XeXRd58LqF0195idUPnl3uAjJjkRMGaK6afCUL0FHhNl2VHaYje7ijhXK0Yn2sRI7FlkYv3nABzJ3gZH86jYYUqBU7w%2FxGCiMHCnqlEtSYLB%2F298KeW2nLKHIbIpzsf%2BLRL62eTuXWYk3%2Fq2WmrQPCie%2BFkPTN16Qf81b2fsd00OY6ADpIn9TXD9ZNGiXVS42XIzB8diE%2Bwo9K0IJGDLSatf%2Fdxtgr0NPuVfPAcLVuS3V9%2BdqJUpwRWXk0JZB9Q1rV74lebi91KczAeqr%2BABprHIvgADg9ImiztmlGtZOdIKf5CHJHftY8vJE96BrcbaQXrpN2ItfhscOqtwPjSkPU42ekpAR7egHe6ErncRi%2Favczvnvwkpmo6QvY2uEU4iOpOaz044cU0OUeMtXTDgrb3OBjqkASXWknnYzPtBH3Q1rY39uhibIel%2BiB%2BD6lbQqPbPtM3fsJfWkUy6xFJsxnF7ddwLn8Vxozx%2BgSpkGU9YlDbxNMYDitFaaw%2FGqVMa5sk5cjeCYECqHbhDbOwvtmnrEf199PEmrfRTEttpaNryxWRBssziByV6nrDIpFQveuFK%2BE3Hs3PUb17HRXzOk%2Fc1QRMf8zljFNQZg1Z8M22xbX584j4CVbVB&X-Amz-Signature=a474761476294637e0b6fd746de084f9bf190d5fed8abccc98e8ad1ca03ec6e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPD5GAW%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHGVALNSoSCycgH%2FkDA4I%2FQNHeyfDh78YDjP87k%2FAuLkAiBlaZThpJxjJD8BzwNVUA%2FTG3BG9EoRMDCiLoGwSCaR%2ByqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqM82t097z4cYOOR9KtwDLMDcaCh9xCBIrQOlCFrrQZpEbvYkYrRCISzyLxe5%2F0ohIw08D7VTQvkjSxggOWEntIlbG1H6LtuyCVm1KTxHooozavsiMqpcdNVDOpLc37bKcAzUAMMbsseMglpcBH2pMgrcs1E6Na6cPmK8bJaHxBZFag9PtGjIGMyM%2BFvGM56y7gPBnQtf%2Bmw6nkBghlJ0TsiuQVxFngSNImx77%2BRFFx3w7XmeQMnqWKPJQysuTk0oRfBTxi8MuwSegmzalW%2F92tFbkhWIFYC25o4NPotJT6P8SKGc1HXG5u9Ksy4OXmNhKZie3Gp8a6gihdwj6LGtN3q89E57QzEsWZRbF4r%2FtzJWvR1Spq7AZK9RQGDk7X8ZandMfQeP0tff6YoqtTlxMvd8ob%2BqDIeLOyx8YTB%2FjZQ%2FUbWXNjvGv3eBXGTtJ%2Byo9ZotzNlwJNU5hr6AKmVlk40iBadGXraANAgwgYtM93RTGcqXluTE3MLANCvDm6g8xWp5FRmOKl%2BD%2BvPtRVXg8FXGs0ly0qxz3gBB27cPsmRWZ9cV%2FJ8ZiMTepGkAW8l9KNN33pLIWx811JQnpgqj9joaOsBgSV%2BkHb%2BFJAZx3pxurnjHQ6hNbiUbEiGHdSjmOMHB7I7YAx4AGRkw%2F4%2B2zwY6pgF0S2QArDW%2FG%2Fk5NtLS2Lug4Ld4ZkBT7sWIh0%2BLrHFM035VLYsI2kdzlpA97fJK03lkiOroD7Zs07Ci7ZRBAQFA2mIlsOkACGiqiX%2FSs6ZZ17nnbWRbpdKCHyrhNLdhWwo2BMB08wX1azhMcIrz9S9%2F7Q8nMN%2F0m8aR6XmHdF8F3D%2B7fevgqdtKTQB1bTvoS%2FmnSmWNm5D%2BIkL8bhPFY4Tfo2sJGfGm&X-Amz-Signature=4fa88a2f66a2a28b5a786302390be05b2ba239bbbc4a1107d772a06ece93a59b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


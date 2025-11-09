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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3M4SPAD%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCHpLzMYvc2zPJ%2FdTuNLfB0vFxKmP0GInS1q%2BpDtVJbkwIhAKKVXH%2BOfmxYqY4SN4VdSxtCKTusNfQNBUnABsjxgrwOKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaLgoCdEx8sHOstukq3ANlJ1w%2B83SPu8ZUfpPu2zCqoj57l2oH6BZaBxk%2FU5iMX9i%2BOCstVRChD3z6qUK%2BE2b9jS%2FiW%2B7%2BS%2F2y4a2mvSSjwCua%2FQUlyBk%2FtJK2geBeAvV%2FCn%2BGJRCmuQlw%2BupoT7be58S2svGYR9V5F6%2FAyQvPr%2F1FcMvmEozG2meVyRYjgn6m6bFbTlXCLBMEzqSrTeo3wHUUx7%2BYdiKmMoKO6eWkCY%2FdQTBla%2Bi5AA4YBau%2BQ8VR5VAWDCyLN%2BjE1GVwZR2sXH4NJaUCuVk56smKPi3uXEcp72ASmHTn9bEEzfA316y%2BYZkA%2F53VfycNU8GqKqwwvBGPx3Rtkjs8cbxGfA7M4NnAUuRGViEjn87EKI62%2BvRrd%2FdEotiyyAmpNVhVLnqU5c8TgfyBwUwc1KvVweqJvbQA86ioL31HvSiUvTjdDZ1Qq1NoHEW0ISNBSMIGxGPzzvrOxdRhyoOOt1XiTaWTwJzrOrl5L2q4TumDZgo7BI2dYlAO8khnX5qW7kLx8LwSfSdufForkPwc6btAQET%2FtkXsHqqcCx8iuKY2lGHDctRzJxmUL8TahT%2Fc5qScGfUFFaktbv0JIKLob6DQNNoh21xymRij%2BL5a9H5tYSSkWstYugWIvlNFLnSnsjDFt7%2FIBjqkAfxIA9JQeKfg9P%2FtrOMu3f19kvn6c%2FwZxiu7%2F%2FNfsliSqGsWB9pMff%2F3vR9yS%2FUGrZAnQHUxmfqTaIRPOW1Tjvae9OO2XW6oI%2FEtbiIJHDePqMFBcQk7WiGrwb0LVgbXO6oQYeZiqdpUmy6Fy7AY9IUhtXgsvc4SPLZ1zsW9VOMIBsQq2y3HXDgPnAmc47VndYW%2BFG%2Bdvvnnqc3hIubjpj5t0GJx&X-Amz-Signature=0a657292e0c63f6d07ac921147ebe1bbae025e1fbe54e87ce9a3b3f048b94aa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZC25CNP%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCKnnmnbJ%2B6iFhQymTkEk0hK601jPoLufe6U7dCGtahQgIgaJ8n4dqurYwBQHtsRBD4ZAaax5Axuer%2Borg8Zjt00YkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2FK3qrmlQukhldBGircA6PHF3f10TtBM7lgeNMC4Uufdzl2%2F%2BcfHW2sgShw00xUpTGQLTXBNFwCX%2BhepXVEYBahZQ9q90EEf2E7383wTSjERiuIEfZbVljE8Jevo7c%2BWf0rdY2hIw4FS4uTDqEbKxxd%2BGx8PaW4gRxDTGtHm0c5ayqMz8iqqx0u9NSJtMrXyDbQnOMHJ%2Fdu6Zt4wsF0Qhhmku5C7889lOuN84G9NGVzz14TSjMUmrd%2B1B3ChJg6IUInSBUPpc8X%2F30NPSmOQKPUNl3tX3N%2BXP8WsZBZEz24CGdRuV%2FGCE6sf%2FPtSzMW7X2YiGZVhjC3c1L2uTLIqvWg9q8DVKYjEkRXQxcFpXuIoBtJXvtbScosIfG7VdFVphAnzssRxJSRKfZjrHdix1h5qvICMZ0vd0n9DXKayUKjvzKLtfvHK3iIoXtfmIVids3XECbZdgrVMqtT1363T9NGj7%2Fw3c1j4N2DuPuguF0ug8Afg6sC%2BKuW6vuQLzXIsU1RJ3g8T75uKcDBiEctQOFKzoJe11UOBZWpJQSxDP4zvpNeQC3wgM2BPdFeWGJG1J%2Baqpp4BvSgOKR5Fb7ORNOZdTIDzTE4jCgRZS58%2F%2FQwb2h3k62BVGfTdnKEL6Fjfv6sVJZnpennBuXoMNb3nMoGOqUBkaecQVkLioS1ENwb8THFx2H8siagCUQ1jtYp8T1FYRf2uus3PWACDBIYMBjSYVqEBIHaXZTiH2ue1SCgTw6lUCufIW6%2FCRnF%2BAQGi0%2B71CG8LyZtWzuWLVLop3MY6elYf8A2MQ49wRcObExLZoL6xc2HrkjPJAmioW%2BEiD4nR1uukWPw4xnRqnzq4Tk1Qj3bA5c96NfAcnuJKb8TKp0wg35E6UCL&X-Amz-Signature=0a6c5a893b66636f09e3b66d4d608cc5a8561b401b9b1a84d5253b213ad8c1b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PHYR2KD%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCSFBCytp8W0i%2FSmXZZuvgMVx3xhMphkHDGU9rn7nL%2BJAIgP4AukoIdiH%2FSHU6prD5Ihq7%2Bp8j4JSoZvHLICapNUI8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMp2R7oRMJPaaTf6CrcAyFm%2FkAEYmHK5g1WlnL1OhAS70OWcoWdeMqcXkQqxyl77QxFwpmFs6fX6I3k77FMIwqdYB7LMYCsGGDVUEsrSWqSqLooJUEZIM7ki1B0y1cbfWfJLKyNYjjmYqkXYEPBOCkBjrgBucaMGiI1UtSeAP2cQNFD7UO5cmR6QctBJrMBsj%2FL2PvKh9UfJ7W0pkVgM67ftV4AQuliUbp2SAdgS8SZlFgFsWsPMhExjlNqZMOWNG%2BRqcKxXw9FUS%2FF%2BLKZZN4IF3Biq3BoCNoMLxNfOworWZoR5xyKdzRsRT1GHY7Kf8wK0wJSpiQR%2F48rPRN0j6pmMCChUezKuXzgnPtSxoA%2BPM4PHgyfyiCySwy8nrvfjWjC%2BDDBBF%2BbuScPbNNC2NeRkwkZYZur%2BMYC1wcsLRW%2F7RrzovRLWDoJkyfd%2FyDPWWKUegW%2Fyy7WMm7sD%2BW%2BvZZUdzGG5rRMlNZp6vsynqZ4p2MqGV%2BDBWEFRyx2hYwiBU433fF9LL%2FULddaNImEQWLnTJnLP3llML2k%2Bgl5nrO8k4mPvSz9a8uOwEoNgRVjY8CM9RkgibGzqBcwtbPsMPszJyZOKD6UYOFNY7fj%2FfCUhmJc2zxUXyu1eJ%2F2i8H51gaYfuUGNqXMzPLWMJbYxcsGOqUBVKmYzPO9%2FfI%2BaMH6g0Q4NVPLZGA6uq4ksW3E6qm8h57Q3IFqHLioXs7tY6RWmREOT0B2WG0552%2FfcK2e3P4EPlOHcoP0Iw8f6ZjMNbWViS6%2BUXcRqnEEfc7h7LbUTxOM60T20QcfOvEE9oL%2BVZPLKG51gBajmi%2BITwYq%2BN5Up2UEurjMXxME9VNnxC5acMwTgVB9WaFaqmIjSnvznnq60fgo9bqs&X-Amz-Signature=c922607e2e417386ff1831fe5c291dc15f4a689ef0dde2b6e9f79aa0330add02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


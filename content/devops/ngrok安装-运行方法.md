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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGVEZMSI%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1lQXuBgzTukhJCauRKOJPYfYWm1EY79SZ%2BVsdb7j00AIgS9eO%2BovqybU69zpiR5AxJyO%2B9%2By9ZVEVymKHM5LjUZwqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJttLGi7%2BFKnOvvNyrcA%2FOjhACwVpuI%2FCLqh2Iwe0x2L4I%2FxGG7TzizPV%2BKwg%2BAWrbpU8mjQYN2U6It0l8azV%2FYBXrrSN3TMw%2Br3TE31ebTPGyXG5nH31M3yraPMSKliZOpncdovUAcqNBcmoQEGXt3IFY%2BKrL5Dnr3hgt7Y63lA0L33c3fMWgMgszkkKmG%2FqixW9fpfoBaufevwF0oaZSFTQ6r8z9kOwaHw5OaCErcqLwGAJ7LpcWLxHXebNySIooAKSJOKh0PHcsmiCQmifrJLbv2WI%2BGoUPDe9W%2BTSoTQNNE63ZGWNFyjWiLknNFAbVY6B9SWutVn7WAoveGEMeWIifAd%2BmjdxHMeUwhvENOlLZtuncNIOnzRvb68KUKhBSG0RppIprcYladrf5RAg2l1B1UC8NgkR8vQ7RM7YgJP2wIrLivhMx2JAsafRlB7ZJbvT%2FCbLm2%2BgExsYE1fcfXwCU%2BVojVYWLxx0bRAOmBbWTpHMd4FzOXnkXbhdJ9JgxC7PzLag7g1ZM%2BLZuoHYtF%2Fb%2BvZGPr90WmVUQbY8J56CIz1mPIO33AOPDRp0pMmU%2F3HERdm3aw3uOA5KRp7ZV1KhuY%2FQUw%2Bw6ygnVMTeX9H%2FaOXsyZjdyQc8HMu9vF1fwqmYnijjGh%2B45LMIeO%2B8sGOqUBbyoVjJB4ae3uLRbpX0gNxeWnmYh1YvPRbfJpHcDMx%2BCQuhXGzkI9u%2FyHNGp%2BLQCAjkYhNtp9qabwLrhnL%2Fc7H9HlG7%2FGsBe9ekpWFlafnjfEmmE3MnXnwh9TIQlWRCxuQG%2B9EQBC%2FmLGdS%2FqLixa6nLMgsIqajvncROZYu63mt0zYkmT2jc6WSR8kTHhctTS056iJnUB75IhxwtR25mlVrSMJWQq&X-Amz-Signature=d99f756af4635d6bb670b196ba8265211e1b7e308825927809cb14f1797916be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


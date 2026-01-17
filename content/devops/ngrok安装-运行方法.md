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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675OEYDQQ%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA3nwBXYecClHFsKODsQn9Cd3tQPkVu35U%2F%2Fl7yEsoGAIgOWP2gbmN%2Fo7bmqUez0fIg1v7lxblk797vUf05M6KsT8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDAQg%2BLBuqyV8PTC2FCrcA%2FCk%2BXEhHi3JMo13hmGWe2srCeMFK1s7ztXVrlf%2BFXP%2BYRmjFTuiPKUT4%2FmhcIa4krLMwYVC5SwRFwN8JioA42foI3xBxh5WMUONcUeHC6GTruWpbco%2FFhistAU70Gbdyrm9%2Bgp6vN7kGpTbM05%2BcbZP6mX1R2wD%2BrpevMwrCj2Gpf447vZkYPpJ84S0F1g2WnRCUOuomV3oX%2BL%2FdJd9EcOr0hyVQosCUsa7TfEMfpxsc3kiKC5jXKxUSKb7EeFS2%2F%2FSFteJZYgcaz20U8wCoaMHFBct4MHepSVPcqfSKCKB30jfNJfBOVJB6DlrIv6Z1Df5MWqo4I4vTOsprqT%2BHInHvasgwkpolHOyGKS71sjp3Im19NGHVsamw0AGVbUYpxf7Si1FZ0R3mZop%2F6PQB9eX0NP8ylQs%2Bim1AQ9kdXDQpzHX3qJiqBGDNKr1Avd6n96Rv3Au5UMk9ds3wL0aZTNbKEer3zYb67RLXH3yU%2BIYEPmmOvjDsVtlCniX3EMGgICEDc%2F25S6rxlrivXJa%2FbdHCZKnIpB0bI%2BR1VCJG2VkodArhEj7Uxdi9jphDcErVAZ509UaIM%2FLlCYwJh%2F20scOQGPct9qdt91A1EsdKu2%2BTwWqfBNHzfTBLeu6MMXRq8sGOqUBddewP7E9JaqHBEklt0rK2WuXTxi8VK6nUU7faZrvEbrRACCD4KZzB3Hu8BayRuATX4tDJ%2BHgVRuLgkU5yUdpps01C7GDy%2BQMFJKLwKGbzjhhd%2FI1riHy%2Br%2F2gKleZjUohSH1iObjhDadJnHYKp235uCYiQwAGPB5yiE9mmbrOBLxbVaKC2uH4C%2FjppIPJnyWhU3jiSPze0gsZ3DvbpUSfEjLfc25&X-Amz-Signature=8e638e219a1d5064e24ac5440a00f46e53a162eebfd61e8a9c44cea503ad886f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WBJJZBV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIHTrE7LprMVwivRadc45FVtePOFU04%2BV0db%2BJPTXq75yAiB%2FOx5Hq%2B8Q7e2BSN1Q3Dn18k0jj70xZ9QrJwDjF2okBir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIM0%2FHoxXG4OTaG3LkCKtwDp%2FuwBgFQpD3yah5FaFlrtsVUh7eXuNbaDR5Br7LrOtqPZSm7vnrqymuVM9%2Bjw4Sq7Q%2FZAVTAb69ihAgHUe1KLfpAemf1fnpisw7Hs5WcJO4Vp%2Fxe6Pw4fjaaVbjnX79r63wL2mMU390buqoWMQR59vOlnq%2BIvwhsiXPxU%2BREdttgOkv89mRYRW6Syq8r2Qwu9oERxEY9AFPvveAUrwifGhly7P%2FLEsYHHoca9j4dWqp0stpKW%2FMQp%2F14LgtXQNp6GRZuIxmBnI%2BJzE7w5oSiRK2eoruve3g2xrwtBdozCQgY0vh9RK3Y93bGf1VQAizQDbeKcV7esm2fn6a3tRBf1pBP0%2Bg%2BcyaQeRO1xQ6ZUFSZtKJQNZQUrkW9TIpt7z140yVfRlX5SbYzg9BD%2FUeHFwjkTdCpXdiHfNwLk8ky9OKaX6I4GHbAh08UreJz09RISjHIZ3mAE6HZ1vrX5ofhFI9BKG%2B847Ez%2BvvJKJodyyZpAOdXmTjKTRuj6lT7soIU6AxYis0Ys8FZLhaz%2BnK9rvmSv3qJaKHcRiIroU%2FSaZMJW%2Fp6a6vio3QvM68lird6GIPTFVq91oRrUgBm32ECSuyrjsksj%2FNqpQHWz2hjZLWiQzvuq7zoexX7L4kwqP64zQY6pgGdrEBUhxppNXaoLAd9KkTyBk66mETnKxDyVdH7RsExkct5xwTCdvz%2FBBkD5S%2F%2BJW0zAMJbMZ6lQfnNoBcD55QWY6USeSwP1qprBv6LlrbP27xq4zWL4mJ1M40%2BqdrN5s2TUQc6IdgYFiGc%2B%2BwUKsz53oYbTWYqw6yADOEyTPRdZ1AKEQV%2F1c57XEilMGtg7qL5iO63%2FPSMzPkVXaHofKcgVzBT8Ce2&X-Amz-Signature=029b27f3815e234adbb5a317ffb0091b5d86f596f836eeb65f9557bca5beff7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


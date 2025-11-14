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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXV2DER%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICBR621%2BDR7blwuNwyTYMI05OQhZCKXAjNfAqLuzUpdaAiAD9%2FHfABElX6RZp%2FqLK8WpKficrmxYXMYtjerBOlFZ%2BCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMRd22A4Er4DpBDcuxKtwD0Ilgo1TaRTArnHlNEAB0KDAfUNYimEbinBTjSL4pgKS%2BvvKHKKLlTBO%2FfPyyGHEkZMxk1Ht4Q3%2BYS6qDaqx3aLyRVK1gyAKKBhXTbg%2FCm3aw1g9aJ3qh%2BqA60gCxKh1DBzzyevNbvepZipywLeDJV7sHXWV2P1%2BH7ne8ZJQ4KU7s74HS%2FRX8z6zk3FM6hjk8MH83EvQZcV53NsvjkuEHphY3kTIvS0KN97VawF4BYMGOyvD%2BR45cmxQ0Z8dX1uP8NsxWPwT2O39AUBbN02ZRdA8l0y%2Frh49YUOqKm%2BFcLObkvBfI8vXbWtTcaVEYBBxeCmjBGV59oo%2FAEKEfnw7dHaFYktaU7idpX5g4RxV9fdDvd8rVxnTQFXoyHW9WV2rROA15ADkMEdl89w0LKsIKnaYdDkWV9Jrgx9hXaFVtuDsyMn%2FJhoVJiCDv7oG%2BBvsQ%2BZimoWOEg4wXYQuG6ZOAFAzL2MaotTlA0PgVaDWhf3mcAqUCz9TrAym94WDaUO6pkd01TVcywyNHeF%2F%2Bic7dWaaWbz088N7isOcduvgWWmyeaab%2F0kqK%2BaVfdMjo8br2xP%2FWS0tT3CYfdeQqkhGjnoBueUhmFhpMpgmWjkVjB8HivP3EOW40cdQ5zukwt4nayAY6pgE28V%2BbDLXXKUntF0NEpdxOi8x3rDMnDgq4SQwWqEIX%2Fj2Ng0y4QGh3no%2B4AdSqPvx%2FnFXlVcXWx9jVEsHpj8DxjdfBsbwZJ12OFvhCc6JREQH8AeJbpJIAfeyoWrSrYaJfgIjhyufzwhCg9XZfcB%2FL3mSdHolbZdo%2BJOb7oDs2PepGH6bq5kwrsMFAUmF%2FTN12Nmf1%2FloE%2BxiaXsxtgKNth3DgIrMY&X-Amz-Signature=b32286e34cc8fdb77db5a12047188924d95d89031b61431017272b243a370ba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBKYXVXP%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYrAibs1c%2FPEjw%2BY6%2FXtlpQAG3VNyCMQjvylUVW13hFAIgZJAx6yFUoWCiVDoUJecq9vjHp1P8SSbVZUD5IlAiT3Eq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDKYkAB8xLbSJalp9vSrcA%2BcpzNHGeHkNyYCJaO%2BsbDMuGHFDTpGAIAy%2BTI6A9%2FuSrFbtcpAz14QTCHk1p8Dem%2BQM5HE7TivzW%2F93T%2BYhge0FP3yVdmIL7XuMMery8I9LVEukZSUcrUO%2FHqcNejI%2B11sSnQj38In1ou05sIeoFDINcBf8oimZlNgTLXM%2Bn2doFM5WKnyPcyuw26XYGoZggnSDDHMWK6vDbhodgRRJqSGVqAvQPtDaAa9End5xOIj%2FaPyZgqQVSFi9wlawCXJ1NqcKsrAgM0t3AHeCNWOg%2BQ36K9wKyr9xyGO7kLsFJt5253i%2BLpYaaZzPJjs4%2FfgbmSgOUJBTKKD8rgJzoJEUnyUGhVHztoDWF8ujobp0QUiUEeVUMLZXnPJ4C2MnWBRjtkWraE%2FRHDUUzJcrvQUl71ehoBFAbCuoxo73QipoxSKQ9bj8rmOmuRc0mNYQHTsn%2Fxm71k7cifiOBEMBzhwqSSlOd7wGYzrZrKYIsixJHrGhXsaSgCfA54GwrKVBBjFQ4qGoicPspQx9q8V8uaqIsiuqo48dpEa8gmL8vJILBrURheBHGR2eWKXE4Vr9c89X9EqWtA%2BfIaMSCgY5QzaCjg4dhg4TcB6eIaEILSl8EhOHLOgVyAUeMKatSHxTMJ%2BNyMkGOqUBqb6mwObhyvU%2BFPwoNUnN4s8qKxrOhGCm11zLeqwU%2Bf9uepCFeS8zouMUeH5GZYQLDgCvEbJJwGlZs1tL%2FVJY1%2BTrlSl%2BSJcv31PjsSWxHFOBBuaJvpFohxYfQgJ3sx3bqH5ArUaVLnx4ct5iEGKdDr9SQC%2BrzLdrnOdd0zyF5ykrjjqG4Nqqyuwex0o93%2Ba2FrEwFN69wMalbJ56fW2ahe4JnYqq&X-Amz-Signature=ab0365fa7496ba191511096904792f2c4ca87dee0ba7ecf6fbbb9e8b79661b1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


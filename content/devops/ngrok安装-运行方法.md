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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRRACDT5%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIEk5jDqCPVQ3%2FSRMc0KdwUXaMewlnvWgeoR0KMkP8NQLAh9oqU7VrAFWjTGtOByTaoL7nTbRSPSetdzw9fM6vs5hKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQVyfx9V86BU2f78wq3ANty7n2H4NbCtzZGvk5yAwFq2cxhXITU2kj8zKt0PCOeuYXuXLpgTUHzQq6uJG8FctR0tCEBA5h7CYTaZg%2FmeEN0%2BCsxEgXazsR3DC24MyeQa5SV247ACutnwosYKu3bFZjql3BTWl1C8IP5wxD1JpL4gvgI3mwMNUtFq%2BXni6oZ0BRO06azELbuIs9Ldx0v2woPmgz5yD2wn6QOnJQLBkaiwoLPaISbVk%2FRpV3cLC14jQE0f1Q75NeMhdzEbBWlH2t%2FWZcRhn96o%2BOpEH6eOyYg6qnygVrJcyKyApPyw%2BSkIjd3D4uror%2BrgxJBpYBOToXqGwvDCVhsGgHWRvivHqu%2Bjpnx9wVsbTt3%2BU6aYyRGEnMzWkfstaeR87j302ZaktZ4G1uJ7vB3uW3a30GSwSVV7VekGwZD4R9xs7P2oQA5pAh3%2BJLQSEo1ID%2FoK3sfKqWQkhQCdqv0PZDPUYf2hwF1VPs3rLefq4kT2FTBVUWznaskVL%2BECrhKBQUDLarBZeMAjaOb6EoYJSQ1zmmFxWwp3uwXOSLq6VE0eBjG4%2FI80VHqN2813idcw9SgSe3s%2FZ7G6qd7%2Fd7nCg1w56KSI0crcBxVh0Gh9216bWLuRa57J66s%2Fy9NnILhf2acjCftYHPBjqnARLZW49kL2%2FItKpkdTNbMBWy3d26wbfaqAqlfjZ%2BcTCguXGmjBktu3tgmyHZgWt209w37NmVUTlFdLjuLJwZmJFKnH6d0VfGXSMD1wYTIzvmHN3Bao%2BViqQ4VerqS8IpKcP395lx0BjYuirZyyUI8WsDAw%2FOJW7x5MtW6zY7frAl%2BLBxvF3oRMOUSIXivEVlaw712HMoCGj%2FZuRAyCq%2Flk35RD4Coo7t&X-Amz-Signature=57e16e423e4e033bb69ca7b1ef3a835137e60ec0abfdae894ce5f8202e243451&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


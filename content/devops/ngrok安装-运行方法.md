<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png)

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

=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674AGDC7Z%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCICX7W4EEu62vf82Q8BrjlCR9UgtaaJPV14NWG51HaeGTAiAJJ1jLHgf2wxM%2FXfslOwJPuctCj99%2BJN4ovghvw8WNbir%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMme3qKkZ9CKba6hFwKtwDVO0eUfYNSrbtHb1r8sDTnSl08cPgKKMYpIZA8YLHBaEZhZAGk9Ah9WsX8P%2BCtl%2FDe5kCqopEhyVmsD%2BelPlBkgYB%2FPYJe8Qf8sa%2B9I%2BdGRZLdw41%2F0UJkxUgQiZqiXnTOlyMb7thRUJqSOZksUewq6ofcmLQnrNPqNGRYZEKVO%2BehNW1pFxmxPvtxYa4LkKoDtH4VMRAuyCZYkwc3llT1PlvU0xgCotaLcVxdp5lEafEa%2BM22nE4LsTbZ80guM63ma6JbjoKyhw1ZLdqiFAQvCyH2kJ1rBKAPPW5WBxopXosmfHtn0rmwiJj4WkF71U%2B3z5dRZI06IDkxIcXq7o2LX7FFnpnOBLOwmtGUyZ5YQlPE%2FWD24wiT2qMmpUAbcBdPaw9mKTz9VH3pMRbJLlMuxadYCjNWWitOK2tSJ0X0%2FjoTRlEtvWG1BcfEG1bCjQs83CRlbjpNhnFTqD9DXnkv5QWq39Jer1PZ79PnMTgFOOCBzgR0Z9XtrS3N6NPPLJeAXV9AQFN5ft5CtRXupVqT1ac%2FeAWiIYCFNM3MEFZpksVSVT%2FMa4aRy9Lf2G49Ph26pohnT6BEY3x5m3uDQOE9wzOKGTcl6dycJp2pJ7XHS%2BiyyGeBeamm6QcWKcw%2F5vMzwY6pgGUBjyWnrmAcXIbV%2Fjjh86Qb2ti7bq0ZzkLoqotmSkuJAxYdr511JU82cF5HeiRIBhqFDssJgtB5yXYOTG4%2B0vbwMgCS2cc%2BYl3%2BVWQ7ojmHydSyTH4UiynJMrS9%2F3%2FWhi4l4tQe6yZfY%2FK5hlc6ok%2F1XU7016rk67FxrPr19gQDqVF6rcEgOcU3WVGw%2B7kWxmVHZDJAOw0S8Z%2FEgIFSTEb2Mpp4MkV&X-Amz-Signature=8afb9a235126874f21b8c947034da9f215f8348b218c5c63fadcd13643fcff82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176

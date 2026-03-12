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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWP2JKB%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWeLGk8vuoVAwZD5G70Uj50damPeu924v16mJvV1ZX%2BAiAIVEV4Me4uX99Sl6xAqEX50qVdUK%2B%2FTil7TTezwU5kBir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMAnc5SalK3EYs8UEAKtwD9tPoU7%2BxZZouk2xRRzUpW64AGAs6ZKshZCdTzZ1YJqpQ35IkZi5MKTiRtw9OKvEo%2BgZuNzVV9J%2FMv%2B2Wt%2FBOkpnOPAoYm72MEyvYVSwzEPybkhxjyy%2F1uL%2B4g8n7RPnQN4EoM6%2BQ9ExZPpD7c2UVOcIiWnAdL%2BSsQEUZFCwwCdRVq5bxkx8BukWdg2xj2wU6Qs%2B9pgtBQDhP6VnLJPM2I7F%2FfM9Bpq9Bmok2geIibCCH5TiaFXsicMWOgQTfBAs8ZVtF7DTcM7Ey%2Bvc3HLExLzRuDO9S2SNx4R3CQd%2FFO6B20krE7xcCu89xwdP9npzcYtrxs45PoYg%2Bkkv2whD3Way8mM169j7RtXEy95byJes8v02wc%2BJTDHAJ935VPUumq73Gj8oufmnNTbhsiYy6r0R0gK3YelQYwFg2gA01inQ1%2FacSQgxGr1OXYSCt8GCP%2BeAHdCyRtILBnO6Tge2Q7J0B6a0PqrXL9%2BVNacdCOnJEc%2BqDiD5Pi4KRPNvmqn9%2FFC3WE%2BtMO3G7Rh3U7IUphF%2Fdu8ctamHm2eZyIxGJyENAcjTw5D7AfgNMat024mCjmaoEAhu%2F2q9kOFMXiBfgtKvEkzZUeqeiBAqwoFDBSDlXshbK5irL2iW6xFYwqrLIzQY6pgEzTqf5xalnPjgmzzmn7HduPGuqyxYxv1GIoDXrJHhCMbkd%2FUzC2oumGko1G%2F%2FLWBTm6bQf2A4qFd2fb%2BCoLZohC%2FZeyg6cG9vGVGd%2BDiS7zbcUTvD%2BAiKazoD88Ah6QUar%2FefkGVf1%2BMAPbctsEhPNrlsJMu7TQtgV9B90VIZcMgK6o9QxE67M8rgUq2egfXJr6Z%2BuogIHaLG4ML3D9BGuCWikcZWa&X-Amz-Signature=a5bb11e934a29f92de7212a4000fc093f3cb28f5af81a234c0c9d26900b019df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3R24XOP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFyLyzK%2FJ0NJN1UAHZb1pvGaTJz%2FpCSV0PE42cciv3EAiEAwmhbEosVWIY7%2F4j474s7kMmAkD08xnYBz%2BhF6ehjIOAqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIKcU4IpbSJs7drpQyrcA%2FBjlRp1EAN7Q9T%2FiudtjRYBKiYKZvK0xMk9qvUEvDYbJbB2qCy4AbKPhPeXUpfXqmfMuZyqBG2dYnmiQAJwiamiBc8NQJ8%2Bzn6FyaKO6z7UUTaNNBGLcx26dxzRuM9PRt1YV18pTspQd71uWEugA1Vi6iV%2BHsvZL4p3KG2pNSwFxUkgegGNnK%2BulsThvvPWXMCBdaN%2B%2BM1RjgVEk6Qq%2FG%2FuQYfHJFeAohTtYAP9NblGpzxeWE2QQp990bUokDi%2B2dqGJlwwsIknfUEyGLmchMX97EonVZ6lbOHwoCaQ92EdXIc3B2ihIgmC4A2kWHM73nRm24oRJ79d2R172fY2%2B47WvPCZY81Mkb6pZ5xIsv1fbXizZcqeqAux6ofYLF8t00Oj66lkoLDMLvngfEdSWX17vRQF%2Fjm3rusgoMgplxScE%2BlTvwkj%2BoWQxjV%2FIm5dZg78qqI6%2FIvLg%2FhKRbY9gEDBsG2COdfGdMyAtDiU49AXup%2FC1A3E6t0vtjUPDK8wVa3GShhB31JA5kdvrH%2BJy%2B%2FiE%2Bw0gHkuI9jXz8oH4cbTcr%2FvCridiSKBWuoUe%2F6Dy3yDZDZW%2Frq8a2KfT6n4MQxrntSIrYipYEV8WPK8sNr%2BJD8oYhLLXJccVwdRMMvxr8gGOqUBAtXvtstsPyCiMC4lJPNstCp6P7h%2FJd89kvZtyxzQx1LRcU%2FLDcz8GTvuOWhfthLqVCvvvVR0tSsHLNNqGiwMN9Ion7pdAuZ2YCpih7PY7rhwlnj3wDet71Divp8u2wWgqtxibVe1hwQ00L%2FHu7yBS%2Fn5HXDtmQzoPf%2BTb%2Fg1j%2FDYUh62Q82lWGfYpb6kCPBDwn53AN9WncPXH5tlsavo3rU4IkAU&X-Amz-Signature=651b7720463d8e3b068cdfaa9848ec24a10a1078b87bbdf91251c9a818cd6ead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


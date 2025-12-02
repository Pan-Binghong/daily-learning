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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZ2MBZJ3%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDyyTe2CIPX3t0LP7gvP4%2FYXofTNzefNPNwQHStjx9cLQIgZ8xntnM5uusNyuyV%2BPwnBiUV9NW%2FhjeYP%2FiwqUbe5AAq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHw0k0cTpz5jyXbfaircAywqfmZurZ6%2F7TfLVD188yxpLCHQaB4YDg0%2FdyIoY1zdEatHRwJZlZ21iSSfiWAj5NMVBAmVVdyRO1agm5cJrW6u7jUU%2FJrQrS4vawGICZCJF3AqmymTMJjUf0qpOLmfbcLbGarNhyYJw4IP3x03GwOe3D1dgzlpWln5SNU9%2BBkcZ538MjY2l1viJT828L4sxhya7%2FfYWltk%2FSq%2BJ5C4okFeFeqMd6F9xbThX72QZ550To5ZPFmaukN%2F6N7dKljRs%2BKwWo%2Bg9tbFREHlgQnqhmSx%2FWqCq4oi0418Yv4f4LzNbqaeWgErVG9Wdr8jU9aPQeCIp%2B8KKIcPbeBDi5RcUKKx2TSUOKCHKLFSag%2F84C0Gz5DwQgHkCHgLEgZlH2wePLsNO11LJzrAUMPZSBLKrx0c3JMp8l59nV9Kqvnl7o5a3wz9Y6QYF9XEQMBJ6k1546mW3T3h9R89Q7rWrAvAIVduBI%2ByxAeVvGjuY0OtQfKls8m6%2FHMl8vKqJfAPcNWAW%2BDhrpCz5%2FOd36WuDKa44Io8qfxcn6IcZze9uKJCZBiu9RlCYg4HH5ANyP0ldQVGZ3guvqLDz9vTqqlwxhz5lVGJarxJjQYr4I4JMkm7MxHMNaI%2BeqR00kf2H1OrMIjeuMkGOqUBE59VU%2FU%2Fcbps4xNF6Nrqe%2FrstPwlyZNsAWIQ%2BRkoWaMZqjDBVp%2Fh5TpPGS9W3u79JlBZhvVUZhAY0pWaupVgC%2Fa5lVCXdzgsE6KBVepje1l6SYTi5rmMUq8g81vKSM2W0UuSX4fpNHCmtS0qqbFnNbO4JTTJU2WtUOnQOr%2F0ONMgeXopsfqHaEmwQrO32x%2BG4DT9HUqSGrErchJ1kD0TGJ%2FgmZtj&X-Amz-Signature=a2bb9f39662d8183ba06bf75113cd1a560bc0604e35d3a1490437ce060715f80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


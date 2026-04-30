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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRPUDOXE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHTbs2pUNahETdFmRPnmtxjAI8dUw3uUlRWlF7vq1u06AiAfRMicw9dkMDlrOBFLtDAWpjafI%2B5vDTEthVPk6jPe%2BSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMAHRPszOYjqBJ9ybOKtwDCX3Tuc0v5WP%2FcfUHeADB4wa22S2i0C2ysNqed%2BjmvBG3Af3hqk%2FeqLy%2FZRVAU1OHpSsCy1JX11R13VCsob7JJqnVCoOxrl49dj73ateC5%2FvBShFqeE27M5qe0AavvbdEkcO2KGDIgxe7Sals2VTXP1YaNd4JRtOcapqiq5icC76RuKIA3Rjxupt6uRXnblvo0RppU%2BRM%2F4%2FRDdHgA1BmRH7zLAXK6cG2vXm3cr4UMUvkfwvdn4qkQtmS2ipUwlZfhA5urBuWkfyJfy7ibU3wZhysQbqn%2BccrkHAsJOPpOCRLM4%2BzPF8NQczMdfoXVsxTfYV0mPUzqn7Vli3ytC2a48psXp0v5m8P8keBBfI94CblFSXB35N%2BlVWAqexR7VHg%2BMSDc2G982z4MlEANxEQjQqVw4JZUozo%2FQExp8dx0t%2BJeaIc9Oni%2B9mSL1C%2BJAyS7GKqsMFrmXs3%2BodsXV64%2BFlAoZ0ClWQjvG6eDRjUfSIdV6P7rWzispTrJ%2BpVdN7%2BmXoI6245mHLxY0yrFjRLsUsMNhcaWvZPo9lDPrabmciEKG3DNxuZ6digw5X2QZ24LGMi8xdWO1szYQzHU5qXl%2BaCK2OyDI5BVjzAo4fooKSjBvWrDJYbDIl76zMwj5vMzwY6pgErW0fYfZmcEuijcQNu4c12m7stNurge%2Fpxcdd4BklW8VRQi50tEe5x72kOiyOQeXHWJhNFPQx%2BKag4WL1xWWevy5hAXJ9Iqm9iW11pgk%2BMVA54XDBtwg%2B08hlg1gSvak1AwxuM4XSC3F8EkJa2TpbIBlTfBCZKe4c3FWkenrjRb3QTafC7gozRWBalvpGws94gZvihb4uFwmHDMp5WhT%2BA1OKBgY%2B8&X-Amz-Signature=3cd39f854905d7071a739cbceb4ad430ae0b97087857235f40dfd8b35830e360&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


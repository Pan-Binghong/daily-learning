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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VBF24ZE%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIC9g8klFrti7PI%2FcLyTTbtvKh5Qm3vEut%2FnZI3Y7vBN5AiBsqtxF1xuo1KLrlevMI8Iuf8EWfYzBGllHScGfcZrrESr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMOXzpZt1xYgY4VkpOKtwDtH7LDz69CuIAsvD0gtWRJt9AbRWxq6w9CCKwHkw4R7sXXFpm%2FOvt9bQCVZLscVT28%2BxcKuAGDfkAQhWyEBF%2BZuDxKBxjJ2etA%2BDTfVI78qKZEWov%2F6wY6M1p5VCZABCBhjbfqueNkBvR9CVdvXZh6SjVjOQvDADYgpXMnoptPxTJ2FExUPXpmb5hPTJQne9Q1eJJxM3%2F4kyOFusHHuV96Bk6rBSJ631G8dU4SkaCY73%2F5KCKZ1Rlty9fK2l2rlJNbxgx5Flr7r1wHMODpUYCCmaS408FBxOsi3mcpXoOSEq2BxOa4oAVdFbTRbShPBKyxZsI1MiqnqC6PBm7Dmy7ZWmbWWu6ZDTbyMi8amWLe18mjNrCW%2BNkCkmPpVLVInIaVBVT7KF9wgzNIqBwEyvXytl0qxlrhir%2BB95YCJ1gcwDUv5C4LIIxKlB5VXoTSbuivgujPsg9ZvQMynIOXwL71ZduUDySSxbehZuz5Z5yySafqeTOyhsZ27094dOQsG0ym7Z7xmP2UM8EJBKCqMctI0EYQciAYkjpsck26j8f9ZWEIVW6Xdnm3AtsokxJ42I7sJNA%2FZObk1tbFTx5J9sqF74r7%2FPRZ%2BturQbWu1Q5Npt6oEfyQI%2FGB3LYfPcwwJKQzAY6pgGACqGCe1tcbAhGe98zFyldI%2B7Q01bQxDt8lsS%2Fj7qt%2FzMgFDTTfgoFqBm99hKSZB%2B7w6keas%2F2xuW7nDy9%2Bdhomdn5kSGhVFS%2BiXjZGb6I0nYKEP7irHqITrYej9ohcogOVGnyrqNsy%2BGSRgqnCDSr44RNa9DpftSqhXRv99g99wGegSdLo8woFAPnOmTtFz2dNNOSvFU09M678bZpsjd4%2FDRq2bzo&X-Amz-Signature=a33a0e02d7b49cc858c5cf3155715c7bdc44a5a4ff54f4cb33420a8a7db4b673&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


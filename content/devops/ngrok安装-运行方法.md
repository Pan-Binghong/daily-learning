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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJPRRCIA%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDigBNacJ%2ByUZSpkHB7QkSD7BmvwEJepSiSmArKEmby3gIgbcKyqzPdDpyq2ijrRN2xekgiXprv92LQN0md13NE2cQqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHkDtmJlQ6OHhQHISrcA%2B%2FPvBC4yM89G1GmkyLoRBWgTi4dXLsyL2kCN3tFjGRyGvQXXaYv7bY%2Fchem3pvkIALe9Zx42YiNBnqlsQmIgvhI4QS9mDUV%2B5gYB4KFib1HEjeRBJsTbYObUvRZXDMbsLvACIlsZL4K3r9%2BbE%2BOSFBgNdb7zC%2FKUtbb0zfgsh%2BA0mlJZfULrChTZajYQprb3iD07SXvp5f2QlzlwT6jm7fez2XNfdVKuJN8Ms4ATT3pGJa8wRp6MnROv2cf50cE6PqVLo4vVkcP7IA2RCBl9lAtPEdwZcxI4M3bnWCdvvQ9jJq7HcAIFGIYPMLYKD9JrQ1j0Ylw0yrAXdI20%2BE3lUVmRCKXOwKYwj7ktEdbcbtqALOGmMn0rDS6gbN4S6eV3YZfOpD5cv0ghPRoZsyuSSQCcNn63w%2BfCk7tN3Yn3KkNZ2%2BC9sDuMFVb1yuwtG437H0zdhJEKOk9PpXBQKmjYi5r%2Bq%2BVwAZ%2BUTt24mmpTU06wmyrmclwkHe8EYqh2Po4Bam1pBPQgg%2FuH%2BhBc1nC95%2F8mw8L%2Bdfr1Vpq5SJCFY0X%2BjScbQJGipkmO0KaNEHuOeMjuWaJQJ9Sig1M3sAQq%2FCrcjvCTBPM6EmhpmI%2BrOqI0DZ7mNso9N2Qk881MLiH6sgGOqUBCD3oaLUSGYgkSydarLUiQuEgGn9y46xHLBDF0HzACm8BHuFyrYuf0zNFoeLXyQfLsJgv%2FMRVOTsRC9neRLjwz1lmkuMCmlZ72Cr5I2uWOk%2FFRX8%2BTtK6Csp3Ydrx2GGTJns4g44GmQHVINloBNac5eTdimGzljbnMIfOTD3kM7Lbn%2BEUyGZMt%2BVgxQyxdQB1BaRwEWHJYdepZNGPxh%2B3KYPvltXl&X-Amz-Signature=c24bf5ce6f8cbc7d7cb2bb6004a165cec352097d4661ee628c0741e086f8df0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


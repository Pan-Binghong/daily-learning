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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RCACTYZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBnuF1hfYbFMLCqRGUX%2Bsai%2BvpicdM0mVP26PZ8NUaxAiEAq26PqKrVXRx0R9lfqrge%2FXvKxXgk73cE1qQnWm1sNAwq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDOF0fPkDg%2FzrlMRs5CrcAwUYbaALRMo36KLGOeMJVQ%2FbHWJnsAXujaSzeJAN5ayDMvhTWzpWp2qdFQFncEfIaJLaBtabNsOUhCBs5IUsGLvEcNML09YSJf7UMHVzgaaSld3ZQEkzNJaRCzVO6TUX7HI0EX6mA8WHRm%2FWwYEaljFP1bTwc2A0ieZBNuC46OWqyuas0qaVjTBDGDglRXFaSYy%2B2PhFd82OO%2FNE%2Fh9mpMxBfDfidNqgo%2FTpJlZwXBRxwlm9baj8bCK1zASq0kuWV5twf7onCSuMFoKH4Y4Mat%2BbPZ2UbRlmuUZSno9klFhZSRAmgyK9nQykm3DKWGMTL8mTijEevap9duleBWH6PVp%2Fxl0vDgHi0BP2Xk%2BNwUualBAy0JrHiKlHI8WttoPthHRlxVLK65pDUz7r7AJZuk40uYQkxgX0y6dLqKf73l4AkpVX1AGgB%2FcHRyPPjNKT9p0iwBoHeWaIJbWuryng9YmXQE6GzMXbRVI81ODqg5l4zhIiqyy%2Fzlzof2oe1X%2FDIxrSiF2Gm1S2gmn0apGKa4UMi4fNVk6V5KftFOKLm7Hq0O92eTXuDXCdJ5OUa8wB5u67MRrD2S%2FPhuhCjSS8ZVonnh4nnrRhVemCMAhV79YUfJHcZPHwAua9ki%2BiMJjx2cwGOqUB8V6iT4R76Ux07M4bXCkGPTlNwprxAxuuvoS64%2F6ZIv2rCz4o3lzBJ96Zvnc%2Bwnn6fEIV3a8T9rkk9C078Q1RDv7J4wNACNmIi18dxxqPOkI1WttNqeAqd5tRZCkZr8mGUhY5h7Gq5T5OcDa2PJJa4mKjsodCSSC2vGJTAwMxAKI5z7TXWnx%2F21k4K2LyI5q3z%2B5Py6R%2FVBfy1WvSqHMlDgnzPnkK&X-Amz-Signature=b9f889c182875c1bcb2e61c7c70b9e1598cd591c31cd4c07ce33a5e612afc133&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


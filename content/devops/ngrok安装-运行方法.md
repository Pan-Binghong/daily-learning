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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5OMDRQC%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCw3OSQvnSfF798ZynenAa%2Biu1MPQrXJdEKSCtEhZhoigIgMA6E51lLQNQVZDeHx4Fb1rOePOS2Heo8dp%2BlPVB%2FWR0q%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDPqQLuPEbS9jpaLIdSrcA0vQVV1ebl4FB6%2FSm%2F6GxHDXLz2rAulf3F%2BW26iJdj1T8gCdHE5nJ33Hf4SWaiHn9v8pMk4PB%2BM7sNdtUN57WydnSNKrzHdU8nl0dM94UdOO0mENfuV4mOMzs5G8Y9FFIAqqv3CT8LwJZP2K2iFrPl5y0m5lScG0ziovQ8o2I697cTpuWWZhF9wVg2O%2B77atrbfF4DdtOEnIM12dl6XdcqVtmcYPU1Bsq8eZlI7WzVZo3dX8MG9xzO5wZqNrwgxqF8hynlp5nBg8nGkzg2gJbjgKNugPM8PNIbwriYQeA3TfJ3pKawVhvfXkEimoCTzYjGddDByKOHM68%2BWyjjwdRMCeya%2BbLAWPnH0qi9wRzoLx6SIYVjlTtYDqVwUYWSQgNEOuZflrEaKtPmQZh%2F%2B0kbnOK83r9ConDPdhhtG9ycJI2gLOJ%2BgZtpov3DNEgUuA9x%2Fp%2F7sf3QJHXa5bLACY0tEk87%2Fael0vsXuZZkaBMetusvS4TXWXpaTQVLmne3vZ81hTCaY2%2FxZT%2BytgSfkgKmG4GgNWCUmFJbNUfjaMiocWuL7Zk6aCBf4nyl%2BYCnLdHoZRdSO3MB6lJlsWL8FtUNGvP9pB9VvjqWqLbkBeOnTteDi6EcTvkWWJ7XEYMLjUw8kGOqUBh6p8u5HiXeEygyG2S4NBdlk4rwMkaRmrT9EaiWuflHAZ15f0l%2B3CmbeJR3Eq6zFZ48zsjjk9e5qoqmS6DBF5S4Osw9No4F1VPV4nThfx%2BpPt%2BEUGkLgre44TsmV0qUJpJcDS22Yltvx2uonuGZchI6FaHgshzBHgsRai2RhF20%2Fs0p%2FdZr7QKUMSHOPfPTAXLGqbtpflQG9%2FOoJJwLICnK5WbRX9&X-Amz-Signature=4ddb1fe747628a661b8401abb4b007e235b17782bcb54e79ee073d6c4e23f5fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


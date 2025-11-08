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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3NUNKAJ%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDSi4WJEboQW3f7z%2F6%2BvMgC3%2BhLdrn6EQZxt68qnvOwGwIhALvIAu7cobg0YVifuldLvyFjuUFD3K478UtR088rEDP6KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzu1%2BlKiKCKKHMwvjEq3ANhIHRxgpxBoolGb7s4Ce9EbM2rS84dToKo8lKkJ8CYcmv7icQPvxE4hKdKD2HifDYWOIA2M2m9i3yBppQ6tqusevQFIjVdvKtp9TtN2yWs7svNwizx6wOxaJA%2BdOX5szbe%2FAiiScdK89jlKwxkLBpDQltdzzzUAZm%2BYVu9tR3bdQSTNmxsSeEl%2FBkH79JvT9boKYlROw0YgTB9UNnALMmViMoeTvrDSz3e6BVvaLMuIImxR%2F5%2BimemoQuh%2BVOkAuE2g7Kcp%2BmFhf%2FUxg4kVBiXKAvZQbxxVBlwOu9cnjwROG4PYijbHuSdefWbv8l%2Fzwoz4bWKtWs9pTQDPK5sri8ecHWbEMPCsm7mUu6Q76P2CUpbOniyPv7%2F1nau3jqfSWvUtvjGegcK5efuCzb9UdUsN0r0qQsImOvknm7nj6v7Beve6f1P5GbzoRYafjEgb0MXH5r%2FpLspMk95xBOumJnjso%2F4ZxfTSi7A33nyLvAN9ypFyxZOjaUgrnCqSAhsxlE4Cr5qQxqj%2FyP4sv%2B4R%2BiCPfAxc96%2Fc8wBiTLJ6JWLxRdz5LLCgRSFYY3Z4H%2F0vsP6wcj%2Bmn%2BoGGVblPOTtdIrxbEyDbLpAO8YLmqDm9OiZLHRKS9e0owS0ZuZozDI0LrIBjqkAVzvJ%2FXLP5c4AnrpCY7WQoUTyd60bZOJMCi6nVDPGVYEvN3GZy28HlJtiFB2aqpuAmjK8F5XLigT2lsnbgZ%2BRZx7x1Cgz5t%2Fu3gD4%2FIO345LD5Glp4Vg5BtiWgG4Aii%2B0hMi%2Bn6gpkORCw2hD61DZCuU%2BJAm6%2FlywIOuN%2BiAJ3O6g9byp4%2BNJKs8zYQi4dcVoPGvCym0%2FwM56KZLGwWlM3c95%2BSm&X-Amz-Signature=f804d05fad06e404eac143622e2b444441827e101e150cda57dfe3aa7eab4dac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


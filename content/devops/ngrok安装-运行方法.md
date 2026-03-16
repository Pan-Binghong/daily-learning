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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X652QOBR%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIAeftRI6P5b2sLvXoxTBV2e2lWe9eNUg9psVx5ndkTpjAiBdA96X%2FhIfXXTouy3d9y%2FOg9NKzdfZr4vlXUmrrOjxIiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BUnfSs8PoIeHeFNGKtwDr6Wvj6pSJkdi4JzsQSOVEhUuPnf%2BiKx5r7UCfgGutd6rX1Uakb2X1r1Tl%2F3qtiuYxWrhEizHqKDxY8Vkqvo6Gj%2BOUlcFplsG%2F2hWetJjldiwBudBSFWKRh7RG1T8P0SgvDuq5GxCiHUKC6Ry4gMGKShMuXxAHuBZTYXQfF7Fm%2BWi690QMM2XS%2FXbcZMbzsbgp98hxOcvxDKOUhf7n0Il75cOM2v4mJ%2BYaQUEPrmKWcutkrntAEpcBykeku1I5x4UuMrgGvNu8kTk6A0F3Gqz3j%2BQN13eOXIZo8Lc2e1FYILBplQWvl45HgxxY0knVSsaA3cCMX41a3P64%2BGykurtwhIe5Lz6AqaWtxn%2B8k1KUb%2FQgcPY1JJzyntcmfRGVPHKo2eeBQsJ2PwGc2qmq7ftVUexwQ5FseEKX5GsxUnTsaQkuvyXTgyXmfj8kmTQTQxKtFLqaKQh7%2F8QUYzqnuCUwOafbDmcpov9N0NTG0%2FKWsMDWH4oD8TQi27PBxXu%2B0lbCUNHUoEsUQlvzt%2BdRmuvv4LiYI5wOyhfou5e5GfUZ3XKpWUGnsyAUCqUJ%2FiTxPS5kdUtmRPk67sYwnhlnmhyookT5r6xIKDTbql1DMMvplM7I7z%2Feenht71F7FQwtL3dzQY6pgEZdl1CCJt%2F65hyauOBr8LNxGSDP4rQwc2Ivnm0MSU%2B8MpM6dQmCKREtCAYRJJHzjjAu46tuCMjzcWk4OvP5va43Vy4l0FiZUQ%2FAYetmyv68XB6g46V51G4rsoJDzVqvJZnGG8Sa1swcuLJZot4e2znZCsenKcGRl9J2HI%2Bl5smfLkeUVqtrZKGCc9HfPn%2BQKTQNXR01V8%2FO6%2FobMf85vVBw0FmXW7b&X-Amz-Signature=d7fc727f75830999eaedb3673dca72406f761b27cce1bb068321ddacdaf56fa8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


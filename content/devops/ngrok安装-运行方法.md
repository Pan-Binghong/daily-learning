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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6FM3RE5%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcZNbA%2FhnHlao%2FZ7zBO%2FQJcJR6u83K%2FZaICUkBDBGPGAiEAwoO1CyPx0DHu%2BNWsNHYT3qPSmbou1y4Hw5TBKocqEDoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLWlXvLzYKojwk5x%2BSrcA84fwgYULvbcaFh7xSb6FeOxMrnfIv55Z0a4LoaVljlcG3coZj4oLJetcYW8SolNjMP2ipkq%2Fv1QZWPcxJ50789em7zhhg5lfYO3ppLp%2Bsk3zp9gNdBFRUZid4trGaPSyt88Gvx83MGtYt6GJ8lrRyw%2FEz1p7%2F7BW661HAOoclOyvNWr0QK7xTmoQbKs4Gb8pEWCpyReHzPv%2BeBL4A2gDByay%2Byar3MjZp5%2FsjciNHTGjtGwdcaV859KS1rD5usbRAMD4YzlBricg3c3g0kq1k6OoC7zuXDEdwqBTQ1gPUzVjkjm%2FcSRG7RQypEPGSJ5UNBEAyljN%2BOSn8To0U%2FVDsoMUx5RyOO3IgJnl0O9HPCcaufCNYSkI7XKL%2FgLt5BMp2WjRwej9rewnfp2RMhimMP%2FulsgzXTn4IrFw1EEIyH4goZ16W0zOKs8PaxEiRgIFCINwctmY6ikYIVE%2F2iFZFLRwrD7jnzCkYfHK8%2FAF6sNdTdFKHwxLifdE7PE9XhPu%2FfcwXGX6%2FbX0yqi4aRe6mhTiGf1PcBf52%2BvP%2F63aPO1L7NyP%2FCnlw7yimE70lI6IOtRjOmKYJawRU%2FayGBhCO38qGhHKOF1Ai68YiPYT13%2FXEmRcdvK%2F8Qf41dYMIGans0GOqUB9YtvPJkyaqTwCYfLapBycAm899UN4IWqw%2Fa3NCVtCBXKP%2FGLknTRqDdOynWHBOk999hno2BcijYw2RxDz94exbbOKah9wfGDD1TEWe0fx8904CKANaaL61T6n2hmGslEcjUSwGY6I6OP2qoPAkiSQhF91KYC%2B72pi%2B60e1RyeI%2BGXgm3R3WKxvGt9jbb5RAlOoIDGtixYT9VtF8Hq1NSZmvenQHf&X-Amz-Signature=f4735a31ac50bee3e7115e56036823384c51761994c2d497e04e848ba58ae960&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


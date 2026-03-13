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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ6KV647%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBCczFO956Rxe7QAVXnT0b2tXGxxK8igAEUo9BAg58ovAiEAsqQ4chiEyxVNF%2FggTkVIj7bk0A2HAEy1Qe7NxxjdrREqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLq0RlpdJKVEY3VbcyrcA5KHpwkgFel0uA%2BHCUITXs03cN%2Fd9ilwnbuTn9GpcGstqLhFJP4DjL7KU6V21ULCDHQZpO3VSt1fMobqhk%2BsmhEgCNQLSr4NyPQguVqQpdc7yTS744yT%2FE6xxAFgEeABh5FTtYlvM03%2BczTQ5oGP5ek4fihUc3tyRbZS0i%2FGbE7xyhokR1F88EDZOfHlh98D2uQmbiNF5x1fQ8R0HVcT1lZ4B8Bmnd2K3ZEe0peuSHfYEpR%2FfrWY61X0Ts0h%2FlbvbynVBYnsoto9sjZZM0%2F1IL%2FWCbYiahIJfbbhzruTvDPRtaGojIvVDLWVyldHyITB2kidrU7nAQOMScc05GFUsNDTnysd3S%2FzixT%2BsaNa2ITQItFkMje6VpfT3rIRl5gctgDD9AC3GVMqMsi28dlBUKKWERfiMgfDzYjzM16fRz6rGa9U5z7H1l5LmtrQtc0K%2BOOpTfD%2BrLe4XrQY6Co7mxTzT8QSecVhx69Qoqey65IEDBlldyy4itNLHJuXXqOTDzKue8dFgqJ3qD%2FiEKcIEuHpvRI1YhRB6R3fvpQRLf0h80m3g1Td3bxhhDlgyVUa6Mp8afTa14LJdWQsfuXFIGdBOmwmSOMynnWGDbRX6CNPmzC459u1Xtc%2FRRl8ML%2B4zc0GOqUBRI%2FwtkG%2FBzUMwK2Zw5b9P4mva2yiTu7EQdk7S4Dhqo6zk90cqBW1BmqeY%2FPjDjEd%2FKHzDlDBrgo0aF1clhqos6Ti46nyArSvHFWCr4%2BGTJotgVeSnSjEI4k3Ie00odGyO4CNfm9u85qTBsu8sn2lQbjiTYrAbH6mPUBVP0GdPnCo3QagWLIU%2B2IFhnmwrUEu4c7mLWPypOtiGAW6Hu8M0K1Id9yP&X-Amz-Signature=1ca3f8f1e1803ea4bed3984f664439954c0d25e37fe55a767b8d0ecc74c071f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


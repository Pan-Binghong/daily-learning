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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7RUY2FY%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIDzRv%2BIACubvqhiMU13g8DUK0jyBwMXKno8IZXcTGApbAiEAwwZqM3Lr2eKw5%2Ft9XXUFLbUB5eFUnECa0XlK4tJgTq0q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDByGveg8gxV%2FG36MlyrcA%2BMg%2BdtOfEZPVS3zH3KQbuncBfPpNYOPDOLGm95X%2F4ZQ4PGwY9yIrd%2B2gINGzaZkW%2Ftuz%2BmroWvDs4r2i%2BkP6JBU3%2FnpcBBhkmFXQI7O8iPVjUQr6YnqV%2FYs7J%2B0qRq3WEzIfQFIZ8%2Bid7kTyB1XsNKFD2C4DrlDow4qUP3HpaeVFwGUDpEr1tNLcWuMgy2Sz9jqjBCydiDba6alQXEHNDBXMpkKDShzpD24Orrs2x%2Bno4ABOI1ruwwpB2ydQ360OfzETAfFQvgwdUz3eELDlRx88lARQeVZ88trEa6SDSRFT9Zzqc1irK8frQBLHrYgVOJIWXdYjn0NVz13tf69FwBTVCXCkzULexZNfeTHqpswM9kw0zW9HltUluh6wTW3gRf3IymUgjXQ1cCm%2Bhq2NzBOMA1d9ij0yznV%2FIpNZnC6IKCNjQ7YmCPZo4ZCFeOAKYUvgVdL6wkB0LIPDsNURosKI0S2KWc%2BHNQL8wmtCxm3m0hvOMIMwaMIanTiH7DzX4hRzS8Srgxh0p4vcS0PS9ZpNVszcRwUSiaYd2jOyrFzVTCtc8f3Gyw%2BQGrr2%2Fvp2lDQ6JblDK4zAICWOwTbntoMNXihGMrpBdC%2BdBWweDaA3ecXilP9mdTepoO3MKKxy88GOqUBSgyVSNhnwiLAxqGnByuJj0SZe02UnPzh95CAT9jz8fsllQXddDT1pElQufxOZm9RHvHp1hYcX5BZVTqHe2%2FtxuBOHrh%2FFeJXnCH1BBZ7YCk%2FiAwLruiO2fvM7qKCzFe%2B%2Byx3641sE19iOyfXkN9T0s8HScmVQTPpXAgzx%2B1%2FEMux6vhDlKJeWXvCuU3x5l3y5TBsyCjr7FRnK0joJy5F6nfGId5l&X-Amz-Signature=8bce66ea481fc8802d734c19e5f765a62ef3c6a20dfdc5ff4cc69f4dc2130408&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


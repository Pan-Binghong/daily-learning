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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMFWKIPN%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIGiyIbbzro%2F1Pwljjde72RsVtStwmHrYb%2FSCciWO%2BY9RAiAu1P6750IzBcizDAjKjSkSWd9ZO%2FSRc0QyEcv%2Bhrzaxyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM3HB1HoilnX7Ns%2FKnKtwD1nvCoSRM3%2F9e7f8oeQ8jnT89SBBj0mI3BsThFJRZp3wL1%2BzA3wGPqgRTQ0kGlPKoNBKFCV2B81IugRvlsXGfOmykNh1ZU7Ej19aVz%2BhvLT1S9HVJFifD%2FPsVP%2FLu8tMVD94wRugyIDNDkfZXL1fUPCn6a4kGILsJinMRUEfp2JigpTG3LoVsGPj2JrNyA12FOa%2FGdK3YqrxB9jKd5aCHY3RJ02%2FuaxeHl%2FVBJjH5drVvDkTH9xWqMGCMtAsszEpguDsuG5r9aT8ZNVORqNBA6ADbXo4dKke2aYtfnkW1EIxs%2Fl4W%2F0OWoQs59FzE52eLk01cPwFB65y5Ngb60eNK5Rloh%2BS%2BFezjvVU8ywCLG%2FMksAiHb9c6zs%2BtRSZ3bNqnnnP58aaUd086MjV7thWf96V2adatdowuAoyBPuOarlsutYp6hJYVVRPSe4bD%2BjN1c66OQE%2BWjOHrB2v8scgYMYQSbzrXPBe9cPqUr3RnQ3daDXjkciK9kNl%2BwrQm%2FWyie16qs%2Fe%2FpVrxtzMvjl0aphJeCtqmXDClDzxEY%2BHjUvjy2raaMoCcrSdwhhJItFkszlHk2ZTW6VowRh48ZaiIUBVvCATAQlJ2iQDDok1I6NfRy7BqupD%2FrfQ7dQsw75vMzwY6pgG0yBiJnN8a7KOYmjB8ZPfxGf3N0l%2FKF986hFAdnJpHjWaAXKegvS2WheblGOjQrfAOMTr42EzrjHmyuIBte4yCwnEkt7J4fNXCXUGPvv7ktkVSItIHICwX7yOV1xsa0ymgBUioCdTR%2Fk%2BR6c9S0Kh2T4P1wjZsvxai4j9Hxiopb7cpZ%2Fjn1HoRXcxRdoeMcNkoyGkA5In0HUBgzn3rLYnHcdACYlgT&X-Amz-Signature=c79dde61d698130a74c009f8c9d20792d1e8ed1bd6fb85b4a2b8d022ddb967f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


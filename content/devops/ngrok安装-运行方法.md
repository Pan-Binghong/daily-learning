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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ7XTBCE%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDoKeoGe60%2BElzRndFCLK7qaq0D5NV3pW1phyXYFTXF9AIhAOto8sDnrcaDa42elEZeI5lOPF60BaoyVLgHOC9lYnUDKv8DCAwQABoMNjM3NDIzMTgzODA1Igysx6cXSyOmTKc7sigq3AMeMPs90HMfG9nD8het5axyNZrM1Ojegg1FF0MNHYTEO6j7gafhU8Q1cgrtGpQGoNh5hIAGs9AILwlnCCtauk%2BETNK9SQlj0eFyWArboawZ1tFUHLslB9Of2Lwyxdg84%2BaAoPbcwDGx8mZu7nawkjXXXBaEcfQoRZbMqY1452K8SCgNd35GgAsATtfAuclCxtOMIExCkb%2Bgi3nKrmKTxdeAIPwHxt5t9O3FZjU3PTVGA%2Fr6ZgC83onsrv6TUL8EuUFRgrTW83UUBNQS5Zet%2FxK%2B6KKrsoHSP%2FTLBr5Qe%2BQC1cJYZ0DeVpHOkgIiPsuYiCvCZpHS8hBqFgXp4aCCMHz6zjpOxO%2B1lBypVLVPWtz4QpbyYcvAvYhNmQMQma91wqDOPSegdEIVIzMCxzuoGEYotN%2FRUSZVd0gExAzkJ0CHUgg1wMKQ54vdvZsp%2FRwqb9yNnR5%2B1V0XTVKCAJ9KeP8kzUe%2Bda%2F8QytaJJj9pMREbOusu2GKMjnQzHOkt0IfEjRBsy2htfUUbgHtkbEPRAZ85XQvVKNbTjYT2Hr1PTtDfQoyv3kFwbDLaXnSRShP6%2Bowp%2BFx5bx94Ou83iLaXM7YwJlPodZnNlUL7xpBS%2BI9zDnB3O6KUB6kuZ6joTDw6IrMBjqkAU7cwLICninmGlVMnHOmHa7rAxm4yTOgCLHrdjycrLHo7tp4pjaPSyN%2B2oxhLdr%2FNCMx7k%2FgjL%2Btf%2F1o1ycRhmwq22fCgoqAc0OU%2F56xt4O6qRk1Czl8ddXyYmTQMufDhQqL5qiDOxoe9ywwCEHS2qshCYfm4IZYViA3yXXFbFkZvMNVFCRtCTkXdXRNsh6rikq%2FoM4REbl2KYlQKcTELQFQFuld&X-Amz-Signature=6a46563cdeac52e20ef112508c2ae0bacdaa2d06633efadd66e0a06e0e97de53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


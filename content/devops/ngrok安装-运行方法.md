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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PE72G7P%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCtCirTs1S%2F%2B6o7veOI7%2FuzuwvU0sui8eFNyHbOyCCg7AIhALimIc%2FW3l5n89lkfVRm5kefdRlkMFGMSbIifJw4ByDeKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3E3ALsWg7w%2BdfTw0q3APnG6PCqNKkNDSGoBQjs55OJNX55GJl43iGJXyUlYuP%2BFAUG46p7Yj52WqTJcgfGNJPWxQMVLFk49EM5O4KQe22datkLeAdqmyVKevFe1NDFc2v6JOybokcOX0tt0Nbx1PgPr8qGZ36JRz5El6fS7TsX%2FIYkfuPSF7r6b0F6VN2PniGjvlzJKIhta%2FEyRRkEtFPO%2FCyTvlCskSNOjlTehpK2CZRzNtS3TbEcHPugmwyGjgEZ9LvV0ECPA7zsZyTG9%2Br3%2BAbeNO5WqFj3eKG%2Fd%2FHq5XASOzDuEGKvisv6m16YM6Z1%2FhUsGLxVYB3RUpa1h4osabe2nHHb2r%2FZATiht0NUTTivdaVWUre3iYDJfRIxU4Ts%2FwejPqk1HVr2VKNwOv5r5HCTkl23uyCbigiy8zcO4RRo36%2FBKJ6k1bPkMA0v3MbLIVB401TrmnWX4AWDRlOLyEC9es8wKNKgl%2BOiwhllLaW8qPq1hmKqINRnWUY1jXoPc6ZqivJU3olzx6aFF8mAxZ5YIsLOO2BZGCeX663h3wrF5K%2BTZH00%2F9b6SCr0YK6%2BXsA%2BP15unqdNeAX1Ayu5VbVRyG%2Fj8QrPn9aPWjWyNHDEkJ0U5YkUsXzmaiNL%2F%2F5yxKwsFEiVnStizDJotfKBjqkAVcC2q6mWCfLls8C1TtLB4Rpu7XkRSe68v%2B5%2B7Blp3wvNAOmsBqrYYGRDID3w5InX7IrUUlgz5QnmsEMu0y6Z7%2FpryMpkoQYLE17Vtl9ZqVlZHz7B3opk45NXYA7VwGHUr%2FoK1HQAJBfIMS2eMBMmZGsXOtrOSdoCeDRsHXlCDMP4VHq9gIEprxk17aU%2FPbvXPovhV5MneOk4CERLOG6R7Wyt6nf&X-Amz-Signature=a07096543fddd04efaef15867329786acc9e0f435c588078efc2cd6e79831550&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


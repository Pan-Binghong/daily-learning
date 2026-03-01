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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IQRQZI4%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbUDlBdZuK34EevOSYD2b1a7hdLnTnjz%2BdeTsvf8kRLQIhALlCO3RH1ljDZxEp6F05ziO2k5HJZqUca6OpVHwyyv8%2FKv8DCGQQABoMNjM3NDIzMTgzODA1IgypaC2oQ0R7lg5m5RIq3AOZKFbdxubGv67GhttdJZsZlFmDbm21urxQX0SX8JZQk5hMwZXwGB8l6avnWUx509UzRH7sBm4F%2FYRx5CDaEvprgt9XfCri9dNHWAljn7b1PII2U%2BMqTk54da4VEI6p5xeTlU125dVNxQiNqYSKMzg7QqVcld0BUSsHbr1bL5XC5IlP76ghIHWj%2Bl%2BIPcf2QS7vT2RET7EDxt0%2B3hva8uQXARfLJME37eT%2Bsn17J89T1jMSKesLDa0goM2uzrr%2BcZrmdQkGNHJq8yitD3Qq2gqIAcDt8o9kpgt%2BWkDlV3pb%2FdKoqgABMOHI%2BU9sbxFW76C7xYBYZnlKj3%2BlmQOAo6LZUn2OklbknPgjk4iD9%2FGwXbznX4oL3eu4TukITF4xoGHCcKPQ9737irOb7Q9A3N7TY%2FAAVCuIhflN6G%2FtZ8TGmo8BPqw5TNsM7%2FPBsNi24NRrxsV3aVOCQUVrmbUpOu%2Fjbl18dPkpjcPPN8AGvTaqxgH4zYlt%2FjzCNiG%2F%2BnsFrx%2Buj7Fpt28gcw4UL%2Bz4mnBYUfGqHn2rNk95SNJktosAhkr4oFVhN3asYTItRbUOAvALi8iK%2B6CpJZ6fpHVfheWD1AGyqnSPN5tGIT2acdRLooW3QsyqS1D1Iko6YTC5zY7NBjqkAU0zPfi6GX2NRId8qCcS9E2UcOppDT0PTaPWbWzHhN95yrKJ4sxChBpqkKZfAf0H12mzGxYhUYk1C1ASUbHE2B5%2FDRuXhObRO5fAY5QK6X%2B5JxXUW2h5IjQMKbZ3XfXScpeCMd2geiPwGan2Xn8moY%2FJPH2Cz%2FJTKrESHjWNa1aKL7ilclGeeEtyxid2gi4pGWmpGyX%2BxBGPYPXceL9nDGV1gyFb&X-Amz-Signature=421c9b773ccd6361df74fb290fb6a9669c9d56673e5aa1cb776443f82b576fc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


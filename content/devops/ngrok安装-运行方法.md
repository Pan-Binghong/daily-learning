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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUAJLTKI%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2sHJhQoh0170hpUk3ctGyh%2F172VAeKA%2FZd7jfc7uxhAiAfp1qj8D%2BWH45Zhb2zkl8Od7o%2BrcTb48Dd5rcGXZJtRir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMAM1djK574ORnebt7KtwDEV4c3SraigKeXbec7J7Rf3MbSrLEoA6lHF0CA52xuJf7JRcESbK2kri6SSQkDY9tlbTM%2FaZ3zLGyOBGCaASsJnq8SJUk7AErpzZItfLtUrnvMUpjSjLcv7ynYKqq7WxLw87CvMEtMpcTOYVM8jKhWkv4y9XUf2MdW1WydRRTbEaFH%2F132VdTbYbm3JZHWZcR0X9ip0T4ACE6G4TGX2yXIUhxa7fhGnjo8Vc3ITCnDU1QMVwSTV7P609lUvbFY%2FyGyxLVxKfYdN3q%2Fe8ayPWCqq0zpyKw2k46qMGwvvfLt%2F129p5Ww6SklxyJBG2VyIRTQbxDxCj5fnFpa6ZhFCz8fAcX25p4vCOL1fAxa7H6LbRw3uy8ENfE5C0OrA702XRTfJefu3XRp%2BusFJtpulnRzpj%2F4DXA3C3chqoMiNrVKhjMHSI%2BaNNajxUsWBU3npXVDUb0pvVLtJxaONedGEf9SUxV0pMzFsVaHFU8Jpmk3%2FGY6Oe5vaYv37HGSYaWIM%2F4fQ1dKiuA3b%2F9NsyYFUMNxf%2FcX7nB66o%2Bw0AJ0xDCrixT2Uqc%2Fd1AJSQnNCX0F75hTNDxIgUWT%2FECkx9T6yBt0ZSTwXvKHIqDUIDLugbNT%2FliM9H1JeweAK8csjAwloKxywY6pgFjLyjjG8bZTRFhRGCb96U4GPvwRNngvn%2Bq%2FBDaxwta1Kw%2BzuuR7Aar37TnyQV0ae4VwvalGAlnShREKnF9%2FM6G34yq7mo3QSpPfKSnhc8ZromP75hC7qxfTvusUNkFWIqXt4mM3RjMl2Xv54GTcRf%2F3j9pzrQrSCd6kSsxggGKiUxn2JO4zVoBbLpxZZdlfWvLk3bM1Wwtz3ApT3TR3Tugs2XYR4Lr&X-Amz-Signature=adcfa7072375d51ad8f4e8818ffdc1688bb306cf7c1d22c61be2f6529813f880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


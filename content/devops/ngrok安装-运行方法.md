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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQGKDECW%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvfmy6Sh4J8wSevYExpUrOjjFuUGSe2APGRqOOFNOLgAiAhIDA7u%2FL4PL5ITN9T2qvtyeHPBxJGPCw2FFtSeLRPwSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMoCsP25rj7VlkZqf9KtwD6031TJ9PwJ8QAvnkbFoMDCLmOro1703pwAZ1Qun5C775ycnKNlK5vfmrEFXSxmq6v5tH%2BtVv9C3DxodRJumV%2FrH9rH4lne7gq7JsOs1a3%2FiMo9HiFOE5Qp60SlyHCmc%2Fe94aMEAgtkOu2%2BSUeXLTOtjGgbrbcYvTMTJ3ZZhHA9lcLzgm7OaUdGSas4baJgvZVw7rCwdKLCc%2FdJACVx3LUVkBmMJ0dF8lIjLZ2%2BxiacpaU8QyTvafe89r0VuE%2BVXkyfNFo2LZiUp5BpcHGOM7rPlwMjkcEmjuQo3uQ3HtpRvuF2YZy52mzDaSHUs93vg8L%2FSzvhGMVf8oV2jFj97l7mKCEbRZcGhOPqfHbO4Mx3IhBhuiaJe6F0saF%2FukOOhCW%2Bh8afwJNk%2FwUC%2FOxvGXLWQRBxg0shoFXvVlBp8reY0IQxKOBm7oIfr4Oe7KXTq%2FLdQQ%2FFOQTH1MRzbwgss3f3hIFazDVTEhFxu%2FtARPSX5D7di5oFyEIkGwA%2BM9c33EX8ww9UYUeYqikb3%2BdR9IFH2Xc9o%2FVNlbYHPDq4qtonw%2Ff4LjHA%2FfJIMUgQmrlDRCguvN1zt%2BKdYQZoJFlmeQX3OVEfT1DH9PQQFi%2FlyPOFfQ01I9CoAubI40wCIw2cDDzQY6pgFB1I6IcyxFir4vPRDUrxU4lq8%2BEAKLmps3%2FLrScdFy4y%2B2TfvbRZinGgZzHTxJIAK0UbknL4rOpFm%2B8Qqht8qshf0VQiFTlwPhd0nZgWfkI6QxfejjutEeImVkoSFDC0FrB%2Bk1wjVhu1DotK7nf4EAtYzp50R%2FBg%2BMRIVF0nN6qQMa6W8ZMzjj8BoAFaUv7Z4iMdUFCb3Wa9Rs6vGsLlo5MTDW8U8C&X-Amz-Signature=18c1221cfdfa921e43a96fd6a95c992c2e9954c7cb3e8e2dd49145386a4de541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


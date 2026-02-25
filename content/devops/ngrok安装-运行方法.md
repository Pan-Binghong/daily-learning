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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GPSTQIX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQCyajy757ey%2F7z%2Fk6vC0XnMFq%2BOU2D0XVeDO7jr2kUqxAIgY0pNHiuiwUVhWCl4AAusFTd9RYfJqgp0dQgq6r3avFAq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDBcHYiiYvNtvL4k%2FQSrcA7xcVn5JRRWa%2Faf6NGbzy0TLbnq%2FMutSX5Je60QKr3M5N17JpGfDNa7%2BO3tHTnrvbtL24gPzWrwQQGeCJUymOe7D1Ed0rAHLjCPufl0WUylGVPy7ahk2UDVadZsmSA5dEnjzEI%2FWUkI3ZpzSWR23zLnKVa4EtG5LcmHezEaGjZneVUR3gh8oOmWRfTqUnH499a82JqzmqRS9xg18RVNuopkMztAYKCgLbnTSgyMTQu6o%2BYzNzfzXX7%2FmhHk3GZe8upS4PS3Tolq6s9cfYyXHt67RtwbapYa6zopFtFvyIqRD6DCJV7R6Uh6GyTKkSl1Xq1wjoQykuoY6KgvgXKJefnQbxsT%2FP1LZIAdOmhx850XCiOaU2psb5V7299iLJPiUMQMLPDJvMOOf%2FmPDwWbRASfNIorfsB5bTByg59U2ygwNDAXmT18AXHA8jffKHZPUCt9SgNytFG5H6GOFtj4RzgvFI1FgsltmipBI8GSJG5Bx4o4H%2FkQx18k7F84I7Lx1BSgM5uMLcI%2FooW3YRF5HdDCbx%2Bz9%2FvLNzKjqHXIqTLwGBABLDkKIQM1KzyHcS9A73og3AE8wlzzrqH2wJOyJkYIpLgX5cp2bi7qR2Dg2a18z7TSrSZ0pMUNBPd%2FHMOSE%2BcwGOqUBaJEAYPRq2WjiR3%2FekMUHrUiO1gO9EnrTNYdnBZbmVQTwsPyb%2BFnPp2IInvQDg65JFrEbIRyOOB3HizMR0Jf0NnnmRvc%2B%2BNpae7E5Okhx8Cde%2Bf7OKsQuxFAR2VrQ1tl7sgQ6SzOsxhvXuA0sXxf%2Bbo4uyodr6ru5%2FG07IqcRrLZORsIfekKkC3s4En%2B2i%2FbDSttqZKu8MT8ZZ8xb2njFXFk4IRLQ&X-Amz-Signature=2fa898ac4120f39021f965daf5990f8f75d43d4aaa5fe639833e44fc0ecdb595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


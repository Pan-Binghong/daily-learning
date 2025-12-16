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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QTPIOUR%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHBOi%2Bh3GFu7v0aFYGAUunl84diAT3Fd3%2FezHZbRKhrDAiEAkiGQE7FWepQeL7cAr6awRU5zdqmZjvpV9QKjNGRX3icq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDOqplsHGGXSrnzDniyrcA3pnv%2BSubELuT7sX3jbYvEt1THcE%2BupwGadm%2FdXYf28Mtp65HDA03Eg3Eb0B%2FGoe%2FfosIINDGjlTFPNFTSirrRcwKXh2P%2FhxbTYv2EnPViI2ueq%2B1owJt8um4mGGkCKjwTOKdwL%2FUcAzhliDvGN5tCiYAb%2BAbCKZ%2FviRnYn8Mk%2FiGjxDyRoqBqauTzlNhiRWD%2FAn3qSW4r0T4psETybVxVeudlPZnBizLRgCLUM9KKv8ZYzfy77lyZYbC4sOF5cX2JjPslr4ZeY1Tm%2FQBul4lTcOnzLXLUIDsPQvf72c8ttW%2BjgLYwzzBSJdmBnOWsuLLHaTPZYRXtwu%2BZwjp7D3WKDh6wWErknkrVmYp5ETCcxoAcNiSnyhH8xKnh2LfWWIzbo35R3Cy9Eahx50c4rJCS1DzwTuTI4bUk2ICvCT4fXgwdPpcPdsxYwTB4KqJGqywgY9XHkIgx%2BLUUqOMICIxlQLw4lsIx5kdpis%2F7XJ2c7HEo32ed9zIDQ3RDpkW7NIPxEA%2BlSLqoG6hwgUuNEZ4i4FR7NDAhg%2Fw1T2dxvpforKMxQAl9ih6dlmm2l1Xo5yu98ZrpS2pt0VhkNDFB%2FBenvWhqWhgzuPC98ZG2Ua92aDnydefPIeIOUjbIqWMIiNg8oGOqUBgjsmBTlamzLaDD2SidasgrcglARGmUVX33sWQjvjQU8E8DDoUEXo9gUVlLFbFhTmyR1ElWSOJX%2FodDeALoQN3661aqTsQ1FCAYoLFlCU0r9u85BdnUvJsr%2Bdc1G%2BTn6C3%2FPhEV%2BVj048HmXXORcMV6vQ0Ql3wv42ePG3sVIgEsiCZufsvaW8VEA0zbYBx4VB6%2FT17GtyYnppVdZphANEx30ASUPB&X-Amz-Signature=6d5acfb72010c8b1601fc6f7f6a87704f2937031b6e5a47c5954dbc981690b6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


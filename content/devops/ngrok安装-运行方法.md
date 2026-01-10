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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCWGUH6L%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRZIocrhBT%2FT6k8At7Cy8WHyo7tLUHH2vKQnIVWfxGzwIgYhdq2x%2FrCRfGKjY0hG5kMpLA7gh9C3BuDxSKzgx8F5wqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4a6sc5FKueD57G4ircA2qBJGb82midtrjV7%2FcZv6Bxbei3gtKBI5j0HtPkjR9x1zmj6Sp0VG1HCvF3nphJvc5jd%2B1o7dIT2jvbZ7lA7gKxNweXnpNB6uL%2B50i%2F%2FxLg55HMQzE3IUxsxx6Ehq6y2X8gvR%2BlguauLxv6nbgGY23iTVWZ9rt0H7i7aEOJIWdHVfMJK2ywVn8JNcY1jx3D6PlUjW2QUONjG5xhm4tg3fcQTpbIDcnAL7wUSEq3v1dB0a7VDT%2FeVuRAUAzrIOYrn%2BnvaMCcZRFpyftyAe%2F9x4SN4f3rgSYFjD9O4CAWBdnEQMp5P8LDiPxWXJNhmcZK5wQdoybhqZ3ITuIv8iQ5uN%2FIl1CwWvBQaBpI%2FCCyuh3KQkbGxgDZLyyD%2FiEMD23PlJ2ySmJT5OnX7xXzoGf4UVOPhoPrkwD1i33bMBULROw%2BRMVI5L3Qj2GCm12WlG8dKKnY08%2F45TpFh%2B7QWHptLDTUA5WFHUDhtKpinjmcXFN9Yw4ZSzPlvYIGN%2FvZweJdlvNF2eghOBqBVMXfFopdEwAzOUiRjhqNzp6fX4F2WCzOW36YsXbewe2t60qNKc01yMZRFQb%2BYktARFi3ryG84hKEYAvGNUGk%2FeMV%2F2wWvkeYTqc75D2s3bW5rfSgMO%2F4hssGOqUB7R%2BaAPtByC9wJ69LSNC5L7pizFlL7%2BA0362oYWVI%2BioYH73O3StmUlkRyngi4FBHc%2Fe68Y2IpN4qd0ebKtyx%2BrAfYGuw0aOfnsjlkuIWYOoUQwHxgzrVJ3nLApMnQUGco%2FBG6vnQM%2F1hdhXfopp8xJY1aa%2FGM5dQom2EFFqXD8eYC2HiG2UfHy0BhahrUgHYqbyIjqk%2FusxCbw6DCf4NRJN0xCif&X-Amz-Signature=6ba70e96b7c15cbff3fe93d507d80d1af0f3e5e2e4564f1eeec1088fc852e12d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


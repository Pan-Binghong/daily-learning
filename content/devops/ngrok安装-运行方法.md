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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGRGL24P%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCnRm6CE%2BG6lB8tP2jN2eFidAxY3SvUOUbOqCrHj0YyCgIhAJCgN5Pe8jK%2FGUcaEpldPNiFB0Uv58zvp5BOIwMdbZHNKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyBzJOZytNvB4gHdkq3AMeOxP8lRppVynilnttDQOz%2FXBy7BpEZgerSe3m5aUpdcqwi%2FHr%2Bgq8K8zHVaxWUH%2BebyAeKrGQrTkXSs88O2SnfT24oD2RuqdJpsq8vYDa4u1BmBADUVahPpoIJpNCpPdQVh35BzC0ToBM%2FxTApcamUz167JkHN3t54hCmoQMHiaHt1pf7J5sxW8tXDIdHkGDrBRvAnJDDmwUhZEX7Zt8IGvH4UTbR2wZfucplKvONYz1Bhfk1Wv7I6rG4NtpNuhOUM9d4GXIz4aecansRZyiwUoqEVgutI%2F41%2FpiJ0J6BIwdYIglQ%2FcXpkEbFaz%2BUISGijerEo4gtIcMZink7V9mBZWw0bTlPo8l4hRvg1mdO7CwNyPWXqrupYnTUF0v9zfYqrVH4eyk3YGu7aThqD01lNzBisKkog4YnevV3ZfRzL9QsTGnjO5OagX%2Bk51DgFugSBwapqwwdG5CQNnBAKStQQMoipkuHGtZ4dF1SAQZe2KCGQRwverOJUIHkjjWIcYa56Dp30E%2FQHASBjm9sBar%2B3vFrbIFu4BQTKS1iL%2BR33w5vFcJ2JTlQ524dukqA0oJXPEqDfX6%2BQDNd5jmaUzuI9edxH0lpyYIU5ygQ69I3uTgrd3PgSPRGcf8MWDDWtsTIBjqkAUd2p7L4GjuAStV%2B8U1fOYtdx6rbVvjDUCAzha4KBWCDWUnCecro7RsSE1Oy4YvFJPZNZT4IB2F4n1fx%2BXgveKacwiHrNDbzEts74onHTsAwj30l9w6H4PiX2raz0S4ZnGXkDvHhEzfGM8Kou7mT5gYgvIXM8EO1mLDbxQ%2F05PFnUYEwJWQ9LweA1efgft9QvJg8fSq1Av54XYnwkWXB328eKSk0&X-Amz-Signature=81965f3a31b762dc6cf5ed2c3269a18454c450eb7615b674489eb9c9644d6ccb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


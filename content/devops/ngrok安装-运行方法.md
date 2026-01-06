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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA4HQ5LF%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCj61r0KIsbOS0rLu370VaCT0azSSFIVo81CQnL6JRVQQIhAI0UcJ5z1ulmqFBIU5U77Pg1VQK5b%2FNCTkuWa%2FD33eutKv8DCFMQABoMNjM3NDIzMTgzODA1IgxyOGojRiX%2FRJ3p7csq3AMoZ2jxsGqrRKwSjNpdHTdGTC5NZb%2ByruahWk9p79IA8IrIBxwpAErwBUyFIk09NZgjIhIxJfhL4yp1eKnwTZF0pGKZHG0kQJFDZO7qEtHO506zvQDgoDicVpr0%2BQGbbNVaMe%2FO8oHap0jI2Vowrt3AqF8lX0lVx6cDkDJsTHMDlku4Ifrt2StYkckfeYB6y00VuGsZqQbs4glEDaLQ17n6xIu6GgR15n5K%2Ba5TCDEPk7sslPOBM23aVY68hF2iKyUB380T%2FwethgjOF6tqc6iPIpVng%2BiFTnCEn7XiRFSNIN5M1suVyL3qWZUaVcmxcQxwHP19fott%2B%2BzEOfO%2FOlYwqCu9x03yQxs3H3RGqfXL0k%2FfE%2Bi5QHrLUREKZ2%2Fo269fg4%2F69%2FhHg1eN5qkwm4L23iPNi1r2sornXHUfpPjTL%2B2WvPZv1vVyGZpXbDhFYJIjZd0QUfDNrIlEQRzMiM3bHA2Srp8uRwoGcxWCFpXPtIMdAtD7SWKghU7XlC7zEGqKBgxqy1eUyBoj36O1ELDnxhz4GthX5bymCzT6o3rd1Ei5VrHLxSlWJC%2FHdemTDOoC0YmJ05LXa1kIAg74EFag5Jpyf0sRSMWfIkCGfDs2gCdAnS2aIkSnMHl78zCm5fHKBjqkAdRvUMqpVQ6MJ%2BsesyePqktLORpkm5%2BUswlWRA7hYWycmKtuURFupJGkdY8kEn6%2Fj3JkV7y5yW%2B16aJwbIoxmslWmWIgAZbZBQJfy4pNCjiclFFhfLl%2FACbDkglp0CveAzAFxMtUdNf2gOjxKDnr2WGsbiPhiK4MeUnoknsF%2FEpP5oRVGTuVDOHdzq5nJgTzJPYdKIWq0mzywmJEn7KIDrZixHF5&X-Amz-Signature=8de1523e21a4086b0f757d7e9d7ae52cff568521662079b87a3343de03404712&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


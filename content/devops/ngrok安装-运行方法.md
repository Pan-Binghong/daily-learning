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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466725GP24R%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGzicxvKHCQM80g7S9BKYNPhnatSeJWFOJ%2BTgluMQmwEAiAzpmr%2Fo5nzTGXBlGMIL01%2Ba%2FBwiQIrZOSjh16z%2BrgDDSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMjuWlcb4aRnRrqJf7KtwDaRm0I3q7FqlmKLybxf35gRXIvvE2rBJXTmL4GErZy%2Bqrv9MMYWUZj00M9wh46L9XsrfCaWHouGY0pCpEmCE6dDIgCT%2F8jlNtLcyI36Mbxi2g1olNgRRdbwz74%2BQQ1w0xb10bd1Pr2kYa7d5pyrkooJVLBlF7PoY7s8PDUVoPcKhdMex90zrz1GrZF%2Bt4MT51atRxUZIkTwdsvCFYdTS2etHaKoosmGFB78QgXpQ5IlR7QcBS4D60eWfAOwscVzKC7ngXGD%2Fqd2qswOtpGuWZtE9nMo9DGvRigTFT0QLHZ3F35cJuEe4uUwnQVmddGQfBGuIrQhqzDyKyWNk7Y1R7D21%2B8fBmUtfjnGiKmFva%2F4Xm1bGQcUOdoRgYXY7WcqaX9hEgchJbViHB0OeTnchsN7NyCuY%2F7UIF5x6VjMP7gLZ26hmhkvn6RAUaD6wQu89NWdKpt%2FwNnE0bmwRz9FqCIyXdSntt1Jvilb8ud6wDMtiaRspF1o5pUa2W6suL82Uv1lVRjcJVszxbBkhPDhYVDqZsu2PaPg46IiQLJIigpJnvBOLTc3l4Uzd0WRhHsS8CQ8lcCsaE4iShghToGb8AHa6vTQTw%2FZp4tH%2FYvg3WJ3WEk04IPJpuGnogTYwwt5%2FUzAY6pgGmOQBGEq2d6%2Bh6ZBI3M27MEMhtht2OyjtVI6SfyvRJM7N298Re%2BB519cYWO7Ng0k8c45Gt02SnBbXmTe%2FOWgwqjrVOmXNNbuscNITQZjxOXS31w9DZaGEkbIY3hNyY%2Ft3bWIhKJNmrZA30ZYfbAJRXYSKzjtOQsjoAyshKuma%2FBMebX%2FsxsE%2FtyyPxiTL5oonzsvb3LiUd5m4FSUnWTWBBdUrSGfiY&X-Amz-Signature=e15e267cd08fa7b8e4f421977b13bf304fe9df1960752305e3f9fed3c6ecfb5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


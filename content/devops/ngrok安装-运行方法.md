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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPIJO2V6%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIG0b%2F3znwzZ2qE3WICbdYIdo6FAHPEioUoE%2FQZlHQjPMAiEAqtZ5gpZzlF%2BpZ6vIfr4V6EGZ6nKYyzl4cjSfFXT9a6YqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyTlruHCjTjK%2BT1QyrcAwgC51sFTajA5bInq%2BieLAgEYR6y0k9eawzfGbYe5n6ektfsDYfAEd4pjKGnLzq0wIww7c%2FmRDZjRjv7watkbQqyNKj13ZfqeygX%2BObj%2BVhaKCDpPuhs6mYrwtt7KaXhXujqutl4bhohimPb09uU3ry22atMHkeN%2BZ8ERlGY6vzzcYLkmUBh82G6XA9GO4d%2BRJjcAa0YYSarB%2FizddGccr5qFVrnkfgj76N%2FqImPH986LvDQeOfA5qx2ih5CSqYXaA%2BQnmM1A8%2BBZGesWvUds7Cec%2FeK8PoRjTm24lIhaPM5Dxw9PR%2B15440WrMfxjW1ajtC1S%2FjJ1zVFdJ8i4qkIakKnkjYn5iaW8Ite%2B7VKVvPAAHA%2FdATZ452a7opbxbAxB0S2zDcAN%2BOG6SVYDfBIvsyhUUzyi%2BtvcfBh7qNSvJCTvZY2qNG7%2BTMSyrzIiBTrzWNqXCfYRw8AqDKJtWnTLh1y51v%2FQuPyX1teNdW2PvwgSvoMhS3fNotpb4l%2BTXWPvmZ4KNhHp42Y%2FD%2FzrEHGaZQ0k5GP5eFVIApx%2BsUbXXnaIvpmDL2A2%2Fy3vD4IF2bXlZXO79kOxPt1QMsqCRAX5HV52S4WsXtaD2uPqdpaAw66fUwHraBm4rSYP2GMM3swM8GOqUB%2Bgjb4fdzztjCKVSmPORMGwaXH3y8EgaRUo86fPVzYIpe5x8Vr1QyD%2BmyFaik0LalJgb5Az2C73FslaqJaHdKSq9vxHDjXgo6YU2GC0dyDqSKYz5NVW1CtLxMDPyukfac37F%2BucdUf3IXYaQTgusUa0qNL%2BnOTJRkgEjVq1eaTUiXy33lltcz1Wd75m5ollQUF5C4yY8OLgFv5yEN3uYmAiREqVjO&X-Amz-Signature=f61f585db7a64ae40b2be02cb585d2d527b630f0246c1807757a5e85d3fe2890&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


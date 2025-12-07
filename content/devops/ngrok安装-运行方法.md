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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQGGM7I4%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDngrmhhnbAaHvxAklLPwXNl%2F%2F2AcgLgj4KtxAiU7eJgwIhAIjFQx0ZDk5Ha%2FfTmO6%2FWzbU%2FuusJjKhPh8Gjxhm2PlEKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgywSVZ%2Fa0jLLOEzoWEq3AOwtunW3XlySBxm94EQ9OZG2JeFxyF1b9M7o8%2FYeYyCGK5qN3I%2FJBilag3CLlothfQuCGTQcvFG2VgrdxR4%2BYqQCvbSGMrVKWtgV63zPMfAqclkz5BY%2BtnI20ryH1X%2FyXYnLtqVTPJ3AbbUs2GT%2FMfeqnwYEtjJzxex3Y%2FeJ6fJ3UBcSNq%2BuRDHjZx60AD5Jc5wXDDGzbkYYUZmzIcpBuAKqs5i9WerFRH%2F8DjnGw6eDII7JQYJlRkaT5TZMCsaL%2BdvjdQK0YVnR0w1Sv3sIpih0H8wV5QTF75m42KpUUhH4HKVLzoL0Ybfg34VWrbH9pu7SC5eP2s%2Bf8jiXcfqHJimhHDPqzVhpd%2BL%2B5fjiGuGG6ySBy%2FcKbiUu2K7O29%2Bp%2BLdIpzZjsFKv3wjnPttm%2FXW4spLkoYiny6EHhpON%2F7Ql%2B5QCmvS3jqpw4WoujN2Y%2BObSa8YQlGwk2sTEyoTvHIBhvBXYh8t03l8i79Rdwlyk9P%2BuwRRc4j9Xkz7%2BCxf3M2x4FHujKzA9QXPYkbMejfYdkqdhHRLQeXzWa9nssVQNWrlRb%2F716sYMES5FlvzK7jxH3z0KL5eBtzBiMoJcSeBRPQfMvyYn7ftMuPa0Zx%2BCMhFHW03BXZXrqXe0jCj%2FdLJBjqkAZm%2Bs%2B24UfdTlkgojGcI3NqdEOCk8lQPIT%2F517rBbMRZEXc5MnBHkGLFBtPFBp68%2BJeAiYRyOKgS3OTyDCQGIu3LVRRrf7RqAV6884j4k48lZ%2FatzIRCZe2xmSE1JIPHRZkWel6elCbcO7JptZRAunuHv%2FCTojwxr1nI0nXT%2BBsR7Y34xeMFrckSTrtsTPRqMduJKG7YzFErC4Q77CuKrtZymwNd&X-Amz-Signature=0ea69b4ae611f0af98d4d785c0af3c1527c5b8409b246229516695a3ba48397d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


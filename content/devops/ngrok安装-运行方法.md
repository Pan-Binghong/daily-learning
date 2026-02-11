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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZEKQTYR%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0UCAPDlBMDUykH1GBch8HvdSI0AdqkGISfVL6VUqT1QIgMf8PFqrerVL6z22rcy8Pr5%2BG6XNnmj%2F4tuv8E5RfhrcqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxt8kaY3RHO6htADyrcA7AXbo6aTl1yUQG7wC4FjBV0lIcVu4Nn9shb6ddJEcllR%2F2NV2Lzl6egkz4d%2B%2Fyp%2Fn6crxAFhFi8WnFYDi7nyfAVqSA9187f%2BYQ8hkyX6w6zJUVvgcqqDcIampk529SlP929PT5Bvnwuo6WqgYG1e3bi3rmMuq6wYO9Xh8t%2Fy5ysIv5ogkvkFh47AWAZWGZ%2F60BsX5qH0WE6mdrmLvA0zSNfRwZ74D%2FaLbi05I8AieJwEwlPCWRscguB1rXy%2FM7CNxC0PKZUrHTgrU%2BQjLXS6uLZ4BkJJrns%2FMV57urwnAUTem2OpiB8svzGTWpvyRwxy4irJluPrZdw%2FNBTfZPlC18KsHvX1eO0d0%2FqFP2VYzMWiJy%2Bhxxh8wRBGxuX2jvQdgkxAcmFHPvInMfV4DH0LtN7S9o38%2BgRFLpYDskY4DETu5uGnQA%2BRItAxOL7auL%2FZFArA%2B3VOgQagk6n2NOJgRzN2Q7Xa1HBTq6%2BQwRPHccqcGHAMNcIxgsX%2BZ%2B5TPjsre4FuyjTJzPc97dxYOjANi7lqAN4%2B%2BwjkdA1MgINVFPw%2BrAHd4gvgIvSD6%2FUYo26ha93u20tMwdABXXqUFB%2FgE%2FwKeiUoma0BhsaG%2FI%2F23UUPSeoN5QE74dJfjlXMPXLr8wGOqUB%2BXEg3K989XC74qcYj0mV%2BgsyEOPVo5jeHqqLVBU7bsS9IorNecSsQNacVyBLMNeq0LPdo7%2FCO8I4x4hbQSydE4w3o6bHIRMDa24pFpyPnauvPnZ2lvw6CRDYMGZt747ajSKb1g7JmdSaTI5uY77bx%2B%2B2ZCTA9%2FrVsoFVlXehE1VbdkL68%2B9%2BkQLt%2FB8BhBk6GBj1AKxTzNwlgq%2F%2FOv1rLZsjQYby&X-Amz-Signature=f5072c0a6005679bd97181ff0cfce52ff9b4c5165f302d3f5a3456f1b5aabcab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


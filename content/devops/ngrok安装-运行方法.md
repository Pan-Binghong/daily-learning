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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVSZCM5T%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDC2pwmpEoxk54ZfM7XcjxUxm2BByI7CIDYo6pM2Wm2cQIgTDhK%2BMd8YI%2ByQsqnbYlZa7LBMvFot1O%2BQoBs8IZJNzAqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhshkP6HupUFSUQXyrcA08utDz1Z84HQ5zVfIZrN3zIS9NyY1%2FXeo0omSTOBaJf1V%2B%2FqNhYKQzsXGBFbT630fuQvM%2F0TZE5Gn%2FlEBGFI5%2BmqzHZbOrzJ8MCG9KSMeLjJorEMv8w1qlvHHJvllk9sFJfBcVJDOW22YPSo93IFHzU9eiwcWf%2FAvh8Gc84L637nMpp%2BDSWTynN7XpcNE2CPslZzI134rPIbYZxY5PugHy2e2jQIFYUnNkkSRGitY%2FstJVSycDOQEsd46o%2B7HoFqJyGRbK8jZK%2FtV9hfiN%2FeAqjODUBU0hlZb2zhckpq%2B6350SRf%2BWybjFgJe7RG6AdwaD5NjJZLgwmGfY3FFJsEC8cyQ0qciiGWdVvbq4Q7VQCuip5ese8VrnBDtEvT3dz59dNSzlK8PmWXCKK7Kjvtc0PX0AgNi7yvdU8rBgI1jevcR5EBetf0taWMMyOCgeb3U8kcuCzL93E%2BRu02WfEQ%2BPAp39t5Hfjnru4Iz%2FgI%2FFzuvjCMMjvAnMDdLgRJ7CrwyHJhSmJhoHnXUTvttEVifhxA%2FJYwoltqJxsRD2uECaOQ%2F3FPHdNV3HK%2BJwNNujfXvoh%2B1Zxhb3gOS%2FyVCqWHQD6uAr2DskXep03y0zza84WGe6hv%2FYMWxIedc49MP6StcwGOqUBFvTyz%2FQuUXU2J2WrOARLzJkmpNaYoyTS4eOl3v05LEzHmrTicEpr1RkOlB9vicOFHErce4KD5FJLMX3Z8i%2BgFWFqdy8bBdnYQrSGXsZfCph%2FP193c0pW8NE5ODlk9LVl%2F%2F5D1OslBeTRVI7BtIoE9zQBTix%2BQR1t9obWaVpyj%2Bd%2FZAaapnkFbr6BeIzF6gBjJuTBuwcahWMP9ak3CE13H99YMDNR&X-Amz-Signature=624ff751ff7f257792910af30ea1d26551226b6efccc15e5eeaf140a0a306e8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


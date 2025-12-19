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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF6VLQM5%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuexUxU6Hf9oJUJQV%2BocXvKR1gIf5I77yaun9mbePFgAiAVYjeryyE3XT83X5MmNwANLgKRfiC0wUKPq9Tlr%2Fa64SqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMiJpT9C1m8gKYrSDKtwDydWcRrFtoqHGG3BHxdxP9LuA8gWfkN9QmM4xkm0ynr4gnOPx9QnMENzQTjfu0RZleVJ%2Bj19MQWHQRdj37mYlSF2F272wYBt6XmVN1wuexo5Slxp1t72EQr4jUBGXYJFb6yvJiHNbiCwNhz1gMAUFPs5vDXMxv3Ii5Pr0dmA5nN%2FEmv2iIvA0%2FceO2Ej2oQtHrdXeKwD%2B%2FAi4DW0Qu2eCyMcn2xIitPjgvv%2BhwiNZbccx8TmpOSSGYR7GG629v337i3ivLwzEIAUo4DJlKRyT5bV4QTPFJGXd9dGMaGw2vv8c8Xe0OGNXTwEY4XVcdbJ9c%2BcAW6QcIPMEdOxS0qTKF8fIyJIVPd6BZ7tGcPkpwM0E9VA4czXmydVKmEMS%2BLjYLVMUH6N%2BquC8swkf6bb8gLdiw%2FPeb1hrR%2Bn6SiFag1lt31MMtbS7KFXt0wQRSwISfcwWHx2lbDrCPjZRCuSL4GaYx1epdhb2H6cYRfsc0dKA8MMiVYInzPQLGVv2UAHm5F1uy%2Fg4obKPV0DbnIU46WnC0Vei9%2BkMgcmCKgiPkq5BBLvzHkaXqsQwFBZy%2FLfs9MMbB84G4hNU3orY5a6hEeaJ%2BGcK20k5wQ5SLctc1KTl%2F2WVEbsrWuN91dUw5OKSygY6pgGa7O3hhJBPgWMwcXqne8kUwQa4yu%2FDOuW4TRHfVJVgSjD7oijohF4rR80TJosNuq7nNM%2FSKNpqEol0u7Y85HVM%2BG%2FwM8ibTL3uNyPDubolDzJ6l8Xc43Vkwy68MYLuKj7j%2BKW4dc3tNSlbcnICUlbhFtTWE5CsU0CZbwpZg4ZxYqzQdtLlPruHFx451YGbjIV%2Fo939hzpvPMr9mDSU%2F%2B7WS7Sgis76&X-Amz-Signature=aa64f4b8d83fca645089431ccd2ef20f72e4846324f548a586860ab0e9db8317&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


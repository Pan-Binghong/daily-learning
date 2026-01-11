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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3IJH2D%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCKUM62ysP4WsryIADpLKU9T%2BEXpz0wDQSXjVkUBznrIwIhANM8f7RYhVEQIaGlpI32Blhj9XEdgPGBv%2FMW3Vrgd42PKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvonMHYAL9ehvvSxQq3AMxc4BV1GMX8aUNZozMNCcvrqQfoFa3XcfcJMlj2WF%2BfH3COUrfpmIU%2FF3XKiE67YusbBW2hgqHC%2Foqdl1TmjckPd51jSds9BvHomB%2B6Rl5eMpJ5CS3U11OgfzssSZlymjzXTUCJmuVtAWI97Pzsbz3hg%2BdxjM26eaNTTp5Xv3lq%2F3CRvHRoCTC%2BIqfJugIXZBrD07qGyIk1t%2F6UOdJSacZ%2B7Z0Jzl6iutST2c8xw%2FkfTOAtuLhjrjlc%2FEhJy4%2BJrgtImZQIiIm7nNszzNl5OkbOqnBHLGvSDP0nHuLT8ZOZWRvYyqaGNreuOsYnNLT7QOMZCrrY0253T46xPFYlduVrI0ZObKWwuWH5%2FvEr2HUnmvlFkWk%2FWiSc6%2FqPCAwSX6Plknd5ffmqETB5wYBSD0IK6tG4cJ2aVsCg%2BL8j8laLfw9vhvD8x%2FsG92pUbSZ%2FlkKwX89LsnJapsg1kOY%2F8JnVqeSITgjLmXdd0j6xHtMcFcRWo8YqP135IV%2Fdqp63mDUBd0iLPYl66Nigbi1LEjLEtpJL67%2FzmKHAE%2BkxV0PesRfW1kFfLE99s3E8fUSQnhh3Ho0aXyBV4GDmlD1z8CUjCx2v4Auhzs01QXXkRFqrx9xlI0AZBg0aabhfTDe%2F4vLBjqkAVDtTdaTktFiQikhgFGXol604HaBNfBwrtor%2BF5ieC00TXBEOEviGefIs9LQtpwoXeOIZUg80PWrpLjrF%2BzfvAkwfxrEAfscHZMZIey%2FGuTQQpQyhS4%2BWx5s7IPwNSfhKRceMdQn%2BcvOPfxNaFwbDavmIS6y%2BDbOAvj6bd8ufB9bihVleO3YEgS88HTSxlOjkRIQvTwkd3fPNbQljPyLhSvWEH3r&X-Amz-Signature=79ee455fafefb077db14a09ed31cc913bfb38edb4276bf6d455f04491499da8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


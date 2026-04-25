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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFDX4HJT%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrFig%2BncDiVc4LxO4D8lEQjcERsC6eJcJpBMZaLvTvkgIgHcWeNK%2FRoqG%2F7Ul7k6V3TK1EW%2B8ZSCM7zxe1Nrj0fBQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNvtazpPpRlBK%2BaOayrcAxOfF6FGSBhXZG2AmCcl1BxvvClCi138hBo5lVPDfW1%2FkZfklJut1uc3k9eaLrk3KI9Bn5LaA0hXBj8wA5mtphjL8cGVbOANeogZjkf%2FKz8Zg3%2BaSXyVR2TtbJmb9DzK7eh7zt4jSVtqjGdfKVjdD09XDmuU4YQ%2BL%2FBwn%2BbjhtP76TBRCrF5r84jEnBeG039jU80gUpfnnoV%2F9G6hq%2Bcd9jP%2BzUPQQnUbsQM2OOrEjakUnA8m20jnIRCTw8jWj%2FDSkPhLAkIpqDvK9HhlwE0UA8INPkkvs5yy4Gvlp4cRhTUwpAljRQLY7gHLGfOynFnCukYoCTusJIM5LR8P1hMG5CrQaQvb%2BKahy9x5SdSMPHXKrXRX4ZLeldeFvUlH7ZiZXyOB6MG8B06nE6%2BTmYvaJMveyhBPvsjo4NSKtBJV4fZjiihSxJVwl9a%2F1Jv7eVjG8EQZepIi1dW6KJveGroSnwh9%2F1V%2BArGeLwMa4zpCZPZEW767ZnaIHvNcixHy%2B4bccry7GVoPFCcIzm%2F3KH3TsSNZiyGFLsWlNvyq2mhCNTODV7iD6LHnX0zEG0BE5kdhgYJkiiJdxUs1I%2FYcNmmXPOAQiesYO0IQrL1lTYtO5wNt%2FVbFYMKGlgWx7f1MJ%2FxsM8GOqUBOjFO5sLpEEeD8SC0g0jkgeplqY%2FP6obUwC%2B6v3%2BWuDTY6DzLdEejSgZqIQgw7YZJVUQVap55E06CrLIF26%2Fh2EvBTJXmjJTDB8msSBdjnUDbs9gtYCn%2FJ7OTpG93%2Bge6ASEPGD66wz3VEFbC5VL5u4yJ5rjYv1vaBzXkSdQ3p%2BvuTVr8ssH7bcJgv0coHK3YYAt6xLEl3zHw9%2FOLEg4V1sEgLcu0&X-Amz-Signature=17f60aa4122637a6e461d8129832134462a7b89f31ab27f3517e215ecfb6f8f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


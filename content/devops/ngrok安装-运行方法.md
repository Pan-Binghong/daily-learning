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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UAXNL36%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDj97o9PJ2jkDhg5VdwZp2peqBP4hgdcNFCQESva9HCkgIhALT1xvq66mCaVaG1V2P0eHlZ41%2BeMeAv%2FZOj0WArimIUKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy292LxUwp1OWwuZC0q3AMlewrFWvDPmXocX6EBFBqLcG%2FcEwVfjq8TnabcbScpIDszTFTxKAAEWjVxWjaPR3WXWu7ohP0B3gIS9%2BwpnMI0H3t6Fk0aeLZC8Qy0%2BRWn%2BspsbVy7GCxAEo0bkXqg8QUPwJhxyq3XwOlxfBBxruqG3xXKH3vwi47TEFJr%2BXNxnBMlMMsMJcTLuZqdAW4QiQOsg2UlN6r1EAkfBp4YDqlI7JYW10JLg9FcbVdLBnuZWKhXiV4yFN%2Fgx%2BCs6t9NgYuCAkRBxRv6Xs%2FPiR9pCtf1LpCkOsB4IOS5O0ChiTDgsbLLv9DwbLYps7rnwm0w2BoJNTd%2F%2BJGqa6tiTsT1LSxHQuOlPE7bX%2BcY0nazuqucA%2FHijvXuj3HjjiFD8mNMwPP5cGyju5DbnaJZoD9NNBbDe%2BXGVJ2gDqPUUt3kD1WkLigy60NeH22Dg5Mc1ykUhFeQxAmH929Hj3u2rq2TUKen%2BeBcIV1rdfAy2EIoXRTZpfU0oHiAxnEgwoE7Ds1YkcqE2FB3hRvUAdSW%2BBe%2Bzg3LCJv0uH8Hu3R%2F8N7QpEZ5htc3kEKG1WviN17ZnaSlSwnWZUv9ynYPBg1TySKXyLIP6WkmIWHBwrMXCPFnUkCFxvjOKtm4xqTpbBXNMzD7rsvLBjqkAab%2BQ4kmtfN3cei5wb6IAh0NvykMLyeumNl6hyRGbHkSnVyx2KFXDHHfvre7wNHD20kuTjErWVcgxbhXDYcKuhHL8WXDljWQAEgjPa4v4iUAe00U5MfSHyxx3rRmmwpcH%2FyzHMD1ZWbbkutXFt35aqSgbxB54lYbZ4nHTtp8rNXtCaS2lWypWvXzig5lP8zchtu2VMhjWPL47i%2Fq0smIhstxMGSZ&X-Amz-Signature=16d2bca2abcce60efdd1b97c0d8c37973fcb700681d97d9318229b8938b97aa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


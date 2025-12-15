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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675AGUIIT%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFBHX2VQvFM1fFkXswCE6%2FIT0a6J8AdEN3Y7xLTOvAAuAiAmX8WxW5a%2F6ueeRfPHJq0y4lytwXyjp%2BGQEDkj3tXgCSr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMRxRWP9AOTKLcZ68SKtwDOllk%2BpGZGLeAPWAGAcMp%2BKMS%2BpjSfeVYRxpu88dpAWk61UUdG%2BajpeJqkUEVYbJKT3%2BftmSWizyaG9sjfVT8ff8t4D5vN5JGhjzrYCneHQvrHgXZRr79Gkz3S3Fof%2BC2ubW6hkHvg1NHYJiN25723bLEpXdOze5abmTD3CSgxyNAkYvEPGINl01tGfEcFxLZ%2B3G%2BiUH0YllTZ5Mwy6DCwmOHZCcMQDoQDBa17fpjV%2F8LuG2ut5nfduA8bWETQljijPRRda2Czcmtd0jGKlgOLfqBfOwPYch928g7q7lSzVd8QmEBxn71zUSDEAYDKj4w8eB3O%2FBSKvtpuo7YwEsDuCLFzULDHQDioOs627TZuREgiBZd4sq6eukRmt%2BZ%2Bk2QBkwceuB6EmuQmYhoAbUQmGrjQbrYLEg7V2Aad6JcWHmTiscxxN3fbloG1MUQmMrf09H5w9Q1zgCrxIWuv3duJjQgeV4UNXNkGyeEV71aqUM3csPVSni4ytaq%2BjJudjSvCUIGhQ7Ee%2FKZJ55XoznYn2pZzAhWsfKcxDtd40SuMvo2nSjfuxOY4TPFcpWAEDkrxlOvRjvBMU6PqwCI44zOvzIwFSi%2FxiE8opU%2FzcQ5FUCSt3uQWFkJewElyqAw29r8yQY6pgGDiVS0YXIC%2BUPl1mN1okyuvBVG%2FNRBtm0ab9kn6XqWZTdF1uZCYoFrGgzf%2B7GVlLPthzreKHbAoqnXUVV3Zid6Yjo4yN8jUGeTDXbtw6%2BuXJV7JXpNHVrgFZG%2FrmHwrnOq7r4rNPv0p%2Bfo67jAh%2Fk7JMPiD1YNB9%2Fr0GLxpg3x3WPb7jkZ7cGwBWuT4Ua8GzagglGeTPF1i5itVw90KMl54Fnar4ZG&X-Amz-Signature=c98577b338432e5a8d7ec0c6831ca540f67597722ef2de531d656dc247094368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


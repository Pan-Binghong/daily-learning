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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GONCX2I%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFl7I7Ck%2FxpIW13ToGwzBVJzfGpdrsgcEY0fLQ4JQ9nCAiAO6GBam72EEWcGu%2BV2lLvpLmYo%2BpGyX8wD9cgmUOw78yr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMVMnCjw6H4498hvYLKtwDZRp3MfScYGgNdrNB%2FjdzdhqLIDRzo2IZHu1b1VQ117GUPyBaE8FI5oU0VyM6IiTQCrMGq3yI9iwVagA79L1eNvBJTCEarBZnXH8B7ZUFMmvzmW1bB%2FcNrnCPtzRmvRdddDlboTufM0cD6b4EvvX5MxQ%2FKUWR9VrkJI0urgrsPWDnTsVCzmJlGHQcLf9%2F3sGozXEzV2vKE%2Be%2FtBRUxE9Lu%2Bef6eBKJGCVXGibUigtJKSZiXhaH2WGUHrOVzWj1Sn25phvCogBHl0qoQQagojlDeppEfcvPmaxle3LKw3dNuFgjmj5ASBalXalqOKJvi3mb1QY0Uv3is6dBaZ7qYkOHNlPA6KJnkXfKu9GzylGEEB0W6XuxO%2FigYo9yXpApEDYF6xuB6H6KSYPQwD%2B5HkABxlFsjo2%2B92XdxKlvlDQ%2FVOX4%2FKVK6FmSGOTHsY5kl%2B%2Fs39B4h4l3ZWOF%2FTUrqprznRd23VMhfrLdhSI8Fjq%2FojS84b1x6TL0f7rYDlCUmd8rptugxHhhMrepH4vTwewrEKoueb3n6rH5IMr4KxMm0fHPiTxs0R7cOMTH%2BOHCnwO0yDUoD7qNfApu1MylVsjsqXfiN%2FnWynbpoGdL5ngX55o7Lgd5YemtZDsRGowzKCyzgY6pgG09YjPLm%2FQLyF%2By9OP7NtHunnxGYDUvxrA0wp6HgH0OB7IePgN9ARU%2BccYi1AQJIJS85mUX%2BwFMbrn1gwy4q37FLNbj0gAxqKAOmIEA7EVx35TIBcBqdYsRarXtJXhzZcMBfr4pB5JyBQsGehv34SUR6gftvn1%2BHuxNuvER4l%2Foj3zHWBWIyq3EsNqAxaKStQOb4pjWBSJ3MIXtC%2B5tGMptvCTaEoy&X-Amz-Signature=d73b630a430b8b6d082043fa9c891bfa43190cc2e911dcec78a9b35277299c13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


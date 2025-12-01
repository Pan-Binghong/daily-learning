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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LUQY2KW%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDIQjYJ3XF5v5oRHVO5Kxvk1jNtH%2FFLJZQ2KEoYxRuHEgIhAJEAZ91GHB%2FetYJpNldM%2F9tH5J06luqu6sGUuOwdnN1WKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjKA%2FkEjvi2s5WvyEq3AOBuQElyGtYcAqt6yylugCerwbxQjV1327T1QytE4%2FlmZTXyzR%2BLyefHz8QPELTVZgYQ8rup94nvnWqUTmEdkBU3vu9SMvi8SF1NJO3wvdUlmUCacEH%2FN%2FjvsAqi0zmJ2nM4crvgFE2GwFoRlycqMsToQQ7l2mq2qJG0NTtco6iHkxrsWpDXWnkwqjb1eo5ojQZ9rm%2BO8cBGLR3D%2BSdWmc9iQtda44JCw1SSBnSQ3OhZ%2FFY17kcW7kQ9ypjXCkauws1Ltbu7gIxTRCGYW8izBltmaKh%2BnfSH6wdMJRnMPCdNgkD6%2FUBxvcahnv2Q%2BZBrqR7m4a8rhbJrg9BnBcZ4Rpt5ZCzrlfa5QmCBNH%2B%2B9L6vh6N9uae2xY2jmjQh9lFF9%2FO%2FZIcN7SXY86EmnRWqP0P8Y56Q3wiqt3%2FdQyRsC5nvFE7tRXySYEgkMa88L3olN1qqFLW5iH9nM3loV1LiATkkFBBr5elUb7Zfl%2BvineSH%2FW83vjRNJK%2BB4b%2BcefSQacwU%2BUpT9FDG96ifkFIKuIgdzkOpMs%2F9Apl%2BYJSVEZ9Q4AhOsPftTTuaAU22jkvtnVDjwaE8T5LE1TlneIc%2FQFg7qTsd3KBIgTWmrHCZkYoH5d50oBV5r9nGcZ0jTCw%2FLLJBjqkAZ9PwgGJj4Rre00GoG0hC8DdD3BnYNeXjKvmos19NLUunRGqJaWEIOcgcRDIag1NgOl%2FIDb89eQHmQTY2XWFZ0QFY3KCenu%2FKCFVOf7rpHGSVgB4qPIi6hENyoWI2vAvy4FQjbIhw7nh2DiaS1IxP3HLA5Lv4FFcbbXt85WWsYCPqN9jKFDFhzQviost595c4DPbXDeYAtK%2BYa%2B%2FaMo3zt9YNpHu&X-Amz-Signature=df3813cdfe0f17e47e9e700067f846de37c20c4833902f89e9330d6d2e3809bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


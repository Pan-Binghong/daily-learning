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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCX34CLY%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFjRjj5NGQd%2FwBv5QUtfPTUdyl8mCL3PaEhRY5MPZvUZAiBrYgi4TPQOX11uCLapTNb%2BMHjbM3rrx%2FzrGWVFRtIyUCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMj5gNiSbciebIIfIFKtwDbOvHItkcHPX9Y5xVWH8R9b%2BSQ78MwpNbDW6gFKrDodKAB9VizLNOjO8efKfRWN%2F1oNOZ89bwybuGeMpPzkYKIVSx49fbwcIssDOo6vc6u2QCAoUOH%2BeiXt%2BskifBa5qBqFSmMBnFbKU82laxg1ecETNzTuQFtoDwUV3rp7rSlHaH5RdZG9KFvtbpRoteeHRCOUr%2F7Ucu%2FeNEpZim4I%2BSWd6cw2m2m7S%2B2c0sW4Y64tAtcyfzzpK9CAijmx4NSW0bF4WwqLXRGgspwZCdX6Us2pI2A4U%2B0SH7zubwPK%2B2c4aU7OeLqa4bmq2JN2nbOstSoGw5k8glfqPbqgr5m7LvDj3I0ELVTKEPItQYc2FCGJ6IounJQBDfd9R08mPJR4LDSv8IzEQVB8W1uYrITq5CZWW%2BeH4efLSpAwnxMGlkPWaQwm%2FCeVcTtBxwu2NMcAY4ythCTQNjJRo1pJkXGSsnVZrwieIPGiPLv4VCalJUfqfD1lHj5C7Mfdgd3JoNNHn3YHR424E2co2nPn9Fh%2FcwAUDXUUMurv2617izmNjg6GrsNA75jVvGcX%2BTZmlJpvm1buYQfLLvvzPl3EYNeU0lgkXE9iAG28d%2B7AmTao0QgtSRZrlhdZld%2FmY9H2AwsqaNzgY6pgHByDmzMB2dRsJJMcVHGTQUvmifMHvrQBsNf%2B55UUMM9OxKCN8X3NGIUjmxDEo9k2WyelraQcRfBeayriv1Hxia7Ry7WEIayQ9x3PQkqJDWAB%2B1pggJqjS8ARtNC1%2FnlAFd8hzWG0pgoxzZ60apwm7xplJ8mjhABQ7Q3JfPEDN5%2FgC4rBtgbcqVkrfXJO6O%2BG5N3LFPXa3FRCPBrYovldxe3KYujEZ7&X-Amz-Signature=bb722b062bb9c2a79ad583e94dcf31dd278b210059ba2161ddbb1da5ceecc237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


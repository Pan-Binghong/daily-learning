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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BPQJXL5%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCkfun7YAUB%2BhgIjp0Hs4L0CSy5thrKngKSmJZ2wn3eJQIhAP%2FRjS2OK1A6ui%2Bbv0O8YgWLQrGmh8nHp%2FuZiq9yS0WJKv8DCBsQABoMNjM3NDIzMTgzODA1Igz4qM%2BghCbbWaFtmf8q3AOzT9xWXLauEKPxBdT3SpxF7gJ%2B5zkvJtWzxfVojFxLqdCEYFEXBi3%2BqU9w0imG2wTgQ0MxCk9ZE8EGw%2BUJSFzf4qURDpGg1snpnNpUT0CaFFSVKYeU07NgsS%2B6bmUxtzKrq52hd1ZFVAhP4frDdwI5gotauKUIyw9623bxiGtdHjowTVofDpkSugozvDyjs41mGU4ll3Q9X%2BNl1iGV%2FTazN9vhztPm9htw6531LfzyjoM8CiFDZK%2BKG5leuXlUzV8Da%2FcgXy0rUXbnhn%2FaEIRzYnYd7zFzyoY22Kvu8VhlONc8sK%2FVV954uQw4CWR%2FvqglZYuO5xKn6cITrSGJrsWu%2Bnni16iuRj67ChhlcyYqZRG7AwEo5Q%2BUO2e%2FKmcnG%2BNrZydARsZUleDlz4XzPcvJ5OTipCrRBnQAhj46j%2F2BsrghWh3WRjVC4eahWEwUYPrY6TroaD0jh88ZlnX%2FM347hlhw72DCPCzyQBj%2FTN2yexvveUfJ2UPc4zI5agExcfMXuYfoZSPcfLIpwX8AhJZOWkmzzGCxv0bjBO1%2Ba6zkXofKIFYeOdeSv3HuwIjt0%2FRam48d%2BCl%2FZqNJBxdDXblT9gfrPJ66GqnxEDIzMIya8sZlx1Hp2SmSaEonPDCyvoTJBjqkASWvJRXvdHF08n9V0lpwqBumAHxf92RNSPHgryLvfV0aMRtYd8ukKplWaWwR9Vr5%2F3AVuzXlZhqC2sWsfuw1Z3ItyL9OoSBOHG44Szvbj4jQNZRESzpxsDsfJf1UtvvT0llOQ8Wjafs%2FEo6FtnMEw%2B9tinB3Pf2tXn10RyVlkrxERF%2FsguajJekIPhMJON%2FoZ09l1vTk6wgAzRiKOvVpaz3Du4I4&X-Amz-Signature=01661945167b42fb853bc35d3f2891d02ed6dc32be068df57c4609bc2c364ff8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


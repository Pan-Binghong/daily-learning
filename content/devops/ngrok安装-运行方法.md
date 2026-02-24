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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZP2OYIV%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQCgURnZX7E7T6NwVq4i8xsOw9g0fRixAG2UhPHumeDLZgIgQVtRQD1LMuW7xIr9t%2FIf1yWRM2EySkDjgHzDRC8eTUUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKYxbH9uY3hEGeEGASrcA2dvMD9cXmAaJuIV6Nwa2Fvev8ax8DcbJyiab9W8Oqajd%2BCalv0JVIV7S4v%2Fa%2BE0QihmvM2XEMV6oYlsgPZwvPlZlUwKCIazgq0xi%2BK4JK%2BS9HrnklbEC%2FTdzdBTZ5CWGmkCYGBmYMnzquo1k2yFh9%2B1WRCHePlHPt4ozVygYyBAW8240ZB0yBlgMboubQWYAoONUAp4FgJgqxawAl93guFq1les9QaJb6F7Jngp110QJvdzjVz0IP%2BGo2uI%2BB%2FwrUXAKa4AIWteANZB1xtTRISCSpboJnL6zci9QWkwIm6S5QKtx3raTMsoMMnI9JizyuW9H7ZKxYp10PSNY6J%2B4B8VwgDRqEfSVShyieAUuPv1Fc02R95HILyp4QyecifSVu1Zh1q5tfYcrjChN%2BPoVfH1aiCpB0hHm9JdhyPMIUHwdHOnuenFvFPZPSxsSdaSZRpuzIDdOu79O7IIEQt5IW6kM34np0a4%2F7R5TvKyCgxBl88f0cu8me68k5PpRBL42%2B6luIS%2B%2FzUsWTWYC%2FlB1PfBTx1QMRJ67Q18YM2ntH4sjy9eBjLKJeOxIp9nMgubDbBKYYdYbNU6dzYZPbzd5OQitgho3zg3jTQNgz8dgRHLEd4YTRQB8aj413dwMIS19MwGOqUBYNf%2BuaEYZjxaiwp8%2FWTelbvYbSer4o%2FIUvditDwpuy1XASLst8qY9zzWqpE00XXNaifLtJV9VPcr0TJfp3vtdA9%2BOALhLIifIAo1kp2xcZug71jDKXrc6%2BC2Wk2fsMB77fUuBdzuslgw9i0k6vV0RwcjQ7zRa36zZsdrq3EM0G%2BW6mYx8ImjT3zvqE1H3e3hYoFxD%2F%2Fo7iHSX3mHCCa4aaSNi%2BfH&X-Amz-Signature=588580debf96acbc1f9348a39d7a49133b7ddcd0ddf2e8253c5f5dcf25d59d31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


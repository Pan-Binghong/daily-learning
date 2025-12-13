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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQSYYSIQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQCvhEl%2B1voUtAT74HbVdekFqkK0gnXIdczYyNXVfMlUGQIhAJE9S5pRZEmSDzum%2B9FuTYW%2B5haU0nAvxKXkyPRtR4V%2FKv8DCBMQABoMNjM3NDIzMTgzODA1IgzvU1YjJgo%2BsX4sUN0q3APkqdETHHHzkpdPnIyIHCguKNCGBk1ahsN%2Bkgha7HxS%2B7k8zho5E8MYK9DaLT%2BBglZarNlSU2nXcuFoISlvDy%2BQoISA0xMCRzyqgqPruRzyu79GIlLEQEA6tTYk09d8tKKjUv5yrxniw3K7zzVt6FML0a83KstmbS89ve0m8RKT2BVFvNi5B6qAlLJjGmJRZmz4t5bUk%2FCEhcTo5IH7Q8xkHUQ783JUmhyavhOwjMJ1bB32f5%2FMseW7UE6ilrfpPfrNgSdBBa93e2bTfJUZo1IleWMrbWbWbkTADNaGd7wdOOEu7H31tD4APTg%2FNhlUA3bWS2OIo8ED53RNQHGgJcqoxcSkx4frrcZMzHp9bT2oVx83BgGC6k78O%2FuHWbtEuvPojS1l67squqpYjw2q49iQ62lPjPKQrQFPwxvw3tjwBH%2BeeuwwG%2Brjtw6PGXWCXYYaXxjh9HOeYsj5s9BFywk53EzHB7xuKOtvMx03hT1nPS5%2F4n%2FRso%2BswfXjHdTTbjKVOqjluLtZLIYbPUUYDxCvMb7C0JBuVqKRDkCx2B1%2F7zR84UK8YckAyu%2B4CQ7ZWPlYvAjU9WjGSbOe6BlrnUpH1yL7DuyZzUmTPgDkgcpCDxlzoEbFiz0FE52z7TDhjPPJBjqkAXx%2BvfXkhjY38Bphz3eBCEUo65jmLQ%2BqRqLdMRgu1st41Erkc505GGNJC5Izt86WuMN7YSa0SJUqB2oJqyb0za7PdbNyxiV2Hut2%2B8i20bmHPXP36j%2BJgcjsUE4hY25djPTPAS8gLBTK2b8QF%2FVo7AC%2BkPiIce%2FpUowgEiXkZzAidoziX2E2ZpiAh0avuIW4HX0leJiBbYao8on8PXpnfn3eY6j7&X-Amz-Signature=f1b961c3800bf034b24bd759277aa7e16fe612e0d6df35640c556561325dc7b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L3JIV6E%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGxXblCenMfR2afxNB7cCqrA0ANSErxJh0Tdw8DGZ5W4AiEA1xx%2FJUhM6oeH8sYfjqDrOd%2BRvcE591ltxb4SQTcuMYEqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdC7ZJPROTP%2BltHbircA6l%2FYPRT5NLwvgkRdZK%2FRJsE3RH%2F8%2BhZYLa7wuvn1yKRi%2FjGldO2G1FMORL4571G9VCTflvPKnCh4574Mw0fYOcb6CI1SZ%2B7aqo2%2BRshqTNJKncc8EWMv6v0%2FTQpAYEW%2BIvquDnnnVN67AtDEd07azW%2B6KZpKGRHpnGSrcHTy1O%2FW%2BDeklV32IgbUfMXFOCrZRYgqe24cHx4BM%2FnNwemffQXQXP5zU5SoWbK8THhuUqVS26k6LtZjlx8ii5kL5Kh7jWtGYYYu23w1jyf%2Bq1dAnl3ebDgMFjyODi6dks1kimw0ZEVjXMySZSO4ulBK%2Bp8VySBegto%2F9X6uFzmJelfcTGUVLdWMvLtRH2%2BtRYkzH0N5hA%2BFchVExvcT8q%2B2Z5eB7v%2F1E3%2F4wZo7bZVFc7gqvKJnKB%2BucsoiaWghBt6XUpubCsYjNf5Pg9mYfj7bQ2exeSo6BNT6rY86bG72Ob2K0xrk%2FFRHeeFNwEgTE25LPOb62Tu4SwlDeqUMuD%2FYnOU2Sz7u7qHaXMRjagAkVxvC5WfitTi%2BU76R7mKdkewrEC4anK7nu6xJX1Mzgee5DDwhVvB7IiIX26sSq6HPvElhUe08DjFWKK4GTore8agrTKod%2BiZMVNzPOxImGtPMLqI184GOqUB7n6Jjmyh7SkOyjvfNSXrBWnaiv%2BbcZf694%2Bapt0pMmlx%2FqvfEbW8yxQwjGWLQGzYOb%2FnsuAjOUTOKrrjsAlkVXIrmIrjw9JuADfLeJFaspJlJ1EM5tEb05vNMraYbs9sbKeUlA5zTx6GL4hsPa%2BT5Uw6GR10Y75uCPryq9D7pAOWv6CdyeUGZrIOgOj9hOiit8tT%2FmWlMMlqORkMoFAeZ4cPb9ZP&X-Amz-Signature=6e0cdcbb78069577fb159ea34f43dd3433441c5fa05ac26b6fb7b2173209456e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


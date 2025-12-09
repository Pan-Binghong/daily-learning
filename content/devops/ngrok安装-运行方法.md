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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VE3SPZH%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyLl3%2B%2BRAiqH2EgTdUt8i5rXyc%2F7VW30fNJmjYBZs2pwIgFeXuxV6pERtP04C2QO4hV5C1BbFGs%2BUYxAElF0yW3GwqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDg5TYeLWjA4AGqtCircAxhclSkEVsX9kCZBFdKjZbVeU9FEIogrzEZlATGIlW4MBJrTaYSodr4SaKNCsmiXrt07NvBcWke%2FfiyAAcPMVV5qGmWC8QWQEPdPJwVOweJJaH5aE1NXeTrs6zKKRusW3WBJYZF1AN4Mt5eWukNqjgwv5Ec4F4%2BU2e0aDLYFQLL5BTN08odawgewn2fqe7oIJiIN5gE6C6gWVWF864yUUVUhqhbicw%2F22%2BdhEl7231pd0w6urPVCmyyTCF%2Bchk0HZuyTfLw3KsezCeqn4%2Fi7c370aa9X7suLto7P4YjCRcOyMi7K6LajhD0hzsMifCR%2BJNZtomZw4wMr%2BCAukF1iHJZem7excwvb0SK13mFJCL33Re5uhNT4dg%2BeiBlBKQ6HAQ5plPCh3GVcd%2BiY3QFlgm8sMrb9kPZjP1bOjChTsXrlpx4b%2BPESmEIbaqgMGGtEAMyJypFfLyU8GEBhU2J9s6Ob5r9Ip650E5ElJHD0u8Ga%2F7UgR4zI3B0COt%2Fse34dL2xkNVpHBoHe29WEKn4HA%2BK5gG64S5SjzKFgGVrC%2F2ToOa%2BzQcF3oB%2FLeFsSECSIOVWst6u%2BtdE%2BqOk5HHqKwswmqIIMNQUV38yx3YmxmkZBiuv5%2Bp38oVnZWaMjMPCO3skGOqUBm7qjgJA8Gwu8CC1zfRuj3N9omdOMgakpJuhENB8FieqMNTvs7NnxUxrIjThvDApVpL5e9kLWKrLt3kOwkJL2bGx60Qy5RzmysKBwMumXXwudyaXu0%2Fq9ep9nVPzCHMiPVyJ3YZthWD2N3OgrDvYuJL9tyXNArATBc%2BjzVj%2Bwowcqu%2FN2g%2BsVKEpBOlQAcpP2VyBNRQOlJaR2rDMEUs%2Bv8ElwRd8w&X-Amz-Signature=c9085f00689d8143131529a70d095215fb74ca3028eaf0b58e558391599a1545&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


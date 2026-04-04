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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFIYG75R%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYtKg5Y%2FZRlPHnmWV7WFinZJTlWnf2jHZcxHoJ6VbVkQIgAIxUVRnwzCc%2FFQ1pq9gKYl5uAds%2FXJAxGCxrwMdp4QEqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmRnvsHbRGOoKJhJCrcA2czHwrZkwWqYkk54oe7PBzkijNTAUTolqKbXY2jCZ59vZqH4w5oJKDyzDT6JIH3X4NAcLwsYjARZOX1RZmEbqVAKGIa%2FLrL6VNcbdtowiRZ%2FdDSdQ54IUkrtQNSLBbZmuIFHdRDUCazcuZ4tCRzh1xK7GfnDFVW7W8SMUeSVJ87p9XnzHnEMkZgvts4bTAiuk0Ex65O4fn8To1hWmLtnSkSeGVsQVDDWC717g4Sm1KlFSXi0OzElLiLit7CNp9Tr67oXB44r61hwNKhaG7Zo%2FzQR4OfhoiGHCrY4pnckI0oc9JAp0F9dXDo2G%2BfdksFtfzGwG70%2Frxx7dCGcTKX9LUwz0MjzWtVFWaT3BnEII4p4WNwLdRIFlcd2SxSRxDIJLqda3QgSOc7MQ5gxiJYfReY2CEwEbtuzDpO%2Bo4FxsjB%2F8eZq1MuNPQTiAoaHXsZV3lXP0GpdjWLm%2FUqH5clhevth%2BM9feNr3axu8b1IKXwNgTKncSOFjsivHPvPhsyoiC%2Bvd2xJ0d8zpFQ096B7Yh6pLhbdr2jc5SRLBePFR7ZR6ylDsbeXHjJvX4jkxBw1dAm7lxVzM%2FSlmq0koOXkKLfNrVsA5j1sfL6%2FXNaS8w%2F7ijAQR6cZE1%2FjrSLJMLXkwc4GOqUBVfRSozXU%2FkPT%2BLMqtzce%2Fv%2FTdwT7fyUevBxKy8fbQjt3JlPvubrQKk61%2BS5MsYid%2BvxLkQoeSVh4%2BTaqALehTXkRTwqmXCdKvTE2vTZdTTaE8GtE2lZdziiLQ%2BPCMrCa%2FTSwAZ8jaRO7A8Coylo6mZB8IZV3X%2BwGV6CUqCqFRgy7xWs2LRIAT4uC9adT11nc9qvzk7XoO1oDjO%2BdCtxQy50h8L7t&X-Amz-Signature=582b106dd17b1e99cbb86823ab7e2dc99f03b24f4f818488d47aebb384b2f784&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIWIGWL%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBrlAUTjtxXf8%2BGv6ElNKOsnKpZJFvpKE8yVBuJYi6yNAiEAskRx6DzF9rky1cDXV01G75x8zqrqWV4kk9PUuKmcUAIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLVLasU8ee6WNcInCrcA14FuCUUkW%2Fv6lgDwaW65drrUT4akBwg4YjZh4PPs%2Bd%2BygMrvVUpbCCbyiKqurOO6ThcYEPDsmEL4nsvoUZooRErIUzH8dBwuUOuO3y1ZUsEGUK0szlGb0rd6bJVtaBwvAdnbSsmYuD4PLnC0i2ZveKGWH%2FlsnCPElosfLg4iskyZ3ztj86MZvDd0HOtY%2FK%2BL%2FPImwRbGTeHDpz7cKQ%2F9q7imxh7bOabqRGB9msI4Q%2BXqjiVvIgJ7%2BHP3F5bQHK6oIqXTNoHwxfqYlKBsuzw%2B5DLEVRz38ZcKyp%2BywSxFbLPxL8vcIvR%2B0wW6A9B3M%2BXwvn5hqw72zFIGrKSiUJ7JcHJk4lqPzMS%2FzcRaBbKSVrlhO%2BFh20YjTg410seN3r5jTbxjdpKRb1hmnHrSAh8qZV6%2BqDpwWLxSud5XS4E8whnD2AEcca%2FbZOm5QZzkqLsmPF0s6aD0SEx9rlnQ0Jt4xZ273eXjJeeEa908TMlYymp6yOUVv%2BXRu6%2F3f454lOlnu3A52OFqQLc9UW7LQznBTm5clJ3lLoHdg%2BzecxmqoQ0ITh%2FB59olgdU8bCvm9wdhabGhKw2zEJESV9VTTcCNlEzTXDIv0TcOFP1grK%2FhSxU841Q8Tj7LQOZqxE8MI2Urs0GOqUBfsuVC4zeq7VUxl7OxTMn%2B3TniVJG6sTDHovms%2FKB2KWnD9cDIzoOGJkNiV4rz%2FRS2RmLFPIB4wJH5A6WriNRXlR5Ujyts9E82YqTNm2GQUpWBUSzEKUAZCZ0CDlwe3Vuj%2BXFiZYlSN2XK88Y7Ugnf%2BLsD0Vz3sGpUHkXjT%2F1hQbsvtht3%2BvIAenVitO5pcJzGAlMGS25O3pBu9%2BI9FFH6GcDjByj&X-Amz-Signature=4bf33046eb083f5304a7abedff5ce32025edef3230c09f6c1b752bd3110b206e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZBLFC2A%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHRbXkrj3d2dQgP74rbVJ%2BcU0RZjXUD0PwmyVtpi2r7xAiEA0gaM6uo4CTULmgI%2BivsycUzqiWDjf62sFcf%2Bt3JP0uUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDMiYt%2F9s9xCzkOIRkircA6ehzVcXSoCC1H9Bm2c24zeaq0yAqHkEfTySeJCTPs72p7PZSnk5eVAEe0QtcnRyWKO63yUwSwg01AaLvIs3QYjicTLByaYZnSOjRtKJkCFRsVPjBMWN7nhX%2FGRxmGh0MsTl%2Ft5IMeOhL9NqBYdTPZ%2FJItWmNfX1a4TvCDtO1hsRSTW3pPZQqFyXSzYzFRWOz6K3lUCiYTzY%2BQC9j8o327gCVuUdFPLpe2YTTYaKmhkpjPzZRZCXlV%2BjCbUhNjCPXAO3cLhBdjaZE7VF44RVvwwxyz2d0yVWFMx%2FiwnrChWJnk09TlH6QTSBkoueMO4sJ5TItj1SeALE%2Bo4bEMJM%2BkZGJxQGF1lCV5%2FfLnpBB%2FgzVNoP29swZ%2FYtjmlxQzZUX4KVfDAGgpW79tGi6YyDtXBehh9%2FndXGVOAClSroHlw%2FCxNh11WBIQGhQfl96XEQHRlexLO%2Bs%2BwTCghRcQJm8ZTytgYRfymJEHJzWZAqE0ywyJPROIeAbR2%2FSiiQVjyEVE6oPFMkaHAPfxl6OyuFobkY5TCOUnhAUGstzBHka0OOQTcOj5rDFnn3iD4UMTuDfXA2T3ueVB9ApcZuFdi8rTvE1X4QXAJkwEoj4M%2FkqmzAllfZg%2BfrPJv7AW%2BaMK2%2BysgGOqUBsaFle271wDoSWlodxXZ8Bb%2Bd4UWBqJOX6f0sRWKbvJi6lPTPVPjxuEciJN9nDcHnkD8I2lWyNbkA2Zb6OQCsQ0or7sZOCyMc8U5RIXY5hcAfEBmuraSMCke9VFz78H1A4mKpewnrO0Yxq27hbQ7UiIitYOpT%2B6yka6CswRUb3zK3iMO4zPhx4hP89mGnE394lrb%2Bdp8PGN3uikvPVsXyPJbM8j57&X-Amz-Signature=8664e5d3e81b257d929fb70c5cab1a9ceebc7ba90d8c5105d6a9591611bf58fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


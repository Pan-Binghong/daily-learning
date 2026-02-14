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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HIIE5HX%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQDhNUFDN8vhFTmBV6QPzFg7fcLqg%2FCcwuz4eunGWKiMMwIgXATGnWwTk0zE6NTcA9vMalDsK1Z52rEJ9YUGFOvZbusqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGi%2FvYIX92jFuZ8saircA1DsWdCTuneSzErl5c9VvfKh6RigsjrdblGGS6vBSNStUu7gJuGsf9zLNzVoCsWYu%2BchVNzdRmQJLxIDMO238sYeVdiQ4uTrjo3HDZA%2B3OdODKVMCqIiLfuWkFn1aM3frjsY76buYbDLg0KJV12XruRpH7zt5MhtoOrWt0saSeE0JZw0OzWWlHPO0zv0mMZ%2FqFssj7CAQFOUc0UBf9i%2FPNQ92Y99I3lS47xh%2F%2Fat0ydipAGrS575aheVB2JnZ37RcjdAsDAs2Wka8YdP%2B%2F1Ozyh%2FnwafYvOPc1oyBET8ZGZqnz3P9DLdBItZsxcyz0so3ejBx4WD%2FhSop67wmiF7FPHqkAJi8H4sv1hxvPKjr5Eq3cGTwy9NDEJLLbcX%2BvPWIjIQUswcw4bHOpJF%2B7nTKtUuabgm1ObHm5E0xGWlEqsrO3sJZd08MWMOptmAOxoUeDW8WU%2F1K4%2Fz46dn4%2FUWOq16MCUvM4D1XuRYJ2KyNO4YNy4OAofwR0vyqs7%2BGfltVAtAlOh4VJZwk3F24M21%2BgFRTkA1%2FH3lzuvAl0Q7WoyE9PP6We3zf%2Bn5w8gD0J8Ogbt5YjOVFEKcTCVdf7YNlYcLl3Mey2ylxMLlazoCTxwzXB3b1Dvr61%2BrNHB2MLvAv8wGOqUBnNJVrp449gWzGoXHmAy3Wf%2Bw9M%2FHRDVNLNHUXXLn94FB%2BUhsPOifNg7VNEbVIED4k02mdwHF5m%2BDx9GipV9foKdHwa24KugDw83BI3JSGcnmgUGb%2F3i5HTkUZ2Wy6ck3Zm3x8JcENtqOEC4AQ6Jxe0WBFlWQMC54EmSj2EkWSUh4%2BUNf8oHtxpWq1qK%2BWgT0JWxyXZ7ZmRZnBtF9xNnlGBayTtlR&X-Amz-Signature=5d0c6694fd75c93a4a4d5f94de68e09b079f893e51563b62fbc6ecf4e8ab7b29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


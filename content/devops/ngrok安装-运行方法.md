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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SK22VKI6%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5gIgezXpF9e7Jgcaj2uAKDAUvOlQBMF%2BPCfDggJQHqwIgGyMBvvEo5QMwJnm%2Fs2LKbDgIqcq2G9ishIjlHNhK1MUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB499J%2BU2jQCAFRaeyrcA38xX45yRlpYGXXc8LQ5UXGmSHv95YX3XrC%2FqfGZ9L45WHIhATfGBTUntvfzBhrhKu7EE8lLt9uNMDTNqGVTtJgpSVTTpG%2FavP%2FsYW%2FGCyxR0ZMsRf8pZ1E%2F9axqFWbKO8YeqXHWWYxAJWXMUel8YQo5OjgoUR8A3Yt%2B2cMK4ellZHBmaMfUiyYsoKjm%2B8PjTH2LZWVbV6IrKWNJTY%2FVA%2Fdo587g24jV86GR3RBLlvQyFSBfzM1t7YChhd8dOfY2ufDuY10vl6696bm7WxCqgmogktdgXik7cdzx5%2Fkkofyd0OXrWS6Io1EGra1IKx7fmntirUTHndygnfPRMrAlIGbmkMdB6r1q5yqCK180hbXy6a9Xl5DqKn99jKoEDNk2FtPoZoireb5wB35FD%2F%2Fttk9xa3UWlErfQ2IydUd9UUJkbeodWVHLfVkbZF9ClFr%2FLJNKJXOpXqidP7FBgxy4bjkWy%2FhRG0K%2BQZ1DYcvaCvXfhH86eGkarGdv6DRDgCwcVQXNCso9xV3ujemYKw3YjzveNb3XKSdTrDod1uQRo1G99Xk0uo2lTiNFTCPu6PD8RUaQG9vvi8enecnakaSv7ajoFTV1HOA0EwwUiogzxaWQaF%2FEEwhvp3inRHqyMMrxr8gGOqUB6ncGPzoOzz63k4VfbV0ftwKSnFxGwkXBDgUiv0Z44k%2BFqBiHUie00HagT9Dj8Ks%2BO6l5HA5ZujA9pGb5XgiaWADeeFjxyGMnv2yqRi%2FI%2FGLgcqT7ww57kV3g%2FOGmfdkFa9wNX1adkWbLFKeO9RIT1YEAvo4vGEivEtT0dqTvf5o8JEZcQajkV3DTYEGVGd0RzPecSMzrDIVk3sK85nOfU%2BPRwfBN&X-Amz-Signature=bca850c315044eb709c4f5ba8d0cc0f043f50eb46b903f32418fdea1201f9d8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


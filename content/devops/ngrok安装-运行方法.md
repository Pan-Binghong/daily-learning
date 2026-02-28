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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666T53WS3C%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxP4Sg9q%2B%2BNILhpUtzlwrsK1mnNmgtJnlDk%2Bj0sgV6qQIhAO9bexBm93OsA6M9vKvPcpMc5jDi3ijnI3rCEgbotYwFKv8DCEsQABoMNjM3NDIzMTgzODA1IgxdGE5Mer6Oxs%2Ff84wq3ANIidJistgIJd5ez%2F92a%2FJqTR8VKf%2FCjFHWhHYX8L4cbuPdm7kejQni9bP9haMLnZPehT2g2uCNRgipV4jasamcm5rDx8BI5rXyQLbzI%2FTFGgLgXosgmh8gJUXFAeYtssq0FLr1dPifzWvY%2BbT0y2VkQeonu9NDgvNPUgUhHeiLPc2KSKzrJSZEu%2F0YvbNkxDQcobmSM31iE8xv4l%2FYu6el0HCw8E1Fis3ZYZ84%2BsMoupQBSHKMTejc6Cl6NSIcGcD7XPX9a2waIzSSmjWIbQ%2B9sltnGM4K99VWI4Sg%2B%2BMLvtW3HfKCFFeVY%2Fs1YsoB4Ve%2FRoJTjRTMGYVyxAOUJ%2FA3G8eCFkOI1zRz82piCZpWClRNxwtCn0TmBlMyqa48zzo3AdkEyMp0Br0uazMqiMcc2ILjbL0jwQSHwEVMbwQNEswbsVi5Bkd9WgGNTmiydau8rl91WEhIZECTKuAWUl3iy%2ByQOCotH8BCa%2BPsNT65dNZs06ujS1K7Cl7kaUhf5vhICPYftQ%2BKv1b9TU%2F5veYbHoUYhzHgbBPKX5F4A9kWDqNNFv1LDZV%2FE2Q7xEKsdf3eWO4JpI3vbT75lBZZDmk8xb5ecVWpYO96cnLTIZB3fTlG2dKFZqxXgQ0tVjCalonNBjqkATK4cFJrNg2DF%2Fzw5e5xlWyiejFs44esY%2BCSYl%2BKKkVUwwDucSGFhXps5xhSykoxl9%2BU6Y5gbz5%2F%2BC8Sz%2BT2oKzP5hGp99g4KNbxFbfUMm3jkK34XLQO%2F%2F3rzKT1NduZVsO%2BwM7JQNobYQcABo0enyJnN5vg3gnv5iuvuU1aE1mTSLRiT8t6nBJRNzQueVIGMTz8KYdIiGCTeF8nfLoGlzUYYola&X-Amz-Signature=4a479dd51ae0a3c684ec19eaee95ac9a555eacb777aa8de42b6b302bc2866f55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


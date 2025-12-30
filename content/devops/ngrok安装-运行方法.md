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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XYK3SW2%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE6VYWI6xn4UxRvj%2BDYyFsEfklw6UvM%2FPK4UFmK8X2CVAiEA%2F2Z3jfKrg7y53pPA%2FZiatrVlgaBkXJg8ncgmN0lsjWUqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE5kZO0jG5uEkOb87CrcA0%2B28AZuanFiB7CfF1loRPRb5N4jWO4I3f4yz4BD9Eh%2FreV3YA0bwzPmV7UL%2FFofvmwP0FmtweswJ3oPPngZPrHcDOGCtfhd%2BxYDcJRbaipkVd%2F44oPWJAHD2dBu46CMAcoxkRiYuO0JxUOdaresgI799shbONBcMxFr1ttp1c8WEmN0jV7HQH%2F1k6FqPDZCDnJL%2FR7lWVoQzhLTikmykPO2xUPuOxXsoC%2FWe%2BJ%2Bj2WSgyMlM84FPSlb06XnVW94RThbuMwI8ss3UGVwwIlb3UGPf%2FxIs5Ba2Pk4Zg6p8b4QlCo1Tn%2F3Maj4io9sVUKZMjMuaAdCq32AlEdD5wz1%2B1EFNQMcdTmPCAwhE9VQXwkiWKrnbO74XtpyeC2BOFNn8xP9EwhxhHRB5lJF%2BScC%2BYCk%2FMqHZL%2FJeZ155Vu7TVEG1HhJFvxLBAiMXz%2Busy6YGfPGVin14nzYbGoCKdWS60brxXW6HnVjq8J2SJo%2BfrwRs3lQwwdHzljv1ZBFpl02wmrPlx37eaRW%2FmEnVSC4WtPQ7NayGt3tHmlqE3Zgd%2BNxYtOy3sqVkR8QLCkMaib2l9EYaIYzWux4hGK7LWGB2NJ843Ja1NzT3Bz0rmHR%2FquMoiU1bkTMo%2F6E1Mi9MNzty8oGOqUBm7iQsHwCxcHsMGMwzhj492gxxVWX8DdvnAYy4UHDq9nyzKsHdOmk0U%2FIW1kmQxmav%2FgOV7EMGfSS%2FS6uFJeBadFSNxd9e%2FHQlIFoqGncXnWMmFiGWRVIZ5D8ptmwZhzvaaACFnOR%2BQ7NP2ZghSznkNtzgRqmv9TsT8JugjHTUD93vXRcnAZOQaq%2FE5SkBS29Tt6i5qCt%2F91J%2BjzSCTIzHyHNngh%2F&X-Amz-Signature=4505c5064f45191916ce8057f1367080b24f242c8d2bfe3ca1cf111888fd1fc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3PSNJDW%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLaEpr523mVjMzkiami7J3gv46GLF14xDrnL4plMmxQQIhAMu%2BP43MqANZp2vZt%2FtljzLgAvlChzk%2FejAXWUtzu9U6KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBQA6EKFrBBqpYIkcq3AOQ3%2FDxBrPBREwSF%2BYxZa3x51VmI6orROjGgA1B2NzK8qQrubLqKKj%2BeeeS6VPUG9hwzcEc%2Bk05qMqKdDaZrE10FKYRxV1U0bCKaDZ6N7ij7MbzoGXuT8U8ARH%2FtwWP%2BehTMBuOvdVqS2oSRoOQ%2Bvu%2FIk3yD50Ua68zOmXjq6uTMPUWeHpbvh6iKIwzEn%2F4D1nqgEDrl6OD0JIEh5WZi0m47AQH6md3DFsotSFBzZ8ZALc6Q8hCB40iqlJDB4sq%2Bg3xRnb5hliQ26qs1rqui2R%2BEvRubKPFHpZZngxvlBjaOEgBB0rv61ZYTI2eCO4PC85MmCgMeHnWquF8sJkPFVRwvGwMlpv0O8n7G08iJfRTDi%2FiaHQLLEcPVkiFnNm%2BwUV3DfwUNRbFALmcP1hP4oO0b5MUEPGyBWkASPvQjf3Qva78egyzFuqCAb9gtYDC7FglzABQhelRGF0qTS1UDJS1HPiX4vdZpa3qJLdXuDA%2B2gez0pZd8PstZwtS%2F7qpmaT32kDvUGNrf5019O%2F6YGWqtmPGDYPkGF%2BwnxwKjK8NB7SApVd9ZeybfumvTxf8lUBjq%2F1e%2BRrs%2Bd0bwfU%2BGfHktdsi%2Bxtnl8JVNq4pO2TygiSDzW%2BmjfAWSPjsBzCSxYHLBjqkAabyB8h2DN%2FNZLSji3lhrpRmBzfoXdKStpUdkRs07ttzgiFGjit8YslAu7d3kfNoP7tNTCx8XwFf5%2BpSgHVjyq3vr5%2FCxh7aEeCLyWdvulvTl4ZHg5rR3Q6obzyc9fU9JrvkE6AgMQ4xFCQBppR9hp%2Bu0yqfOu12uUilLcL%2FgAgelbupFUtCwDdmOczWcAv2NhI%2FisqgUO%2FOTY50aqbcSNn0eM69&X-Amz-Signature=c050aa981bb178dea14231c5e9ca1514b54547a60a071f92c6f36a13dc98fd0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


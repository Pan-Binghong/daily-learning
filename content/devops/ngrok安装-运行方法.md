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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHBWLOPH%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2Vs6fq%2Bs3ZFxqciBFSvaAme06UVQwE603iSqsymDN1AiEAn%2FlANehGjZjMV4TJ%2B9W%2BOd2cCj4TinenY3ttBeXde10qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3%2BXlysHL3lWWOzVSrcA%2Bah9zAp03EX1y5D2twQUK59rXDyYoT9b92mRf%2BcZeZAOYkxCuXO2jfpg0ucvFuoSVq3G6JJEq7OsDk1GD7ENLNPBIOQ82f5xz7ycolSP0993NjaV21MtsqfQsUSFy6VK2T6dwG7V%2F2mOWs7jrKJbUHq1OJLVlNZ3dnb87hK%2B%2FefS24WJOtdrd96%2FnODPTxXeiOC9nX2wWz6xN1TJccUrBYKDj2btO36UFeWc29Qy2rAPootpCQvdFqmtna7bEKs80W82wrsnjzadNzKyo9MrgI2Z82%2BwA3ZSYnLTQXT4MZSOIgV4%2BH2A9HmGDOOBlLI1rLg7FXU1wndU2MMcwvNER%2F99vedsX8xUj78%2BigxmNBX28naEbl79%2BjqzdXMNaXl%2FnFqfvkK4UlwF0W8w3kjMEfAssgf%2BFhkF2dE0D6VwOcaTAFEAoeGfhqK2%2BMFvBFkr51jqIlpvObkP2DSEYCCYwooHbS4EJMeRSPUKqlYOwcVrQ1pecAiyKRb1D2WPv%2B2kYzT4ETmoGj%2FP81ORyImO%2BvJbKmHuIcJSxKp%2BozjMqX6cl4kWeFYZggclMztxm1ApP7yjJfvsH6QcweTwSIle%2FGhoYoqsOf5w6%2FIrq9%2B6rRph5SH16w9T8WoE0k9MO6fx84GOqUBW0DXXCpQkIUFhyCWpalO%2Bs%2B9rYR%2Ffq47hC%2FSPzuPT8IgMzix1N%2F9O2OOkOj8rWYcEOEkW2A3l7OcVl02YJf%2FXk4Nsw9hxEyoyqwZuGKemUv6g9vQKmf%2FiQMF5H7Ql%2Bp1G5MUR%2F%2FWXAel15bP3lRWxBiOVFt%2BjS7LdFWDcg8QydAZaVU1iLepL68pvwVqAfo%2FKL8HxQYM1uPj2vvwgzUAdCaquHkx&X-Amz-Signature=08a4e2c3dcf4b42fc4f1820b9abf40ce2d4a6bab467a8434fb40b0a3d8bae0db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


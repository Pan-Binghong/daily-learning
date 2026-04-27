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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2SK4Q45%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHE9iXOxGgPRFy1A84BiRdTcQaEnIuthz0M7P60UcsUwIgf1B%2BeEQLQTsI29Pkd3oe%2BWoed%2BBBRftovDBjInXpbAEqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1JaYCctWDbN341ByrcA%2FTRJChA%2B%2FQ6llg1JyUPoqCEKlY3D8GVic7C3HFDvkR76RUaxd0DeM8pNPzq1n1zwnrzFxBYn8NYDj3cLt9BcSX9Hf48achfOD6uJaFtDLbMmjwbQ0ryjDl%2FxUIP3rAzjrIJEnELQi51b6OWD%2FU8PLvLEeyhQjFNqNrBD3T%2FVj6mCLq8kpvhczzhlUZL3y4ZqS2rPARN4DiSRUcXaqxo%2BoCkT76hD6PyRYra8O7do0YdWz8eA62bjpepLucej4q%2Frzo2ckryigHhhByM0bqtS0NAzQobfW1uCJD8a0OU9WPMRdDUS04jczK%2FXtt00FVbLKUUxca%2FMm%2Bv9h2%2FjemBfpvH0AhgYfV91atRtbi9bS9wM8V0QbWVYci1FnpIHQW5PlYlorR6hvdgHHAmMRfUKshungt3rEF%2BVvKZgEte1vU0X6NZIM6muHqFBWz6vcVLUYEYNSjhjMYaxVvbSiKqQ9432r9keBswJqou5%2B9j6un%2F1KkykQPzwF34rRIDmFNWpWTSB%2Bf5I811l%2B3ACYMsnI6yxArfCqLLWVaDo9UG0oO8enbcyuDQIMX8N12mC2sdJPLvdy0e%2FKjhC6SP%2Fe%2BM1Uj5gZGVEoMSuSBNLnvWF1VjM3sP4oztdvW3hE3oMPy2u88GOqUB7ZHv1INp3qgUqTI3Rm6DDUWGJF6Yo1UYgOPYjc7Wszfw1gscfYi4k%2FF%2F2Y79%2BIN1vlgBSUrIWICixIE5HAqA9KK35xJ28Vbr4ZJxQaVEApzEOuf9ibGKrel7J91bXpS406qv3%2B8WL7fu6nPLhj8Q8Q5%2FWWJysC1SQJ2FlX3gmmlS3Hvgq0O2qEq3ii1cu9mNpy%2FGtvvJiTOGE412AqHaS21VtuiG&X-Amz-Signature=9dcfbd73c866e8ca8a8feb0ba63d0d1960715f30624fd681eb1e18d6e1429132&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


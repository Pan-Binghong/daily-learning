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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWBIXOVG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYXJxwA3D4xRWNuOBEPLwXDNMVNQJTROOL6hWCLm3CKQIgJ30MTWJTu0WXCzug3AkUfkBhqaRnTkp5JmaT75hKAh8q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIk34p%2FhO9%2F23zyclCrcAz1nlv%2FqtrmrMMQPZ32Dp2PlSS7q0XD96L6oPFnekhzM%2FyLqy2V5QiGorr5ObQMPJarz3S4HcEAzIXuLN1rpSjpioa4InDsCU68QJhV97XYwvfCCoVbeXfurjAmA5JwO6nm44tNiNyamn8A%2F6noH192hHzGJGI%2BIpHCleCAAAjE3xZHn6SvKxE%2BN89Y2ovDLaDTSp%2F6mqnCVHE4h64awoFjYmiRMblFhZmvCqvlB%2Fzbj%2FynYZto%2F89kIYe6ZvkPzfgCmetVat2kfAir%2Bq4xm1yj4WHLYVvhO4b0nXI0VJ2FkS5jRQlO0h%2BLR6xZLq8UIlW%2BU7nlAltd3T7AyvhPMIwoBpELyTz3FkXS3cAdJY6COnJR3%2BNlWh4UNuBbLK%2FRRkbl4OUTBqn9SHzeB9OeRkhuu9qo20AvpkBFRT%2Fc4l0tUigauTgZVeHMu%2FxtfFf65L3Azqt8uF3UM%2BVmZYpL8EjQ1jd8CwX1Fsp6%2F4VKC%2Bzs0yEliudtmgjK18f%2F4N6DvhlqAgpPpjU%2Bxxi6LlPbE5KC8XXLzmWX6AWaDG2Q9q7q%2FcIrSQB2lMVRXgowheUAvjz4cxQxpttzzHELdYiB7KLXpOFlloUbWOnXjAH22esKQRJAZeGuI1YfC4w1KMKmvvc4GOqUBlPuFSgMWGl4Xe53SnZM3xc0ipOn%2FPydAB9Yo%2F2b%2FwPRM3yFgbYOhUZFUXA5Tm4Y1CIfxIWZZMHXdDPFR0kTAwoXVBWK2lfjmSj%2F9SeUYCcHOJ0wZ8dUQ8m9sydLOc5nscxmL%2Ftcd4cx1UbiCvAK8efaTrrzKQy4wPYjvU%2BINpLT4ymieVZl5Ty7eFn%2BhA3JX7prGrOCSh6yrp37cI0jB0bIGBhyA&X-Amz-Signature=86f66d8fcfb09a87567c5f2e84de84933398e4b81e67a8ade565476e9d3b750a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


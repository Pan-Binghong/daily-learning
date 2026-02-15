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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DMZ4RRY%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDIbvOW1%2BqLnxTtyQSNIdMzp8Z5ohRQ89ssUHXOo2vDiwIhAI8RslE8tJUvwT3rbk4NAvSkYBbbtG4pZksm%2BrmtNxxQKv8DCBEQABoMNjM3NDIzMTgzODA1IgwLk9qXWxfo4kqO%2Bhoq3AMs6ThP9NBc%2FGeKTGmG96ykRZ1KO4Cd5GWTKeMYqdcMudyP6Vtxq8naOyAHG0jE6C4PJzTEIyDTVRAtR4q6Bguhmf7eha8i0xerZVqT9xiJT7sDBGfnvTVne27wQ%2BJtZEzXSbFiiWQpbp0cZzTGY%2FNPBeScfHNPyhcN5SBDjeactK%2FQVAVKR%2FILOsivWWWECqrQX96T8NeZnvLNDX7Zq9F4DDtSRB9yh31UsQiwmaCLpXJ6HBMkbQPlK4wn0OSi8BSMlTpuQeEHOlSy3e8bhOa1Xxc%2F5SA4eXGdIxi4llycW955784FY4BwNyeK2qgkKsXLW2IOw0NEMaMBsWTJklXJqKY16ZiABEFxcVR3wTxAipOIH6NETbWEXcHea8XmCIoqj%2FkmI5HosjZiPl0TQbzDGxI05e30cnZ1%2FU80l7WbGoY6ypTNKiwuzCmtmllqhOnQ9A10MBZKBhgATif1p6AnbI3cGvOf%2B5VmH3E2YtyMyMz2%2Bg%2BlcZ3%2FqlwQZPV3DeP1InASg2IfVzFvqW5oC6XDventHiCMpwjmazyyQOrXsSPzjtrw%2FmdvkH%2FJctgBeEbevtcMJlM7jyFqwc5u2Ga6OmyieGxyekyfrBm6f2m5jb9e1tXzvKiEznOM2DCen8TMBjqkAfCBr%2BuntHkqgRr7EwLdaa5%2BFfj2DFu6xneCrnNKdpuOQnK7%2FiN2yjzlLZM8udbkdqw7OkhzRisu7eaB0awfPf6GeU%2BRdb95euDjBdHFzvJtjk1kQJtitV1fYksZkj3MLK%2FH9Y6IMgdqnjJgdkSkyE36b8owrbb1sNqdLD58hH6bnz4atqJlNTz%2FHPO2b9C4zJikTAfK1S4IOuu3vq4x%2Bj64Av%2Fr&X-Amz-Signature=c4aa214a88776a717932a02133dfcd91da0cc0f91d7be7be24a4cf92650fbfcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


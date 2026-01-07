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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZJN2BHP%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfP3Pcy8frWfM08MOBxdVqVH%2FFNXrF102LR9c9ju0EWAIhAKnBt7yyx%2F02APQrkRxjV0qKLf%2F2ImH2B9CBtpMp8T5tKv8DCGwQABoMNjM3NDIzMTgzODA1IgxInkemrEbb%2FA%2F2Sysq3AN4nKQUYYoSz0nihut8BfKcEuAYleWYfHgAc6K483BT2EP2g0akP8Rt%2BHgMJ6L1XM5xE%2FPTaNtzwra0uCxZrI08qajWU3UH1Uz5oSgjqqVvR%2FsomGPjdY4LJJUWQdT0GCp%2F%2BLUD5uqbxwxslb55YygvoWws%2F5reslU17mutP%2BB3hYaFgc7yZPyvclAqSsNH1UiTN8pQH7E4h0xEfUjmWSyePTwj6nFjdd4HwC%2BIPBb3R6k2uzSKGBwFLQejMqLZmpDn0eqIID6BaEzxqWu2hWCw8qw%2FUkhSOR%2F8VzPvFokiUZFGv6TKUprNBYKInwdlH9VO5Xx%2F2nez1dzcJi9Ub%2Bl6P87q9fkAF8aFBz62O91K3cVKKO5oYRFAw6k2CkOcDMsS%2FAhyMdCXmYuPybXJZEGs8GkNMUDWYDse%2FRpmolzPdxww7dzzDBr82AYC2CTagymvrOYQu8x2As26wSbDjn36WOrgeY4Yam0B%2BlLFHmR8UQSvoej2QiTxS7WOOjPhm6O3uU78r3moC1TXC2GvpJ3GZeDoQerJ0RnQgx4RO5kIBZXhGgVsOpLno6ZiU0mBpqcCiz%2BV2h%2BPwOXuRYSfHJ05cI%2FnKunEWeRpCfyJzXOHkVOrSaJOEqncAWKvNzDWjvfKBjqkAdDq1bIdLQmp77Fo7ksdyC1O8AqNqj9b50STiGp5s3xPDXKl7We6Otuv%2Ffdyoka%2FXhGdnN6d6uqPJKCmigo7i5HTGxdviysC%2BWByeCImd4pn2S7EgjadEqlB8Gf6WbocfU6MDi5GJw1%2FFIIlyeqj3fwSmyaz1nYOZMHoV2XTG4KKNgCJTjoISJ%2FmHlhKnHBiKbL8mqsIImFbQwT2WAWwuiqBqvlM&X-Amz-Signature=06b89c75f5774afe3d912851c51a698b0dbcf391aaee4e18cddd060df3991758&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


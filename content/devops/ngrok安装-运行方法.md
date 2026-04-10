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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBUXB423%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDeJGOtzIgYibpnOd0DkkW2QQQFs1Kk9goprPSvLr2jAwIhAIgIlDOit4fBQs7VS77tYcd%2FHoXpYJHm3dTldVHDYC%2BjKv8DCCQQABoMNjM3NDIzMTgzODA1Igy07dJiFYz2b%2FBODGEq3APmDqEGCCanpA9B1HSKoqiz9QWnOcuh5QXfLT9VBM9sxp4h%2B3tIvy9pbUs%2FoAismCfrEHGTyFxk76ddoBSOirwJ9nhyAe%2Fvm4oLP4rEN4q2Oi0wfgRqUBXOFYkUKt0uxf9sXJMwDop5OADmpSoFnQJoM5MmonIsJQ11WPkImEdqm53fqudGV1P%2B4ute4dMSHR56Di8kKW3KdH%2FkcWgdxWhfvxkjFuYXLgJwfKC%2F8rQXMl9W0rU175xIT149LixjYMXlckscdX%2FBA7itxct0fyB%2BFoyec5dP1AG7HZEsjI%2FV8VseFsPvO6JkFXkDkotGjahTjvcRZ9q8tJlhmYiTl4ilogCSZ1oWFbwOBl8MuV%2F3gI0CC4GJ%2B4Q7GEzFEUsLRAQNxtChm0dzqUgsX5biizGW2A6X%2Bok1YOuKbkWGvwqVD0WCtZkjdmQ8Y4GpGf9y7GqVKZBbfC%2BhoVSml5SpqNpyU1nJjP1guieTrBY0rWLPeLZIl2389CoEfKWBSFHxCBb7rHMmu6pAgwmuapq2xs4dQp%2FosKgQ2icI7rSvdnV6BFVxkI4%2B%2FSeRNJ2T1eec1h3fM2gO3fYBnVn7L%2FllvC5tgDX1nIEM9Poi8HgJZH7IHpnEQzKPAnxozZsfvzCAxeHOBjqkAf%2Fpb5erF%2FvLTAiwhcWnyB5MzuvK1JNkshL6sT1b4cBsaiO%2BspmeXh0snlAvhOxBgD4lQHKWnzIoopClTfN%2BxQ9FDHsE1noiiXj%2Fmr%2B%2FvGm12v79GnU3UfUjWJYDKvPYfZ0reXNMyTmg3latoptVIWOaGlQSKO7VhQP4jxSthEFZaBitlQrpfrHJ6a01YIn1FEvBtLkTGBgvBf0xduyIpfIIhOEy&X-Amz-Signature=96588b58050098f185be7d15d59eefbc213ae93230f1a9236e6159ed0bb3fc1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


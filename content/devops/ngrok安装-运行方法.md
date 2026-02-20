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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJNR7HH6%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSdj%2BHIf9njxg2pLc0CmBgkXNIuMr8AF6GGqlCDoS%2B0AiEAv5neGO0Tt3Pm%2FjRNx4KL1nUoBEqg%2FwCfkpAVNecue%2FQqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMkfc45bf3BacMXYuyrcA4s7HCfSYyEzzjvR5iifJNhSqZ2AlSF%2FzBhWNU9sjt5FWsas%2FhWbTm4zyRBKbr78giNbOiOe72E60QSHGxFC%2FXJEAnyi3cqAvrhFWBzCxaeblmCVPV7PqF9S%2FoQ%2BqLgljywlLAXpcOmr6Ps0W%2BwRYiOIZosbT33z%2FaNo%2FEXIPo8ax29OfBvJM%2FkcnGZeDT3lku479d0Tne%2B7ZRvig6Zvf3BU380oNLGbrrKJXNYtpzNLaT2ns%2Fks7%2BR%2Ftjb7PQuEkzHAW3zPUPnhSc0T9rO1wgivNjxTHY6VoiAUvqIwUwe69Hxv380K3QtfOJMJ3fb7av0xSONQFCu3bE%2F8jSoQgl%2BVjsSkCeZWtiWKNkm6YllGXx0pyCziAVsdg7cw%2B8aWsFp0KygS09oGeSH9iA71GxVhAr1uB2X6myTPTVTQvzT5e1uvZRXoY0SAgmjiS8M3ij1TQ%2Bs%2BWGPDrJblURhAkrzjMCt%2FvKvzWfu6ZfL%2BqmvuGr92vLh3q3WgFYhQ3W9Tg3luzSeQ5VjlUglWSrKxW%2BUokbNM%2B0XevYMBki8N3gnrUyxD%2BlSGo0HhiV1utKg%2Ff9SVPdZFK7GEnI21LDFIxCP%2BgAYvOnkXpECbbzaEewm5QG5WXkD7eZlG54s4ML6R38wGOqUB7%2FGc4NZlio%2FGhHQxNW2rBnDgPwPgUQ7z5oeRRUboRj2oMNWjF52lxaJjPNGpSHBqE6pVZ057acD4U3fQnM0HscL6ZIWehP08vKoEt1QwnO2jHBiBhGOEKx%2FepxXEC1o%2BGKig%2FtBfiyQsxs1Cud7H3ThYIBJMroLgZpy0VFaUgTASOeuHApt0RuqYaB3ljSU6W10YsFJ210T2lr8%2BW2Pprq%2B1HLAu&X-Amz-Signature=df8c210a8bc89acd1ab71b87662a4f8b7ceeb4bc39ee08802f4ab118c47928ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


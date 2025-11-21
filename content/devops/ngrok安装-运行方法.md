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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJVT3CAV%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIGlefwU%2BOZlcedyd4Zjcfm2UULHB4z2WAKvwMXMY%2FeVSAiBtcI0gROE0nQEoIz3OqNh2RJCCgWy0m3JNKGyEpxy3uyr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIM%2Fkcl0nkSJDRoogyHKtwD%2FMgQMJFxMgCePjvLqZJDV24q5kUV%2B8%2BWSdft6L9Mp2sZ4LBmwx6JnMAYv6mJX5yGD6j2GgxdYWBfd87VM0W%2BBFBsIBtRadN3R4ZVrzN9LNpabeQKaNIUTm%2F2F55LBvb9PdYITZGtrJ%2FVr%2BrS11%2BAA7QhXu2n%2BqdEWDCrfFlMMrsFzWFEHeTR83ivtuWl8TMY%2FujrI%2Bd6WDYlIkRqvUS4GVFVzF9ttnvr1liOZRlXi56jp0fIHTwbyum%2BbXL9Naq7WajegdnhWI0Msnkh4zM6iX9wODjAqAW%2F2uuy%2FobOrSMTCJGzZ5KxOFXQ3pO2LP7ROqSCgNoKgcp6To2xW6Ho4M%2BbS7enRQ1wN4gIr2HGLmJ%2BtpPETCI6unRpXdeiqdsYK9zLDlVaINK4vr%2FNdYM5FYUgdy1emtAQbOtgedUNLKQWDDymokYEo5BU3EcIcZUpgFpvcT0RvNdUouXc%2FLkGFzxRvz4QwM64yTjvxblOwkXaJFoV%2BsdsQj%2FllBTnhD%2FRR57Kbsd3tgnUGVvvYdU6qx1Vau8i3djVGHqpVK336d3Z7vX%2FPu8t2RlUvmGyi%2B3cQZ83aZdVhqrbhuYkcPk3SUA5%2FHLe9ycQR%2B60zIgU2Kl6j9ZIPGDlaa4XQ%2FYw4Z7%2FyAY6pgHMviLG8QB85KsdiU5kraH1TZ1QDWtLTW4Wwq9rG5%2FOb4gT7UjtiEgRrekuny3DfrUBgBaUHlg%2FY2vcFwxBRgM%2FRrStl1apteh2FPZ1PYTLBOrzcRpiHv5vc6VRhFz66pFukpJhrnujZUMdj17zezniqEy8CHXZtrEGT%2BX%2FQTpl%2BpAG%2BhsOA6SqH7WdDzc79f%2FR%2FDOemVH9QJAx5YPuhSmxIcY0%2BdtI&X-Amz-Signature=bf1386962e9182c200a6d9219f5b8877a7d814fa562c5f448b79fd56867791ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


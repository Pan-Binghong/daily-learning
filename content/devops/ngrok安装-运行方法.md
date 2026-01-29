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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654V65BXT%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4sEkzV5rHxgKeHW23isUPueVflIwFvDwHkQVf6iqczQIhAMMq23ndHMxPpP4EC%2FVG4bZktuMwZ2m7InpKzF4%2FgmvjKv8DCHwQABoMNjM3NDIzMTgzODA1Igw1lw5pgwU8l2Yvv1gq3AM%2FtpKQfP4p1xDSKGqevXjpu2C8IFFLxs84ajrh4FYWDBygA1FwEFcP2GHAF4mvhj0eVMzC0xNyv%2B3%2BAhP4W7ONMPyla%2BVaC5%2FC29%2FSV6Y7FtVTnDHbYuBsixOz4BfyeijLkhRsY978e8Y7Dlycq36xodvy9VgbSbg%2B95CHRwlx7q%2BCET8XNTSSADQWps2kh%2FgQ%2FwD6ISJwn4bSiHlP4uApKkMEn8kxBEFDOhDEaDoQhHqLE4M0%2FD7S802iuXmiX8rUd1NeI1ggNjMXAGdtN5eYVww50QvB0ud4xDjx0Ef1527GGAw2ruvQWJCATvHgd2rkLVTOU%2F9dQZlKPFawgBH7vU1%2BQMpClbWA76%2BOBj1zVy4LEF36G8qxfiARTUOX7MQtoztKLCiJgg0dE%2FabViBOlWc%2BZSweSp1AE2hSbdFwjrMjhlZq1TBy%2B80M6HBVsWEECif3LCI2hC0JUhg9LHsUguFR35UhuZ%2BhmODqfKEIkEfb%2FobPxS40QzF9zbvlaFuSVOzH4kr43Uq1ckWhiZ%2FFHBYgXEkGm5mFuX2wZL7J5%2Fl24qFQjG2kXhdD4rKCa%2FbTQ8EHCf5v%2FZ74AZNyETG%2FELOQZFdDY0TtGsGvm3%2FsGrb6wUxIozhylQa0jzCTouvLBjqkAW1FOC0J5lATq7r%2BkTnzB7Lsaomv3iXZxjrmC2HaDA2uiOoo5dG2PYth2%2F8pweQ%2BQi4txzSN8W5pnSW6VmtSa415WMEGDSieBDnYotq7TReQ6hjSspC5wiqNmuQF1%2BCQc8%2FAGDfvqYTcrxVAg%2FI2DyH2rCg%2FvFDcMGOeleawSOY%2FJotHK9tesInVqwcBDeaILMXrbg0NXLDdV%2FYHFxU6jfwCsA1b&X-Amz-Signature=25c451beaad5d813d5fde0e6ade1fe5d90e23d8d75c9fb46a0f1137955760656&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


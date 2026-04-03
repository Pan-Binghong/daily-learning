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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSODEDFQ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDQQKjraLXbqW9qepmANKtt8tpsTMmTGTUbPGAWOfyU%2BAiEA1WaAzOye2vGkvJvJUVDizQVESCq8ErN75tTkpx596mYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDNMZoR9XyWT2Ns1M8ircAwF6ATX6TzyjEai4kqaZgxuBdV8%2FQFYKlYMcvAdHJrlCYddcFbGQAjOkHj6LU62xxd%2FA1pC6mDx4LqNy47hC%2FnmOUWRp50xJuJoCkp3pD3%2FHifpFTRTGAY8rfk6Zgb%2BfDeQcx9TS8RjjrtQ%2Bzraqa6AenuC%2BUnGjtauAjrfb2oRdR2nuJPJuUKZIVi7520iPQ3ZbKwIigwhCBJ6mBd7tpKd4RwA6O4%2BlBTe94eqMTXGA7B5%2BPqa8t2Xqrskz4V8yNRaksscYr3hzg9RHWoB3krlwcjH4ZtGTvAZDkcRysD21riTkUXHSTjijw7IgJff93YsKGz08Yi3VlseXZ7W7jJL1OrbWJmEBKlFDactuOWzL9COMdA6rhIP0uTNTFMjBJHkRC1dml2sm4wevgQF6lY9mhrTHqmiels6cOLr168jSmsulHn1lHzCoE12aJqyyaD06pXvjF1r2ddKH2HcIp7I9osTxvlFaTKnCKaARjximvbPUBUOzPC35PIMs%2FNPrFP8rqQDJdmOl%2F2lTNgpJHSITu3bb0m%2F1glvnlhdDBhDAfluKRJTHXKRihJgGNuxMBVmFAul2RDc0pxUAgNBdMGzII5wKlCaMdm6OG%2Bg3dYS4FKfUTbKEUX7LvRWNMK%2FlvM4GOqUBoQ5YGzWz3h0LzoPFauMhYO%2FW6bhV74UwcLHh1NOfX7lUY4w24fUecMEItAlUeCaSUGA1EiXOMqIkzzEc4SrmOE5eR2bkmku5bYeeikBJsfv8r01CgfXXqNGoFd9%2BiY5rmXc5qITglHZo4E1WYr6Fx5uaw737KC58NBsFBqOs91oJsisKzE66JDj2VMXL7qTgWIQvMLPERJU3flSNE1KEaFBu6PsW&X-Amz-Signature=d5b1ef5eb8c88b0b820792a17275fe490f8415dfab29972cc1a491c7d3ab9509&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


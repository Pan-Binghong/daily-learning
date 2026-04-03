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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVROQKLE%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC33zRaPeF4GouQ0XyqJQn5orJRhbVc00oVDpmt48y9FwIhAJIjhpA6q9G%2FDCMDn%2BcotG5oPUayR2euRSpr3CKsyuE7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igz1jOhhslreF4vPc%2F4q3AMO%2BEQevEwl80rlD781oUcxkOn5xbi6jupTqeVg85Qa7fENYk9rLL2maVubWl2An%2FFHYGttGcTctWzC2cyW%2B2wxSxQxqpmfh59jzKINOYyTBgbl4shZ2vfipTEKqLRNuP%2B14o1d9MskeCw2IOfFusIAhd46BsF66BAEQ%2FMVcUZZzctQGF6LdjuKYTAnzf7UF9M16NBs0UpXwKAXM0hMee7BMR82TxQdL1AbFIiKUTR8ZMDYP%2FIYwA9UQlKE9a1Sv4dykKNq2bm3%2FCw%2FEZjTESiytES%2B3VNtXaye8nmUSzpzq9T8%2BuEFES5wrfY5TlSEMypGBqv3nzK2q7fdaFqH5ZsXwxP4hNSti5kralOzK%2FePQb6%2BjeizoJOTw5snu2d3uFJm9aTNYwl8RWOwuT62Lp%2FQk6ZvGEmzuVGMIBLzKnxf%2FWovK03mJO4egSjD3h%2BtYGY6E%2Ba77D9Yib%2F3Lp%2FG8drWZpNOM9oqtr6FIet1xLnD4h%2BlKYlMYlOF4T6G1bwAaZjg7DrCagZN9DhIM1iJ9OzYVIPKmkjETSKCz4iiKpRV6CTMjYfDNpvY01fUuoL240ezFtniyUjQMbZuA3C45iU3WSyY2oHwf1PP95xLuaZDMmGJZhTpjvGzNk2VGjDcrr3OBjqkAWyZPsUBliiTJnPk%2F4rSztWh7McwmVGeaqu8a3plzSBumvLQg84Ulg2nFjyaDt38udAu5o51ZlCYUv%2BaR8poxyxYs9067Iiu%2BqlgNEbD2Gz0dD%2FPRxoYiidDc40I0hnmPnUSxxeOOLaisQOLuZPoQ2MZgX3%2FlsyBsfzeTqHPqs6X0nhKUzHIZiGHdInp0HY8uVjOAqMgi%2B7ml4cetOGddIpvoWxY&X-Amz-Signature=3a500ab14e918e3aa9a6bb64814ecb9962edf9c00019983e1261009102e72416&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


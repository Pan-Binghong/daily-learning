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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCAYUODF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICerwloUVl5y4BZLkk4Wp3pt%2B5Rcy9SpttjCq3%2Bl0lDBAiEA1Pl%2FV6kzuciJfvIyUxKWRwQeyHOWFBi34HfYqbh5rxkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVpC5ZZcpVzeFfSkircAzyAJ%2B2QR8l1TeHh3n91FvRhHT63%2FFmds5oU2XsAzLT3V135NKoVijiIh%2FGn%2B2O6MsbcY02AU7Tscbpg8NDpL0kvl5sslordbhZvvF6fJqF18Vw3dQ6T10KfKInnI0%2Bmq1SprMa21Ht2YTFgWEnRG%2BID6dMXjspXbRRiHxSVZwCF0ylpuLsAwD8TDGtr3hGh%2Ff89nuAhY9Rjd36%2FZkKS8OEf8Wmff7mn8sCGkUSsX2FpM26tQpL%2BcVrTRc5k%2BtvOllBT5xV2hXWtOwVdvaS1V4MVU8gDrQCq2rgfXc9LU9qENk3M9oBDnqC2aBB6kwQwtDzx3B8arwLexe2JHA2dLyb2VKeMGIx87k2rQUlGwYjiBjl62a%2F%2BbDAlX0EJQiuWh4Kz1uDPRuFdvDFZLEjSncM6ocSly%2BRVkbtm6v2ppYzkPB2XojMdNZjA5%2BhfdgneWYeeUvnk3dgdtI%2FOsOyyOhEMoDVw%2FLLK%2FjIKQbfa8wx7WqXYXBGh%2Fb6W9w9ZFzX2TLpImJCyXxgLdXH6f59TDgobTmwH%2BIlJQSK%2FRqEiVHuXWQ5b%2FdwZBOdY3Or2QjB7QtrlrshaAq6SaMjUaDRE1OFjeKy%2BbHDPCyKMVtyQzJIMjy%2BRBaG3IA3kyXwbMOi85MwGOqUBfa7wRtxI2zA6bsFl3x%2FV%2FoKonXB0t6RtoQY4%2FXncpfYxQjpwkD%2Fo%2BlsCet%2B3cM3u2iMvpRcX3RZTBb%2F78S0eN2cNIgNKymO10tBviiudWgSpCzG%2BX0a4PFukr5AsOQ8aQ3b6HsUOy7bB%2B1fxC4aw82Yiry05K%2Fqz8%2FNzmfYE853AZra%2Fu2jEgGQyICRxnKrvFJqa7mrVS8byVJeiJl22G6pEFv0Q&X-Amz-Signature=1755960d01d3d95fac3cddea9ee15c5188a7bf564c9795c0452eca4e1d92ff79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


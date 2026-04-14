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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2NV4DPP%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGI4X6asWCmrj4KaB%2BRzrEjkccgDzSuHH%2FNekCMm3GWzAiEAmGXUU3s1KLEY%2FSWzE5Eazk%2B2xoTkts49YqW1YFrfC64qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAkPq%2FltXM%2FwsPB2mSrcA5S%2Fzl2iEKcfJ%2FuLK4hVzmXpxJmhfvvYKrd7tKriTEKGoEIex2DOJdCpzW5pQjYwmvjogDYkd%2BK2WslV3kDedEdy2Sll34YwPGkORzCmMoXkj234vfoZN6W9QgQarPCn%2FsHZFBO63L25qtyj3GscPQP1t8xBlzLA3%2BVHR9OlJeGFY2fvANFIU1Tuu3Cm75OCFU4CJrpoGVEllXNNaZW%2FyD1iDuXCrGdaMtk4LPVsbuT2oN9qbTR7WamsubO0UrvXo4fAkbgwJyTv%2FIG08%2B07BlqnaFfUVnNiTnWsMjVm2eZnlH%2FTYdpsOM2JTwOBYbqE5Jp7MriNZ3DbSnDNcLCMiom%2FEAplamdNDrBuI2kquTRddk5rbAZ05qOJbsDaJBxMCjGBvcen6eEqdw9tv2sz4udUyGYdn2fibZwSE9SP9KudA2K6KRmSsQISrhvS19sC%2BF2iOLoCHse%2FjKsB%2B5YL4Gca%2FCrQdbCWXqMaBOOt2huybBeI6IHu4%2Bz0VJPIQw1TspUuIx%2BQNJ6ai57RGPROYx%2F06BHXl4Y3evy5U%2BlBxvOkSh3DwjsQCEoxJObAXPoyjwNgTwzNPdmeBaCXT6iAoubnhDK4607rwQ3nT9O8iYvufL%2Fee64m3yPRKsGxMIbh9s4GOqUBDQYSk%2B1XbxVzgqzU9tPmqg43fAs%2F1vSQO248mhYB03uVdc4PKcErWfSwwTM%2BcASosAoKkKmh4r9MJVtCBcL%2FjqIq0ZVFJqFgz3TvGxO7h6XV5vGDaLr%2BlfglvB3XqQqaNu3z%2BN7HZdjuEG1%2BghGXmTsP0YKLENmqW5wzXDvTIFlPzGPw2gmPsPHQAcQ7dxiHs%2FiUXZDYNA87gyQbxKGNIS3B4zH0&X-Amz-Signature=30ae7fdbb883e41d5e3954b1b04cf98ba595c6978062c00f96f6f477894b71eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


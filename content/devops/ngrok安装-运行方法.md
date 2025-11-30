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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRD3II43%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIGjb%2BD%2BfmOIQZAWHxS3oMlaKHYlWCOucZQXvL62kFP91AiAsLkC42H%2FjDHkiqwCOzz%2BiXiqQlqFmnZuW5DPot0yMiCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FVC5BNq2OALnrxPKKtwD30zC%2FzeFD5cexbrP5kyvXzvjAKRTmjjWp7xjM2TM%2BhsRebrOw4HXrX4tOyRwjKYxm0M2ArbXaijKKmXIdWxp0n5ZajgKf4OJ5oV%2BINHLAtHxrRj47FF91P%2FfaoZCmdmlPjGBfNohgXYXe1%2Fvm%2BED4o%2B6c5E7SkImoLBF4r2GvaodZJ%2FWeN9vIbk0sN7MLiEQeAL3g8TVJOIDmwGrNjsvw9MuRfDcIPcBrsJzI8ZfOS3YYIGvApbt%2BIinMOqvjAfz9fjw3T1oXDWevwrD0OMzBNXudadd9sDdEgYOkwu5JeEaxao8%2Ffc56tdLWIknXKuxqwswLnmt%2BqqtgqJm87y7M%2Be1ai399PKHdqhAygM7fPTo%2FqBUQMKqIRKmYEaB%2B6XbtoEa1VmNXyFtlwqnJP2NCueh%2FPaiwM6haX9lAQ0fLokdMzsGjNEkhNPNEs5hLOo6T6JMJ%2FHIewvQfFnMWdKpCkYk36QVblIcervKbvoPEsugjhQrO3%2FQKchURELehNKFKA15xh7XpqgRxGBEmgYLoEOmXdc3bIXpWPjLzKI6VvLLQCPS03CfaFoHtp%2FT0VTjTYDqz4uDQlb7uLjwy3URjQ5AQvi%2BM%2FNo%2B3xSFnKy8jD2spzwnmVNrL1UX1Ew8dGtyQY6pgHSKgvMKWlUXYAPzWWG9Hpiw7%2BQJeDN%2B25mFHENRlrAJsi4xFyBr1pM9ArWfgL1d5xb6tcChiFnEsX3libvlzdkR%2FLJ99uD6GmgNFmC9onD5Bt1J7iNdWBQJfP1%2BuTbj1%2Bk2O67mADq%2BnkEUJMVxPqhWILEtS606ZkOFSvb%2FOk7tA8%2Bhpm%2BZ7%2BPNOa%2Fl6KZnRygsEAXoDKXt49j54npoq%2FsTWghc3vJ&X-Amz-Signature=e16a3f24682d9eaacb9a411c33271d778a228711cd5d6fb11e5f964d38ab26a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


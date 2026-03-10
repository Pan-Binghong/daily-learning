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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKJETMG4%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIB%2BvRl3QquFaeqBHp33X6ItunaZZv8vALnv%2FSp6TkiJbAiEA3JHwsqIBo5HAF6PQfCmO3UbtTUZE8EXzvHfcX4ns8FMq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDONgB52Swvk1g3rz1yrcAzdRJkNmRioY7iMdQ3Lyl0ijXRjPTOyvPkbfigDqRKnhCZlS1968RRqjXW8phjLP2d4Sdjk6gJ8aJw5AYGowi9cW9GSSEwyrue8I0kYYerqw%2F3EQC7sMGGFpnKlUMMj7t3S5oTi2Q0yjWe4qtRWXJo3GzCr2MOVujjGPtY%2Fv%2FtSdtd6iQaVf2Xwc0aTXOJSLX4ubOiAbXVirhPzG4Yt6vkUIwvlhoTNuEO9VyJrjR1lvtDqH5qhvz%2FrD75ZKL8gNbzlhlqWRzeH6xYLPBdJTYeJzPWRci%2FOtzhIg%2FLT%2BumbZIPRxLxxNYaK8w7w0Cm7TfU8Vn3AiNOHj2diMGssr0a3Czaej44QKnaaNUpv6DqtoBbPRe0KKdD%2BgIAMXmETMCuwp1WB8lE0zqJLqERSDfV4BNH5LmeOyFRCnkrZacLhQA41WsenhkrPZbI3DP%2B8nCjMfMKzRumPbOKoJ0kuV4%2FmOE7OjvpXkhUibU2DkXdWrMmpmS0%2Bd9cnNUg4RzR5VfzUCMAhQ5ASKUSf4h8EGYgzcULOQJCpD1QjnBcRe8T66Fg03NTgO2SMTo7liOUmDXSn2E1QzSGZGDTBjSV6GBtJ3OmmMWKDagANOygqncZN1NxrbOBBt5%2FfESDiKMLiQvs0GOqUBwfQGp1%2Bk%2FZGXuBNXm33MNVRkdo%2FCOMz1Xq7qz27lp3p1RuJTagDRVlgstrgsFU1xv34C%2FqHsjLkWYe4QLUd969xDVJ9juizgumKzTKfExUmVMe5Nk3uVZBlALLLOYwYn4AINFQGILFieY9DOiTMEq0tYaCsUFtrQPbsF3M0yhlO7ae%2Fv9Wn%2BfUX6gXgh4Yn9557%2BnlgW9HbEDimY6izvOjzHavZZ&X-Amz-Signature=55a523cc50c810f882ce4d7cffa1362b5f17feb88f3763f62791cc7971e0d498&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


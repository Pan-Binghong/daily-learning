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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6EDA6Q3%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBZC038zV5WG7EPbtMMrsJ9i3HXJ9q%2BczJXngtdvXUVeAiBOIo30IpZC5viIGia3g1aFWoXbwBTCWkDlzFzsJ3mpmyr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMmYvCQLrSCEgEehDyKtwDqm1Mq7qvG5y9tskMchzH%2BwuiZKUQ%2F0HtV0MhRCAEPD3XSxwwIFaQC6nvMXxREM%2FbWsfDx0P9sgoCC%2FNoIqKmrEzzY48AhV4bVmFuyGa3CKVTVszS25oo2ZjPqqk61FUtpZOWRSPw2RBMOVjkhCexJ75LxsBeF2uk9%2F2fmRRRDBL47Pzz9qW5WV38HIvE2uKux9jLdu2f7pOE6JijFPRxDIyAU7iTyCkE0NyPjlRPw9atlBex%2BIN%2FJFQjTraFr%2BdGMyJnJtalICWfEOfrm2ArHHmKjntCitc2JdLtaTSdKaqUCIB%2FT8oVrCTNwnvcYrkZYGvJq9ETkqZGnzNmXKP18WqwfIP7XvGO2CDx60sv2wPPXlvcCrCtvXZFcLk%2F307w9SlixSKg%2F4QcTf35pF9Ja%2BM%2FOoP1LikZt%2BBY2%2FH3NZUlBPNErTA%2FmV5ph6KXRJJr7%2B86r0iqu9JBIWen0CcoIDFaJPDwXw%2Bgi8rVhWHkqujo%2B%2B3B%2BnVy0Ax8w7nIkMOlG3e%2FKs1Q2wOKKTYHGvRG08AsCU1W5ddJ7pDg4xiivPg2fp6t4ySNTP89j13Vn81dYMKvF%2F%2FUOC2c%2BSvM48DbsUp6dVMTLcDFuOF1HqmifTqFlL75vqB1HE6aulsw3uCsygY6pgERdSlqKDgy4ORe%2Bro6DLNQjeYvAEqcuZjRCYk6W1iym3GnqTiv4LIGMYGFjOxRpabLZmIJzLl4b5BDF83cMAj6hK6xdRDShKXkFFkINc6077GTsnzateU7cDgeqEcMD9z8xovuFVifbk7DvoV1BocsF6HLBh8aLwbTz90JG6J9iph17qk8T6Xez5Ygtuzm%2FqS6uGHLBxI5iYFLzM0aoAwBVLpKnk5e&X-Amz-Signature=24a8259afe0ae29a5a14b6e2e3ecce3c0271a14984d9776a32f2823100f44068&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


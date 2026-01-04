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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QXQBSUC%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIHh0rATScb0AbMULIJJ8b4qWt9HvKE9tRK4eymoeelLXAiEAqly32yQgm33nfJA9VuSTn92n9GgNdqg%2Fjg2sbAo2kiUq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDHkli3SAT8WaJ8o9MSrcAxqeEqQZ%2Fj5KhzbihFhe6KOShJosRlccvfv2fxYmbV7GJMwuK28mxZ1FSQcjA%2Bz3dd%2Bw8C1U%2BH%2Ffyey5LFSjhd%2Boo12qT86DIFOM%2FAkqzycoA2bLx88cJL1EeIqvQUXzWU4sl%2FA09K3LfRqovU3DENvVr%2FIR9M6lWR19nkFWG8okJ%2Ba7xg5vwTXGCTOcBXad1JFJZCwVMdGZCtnrsHHabeSxrg6EZzazwwwvvIGk%2FhOSiuEf7i9DUJq9M%2BDZ5eOtISv%2BTckrLlF5pQVPF5Jr46DKLos8fXkHXjBEkodxFdROz%2BW5AIu6ThR%2FMLacnNHyehm9AIW50xpQIkrem3DC7aBUlMvfZ%2ByMYQkKsOzrR82buYdn72HD5B1oR9MnUWKTYF6P6d5RWyFwZLtwwD15NSh2roKguagQbCbySJQuAL%2F2YP%2B6oNI7Wf1ITHwgMkyJBXcMaeapiuzjkClPyUzTY4qNnEq%2Bh%2FIaC3UcU%2FRYVOKmITnGsq9o1uEbwEQSx6d8vnHpqoTm%2F6GScaFGsUT1lKX5uAeglOquygweSE%2FP%2BKPT%2F5vBhU9FuCfMdCtwfwPDzPHfbJt4KQOQonKWEnbhpwi3SruoNxZA3lcxY8ZhSDV6H%2BAFQtWy2v1cSY70MPqQ5soGOqUBPCcjkgBj%2FDKvSGtYZ0%2BX9BrkxXw4jZpfFqcij80W1lP%2BUUkH2RxsuXpcp%2F33BUNLeOZe9BPfHZ30f%2F8L4D9LcyeYeY0O%2BaxhxHa9KFSu%2BzKMnbAFrUQ%2FV2G54boPm%2BOBCX1hnCBI9ubQfQz5HfLNLjuwX0Q3OALTziNj74WjzvFZGYeq6wtB9JyDRcXNtC%2B7lOqO7AWaYmB%2FYFsBNcU5ta%2B8fQui&X-Amz-Signature=98deab911a5cbb397e2c53166ec3c40f7635a5bc09fcf98770e21e1cc5f62178&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


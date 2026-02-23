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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKPAFRYB%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQCAcHA0c79Q2pqCN5Belj5aoBPKDJLMz%2Fhlo78k1okNBgIhAIclKhyMqeBoBgaC1cE3lte%2Ftx5%2BCC5HHpTe78uR1Vr%2BKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOSxTihoDc8oFSF68q3AP4SZAP66b0cs0IWsN6DhoNDv6%2BBKTzkVFYk0fL2G4KZqiYxQkjtv%2F7HK7ihgB2sqODUTcc9UTaJCRBlOLPyyZlSVHHjwpD9BSZkTaXHcnrY4d4xZCt8XmbaksUsMgvvpqWLHG0PJ84BaIPYVdzZmGhSRpazRGkOU62rEfRO29Xot0s%2FeBcB2NJMAQHqHVaEVsnQN7VGwAgIH1Lpnp7unCP%2F8dKdwKbWLeCvhKiPm0zwSo7QeuTrdqdoiEGG1DOFmAKu1SY8Wl%2BysPtvb%2FzHOBbcML0ons4bB7uktqJgZLNZqufvvlhlPCYIKS%2BQN395ZnxHEXMjxxodX%2FCTR8wX6shH6iKdwRiG9dzDwQad0XHS9LXMDB9kQduB83irfOOc53uG1hcPk8PRA5KVtd7k2Hi1ZHf5%2BMby1QGZwwCdaaMtM0Jhmo%2FBxa6TYoTYFnzxfLEpaLDClkYHsJkHty5%2BIJr7LckMAouxuDHgyWeFOYHxOBHuz5n5xkGdq6P12dJ1Z6LNDLFL%2Ftf1HU2P2HtXd5LC9lA%2F4fj8eGWUf6pV0DKXvvvsmGp6Lq6WMM42%2FhVwgIyWaFXKGI2zq%2BhvpAgDb36u6vt8RMGogbGNDBZ0qnY4nHR1GJ3aNtVW6DaHDDyku%2FMBjqkAdFUU7w%2F4jm6E7Uj98gdagmolwbIiWtuhvw12ZRDg5ZT8qK0T8K3TVbUbG%2BsW%2FrR4wLiId6X%2Fl8COyuNcYdRJM3PUQLcxPjLfnNEeDSj7CSoCFI1XfdindqALmftx4eDk4%2BMMwdft%2B6n4SZwaXwdkCYEam5hXaGsPQO8K%2BFAYVRrUvj4qiz5PzDhagKvPks1h58%2B1jPzAWP9gmcKoV%2B62r2nGGI3&X-Amz-Signature=164262f7af286b3f89fafe1cfe3945a6640146281cdb46fea3b339055a157688&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


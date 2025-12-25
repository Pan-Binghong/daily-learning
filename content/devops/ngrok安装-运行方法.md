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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNYS36TA%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCSUPmFQaNhGq1fA5PL%2Fgs4TSCVHa6dM%2BUM5X677IjDPQIgbXTJM%2FRjkHzQB2P0TgnR3Fbtss9ejY2AEuwmOggtHrgq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDHar3MvSODRUNf%2FjVSrcA%2FukF3qLKTv2nka06nN6giHEtIHvhYqNQ%2FZ5ZxM7zHxZ0EIy%2Fh4kELxNetuRR7PWHr4CHeqahxrpXEJ2hy2KEHnntBm9KrYUy9e94%2BgZxwpjNx4kSKx3aZJi5Xu5Hr4u5OUHqg%2FXdHphUjw%2Bi%2BZrkYWpp4b6iXSXUyjnUaWkKZN6MuiUfJwO%2FIHQC8f8yvV%2F41doGShMnF7lHYZs2D6l%2BxsOEcjSWfGAhwavpxEQk6sWHKvKq54zL13ifo6jqxn50sTqylFTrwhqUaR4NedbrXRKXs%2BTe6RYsD4E9ZXbNPdD6mD3Ue4GEOYSeiSXLOwWwpcQSAZCAVe121WxzH64%2FtUgdOQ7oH0T8qx87GPpU7a4hh31w578beXGc9iftZfhWCdjzJWLryiUgbbgNNr1bQ1wZboeXaK%2Fj5xzvjnt1VzO9Dgspje3xPOtgJJj0alhqqxGVOLRvoQ4CgN%2F0rgENMySYEhmxUhG3ubKVv%2FZkSL3tpkZdRi1RAKyKWw97jtjLPZxqvjfpSitX6Qff2Ba7yYaXmOPnvD5iS%2FKjOViY74eGHQoZK8PI5oQzlM9J47xGRcTqlntxD%2BXBYw0PsEkpYcFvrTJgxJvZ5PiCnt8UuvedmpA9HbQrgmsb%2BYOMJCkssoGOqUBFO1BUSk8GNczkpkqKyXcsv%2Bt%2Bp4dCRyefr4CKoGXqgiJJ%2BUbRiuobDSJo%2Brfg6%2BpwrTLqZItu%2B%2B3j5kYFq4iYRbJMAMeTRkIZFa5ZMw5bP02pCxUhct6VAjh4FE%2Bm8kdPzcw00YwlaMv6QA6w55HMmNpy9GAPyfzwUytsJv%2Fj0%2FBmmNh4Hgm4VasX5hgUX159qk7IlQKKQ8o20HSLSENk5d3SWOo&X-Amz-Signature=d8cafebc3af897116a57a582d133160eed9cedd3239cd52d1177b0d9ef73a165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


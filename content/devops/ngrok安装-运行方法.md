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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXG56THW%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAiRMk4yrNmESVCN6k7x4R%2FXoUspoHvgWjlq7nz5xRDlAiBZGFg%2FtV9ISLM0Ketl0BPFKiCOq4ilXrjN1mibtLyJ7yqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrOy4cCVjosa9RgE3KtwDPuK9bAa%2BRJG4aJxxS000iZMkZKM%2FahqkLUbhHiWahx9O9FlZHkomxTl%2BTeY1z762ShURpaGIjcJvWm793LgsK%2Fnfd%2B9IN8pOL19%2BEvjuKeFv%2FNUwh1GzzBQwu%2FOODYM5688uwqzf0f5xpLcTLqpf4PWRCTMtRM17uDd7JBB9Y753crGQr3YLc1%2B6ff5cq%2BoCLmUoxWkU9pfvlehY7ioESsbLCEJMZSkSNnE9bX0eWJXp82fI%2BfZGEFLD%2FZpA5851ngaaVv9jQl72zwcYxy5FbWgUbcDhaNzmQ6sWvTSfAUuooQSWfnzyiZoIsut02NTA%2FTSlKUAz8I1YezXEk%2BsqoFBoj43PtVVMCP1lpYnNetLF9QJ%2Bck%2FFsHcNoZjQDf9OLRCh76VaVJXzBlu1yCCTFs1DfMAnEn08jpFzx56PiNvQDZbu1h%2F9mj7O%2FoUgpfSFRgui3pgdkRX962wQVZ%2FfqFAItHk6CqMer5EKW5cqCm5RodiT7LQDzZZqxAdVNjNXwrfS6IhNAMtJRp3kiAljuS38dXggXmSfVNlD%2FQTVzNovOjixcH6lcBNkCiUdDI5zxI9o6MYuQ8fjEtMOANktZ1eqWo8yaQpDthULkC%2B4Jt7L42blXU%2BPEMaRRw4w7fGvyAY6pgH0YAJ8Q5pbDSrJlLmh5VpiI1oO4fDEMZZtANX5BTT7O7KWFa4WDd90AxbbABKt4tXPz46SglLVeq2DyoWwpyL8DH%2FbDCkmw3lUXKtJyDxpk9BYPeSlInMDelDkf9T4Nde5aXtIDZrTtXAJlAgLWsUNOLCgBs4B5BlocZq8JYP4e%2FNDrWQOnmyG24VdxW8ZMg0VVLCrZrd5bqi9bEPgOZpgw%2FZjyWap&X-Amz-Signature=5275ea7b0a5d7932422ef864a2f06c3da558dc48b42549f1f4d1de0adbde583c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


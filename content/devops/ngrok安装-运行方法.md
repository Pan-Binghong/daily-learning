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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYDKFNSH%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAw7yHnSqnzD7776LeDTq%2FtPUjT9UKpIEF50%2FUx7QrGGAiA6GGypjFAFjplmJyknDkLNdT9FwfonChxGTBhd7I%2Fv1yqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxDywLwsYsoslpvJYKtwDdZmNQpk97GAfeGQtJ9OUPzHcadsGYfXA%2FwZdtHQTdwuvuDTAxgYKs6Ljw8x7mUwdMWI%2BvulYlDlLHYYRo8EoeCuBxN9V9Z3PaBqaBybGXnR%2B4%2FeAb8paRvlYU2W3uYwrnFotRhfetfjdmGmx4KZR4kxlEXqzZU80ziE%2FAnda4OmNKaf6mQfo0n%2FLuEhE%2BkrUvGntu%2BmAo5xTOF19lIZAxYOJQx%2BBgBCNuU8TODXc038UEkRR60Ej%2FuCrzKp0Xf%2BdmWqCNOE%2B21vOkyTYkdbe%2FCSoyuPjSIk5T5aKkxBKprXIIp1bKFYvV9o%2BQp7Y%2FGsag4ZdIFJuDKOp3xZETNcANl%2F%2Fyyavy%2BAr54bYm0p1OWNQbDndMEGmo1ipGLpSjiDy5RHVyICBra6oKuAa7ETgoRW2zJbq1Ls0M0suFWrzRvHcPYBYXU06Yf0uliwEZtUHCmpyfpwKNmXclmKqKl9hflVvlKuHqk0n5hPdvRz2KffNzjgzKGooGSDMZrnSLRjRw68ZE5h9un%2FTRzLL5jiuMdaaXP2Gg2QlrQ4Jaaar8PYtb1JleOa%2FG3D%2FygYBC%2B4QYbqSbruWojeIw3mpfMag8NtAh5371V1Zy9YumbvoC7obfVqT4ZyXmn%2B8FAIw0578zgY6pgEhuZnbHBSTH%2Ber%2FQtE7Fnffy%2BdPAsItEeyhWAa7BqwQlYCmJLN5v513tr%2BOcFBkjGGx8VAJvDguSF3sJ7ZP2HeRVG0lABB6QumrdMHACftK7L0pFUbA3vhUb2F3Tz4C2HeZkraAsC3ktJK5fcHUQfCbksZOww18%2BFV0V6PoNk6Vl51PiD%2FKp4o6Ak7HsoAN4eyAdgEIj82jH8QYFhg5UKc4T%2FuHGio&X-Amz-Signature=31caef584dd08a6ae80de908bcfbe192b77fdb68ed9df1a5318bb461ab56e5a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFKVPXBL%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCH5JEMD4mueQ9WjeSsgRP6gNzFXchciDL2oD8i0jXZmQIgYiVjUbDUBJqniVNHGKffmO9cSITDhF%2FGkzh3bH%2F7waAq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDBmmUuNbbEap2Zh5YCrcA0JACD9HHhFkTJ0l2d3oxCDkzz8iIwxOPqbM2XgWaJee4URQkHE7bfqD%2FYULvkr9k9%2FE57UtRmRr2BWhG8fWSbtxWDlJefdOSvbXa5S8jcR%2FJx%2B73eblQ%2F9s6iOZYDpKWHc64B1ZP5pC9HuzHTnZguBSqo1x81BxaLoPBSAg%2FnZB%2BvTyzWHBiERdalQerQ9Fn8lfwLYtNAAf6J8C1GIC5G6DZUB%2BsRzCbu5cCV1%2BOrGVWCoS0GkvO60KfUQP46cszdCM%2FADMx1BihNq0z93Q3rFaNQSHm9mqZeSep5y6YImdsA8N4XzKk1VOTtkB%2BE6iOnHNo2iTZenEDVxOCRwr6z%2BDjl3nv%2BzZsufKzMkTAcca5e1XIXHGAv06eKajXfOWpttseKCP4fzc2ZxSZisulmBjISu%2By%2BSeDq93l37a%2Ftp2UDH5wWyUYYWtYT65%2BWhEufCwyr53vKmr8QjLAmTuB4Igw%2FSM3P5t1wcfoV3ua2z5Na01Czin4oH%2Fpa2Mzp%2BTWBNjFadVSXMouM5sNN4RjGpOQBoCVRyXKhppqAblpC7zmfTNxShGi300SonucVrbfOi9E6OBa9vAe0i5kq4WP%2BpsQKGFlAZNKj0Xmubvs93BK1x0tZnbheBDpAZOMMWtlMkGOqUB5%2FO52C7rtH49YypzqHsOR85evO60ZU45amic%2FB91hC7cTIteqCdhWWx9QFOpneUNuY8ibVJuedxvADVeQy72hTIeRTet4ni%2Faz%2FdFUts5Gpc1ocX8emzrRnPS3OzuKsBHd9x%2B1iSLVs%2BCdDZhTxOW42dytEU5%2BC5OXx1UprqwTwtQg7JWIRdy1avrjw%2BuKR6D9uxgFHBAHZw%2B%2Bu7Ns5K6TYCJ1Fy&X-Amz-Signature=1947f52c5d509de6b80ec3979dac8f9d70986bb018dadf885d1346800b2ad398&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


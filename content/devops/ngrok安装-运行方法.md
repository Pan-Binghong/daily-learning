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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z4XM4QU%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIACXRg%2B9c6n29FLdXxu96GFi7nJhTNjfnhZtNEv8ouQ2AiEAn4mRNVLG%2FFVrL2G47ACpB2tbsamou4wNini%2FAgXIHHIqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPD5K%2Fng3uVDttkl1ircA5SJaAK7e8nANp8%2FWUlgNP08Y%2FpSUoSuvTN0JXcT7kzBTnDS%2BcpU6eRiq4SvcnPM4CvUKkUutYpr3%2Bu7iBEkg2W7Irlml1XUOgEKpl4tGg%2BU7A23QYJUBWUQg%2FcU07WDtoDJN0zY%2Fb72Iib%2BVknGRUniUUkDLc4nFmutwSA0NGWfgUTqiP1StFrwHL%2BoCPfPtuGCkVJFmd%2F2Tk8jiFLrqAVFRgbI%2FdzD2gxgymvF1iZTomTTnFZOxb4q9Q3fU7AtR0wxg6EmsWGshI5VoogvSnkwC%2BYlWN8ZLELvuS0EYBBk9BR2OA5hGjwDWvYDH4RQCgxPMyGpAzvmT358k4XBnyXLEMO3rXkDdTN%2Fgc%2BXQsxJdtPgkFSH1EdVN06Dx%2Bon%2BYCB8TGBXU8CaG24Y6vNmtobM%2F6JymPF8UIuP%2BPuYQBW0VLeSrfJ4S6Vt0AODdAqCnL54uy5GFDYx4v%2FSiU6AKQiXdS98ijnU8p9%2Bn87zcUnsBdys%2BptfQzHKEKVj2MehnmZG%2FarYqHf688XgJazRr8gZNq2KVkMTd0L%2Bp370zY3kUgZ%2BfIl%2Bgx4vX%2BZqTcvom%2BiHEJJtSyhcg3fRqFBkuPimzKvA%2F%2Bge4VN0cDfS%2FITQyDbljeBzqDkVL5BMPGIqc0GOqUB1cBMlGgQt66S6lgm3sZ2T13%2BDtIVfP7Do1TUp9vtuw3Y1KaUYps%2Bgw5ys%2BvlDUSnetFN1LXyh%2Bh092hhobsY2Ds15irB5uKweILxUCt43PqLIiuGVVCLC6RG%2FTJuglWlbDHkbgNa3n1RPA9JMWX5xdrmOxgb96yNuXaSkfiMKhfeDFTruGmmzrt02NlTGIL8h4dwZgc4e0h705fw%2FbOD8BTkQGoa&X-Amz-Signature=a21bc72bcbecfb2c60f5b8b1bfe770df822dab7146dc9017766073b34739a6db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


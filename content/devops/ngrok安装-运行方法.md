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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO33UCC6%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIBo5AWKBTynPghnkurggeqKGdlVYTallqGM2H0EWhcRzAiEA5ORKhZG%2BNhfnziDWvZTh2tx6fyZ%2Fiw6q1fkvSVzndWgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAqpvEb%2Fewqlp0oXqyrcA6fLW%2FKL1esLPtzO1mIkKj7O3C%2FKge9DAr%2FdThPZUGIoQfHZKjxlsftt2JMpapeGOUvaRU4FBg8EC5%2B5w6wO4lEvSRUi0uiuD6TDNfEcblFT6YqyvLN3zv4S8SXxJOcgmccB5sd%2Ft6YcY9OsXGJlFZMnTwR7if%2BxAumjhow5UBS5vXPffTxeIGCeVZSZ0gD4JG3PLTTRYrt%2Baty%2BnEd6%2Bw%2BupToX3%2FCocmmEvqrSNp5DK9VD9UJPhyqHTA6wdTpVHvwyYa9HmTjaMQ7AiMpyz1BUEwkhtXBaprpuDESx1Eek9WrW4N1hYZ575OIuwLKrYYkwj5VX1B4S7LbYF4lTEKYLec%2BWqjDsd5k3AIIsAbuUyrkObY0FBUgX%2BkO1q%2B6aLE9ZnIVuSDvbf8S4jbpD6Sye%2Fcb9Ohze0GX%2FF0VlNZxosLAI17jA4fE61vfiYo%2FaNf7IVXoqsCR%2B%2B0TXkUoVzhfNYNwYSI9P9%2BHDOxv3TkfbXknHN%2FSGwPG%2FlhWeUqhe%2BQuPbgdjUdP1mCK6%2BBGqaBB79ApJTTLgZ%2BLEUTA1a%2BCblIdNJJmkweF%2Bobowz9oObjBF%2Fhpuu8FJDCq6xheFLSRPgG8fWJbCTX6wWxoZ1JUl4cp5tge1HIsqiyTXMPHWm88GOqUBJZ0vHz1GbtDxeoJs%2BVsngmNo0FlyANxtH%2Fv%2FTkVIHu5EXph9hBQ0kYFPQVRLSCpB7YBs9kpljXl3SpexOfLi3y%2F3zVqDlpQJ5PwZXS8G5y2HrFZKt797lXFVurLj0qIjBnT7r6zEbaXWVz2iImCabU7BNB5R5QTxaMk30QodtLaRS8UE014Y1E68XcR0kfWCGwmlXHa0gECM08pD5cc8Q2X4AxNi&X-Amz-Signature=7bf585bd1637079b53584ddc721a884ffada69ad651589badda9606808f6b6a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


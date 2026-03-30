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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPWOE5EV%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIAF91KcKWRQD1q06SoX1Wv4K8MtkQ40MI%2FuX2%2FSjqAKpAiAyEZO1OFXAxC3aLxrDP%2F7uCXWou8k0hYVEe8wSsbsk0Sr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMAXzBE6jE0Gi6prlWKtwDktg3E%2BjneYDQNpo5b57watoAV3NcT9qCLXXIn05aWZ1fpxwJXH9ZnejdBXaKCGYqRX3Wye7fK3sMz1bM1qHp%2Fa5lh6PUeKbZwqdDbjqgyCZhF2KcVYFplfmXeya%2BWcqW2I7BLOzTnZxj8QVGpfREBxP1MfmEHoSLQVGqyxREsawUuAJd3k4%2Bz1KUSTs84bk2uqhIfiqhih%2BmUQsssJNYqRSCdmV8z6dAzSq6HZfMJujSUPU%2Fj3Nq4NlYywvmj5lMwsS8dn12jSFL%2F%2BA0RikuMGe9V%2BO5GKCTuwi37gR2Y0SM8HC6JLBN64s1%2BVOLofv1JRZUuHctc1eAzaIa05519AGBUFbyP7a2njrE60xn995yT7%2BaTk8Xgj8ByjVWJ%2FRFr4yXiju3M9e3KfyoNC7A5JjjxVlqdSoMeHRzG74EymWJHhQDj4ibZ5i%2FsTLS0%2B0R9KF804NC7djiXV%2BiEd5DoC0zzvrW%2FqLo4usVcXeuEAcS0RIoeQl6fAodRsHWZ1w3A57J8SjTKkNXcS0jrIeh4QOevieWNnqhw%2BH7mzosADxH9yFp0q1v8mYfOeu4YVE%2F90RbY1saDlLbPG6vekEFNxFe7drKVi4n%2FloqMoRn6LAd0hDXaLYxywx9tu4wtsmnzgY6pgGLDo1%2F4VLsPO1QUd5tDRBkwNaUiBWacMT4rtLZ3OILyFx5xdcHNwA4X4UjsXkYJxQDSloLN%2FYIQteSF0eb5WLukBC%2Ft%2FcUaUTYqvN6q%2B%2F3YcwNBgdiH93YDtVHQFdb07Uj9Y4AeTCyYbFOb1EIt2f4%2BzH%2F%2BeXUf8tYyveejHFraIwa7BGrDpXpl%2BhUR7BF6QBeURq9kSZ%2BL5LSNyEzrg3x6edSJn1X&X-Amz-Signature=ae47a7fac41d2afd45a7b40facfc0666f2c707246a1063c60b731f8547665dd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


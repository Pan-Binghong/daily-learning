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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SKKJJLX%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDJMXVdFXXR0Ozp5q6xo7QJyWwvhirDJBIdRI%2BgefHIigIhAK864cmL%2BcAFV4YlZixTLQbuy%2B7mTpJUkmRi8ny4SFJjKv8DCAwQABoMNjM3NDIzMTgzODA1IgxbvulJhQO8rMDSDb0q3AOsGe1uR%2F3KkzW3vyMd%2FQ2g2Q%2FX0op1ZtUPT%2BtwNQGwsnUR%2Bw3G5C2XrlqTMGqFM%2FzcFMVod9mxqJZk%2BxkR9wtzqEc%2FXQbpnv%2Fel1qq46jMT0YfJCZel2IiRd6n%2F7nzTuSua7%2F2Do4Ncx94NvqYrGQUrRobk4SJLSWVjOJMUcMzYN8iXq8KavO5OsnkWBs%2FGYpAhq5CnMxslV97JFBR%2BhxOudLrYc%2FZR1qcj3ABnlIQh1xMRzciB9%2F5aEZ0VQwO3FmTA4Vb692GY7lUSX66BAYxoyELsuJ1tjglw3%2FHB7CKDLP4smIQdJf%2FvH5pf%2BSulxf1%2FCHovQPxruoT0yk7s47iequ1mdCvl8FNho%2FzYQezMKeTS6rXqcducU1ONaYh5w22D7dYlHeM%2FwwgJqTjVI6NXNOUPvzug5smbtcN9kq9Uwcm64YGREhBM1VzjQMLfmZ4UrgB3QibTYOBBBh3AHAsyzHt%2Bb92LkcP%2FscvGFV1o5KYUq2Dt%2BQ1BcVkcPvlsH%2BQPJoAMFDFE2%2BWLafbBHGIe6XgYkEZQLBs%2FbJ7eSSgZsNYqGWxtLUuFPpCsmCWKlKLcKypOlq6kwLZ0RntmZOyq%2FIGtzktjJlK6s1HWXpFPAIlsURk5hb2AJvxDzD4wrPNBjqkAZICLQ6%2FxKEH5mGxKMxIThScsjnhVOMQI%2FsbMHlEf7KInftPp9LUPs6SbaoS%2F4%2FIfm0s74Oe3qpS%2FWfMCKIHtCI1abf7o8uLIUfnz2lOgRtZzX61OBLXGLMU%2BqDvdbJEmpEDhSkvdMHleXlJ7TpMiq7C5vjqobSRqjz3YKKgkOBHTrg76cPuUzWHqt4zMFaiexxrpKilSLiAiSi4en2XAbD4E%2B%2Fr&X-Amz-Signature=a5a71f2529f3e1f5dae418f1768f8b0470228cd20eb21c2707099751da63c743&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


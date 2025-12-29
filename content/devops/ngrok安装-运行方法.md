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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CSKOG2U%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjNDqayLIKFwmISCmfFsrT8hPsQZNPFUOKzQ1FC3KhVwIgBXhchlUA6hSxLBJq%2B94Q%2B20tOaw0XpdvfOi30hVcSAkqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMyWkZm4nQuMaNEj1SrcA0HX2MWJfAJ0eVoak1l4ZfSZjbgMPL6l5Esyae7Q96M%2FipMmunaNryao6w9izZhuLoMlmI7zGhz%2BSAEFAtU2stAA1T2sSOB09wfjXOCLoS70VLpYbUAdPhUvXBvFxzG8vQv4z%2BNoRlV5T4LWKX5xm5O1fNfgCUvnVyec06dPdS5pyA1DYlxbEoO2PT%2Flpxhpl7NLHOoa78gf%2F0yQlFHXpbDQVZ5Phbc5fqRLs%2BZFaqkKyjuhJcLp%2FQJu%2BBQv%2F7sbDnJJT7vtl6puaeKAmJPf%2B6l%2F5wxt8rgUXO7dTtnlMvfd92bjsVTs7vV8PmTAv0ER7ToyRJytfjbIswWRTnwkabY1Aw%2BCEeIzCrL2BYATPi11GOMxiEn2itA6TQP4RqtpH67mdy0rk3K4lhRGNGTM%2FkB6oi2COLdDo8SF5oG9W35PnjdFaBN3m88aLvdQ7ice1yC%2F%2BapU8gEs%2FMgdghXZIE8oLy8gzQt3r2lRw%2BUoYgb2zy08zCF8VTbz0LvLMAxddU4HK4Pp%2FjYSiWWKeYiPk9dmPeODdtbpNBzTKLvTRcZLi01dATZxKEcj4bJSoAS%2FQZXwtg%2FDb7ZgKvcWspUkruhwq5csEY%2BiNZwQKo2Z0yZKoJFF9HR%2BUHZHbuONMJqgx8oGOqUB3XrBNLDKz46K0fR9ZlVtfPVZ%2FjCgORcVtz60z2n4wsp9MwC55EmSgFqPrw38fgprXVsdBB3vjeimSpBJm2YYkui7qMdP6ihvWmnD9CRhmluku1yVEQyfin8wvGMSm9hkSONl%2Bzg0uDOdNJFYOTjVzE7yFmx5LYEt6lTXF%2BU%2B5ANdyS3rL2P591oC0oEpkK3RVFquo6BRQpJ3L0ldYi0hoe1V%2FetG&X-Amz-Signature=3221c7f1080f113b1c51ff173b6c04002358fbeb3998683db41546111b38f1c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


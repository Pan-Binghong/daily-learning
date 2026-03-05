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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7W7VMS4%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBlj8UnF3XazXXGbXBVLLhPPyPEV5WQWL4P3qXo%2BgFpQAiEAoottIa%2B6QQnB607GSof8HAvqgKRQ960%2F6NpzYScuZZQqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMUTohmslFwMF5gpASrcAxFs0Cl4xuvevqdK142038CM98vQwGvC51H%2B%2Frn1ws%2FJeUasTwRFVFPVP%2FWaw1h6NS8557Tq92Y2V0oenK7VxTUhxx5bAwMao2wDfw7nWCBUvM45%2B32yOGOvgh54d5I8gFbWH1oSKGV6iBHSAttyzw1tLvSwn5fN%2FTOZI8ZVIkm67sRa7lHhyJP9gNc3tgluLW8Z2jcPO2VOZz8ohPJIojKDa8O%2BRzc%2Fr%2F06VaYsh4QN07yagr4yRKgar0w0%2BwthhXxkT2UPzi1Ms3M1sjA1NtbM3Xxukfk0mowNAuKA%2BE2H2WJUEKdQLuRCtv%2FiPXeL9LueSnzJFoTVUGEJUkNBh88k%2FjhBGX%2BrNMUmo0I73ij4vaK0%2F6ffPW5y1GIhgDHYMButUFf7qzsR6CET10gYJxct%2FQoREH2duz3VlphtwYz8hf1anUNV0LhUqm2Bl9NvXDyj1bDBOfvEkLa%2BiQ9%2FH0TZ5BD2uzytrt4tAwNerWDuxu%2FE3aEXknChQRAVcjKNH%2Bx3aU1UnHfUGbzmw9fZTpUqpcnk1HLrK4xCKY8A6szTAIppfyI1Mph99nj9n2O%2B%2Fb45P4%2B3CsZPFmAK%2BwCNAZaEvTrZdPzf%2FvucIfpNgY9qxjEoRSZELCosFt2%2BMJ3eo80GOqUBjiW5tLlqHTmdIocs98XaMuUpDbNwNgS9SN6wGogmucC6Y3jCxSpjkqEFZMQSqbG2Y3PfSYorx9OzM8aAjqPNHTeg3oZoDWC65Z3911n6fdGS8KmpKj%2BNsaB47a2bIE89NGuodkzpLq7u3lNgTOXMWEFGOkPAhT4aXv0BlieWwc%2BJtmTjUxzDGdzFZInN03tdt%2B%2B4oc34DHzp0p6adI%2FWRNhNaUAN&X-Amz-Signature=13eedc7feba0ac40616c70b362def734cbab81626a74d125d27e2c53f9cc393d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSLFTGKI%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQDxXR2mxltEtqg8vLdYBZSKdA9b3oyxT2jMTz1LMO9c5wIhAMy8rpFoDSPToWFdwQrQB415UGoLuknMtaUucY7vki0CKv8DCAQQABoMNjM3NDIzMTgzODA1IgwlhTBropPvnxITDikq3AN%2FFryHQjky8C4%2FnLlzrFOaVuumL2QkktwxYFcECDF%2B858mwCG2M%2FB2tfAmyNlswYOSQs6OgqSF9ou%2BAgTY4IRlGxRkTDMP58v02BV7pVagVq3LtuRHRiG2z6CUArEWUW4cuDObX1kAmfnqTm40%2BlKpqp2IEhHwh2pMzh54YRQzWP%2FR37qv2%2B5LdGFUFekSJ45Juzb%2FWK5vTZP2hFHxT2pliAa4Mi8e73RzXeI9ed%2F3zb%2FJiztC4ZE93ke7cDLJReyiWbm2s9UJHzNdXgzH5WdSH%2FM6ELLE6xnkVrDhBX9WxlcR79Rsu3tQBsOerM%2BCsmbqFzSv0vFml3Gm08awFqRVRVXCi3BgwpfZwbLaSzve9%2FS3ONSsBMcLn%2FLW214wi82P67qOS4kqBEefa%2Fl8N%2BfrQS40jgV3xpsf9VyNqoGarWCgvIro2gt4i0Oq0dpzJLJk%2FUSRO54AjHVU%2BvQEU%2B8AmDE8mDMb8UvnyYL2YpUNBHY9BfJj5hkvg%2BofRaY341u7FcNfAyPUO1Hqm5CERsJlSL7mOejBQSZitwNjArrOYrm40B%2Bi8KUfl0iKQm9vJY9jASWgjxMGnZziwpvsxBxQzYI62nR7ceriFLjZ45ZlBnaHi%2Br9fbfBoAPnBDCl%2FKfKBjqkARv0L%2F8dT73L7FpoiiPG0groee9q6fFNGpKhmjlvD0XfYK3lylWHCBiQGWCUpwELtRyG8%2F4YaF3V3UJYHlNaGFvgerR46EI2bwIAyBDH%2BPAqP3Hm7lJ8Dgejw5EuYJxIkFbGxTtzzVIM%2ButyUkGuIVkyZLU7p2LCv3aBCzlTO0W2g%2BOwcH4YNzNclQNjjOe2Mlp3kRLzwv0X8dYlfMcZN3c8mnjp&X-Amz-Signature=e0be49d6772321f8a6eaa85d65ae8432411b8259905b3d5062354983497937b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


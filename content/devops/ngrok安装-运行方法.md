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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJFCGB3R%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTXf1GW%2Bjo0striahbhjvSHGYTU33oDLwkdmZ%2FRCdH9gIgUJbtrgRIrNkUdGGepYXD%2FDM%2BwAK8STg%2BHQcgHmxaNb4q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDJ6zEiV7xwEoktfj9SrcA5ETiBApbsPs7XSEqZKDKy%2FMo7oywwhGLS7ZCarhl4Y%2BRct5vdDzYILMvoxIA0%2BjWBfTC7eJoT7M06pvUM2n%2B3smaX1NdplkFRS1JGs0UXbgrZc3v25rIPKg0RlB7CW5Kmvtycrnsf3Ov5gD0EiGhXmIe33ZTvSJwt6NlL2o6LySkgYk2qx1%2FoqZf4rJ0BOqFqhHIMpKJSIFB1v5npF0D3l7fxW26rOAD6BXbz60hh7xV18Of7p7zQ0l0FCCYGA9HVIkDoK%2Bi1bMnzfEZjvWOQEQafrsDrdYUtTHlbBX22PQUKLiwtSJ0WGKPYxzyRddACVehDIIIphJC%2FbaOQX17W%2Fu1PCyty5HruvqV390AKywo%2B92w%2FlGATpi7M0A8WTD65OmpQOvrwB2QqrkCURqo%2FlmZlkX7kGolV58bhIbzV3MDDL3ywY9WNWw8XRlLrzn6oV0oFYPxUac2zND20vkyqG6gPuODi2eBwDk1K0OjI%2FOO3vH2JG3P09I4mG8H1gTSoHf2eIAnqwRkaynb56FtMDWUKyP%2FVpiF8ypC0MUajl7uBaJOkVqps189HFF%2FgTrvUY76yyqy1ern0Nu4md44qjqyYW8fYIyB4pnVrYAOjvKb3WhSAVWrQTq204SMOnqvMoGOqUBh2GjqhzsMScY1NYmf0CQZ6vNkUY8%2F%2Fzo9EWp3%2FA1QGA7J2thv%2FPnMb0OzkVkiKyceuvix6lHNOLj0DxoYc6yuF1YPUIyafBkcHPbDjCLrTiJHhHfrVei2ONYaLebqukYv90sc1Iky2NTtUmXd9r7r8kZOx3syK%2BoqDlJmg3HZE2pnOiR6Cg0TF5o6SMWg76SPPrTUI2uIl%2Bgu9ri5E8vVIJykqY7&X-Amz-Signature=bae05ec8f0a2d3de15d3ad13006e46def72213929c7029225f3470d3f917c589&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


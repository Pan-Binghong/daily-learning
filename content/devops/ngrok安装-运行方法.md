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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QPC4WLI%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIDrLGN6v4Dq0QuEgWAsxjgBVWswI9epVcm%2FXQWvJfySSAiEA%2B218Joi7magAZ%2FMLx7QHYSt1iIBbI3FUYFvOymwSztMq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDLovZFDT44dTCHgfrircA5fwBUlyY%2FoMMP%2Bn6GnMgePR5qw2KVSCqTtZq87dQjCqwQh2AacYisotAY7FKJ5AJ%2BtmZeCyul2HhGvNKEnjRsncEdRLEVfUK1jUmcXvuIP%2BJPsnOEe8Qv%2F9JGCPQ6EaEzYTp4ruNZeWjhi15%2FNQFc%2Fl3bA%2FfEIxl%2FsHTSyMNCGM79UquhMl1YHiHE12%2B6BseIl1CfUtcX%2FIYtUKVYv%2B5F0sQp0mqDZXohxT%2BeuZyJaygalHPtmzdW4SX5lLo2iSrXIJIx9GOFR%2BgtWg67cIKakHQg8Ndc%2FeD82lraFruhi1p1Lvp3sO0PJo8uKnK9hau9w7WwgYVdADn%2Bd1XDD4LWX6QoHHDgLpEJco%2FF9CMxmiDwaUwGzC4wDkg1c4cZHiF2KovM2c410%2FJka2oApYpMWJmQGrnBTXlgZjJV5KDap0J05JQKdE7efXSrTrmkbz9FbXn6Ceg03VbUQB75%2FZcDJW1Djfeep67VCOdZZP%2FmyaBOS2PArxR%2F36NQGTVfKzNCF%2BKrL%2B%2BZgUZkVhPneDsIiCfteAFUzEPrV5Dyiw5sJr9YCnGqWxPAjs%2BFUOWhyMdQY%2FMSVFkkqImYb7XDNBds6tYDTAmvuTfjyXXLfe2pAldtb7RiWxyc54vsrBMPL34coGOqUByqq%2BksOrSerBkBaP2Ewyqe6tdHvQdxF3azyd0%2F8Y6u2ws0DR9pOHhOmeXi%2BWdopxp1TPNDauYWt%2BaYqTcZFuRHHzi1RhT6cZkbJydudQ1dStT1BoyMKE4PJJqwL%2BQ5hsDZcRNAAuZy5AvL%2Bjz0uw3xSLXTBv7IcCKMRzgALCgB3qEfft1lQNjpCIg3dQO28TYAsJBSQXvjzQV2hT5Z4DZT5V5wv%2F&X-Amz-Signature=84d3f311b419f48b484292345945917d5e678b6ac3fc6a01a17e10d250282953&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


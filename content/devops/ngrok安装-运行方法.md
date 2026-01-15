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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEHUMISG%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIEnxhD9MR2YrA2vPcQG%2FMoFKffqjSebejdY2jprMNVX2AiEAqzjKnoQvSHrTG0v%2FD0lh5Kwl4utsDDiBMBEY10MOjYAq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIrvp04hX3jJR3E8oyrcA75RI%2BdJt%2FHuu9ubZe6uVsBujbvV1zupSNeKYRiBX4INXRSZ3RV%2F0P9WXZ7%2FTj3Nd%2FhHQsgBlc8cyr29%2FQyG04jWjwzRVoutEJNmPGp5S7Q7nTmJDk2giC4AMmnwKwIjK6BDTX0wBxhI8s0FmjqRIZiFUalpz4X4i7VInORq2Kq%2B1isXRmh7DngJpI5oGJ0P1nDyVAB%2FcT38eslcFVkvVXLyggBeQmZxkeH%2Fy9L1v%2Beo9a6PvEnldmo2vev8%2BOvTBQqe9pVJmjQpKDCTCfz1FCihDGDz85oCXP1%2BfFdARzpx4Gh42HdFkJga4PwcoEm2FAAQCxgm2TrfMdr8AnuHyVpZxvcCCm9%2BBhKosOkKDpD3umgMLjY6si%2FsbtDLBGJCYR9niQW2aqjp5OMApsJimnBMSShRzVm9340tuFMPl96KYRZaxqeudwhqkPY6C6TcKFq0uGtFWfmeVBrwft%2BtykUdvWgDbeceQgkz0Ky%2B5PP0HMPhnonh48anjWde5yGEpPLzAFW3nLvLftV3IsdvwDW44uEwrmAIYP01wJpHXYSf5F3YmcFIW0j3dZiqUd7X%2FKd2NhgzCWA%2Bxhkp6DSGi%2BpAriDYnw4vnsx6BGyYu1Qf406RFKprdyxryiZkMNKbocsGOqUB%2FtmAMnV6aXmPIDPvpF1WxN278xtO7fL2y2SLn3b%2FTLNfodlp5uoEnVkQTlfaM%2FjDwk8A8fxcIbJFCTa%2FVUb%2BVivOz2fLo%2BLpDfXQoMXxH5XSKX2pXJ6fWxMDWz2Du7xyARw2bsU0qVq96VGUvYx8gOfa6KzZcSxAmTMCRr352M788Tvpwtd9b7F%2FqP0FA6T6pm6UevUdr%2BnIZgDz5mAEIUBwkcov&X-Amz-Signature=4e0bba696115c0c71a5a6f96adb760bb514bec124ed0f39396a2bff8ceb2ee06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


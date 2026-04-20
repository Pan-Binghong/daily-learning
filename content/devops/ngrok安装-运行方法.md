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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJIP7FZ%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIBb8SA8B0GKbcGwY9GGL2pVmaoSeejG0ViTBDJXZWPPcAiBMIFQeD2X7wY89vqeB3DaEjHOIWwLbp5uh95voroN6Qyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMSpBqm1%2BISGsQN1ohKtwDQV5TgX8RY30PM8GufAEUleI%2FKb1hcXjz5C8%2BOM3jCbf6%2BxtB%2BmaOPuMWYuNFh19NtzFiZ47r7QlyQh3XKMIniOOhLp8zFkcCg5omLAv7Oc5SBOjp17tDsAhmNN9JaMICjudzSu7ujJNLGRe4dqqHiX8iiwDOrv6JIN9LeCXUrZCTce0f%2FT8rg0UrrYBQ2HIFB%2FhsTr3VBor80H7tYsGU29nwuvGeQhIyFXEadChEmCABK2hqzObRhGSJExrymsgOoPp3aCpqTzjIJbooON0UsjL2mL9NZzxp6wHdu3kRtnO2%2BYAVQkNfOABTEmeaTtD1s2LlVSIbP4WnXB3oyi6%2B6M8w9tC84Znrv6T4BADC5XHMSE3cDOO8Hreh35oCWmjjyT%2BD7sR5CCg6FahW3zRdDul4OiU8ciE2qKfa%2F2G1StHPazpbrsM5eLKTIeC6ZhtrD4afY9G675TwTRJW6iEwMtRxFhTgUsotF9%2FhVrfbQGE107ZUHj%2B1ZV4PezGbJPWS67uoTffnRez0YTvfQq0HIUT272cyvynN1Zf188RDUrn8GNA3EuRZtwGy%2BanhAhVW%2ByUwWExKApLl9uE9wc%2FaJILeBoKiDC0J0FM4trUYQqGgefy5TXxMXbd5eWUwj5aWzwY6pgG5CR%2F9JR41YGzTRYqQufXeWoWirH8qxlgUp8EUNvITi%2BS0q7r4jv4SBF1AnSNSsihC%2Fzj3Ee1j%2Fvq%2FIZLlNovm%2FZcPrBM9q6cjw%2BPsSAJw%2FfJl6BR%2BJFRSXWIZFzHdTy8VSThJEozRZ1sOMUYA9irQfTrOW5noBc2LD9hCHwFqHSvaSXj2qEPquHMx0H%2BlPN5yter%2FKU9E9U8FQ15Srk0rSUVouKKU&X-Amz-Signature=29261607d5622d7bb5d687a7b8617b84004f027f7dcb32edd351e22952b035a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


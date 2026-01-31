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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FPRBL2I%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmpMiFXS9igOQqGJjJuT0YyD2dbQTONeuSCSjjeyzFiAIgZ28PpKszZQquKelwimKXZvxoHWDRe83hJOjzji70Ef0qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzYihnDEec59KsW3SrcAxQBFegkhjRYWQVwLSk7DYI7pfVkdrUy9GEuTsIARYmb%2B7HVsATtw8%2BN4BHQo3uAa0efmV3uIlLQGHtnNEj7cEpv8SICv0Rndst2KRM8d%2B3irq%2FKvS8m72PWs4cZMPtQtCPYJN3MgyhBgDTidjnxEMqJFXMuYY0tBonzBXjnwmrhpK0PfKtlXcloJV3WOYz1MWQyhLD8KjtKiXj1LCJbys%2BeKw0iT4C1BVvw5ELOwVivc7y4BVRVs7e%2B6%2FDmrW6OV4qEdsSy6obzlw837dXNtt1mvowubw4HDmQBe4LeiiJt2ipR%2BhJj%2BsRd8ibXTxAxNeoqfY4jfdLkSYB3nx7JWmnjKyRYo5KHKjRdfElEsXu3VSOj7Bcj6%2B1tWUl6sl8Z03MTiLiOeINLH6dC9exuhmHPcLv4P5T%2BjYxiA9EoUp7lKBNASPuoBIe34AZty%2BV1I2zUxxUmzTKWu8i9RfWxfnfaXt8BbuuW6JpBL6tHnu4j95z48NEHk7KttclZ7BYXqtXXUxyiOc%2B9ZmIQ%2Bi5L%2B%2FzYufhZzOM71esIh%2B3AiOM3PdHwpU7S%2FxFOvL1JRRgEYFr%2Bzehyzfr8gbLL7HePuniqwxtE08cfvyYn2h0OqOq1VpjGdqzjxyCpihIKMOPL9csGOqUBKYpLu1tZLJk%2BIvZ5ytJ%2Ba1Y6LtwzjTGQ7mehBoxR3Wi5bxzIZtqcKqhFsiMoEjpZaNMxMswtIQNE4JJVHKVcpzyueXqwWgbd7ZBULo9107UwxBl8z5PSwyNAc%2FDfFr6LYENJzOHTW26R3rOOWCSR4yH95oWtp3jT0%2BdQpQ1dQvjLEULjw8AtjB8rKxTpvMvjm4idaWIY2Y3xfeW9M%2F73c%2BwAilpd&X-Amz-Signature=35afa28c7f6ca694420e049e61f8e01422c8ad4e754e80bc782d9ebdb2dfbf1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


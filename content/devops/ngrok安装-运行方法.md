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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGQLV2K%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BSKt0j3zS8G2kiWejENWjy82K3a9ga4RQ92hCRJn5HAiEA%2B9ChkcGPWyKevyB84Ehz6ZzpdvAHd%2B93NLoYWdGb%2FUIq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAn8ZcJNwA19bBltsSrcAyD97vj4pj3i2zKhhfBp%2BwY%2BRLr0KZtyc94ooCC8Wxwl3DgA9w%2FibMhr03daNij%2BI7nmnAzjzfnOZFkwu2p4Ron6JINW1dgpLEafJkNRovTX2MZ2EqUtqzsS5zDJD92QA6wNP%2FWevD7LnHRb0DvkJd2y1sEj9SXwYZM9ZYuwmg%2FbbKwcMZJlAZ32dMnwqa6o6uK4sjkYeyYRrBIo5ENzeNB%2BNG9aP6VnQ1UODTzp2pU8ar6gKTUJgWI%2FFu5cjwN2S98AS7fobbZGsOlyNwjWFZlWGyGD8EymucC70le4PufPJUFTOQp1Nd%2BNZhPo5de6YTC7%2Fvdgr82CAqFZwG%2BJwwvMeLaMccZkGlv248XDNC2ZdTAX3x9aWuq2Yd4VRr0P41LFma4pmu3a54ie2qjjI9XBoYfTNjz3VKuIxsCZRgu5Onl78JQP814gw%2BJ%2FMGYzr2DZCK2Q0JAUKC%2FYgszxXb%2F9aEVq4OhniOm9DPLiCksXslaxkIKKKSh7PSeADNIV6M4Lgdy5O1h4F0NRNy%2FvWaTwRPjDoLZ7fLMpxL2OqY7XKwItypDrrq3liHWoa7zZMKWfV8BLavqZMi9YIhmI7305ftwUGItPkFpXQ54blv4htoElvZ6%2BRpw6BtjUMIOxmckGOqUBO7vdoBjC4DIZbHWZESJ7Bob2XXR3%2BbSyL8CNH%2FW6ZeHfBwvWc60eQbM621toMgODO125MFXRbhvkWkQtCU49fQrWaGTw%2FSEw6GfR99Uc2LojXW%2FCfwTfDKumPetUXIqldzZUorQBqKT0jErx%2BpoiyppQq6k9ydSXx8lxsMXslkF6OY9g1K5G4lTCKMzgtRiLmQCzoL%2B%2BxGd9QB1LSHrdL8%2BVrGMl&X-Amz-Signature=a567782eec2693ecd6f159136456be7f1577e14bcd28f46c18fb24c15e9b5e55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


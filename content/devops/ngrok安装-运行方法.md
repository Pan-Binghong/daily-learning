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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIX2TGJO%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGl45ohwQHNDTrAoXDN%2F6qZ2SPIqDhmIZU9HEjNv4VEPAiBJjF1E8uIO%2B879jzXFoctuAxW2yruVtvQ2ilFsFz2%2Buir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMH6d6duWtcWWK%2BY6wKtwDOzbxzwbpnF%2Fn8pAu7ZyP1F5KCSeefWH5rMLUY3c21UOzIjmT7EmUMNK4KtAHOcg4e6%2BrD8KVRwvC74paD55X%2BRh5RckXVmd%2BVtAdvryBY8fGJZub%2B1iokfR%2FTjzPUcssAyl9Pe3j%2FeK5B9KQir%2FR6FWsLNB%2F4Pq4d3mckEzuEFFp6DHShQ9AEOqdDW0rNwb5337jldg7DYaVcNHnZtrblCLm3%2FJveti30QmIMOnZgEQcOq2Oi28RMYDLfkNa27yH3dyRfBiGDQlMXOTZ%2B6DngHD8sJzchpRSUwf3Ysrhlq5y82C6XCTDVGKHwxsnepMBSCLkRoHoAV6bm35jfloipbX0t5sgW1YWgSpTD%2Fmk%2B5kbTY0cO0DncozV5Vh9G5tFHNs8uqFKjNuaOys%2B%2FSexSIYEOsVJqSOZUssbqAExHcOWxn7s0h6epHOsNtyLZhxBV33ylqzs%2BucBY93BIjDefsfQFYKdsooopoA7BtpKJrWFKp%2BkLPB3JFKWvzsgHLXby%2BXadvl17aOU0qGaEzfsr6xaAkOrC4MU8lWHVhnmu%2BxodAweb%2Br6BPzy%2BBWIDuksd%2B2Tlh7tQgdzpiL%2B5l%2FUrcHj2gHaUxh03c%2FGR9m5M1EgeeL7%2Bhb0pAjbUEswzIbszgY6pgFIxupOvemk1C9E3tfMgl2AjUVjul%2FAqVV3mFg%2F%2BNXWt1mnTx5B9p6tIpfSBRGXZGWLA%2FKyBDgH8gesEFyVdGd3WsYu3fnORpnoINLVrCMWAwfpJi%2Bh1uDYDi%2FpS8xNY0BAasPzA%2FE7d%2F8b9%2BbHaIxMf%2F8amBF0GE33kUVGOx0cX7oWvJ9jBf7KJqOd9%2FjvUUJPlF3L%2FtbhGrMYDsDXcpAn4le7DpP2&X-Amz-Signature=578048fd9e6359a01d843878f69b3c077ce834d840213a168605351954afefa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


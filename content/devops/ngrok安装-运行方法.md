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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP2MFMOO%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDtHTYpGs7C%2FnX2DnXNXwFPZAWuOnt8%2Brp0NpY4REfuaAiEA16avwWmMkVzWbGcObQaQq6WdXUdk5BqlNxaW8Pnzq68q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCCM9eYl6TAbDKZhLCrcA1NgKaM75%2FSMKfmhVPz0kboEqaFGvywrg1M2ouVmSOcgJYFRt18rLDmAp1Xo9YgU7mxTzfxFTVycooVm4XckpXVF2I1rZpz1NPjYky7h1SPSMSBgJ%2BLJYPr4P%2BbAFOTteerXIMDNhkN5RNmgvDntWFyzVPjDSNzU0PSWC4xQ6fM0tBWfobLfUrXymt11YJrB4mXiurfBR63HdVTK5%2B6WiQCcM2zBD0srgLBP%2BkeKOLhzxlvKMS3ifrua0WiMLcKz4qRuXDnZZPq9rFLVqR9uU7WsPO2O2E7RIVJQyh3klcDk6B%2BKtLAOO2%2FtmczVM1DQ64XxI8FhuKQ%2BvVOa7ZIh81BqPVuxN7ShAIC7pYLg9IZb2qk1b%2BFIK40WV9M2l66tL1SsemguxiSp0oqWUP%2FwYaYXXiavWKbg6B%2BqLecLlPR6tIV3Blw%2BxFA0BhWfOGbVxfiVY0OVdQBdMtn4xs2fEhDEF%2FxuepPQNmNA4n%2FSJX6hIEhH%2BS45FYQEzp%2FNq03ipjsHgQ6rJkrlITBUMpaNCIr1%2Fsjq6Jpnq9Iq%2BP2t8XI18LlKiX0GvjEBnelFw6Cam%2F7EfoEpa6GnNgMKwhsk1EIBiVCIDl9g%2F2XWgj%2F%2Fk29FyYYNG1p7KYWcinrIMKrcjskGOqUBVfijz9AugMcNCcyONX%2F0tI06KmxAyj5NFMDbCu%2FWtl87xkfLur%2BZ9Up7%2FORXZmZIaGdMxaVOkqFQEOGPZkv%2F1ucdrvKwW5FmpWr04zqF%2FLxYvdR6CGhLXf1gmMFiSrhhmGaeDG%2FYhwlEsvYyc3Es%2FRFy1KFrB4swMjFfqOYgnvNpAPPlPiVh2YxMlZtFWmR4t0XPzEzViMUEfsFNs2Ddfsf3Z7r0&X-Amz-Signature=f4f165d209eacdcfd0fd390d2b2455e0bdfb31c4976deb416fe33ec31a20cf72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTPNW5PV%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2FXjb8bLK979y7vJcAyxlrPVsVq%2FzC4N8A02DCIQzKLAiEAqNo4MaH1nG1d0LXJOSkOi2x870lvblmua890SBNJAKMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyQG50a5ZVdVXul%2FircA2XAJ5LmWfTqHlX0cJDjfUqAYlJBh8MXn2bLtFh%2FEIoDY0JaLIdXTzPAP0tHlYi2Odk3Sz45d7EuzqV3kBtOORX3aGMPAj4v%2FdZYpT%2FYhqA3mrkabpIe%2Bcvn0Uq6Ii3Y%2FJBy%2Fzec9ancSF7m4osVhJc3aDwF6WLJwRpAAm6rWx86TT0fUc4%2BIULIpzLYjl55Dy2g9kzJ3Xj9uVU2OItEe6%2BfGlYm2MGoFdtRM74iLJh1cYlYoSjpb9Z6Hnwgt%2FWcSvKUMrVXvGpBfN4FiGds6Sv9CxazaMZqy6VvWyjI6kzxSKE%2F40E4O5swxu%2B9H6HLo2FeDWNiCRVFAfMqNzkt%2FernqUbNTbGQlic87%2BQyHs1y3uM1YTS0EwyrfFXYMOtdoicOhOqYSmjNMxrCvNehN3CIoCBkbMlkSV8B%2F9uxv9n8yVfWkimripKpFDP%2FOnAEAs5cph0pPHerK%2F2amTnaicDm5JcNZJK3K6QQW2kV5SgFcU%2F5OwbkvFxheMB%2FCw%2Fqr9EphaBqefE94e44Y7o%2BuSqB0z2GtKFEpdFbKpvTLif1Du0muqqWEUgF1qK%2F9GqoOVN53Magi3fc362CbYzjV8kzw9vzdV%2F8chOFDv9HADQh111FpZrKN6OW3x66ML62mM0GOqUBDRYpmeZFCtCivThHJQhl55KaQI0WaOVL8HPgmO661rZiMCLwpodOaTpLukch%2BSAxSt7f2pi1BSBgwBdHd2po5I3DLLWRierP6qNPFimbQ%2Bq0pO%2FV4dj2b6HUbdbVXRmJJNR3gBZLmuPZnynXuN6I2y4JeXbdjbFTfUDzrtgJJe0%2FmRQszia6QjcvD8vX6%2BuoBghz7k1%2FeYjGVTmaMIuJXvR0H9O5&X-Amz-Signature=f14f4452740f783ac0cabd7744e44e738e4e1deb42a782f0e3064ac83b45ca59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


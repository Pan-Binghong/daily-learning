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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MBJJ3TR%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCuNeepG2eNCagWMBRS9U0cldexkIB2P6tJInLc6aPSJAIgEGBdGNIzQpNT2ToopBlPJuDiTfSApnOYSE6B5OPhL%2FwqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqP61wKpoJwzDRvuCrcAyPht0dNrBu%2FCzjGRYDzxQb7nCgwIM67U3pnxYeUuee7L%2FGd4aXD3t%2FG%2BRD71XN96WcmG16tQHrtK6OWCAl3xwoyCtCSTjPAJ0rvGtNg9bZxwYKJgspuY2AWxTs6Xx%2FCOPBsJIDUKood1NXYOD%2B3ZuQ%2BDRlTxZ%2FX0m99yc0Nekq%2FMWvlnnwO%2FFX6pB2p%2FIAZpJ8NcUNv9MCSv4aXdqHE7WCF2ouZWSSUH89HESzB8bOrOjRYVzF%2FyErSDNzTYObmCksocu%2BG2683YpZExkco%2BEuN64N1Uuyd3OxjzD%2F8gotQlHX6Y8zHEuA%2F04DYmO0MkVEG8MXcamT8a7bS1eyb3DE05HJnIRRWmzpNQ9Q4moNIfK33oo%2BRR%2BxuwXyLTAOOJHsrvgVTKmG6mi%2Fv0jPWDyTSulLvTeXKhU800sz6Xda%2F2ZANS18FgKYWOx7Pqvm%2FXoKmhWE%2FAHfQmBsNzLBJw6UhXi%2FLQdND59teFSaO%2FuEYSdIWvpasx4tplHv%2BJtogx%2F6jnfOBi%2BtMP%2F6RBn9EM%2Fhxgqt0hvqYCXojvtAHILWzD%2BfKW9nq4n6eljGsSwLe1at9nNvouPKCc6GnmZj20ol%2Bd8edCajnvNydT6L2xmSTGaefN1odmxnP8xEyMMT3kMsGOqUBWm9Zft%2Bcqo4S9Zgcy7134m6YUsjpV2MXuXHkyfJmoad97T%2BP0oV7y6UN7MRkiskaXWhXKbFalsSph3GXgC8WIsn9N2pt0hln1SEzf93D4PEZipkkez%2BAz%2F8Fcci1fzTFbg53tPwWYhr3oLIbWaLFRTT1s9v65N4XpYIMwNzgOn0BOFR%2BU0fWy%2FAxQ9m50GQYG0aWplKJ6hWK86EdRcN%2Fk0jDr4dz&X-Amz-Signature=259b4fa4c1b024d63ef0f620b44de88c98b46969a949e657eef06752ac3131ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


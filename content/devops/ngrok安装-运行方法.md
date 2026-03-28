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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST7XOJKD%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQCfxvhqUpcx%2Bo0qLd7tymO9S12IfQ2fzdkyLWcYFD4h4AIgC%2B6JkiFjHE%2F3xcR392ZSdew%2FfFDvEdlQSedhtKWbAmwqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPdJIx3fpiFQr2vSvSrcA6cvLqCQhABbukYGR2PjupOfaeB14XhmemsUgsCcV2OohuxdOEXoKhugIKrJAo4bcgxCIiuVOqzff%2Fof2xT1%2Bc9DuKOCRBRo5S5MtSjWxc2CY9h%2FIs1%2FS7YMDJqlb6ksczOj8iHI3dvZtYM6zmpTEcqyGneGO7JR9iExI4nEuD89DQgfYyqs%2FoCA677p58QACtBYRuGvW2cXho71lIvsXI86YHj6wxtYVr%2BjT22DIQjPPrqn0LwW6tsPfk8a4SDDQFji2y7xKuUD4I3Z2r7YQReydefJDvhfW7vpifCZPlTykTAtPB2Tf1Tou8uivv3RpBCN5vjuWDDmxGweYHPpM775AkovplvCSiS6NKQDHcI8uqC3IryKgnVp5x9u5IM0aJD%2Fb3%2BbAGabp%2BzWJvI11C9ewqgMr8AYHP%2FMphchrFBHB0ywY6ZYZUATdA5V7y7c%2Bb19dCzSLwUxqxVc4RpMiq4CoWgB7lc92DYd%2B%2FAnh8B7v0jBRdsRwZzo2%2FOTcrNq9s%2B9blAuE6Kfr5aioP6snchob7MpivIWY3sr7PYnmzA4VPx1flWdZAm10xJPXGE039xu3R1FxHfC9Z5OSHYm%2FZMNUWVocUB9ECY5Qt0%2FPSeJwh7SXS4TcpE9KM6%2FMIiMnc4GOqUBQ5OB7aUyMXZmXZre2HwpImwIHjGDv7hZovzWCBGJqPqOcwlB6xYQXGZS8stk6U1EkQRAy5ZqkDBIRYAK%2FPffpJq6QvgE6rALeYnvt6UTQqZjUNnab%2FTeP6fY%2B7KeIlRAEV1POHvoRgR%2FVQNEBOC%2FC5Fc5mbA%2Bjuo63zw3cL5CrrrmNQ2nwMdWMxtcvPg8JKwXx7k6scG%2FOgeeJRfV4xG7CF2%2F2TS&X-Amz-Signature=fa6f483d98d65ac6ac9af4e7c26f39d463ae6f150b94efc8402864e9e3663b22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


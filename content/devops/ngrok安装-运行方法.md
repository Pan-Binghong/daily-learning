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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7DNT37J%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoo7IC3nnOKNHpgo1GBB6aovd4NhUX1ShZ40a3RUmsLgIgGkoDWlFpGSFqF3TRRtg2ZKDfB6FgBVZaNZfa77nkbxMq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDIR8FP4B5xwIshQupCrcA8A1N1nqro5zWlM6THvtO%2BarXRKy047EIUaQYrGVgYsttvkLoaMpIn5bOaTEuBm3vBg4OIaP4TsI%2FgsI01rHG3KKygCiLglphU6ub2IfSrgGcM0ab7WPJ6X1nYKWSahmE%2BtLlmtUBerufmyvndGr3u1S77fyJkJ4YP0BFOrJ2QOguWtJdawvChyM4hT7B%2B5rdZq4u81m0FFRlK%2F30Lg7%2FIOmuhKjgBG%2BGcnClE5yTj2eyHT5PSqa9zoLV7QAmk9v90G6eTJjbXrA%2FzBak9I6XdGr77xC64NCAfi5ORuFFIjLjjr5OaEFEMq11PiIRURmMWN%2FFWcva2IMTW3xCzl9GclEgHxu6vkk8X6oKzr5hvxABM63wvgsDIjLtDTM2Wgc5lpX3eIPovS%2FqYMtPWXdqFpxppmZAZtowYxs280J4UNkzsI8HvGRjISv2Qy8vrhgRgS3HynHyKsuZWE9II8Tbh2aqdVKRjLuC30taq713A8XVNvPbYYU7aMfMOJSN6WgwigpJdSxjpLNozqlxfJD9gkAfAT%2FFhCnhirLNJFNiOvfOwh5D19mKvfeg%2BaClYzlXKqJaTN2Jeak1KUQjP9Q69KmJmVz5pROa%2FTE9aQ4iPifoET23N6Dg0Ox4YIxMNigps8GOqUBZSDFG9bM4Cx9yCvB6juXMHZBDkfyeSaULD0kpXmVQVx0Ex4qGXUYJyeDUvTba7W7j0AmaGaoo2pp9YMNlVLw%2Ft8dDlbzD40Las3ELj5WW7fegRoF1XsLK15bn5WoKkh8Q00YCvHWL0%2F%2B8DVB28UQvX6OJUTKW3bRyQM4azjLNBSuUT6zJ%2F4YsiBl6WF5xZipmr8bRzcH1lmPqMa5Wp%2F9GT7PZYa%2F&X-Amz-Signature=6c9368828f96dd3a7e7a1896a5ec425f60ce6bb0d147f2b22afbb32d525ae0f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


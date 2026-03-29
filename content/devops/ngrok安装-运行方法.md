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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X62WANE3%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQDc2GEOAMqhD2xvT5%2Frh819ya5U1Md40ZJ54Ht5WHdSaAIhAJJgtJWw45oUJkT9HljzJMIHLcwAtFoRYwn3xLL%2BuYKBKv8DCAUQABoMNjM3NDIzMTgzODA1IgwRmN3dc6vW4LuQ3Nwq3AN2ieaPyh13wH8N5jHPBfO42nMsUPXsvglnjv2%2BBK2HkT39RYQU2yTPujw9xcXhtUyMxZ6oGGY5yvdZIGnhZxt5TMEWVsUU%2FvYMH0aIPJHql%2BVf0SQgBHtJWM%2B9jCi3HnbkRDcsEF4Wf0HebwxkU186CCcIDbfryDW1%2BBIzzoynRTPpZ%2BImOvqwxGgnm8cFXmRaGjjnSG6T%2BQT2lhcgnh1GpxeVQ5L6PdEb47%2F0xOHBWZlI9TgYIW%2F%2FbRXGZCzHFbfRiw0RnsPtcs9hC0jfXIS3Kb8eEvu4XZ%2BzgBiIfRl7OgxX2axn2nfrETXEQWbkL%2Bwj07V8CjSpwV8RW85Hc1FFHEr12qVonyYfEqzRx22stw0XFFflGevU%2FeQVuEDnAZ4NTpSog4%2FcL88uQA17O3woXM8FVO59vIK%2BFTxyMdwm99iZqPbwpbS0pB95DcF8xsPFt2USKgzRGIHsShVNYt8bnwycmCiDmZUBPiDIMT48i%2FTp6eW%2BQPVvt9y6fTDuJBEB8qM81JHdk1QvwA%2Boql1rKIvnC8agkhBqukmke%2FspxCz8k63xwvC619kFvcoLKZjWyiZk%2FmidfC8eK3InishtoozI6g042JHYxlPfBz%2FlEhR%2B7L%2FzS0lCNCHaPDDuvaLOBjqkAdxLDfu7ZS4aHTrO7O6szcLkVHLZD%2FjcajanHW%2B%2FxULbkXeA9T%2BB3WcEN8nkkQMe5LoJtDYlIlruNdwLyIcBy8cRdE9esXiz1L1J05Vq1Dab5vxK4Gg7b%2Bl%2BgIA0LQZ16n3UPb707ivPW%2BGA9DMfE3kqYlvg7D6wC8GMZ0ISmsCFSNaBO7Z%2Br5aBwAVNvvgDk9glG0NKkC3R%2B%2FEk%2FuiE%2BLZouI0u&X-Amz-Signature=eb09bbd93c10e67109443619ecd7a6da5ff29eece92d14b1ff9cba447edd75b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTMLEPF%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAaPc07ZiZbG7h9y6BPhWjh0ZkvTDpgv5e7oeYyQsYOAiB68u%2BK%2FJxl%2FYT%2FHme0T23Ob2%2FzwIhmfxirVU1DkyvNESqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiNQEL58TLTt%2FydIeKtwDs8GBOzmsRv77bZzOLOsD0o9hHx7UYA4DxYwnU2lCpM5rh5Qfq2IZslXXD%2BdoC95%2Fi6J4D9TXDSVzfjFkUqINr%2Bi9JFLCl6dmKRTuy2mFUy8nFDUkBChMfPIliViGXN4IHUB98JTIRQKVQPaHizYe8lnsTUIBk11z2rxQwSmeM7Q7dC%2BEGcpw%2FTr4OTUsIXKxsDCftK2CCjVN%2FW9OHbTpfBsihuIN51TE89njR2ocauy%2BwAA5d9e94GjWBpgodiWQzZAoR5RP4GGDos6vSFkNeoVtayxujt6%2BpX5nvOjdSGimp6f73FERTG4q5JsCMpqK09o4JsCmQulGzaSVIVVY65FA%2FxtnOmaetfP70NFpvdtl3%2BdEGYAWanM5PtmKYWyvpdREALn19dYr%2BCMnvTitADREb7um30c4GFnLCdi86jtOJrS0sZ%2BjKnvvszHWWZmh%2BvJo3OM8OFzt5tmmvpvZL9UPp3xjuWzIjhPhnP%2FzNTnAd12FSzqwycEZz4PCOFCoxKUrzXFvVxhm3JTIfipe83J40OoBIwsB9aI006A6oRn0EpwXvrMd3xvyjXdjCP8rD4dl22Wv2oEBKB3oVHnAIQfnyhs8mihAbTnZBLKfRFh3HFrX3tBwkUI6YDYw64HTzQY6pgFZveh0V5NkAZtdmJmFjOd0uS3n5a6JjrTz42IhITQzAgKkXhvqSMQbTIPM8586upKbhqf6pRea18x8u%2B02n2P2Wcpk17CgTEuT94ejJConG7Asx8wtOm65fWDXKv4IYqiGdRiKzCUUFSS9oybRo0L%2BSvu98UBN%2ByjofyDE9t1cPVFje%2FoaIMpCqOzgk1rxPjZzcBQlPIZUyg9A3g1AWvMZLnDFO3Dt&X-Amz-Signature=e1b8942534adfcb26c8a524395e2b4e2cf9628eb0704bec1fa45f85faa6adf0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


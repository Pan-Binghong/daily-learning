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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIOX6TZT%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC492uQ1knL94DqyUnLJiX5%2BSbREjDoh2vfyXAlOlJ64AiEAnUZFDuvtpmZDOZCdGRt5MpgKsUHMp78nw6JxH%2BSVYNQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBmuVCRaBEhAau7UyyrcA7Rn555nYcGEwHBqIE7uvGEUxGnZztn9QwsGGlBgqDatP4Wv6y1GGHFVfz6tsLr%2B%2Be96g0lBA2inBCP2eBAxZ1xVg5RP1Or1gRNVrN3EQCbQS%2BRgr%2FNipk8TyYFFue18YJ89XCZKvWwmCipk%2B7QMz%2B%2BEmBYV9tcsseETObtJZhWDbXHD%2BSDyjyvJDJ8nfKrNUVTvB80aQhQT0UtncGJ5pA962iaYVJB0Ab%2F7KdQ%2FZx1D4mluD3rmbhb11vxX5rQVNeD38DMxd0Niat50QZTL6n311qKNswtfOTaeEV3RWSWvBOSvlZqS7NdWr1Mq%2B3Bg6SRJf1NxHifvhSmipTURNapHo7guVCNa1i7G5ntv6uYltijAvc9KGZ70wRNjS%2Fg6POidclavlSKaHOa4V%2BcUjhP2rKneVik3YfN%2F5GNrYX39YOmQjMmnskxQmo4skUgrpW4PmZz4zRXppeGc32%2FmCy1I6uH0RXqJsWFXm1wtLjvmdlvCx9yWzu7AV1zI20r3KiYzB%2FWySZDa3YHlf1mwkAB8eBo7N8FOr57h4dM%2B2hz0hgBZ2by3vH718l%2By9jvJHDHH1bPVEyL%2Bd1kB5BfJnWunvSBqhsnK5JZrPi5MD837bpvCUALzGgqXSaDiMNvg5MgGOqUBxxlCp0rfxMf7ArAXojw9CWSiseE5FBYXE59bSEIgcfU8SV417oI50gpJ9TTITqrH138xDsh3GZgsem%2Bl1iRabGOf0moL5q61WHFjPhc7yIg533QetziFktAaMcOvGR4rK0NBa0PhbHkHRwoQT1xjWpWSS3gKsPN4e58%2Ba5oiz35zzdQE2Q8uy0GA3L5I%2B%2BaUWTNs0uMUGZe5JHb3u5Y096yiZ7jM&X-Amz-Signature=d1d8183f974d1b11c7d39c2320fa0841735ac33db754967cc80287a322cb8f8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


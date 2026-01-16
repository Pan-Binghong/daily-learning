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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XD4N3IM%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIBAr6mHmMKsscGqwDx0trWoHSs4hMl%2BP5jWfaORRf3ujAiEAiTgfVImZzwGOmmd1lmdjexIiO8NdP2FWurB5HQ3WMMsq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDHW8ie2G9yuk4k%2FbkCrcA0wRpKlzORD%2F%2Bp8BGssLhzQRAqLHqAnDWrtibt0nt6JoxAe4najhCSmPzi8NazZjEHEEqOkkgRoNW%2FQi7gGlvVq85mXahCtgiBgghzYJPzT%2FArJ1F8%2B59p88lsMudOhrfjJ4AvA0yxVDIuzP3LLhWP8tutNcsZZzWmPLKLFsJyQmj8p5yqVHvfdX%2BuI%2FBIYX2N6Q6hPcHvpzRC2vz3bNFzhbuuLGydibg0uw3EXeWfhjg29SCIyodpt5v%2FkVEEGQQhQJNPGDT6Dzyvb9UNGuYCH9F2t6iA1UBSmrld0iayaJisH4En3q6Aq1FcOX5l%2B90OoF1VUSSeRsJ1srG8HnidvsFfcZiL%2B35NakM4p%2Frz4fCFLJbxrEnazIpX%2F%2B%2FJlbMRO3j9Vie5kiNWa0w4IyouHynSZ9ir95CsEX8wvHaDGGDphiwTxkoh%2F1VGP7XVf%2Fyx8XI5fXm5Gz%2BDlzT8mfO%2BuN3K%2BzeiD8dbjxH5zxPkJSUlykhVb1VVpWhjqVLo45fuXIAaqwZbC4yxIV1mTuCvex0xpThVEZo5VmWrx0hoduyB4eV3TTgGjLi4G0TVL45AJYkmIzxbu2ErG7qP3lddxTmlnz9vr%2Bfz%2FirJFkxHjqXCW2I6KKA0AkkBKPMJm%2FpssGOqUB9oBeIQWBbWdAGgFw5LiYI%2BS8yagoGGG%2BOc4L1Abfn%2BVdoltkKn2xdrSmzHJ%2BT7wKVUH%2FQag%2Fwbe4O2%2BjuHon3kEei3bnNTNp4euJO6YIb2rGID%2FvAJukU14i3yh264BcsBx7UAuPVekt%2FehI1kK7taoJLFGdt7VT8tEzMSpYX%2Bjz2VnUUVyDdoAplH42R2ZELzVJpJwNbZ3HtRumkn1AxU2iDhFy&X-Amz-Signature=90d5a30aba36055d239f4bb8e1898d3a80659f4e4940a6b8d23cd72a6034de49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


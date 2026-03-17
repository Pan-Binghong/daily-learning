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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YP2GWCJ%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIHvakOhvRR6CxE%2BUmhqutZO0xfVINx%2F9mEX3XUVykV5RAiEA6DIYYiE5HCDGxiDIlfLs3%2FvuPeetrdtagDt5rhPIXyAqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvGyIbfUw39XuBNISrcA1oQamNd0dYrlyN1XtXW2BiOjNILVQDyCq7p0cijUYTgXdJJ%2FWvYSzw1lBsBXaNFbmYJQzR3BSEAvKpgXuJr5VH%2BmDTj%2Bisri6RxG0m6HZj9UPTrJNE%2BwodnP8Uiq6FXCnofNSKImdJtBN0UhhZs9GMCd4YkM%2BzR%2B7iF%2B%2F3HIBGXfEliu6%2BnDMt%2BhmNB1C4G3laEDsQMKUsdfi%2BucSyomsHa5szZGDZl74qNyaoGM8WsUXWZcf2QIkBQaiEQcNhFAYV2X%2FrGnAv0b0cC0cQp0hRjvUoXQOEkw9SnaEWf2qK0oFQIAxNNTNK8yEGUX0fnI72OcFmfC1OI75EHI9U2nEZJFqILQS2B%2FksZaTAWYv0QptxmppjFJVm9qNdkxa7z4FMFDyHTpa6eGZpiQNnC3zF8eHde6aGNQCQ5nPzq6ftnUFRJseYx%2B1d8PnSJ5LshiPPh2NWlxyg53zdcKR5EJh8ZAftlJIVtoCEn75Y%2F6l88hGMUVxbIi79W%2FIf2z8L5jdltOjB1oCRsXoSUzeOKbu%2B0qBFB4GU5lBgFrviMWxDU67VCCpMru0gLR0wCyKBQ9HN1SWpGOli4DAS6t87z43%2BexGGjHDTX77NH32N31r3CSWF4M9KoYNVi1te%2FMNvo4s0GOqUBp9fLYIGkRL5ShnVC99KRdVPV%2F1FRVq6B%2FTOcmpU5dxZBwLmhWvLdSmeojkYNfdqoLecVPWSsMxyo4X8hNTQJZX0CwVS%2F5U6usiC6Ml4tjP82Nqlo7rmZLE%2BNe2FsaET11PMS6EW91txwyPc7LUrF15NXdn9qCn0C4Vxq20QJUKMfJ77ubwe4CqJKmb6Y8ZWdEpr1eDM5m2n1Jg1%2BYepQKBZsP2VB&X-Amz-Signature=944afad76661e22be07303945d099e5b04266e9c931704802b1d231236741fe1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


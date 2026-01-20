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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWFAUPM%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLBbXc3eNPrFePa2P5H7zVDJLbMTxOT6q7DTKF4oFkqAiEAil1TGRt3cI8XtIh8ipaQ%2F%2BeNz27kx24RUp%2FRjoXfgNwqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfWobpjYpDXH8GdxCrcA9ASaAKJG90NsSc2LaCzu%2BQIfC0QunOUTVdDs%2Bj2YYzwU0Ydy49NndYeElcgscKveorV%2BUiBH8hZckNhNM69MLb5T%2B0QvUg%2FUV5xq%2BIjIAXaUYl%2FaDxnQlRXiwbfPQ%2BId144ItDgG2c8mwjtv1wvQSpYaqKR6HfEV%2Bq8TBdGOGPiNWOEwFtyxivCfExy%2F%2FCq8i6tRAW%2BPTziRtGwFq7d1yQ8TsLoFTP9%2BMRsA9xJwwy1RaBT%2BytV2kPv52fZgSrguXLhT0%2BtdrHPLgtgxRacild48pbSjnSaX8qxhHfQM5gTld%2FnxghPrU9D6ersh1G0aXWCStiFwhSIsZmUte6%2F3H3jXLQUcQ8%2BNqF0vEOCshtR3RC%2FW4zT2MX%2B7lZsUwW9Pqkd2gpdR6iMlNDDt1NUUdUCxbBpK636H3hSz048v0Org2Uvn53a9s7iq1YLH7CdMpao7uVUzpAauucX5y%2FF%2B1jLNL%2F31WrCyx0aO%2FZQRV4V8UD6sgL3CxaP%2FxdnT3xzuQkvHR5e6d40hT5DW9a6NDjBvOFuRCGC5WTpmadz9oaDvc%2FcGZzUMYcG1HsoXzgQ4ZPc90YFXbOh6n9Dn3shsxgR4dYcQS2gBaJ3BEJEsuVNwWcdGJvnbyVdTjZwMNL0ussGOqUB3xt4uAeX35KuaxlGftHsV711ywP4v8tsVdvgN%2BTxL2ITxMczkRntkBXtGJ2eu9653N%2FsdWj8Tpv2VkIcEYEuNAsjKPHBBGHNRwWqWfWD3nz8IzAfgQmmLj5%2Fokrm1SccbtHGphD9Xok17H8bOmar%2FLs24Re2v4crWtBIwNghS%2FXNEghsN5zsWCKW8AFqKCdLe93ebxslKqfpEZVGaiwY1RMFao5j&X-Amz-Signature=50e5a53d64e3c6fe78c25747e485b0fd3c617e6b3d9f17b6722824204e5e0ca2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


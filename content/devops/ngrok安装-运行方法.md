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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663FPTX6L%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDm3q8sTRLdJerH1IkPof0xB4smRp2QWdnJUmZh%2FA4VVAiEA3Lt%2B4MtYvnQPuj%2Fxih3%2BIMzErMjiW5Xmt56hcalnNSEqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrKitqPuEMlq32Z2yrcA9kSDYpRTC0YaYRWNg9OQQmUVszDr7WUys8%2BRmIR%2FLsnYpEazS%2BDozgXWHd4EtsM%2BtxjSyotxQMkC3HtfMonpauuXzPxd%2BAv6NbcS4alBGA4w6boq7qunNBZqRvofqTIhO259Vv7V%2BVNkqNfGFV39Evb5koqR4OjqZ6IPc8QM6ZVC8jPrZGiyGyYm243ANL7KtZnCC4HDejBr9LLbpEOAxp%2BRpwPahR6RA7wtNZdz%2BCdl0tUIGrqh24bNSdT%2FPOLaL8BRY0nTh4cy5PDVoQoBEqQ3rRGjjRkcpnUaCpZpGowCxVM5XpzGO3nT6qrfFrnFvSF%2B%2FiT%2BhBfu4OtmTQ4tvK2eKTAqy56I3iFL90xB%2Bn0v8whw02gFFTClBZBzYLQEhRgee%2F%2FWkSBdx9K9RJKpfXPgEIJ6WpMOPuGjXRqvlHHcfdHHPOHjQ%2Foc%2BCflnWvRCMaUV2f%2FtxY9EHyDj2mcj5MbUJNkbuNM7wnACpQB7nJc9xUMXZDpp89Mz2LgyyM4gj7kZpUjJ3Y5UQuCKupXmhxT5D0Tf27qcxH9Fc%2FEAm2QSWlfL3SQmTIm9EmDyIkoiqVmufrk%2FaRD3HzLbReg%2Bz%2BLeXh1Wsl2%2BhjkdPqGOTFxhujNDSFTEVJV54RMO3JjcoGOqUBm00v6tpSe%2BHifeguiuPSThCiS%2FReMjhLW2WiM6RWlmJWzNA%2FXf59QSCVb2kNfmB3ABAV4K2zzwa2kPgPWlIG4OkTUpF4uG%2Fpsv4l5XATHWZ9Ogf2j8B3HUgS8Rqj20kSUJdOXpE3Ugxe8h5A9uhMCB8QhPs%2BtamydjHSL3oJE21KDzFJpk49nb7hCg7vo4VVMr8lFka%2BRAHJ4WjchfyXQSS5zRZW&X-Amz-Signature=6085a1ed98ee59f2f83129e858202bb5f0f4ccd92b07adfbdbcfa49ea862652d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


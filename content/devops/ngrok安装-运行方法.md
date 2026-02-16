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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWMOZO3F%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCxK4wxSS%2BqP0OSnLJ%2FQnQYGNRTzZ0zr%2FfpBQVoij2kmQIgMJ%2BwH9AmMi7rgpJXzqe190P4l%2B1Cyzl62QiVHzeakNIq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDKuuDtnCz%2BQmMHl8tSrcAyBQ%2FZq6kuzFVptuIoXBbpCF4WAW4vnQQGApINAwrcacwGvElLlL6r1cKDd1EmMtH80Fn0RdFJpTLFIDrL0FxYuaZAF9A3u6LQy4REPCkrNNg9x27HQ%2FcuP7VK3UGV6l8scmHbrGPMoBKWEyozobpFFd4UbFXop8V9FEhhG%2B6g9tSRUYt5Y1w8XLB%2FgqmxoeBakYND90laagaPojKzv3a6pjc6uSV6kLJuIodwLsc4CviZVJjMzrhYJljI06w3bmo5GMLmAdbRpSWYQLkmH6d9vUP11FJx%2FkAQzcriDteiu8laSPbLQ56wTzZeVJ7dru2yxxPtsvnUtm2u8oAyaFMYgXVFqMgEbD549zO%2BYI%2BPBx0T1sVnQ%2FjOBksYRLW0zaSHZ%2FIreshdXLDgqq4CAZIEeYRsO%2Fpgg3lhUqtW2pu1Lp%2BqEVDJIHyZI1o%2FVqLG0v4OpBeV9aDN82WNOK8kM6CHMrMnOH1489H7tcCz%2BJb0SZMVtj%2Bd5wcESWtaOhak3XULlrzS7ED4kmzegAZaHD4u1Eph5aGDY%2BsRJ3Vx%2FFTSQUYzRO8jeZjI39kE0VCuYXO%2BYhjIoWEmEhMXFjz6M4VpaIMymD6dfyv9dI8OszvDSNmcRVeII08%2F4LzNCiMN6UyswGOqUBIzYHwNRFu2tWB6Oe4SDKg6QzFdY1R%2FlS%2FoaXni%2BHdxDLTHKW29STVEPLx0f%2BorvqrtlSIyIdnUZmvTvjAzjoEqbwy4NARLJdapU29c1kMStRGVCJWjNx729NSWyLU7Ep%2F8DxnxezDSZJBABh5Loppvxe5%2BhXktCEMvLd4r2I2o%2BHLdHpkECbE%2FiBajM0aX2PjTuopu3kGjkuCYkL9i2dSXhGrn%2Bq&X-Amz-Signature=9a8d8a775a79a4d88e8b8f52301d8da407e86816cc7dfda1c5770a373e45da77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


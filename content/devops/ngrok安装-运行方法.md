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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP3PYHMF%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnYo%2BgL5gA8J3bo%2BUQn2r39TEd84uTLkAQf00kHCBpWAiBBq0woq2l1C0eyQU5Uiy%2FGREb1F05U1zdWCA0jOXsW4Cr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMIQQAK1lN%2BEle6DgTKtwDpn9bemNUNnHBYE504IAg5KwXQg%2FMeLKjnawfHH4i8%2F%2B%2F7BhjGS08G8Tnkg%2B7tHTyWqY0O2TVgOztocb%2Fss0hIm%2FL6ec4qYrv5mP7nIfXL4l0POPxCCstSk%2F%2FbnGreFuVCxdmzpQoN8mE5r5LM2nanFMq7of883ifdxmH5pdqT%2FHaXrU1zzG%2BkACL2%2FsDOUyJ2F3%2BzvcecVI3w5CT5rDriGUJBO6KWCMGRvVZzbGvy%2BpliaRicWAWaccWZvU%2FXLNn5clycY7crqDgUzPRnz95LSUzGt86fvhyGGumsduBK10kTQLl6zEcMhvekCaWqz8SqE3qB8ZITBYhh7t53ytp6872wZeasqlrR0VZ2kgMeVwXDOVfHph0gEfYei0DRoBrQNmV4yF0sJgZYw51HuB0EgAb%2B6%2BGLytPVXzutLgSNxZ9EDVUzamO9irkTUhAQYj35lJhA3rOaI5a%2BjNqsSEP4z%2FlwN747dhLEEmF5QMcXxj6r9dzGIj00bMXuin7SnXcixWh0xgxoRhQPujHfOpPF9XFQbv3NUQlDymdqNcLHEeen%2B1L3bNiuom1wD1StZAS%2BOkIPZ4Sn2mS95r9aiRdBDgR2vyMOsqBtDgwVz%2Be2VSbLyCg8G%2B9d4IyuGswqtLgywY6pgFmwydaJmdJqcr6vvN75HR92ukjiSX8XTTvkE4kH%2F8p0IAM0AK3alta%2FEcseFaw3B44ZwXzsq%2F3bELsIH%2FE13gIz6dKZaOlSLcBfEAKTzp8pcebVOk225PtilbEj7ErAN7vSolYJvtSpn1Bq2n%2FaO%2F0iNNPbaoEU1wrHaZvaIgbnV1gww1ob%2F9RJ16ZJyTeeAvrn1eUGpRbFbrqrREsOAuhbiNEpcSX&X-Amz-Signature=2154306c15be27685cb55e99aa4e17f90d0e6e49ceb80a4e407278536a704634&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


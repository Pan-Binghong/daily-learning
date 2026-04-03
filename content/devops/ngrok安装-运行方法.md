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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H76EJXW%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqMz2B9XzqnEPLKeQTg3NI6tryBAqducGEYlM44%2BtPDAiEA8Sa7hsUaKQaaup%2FL%2BQkGtTPmWRlGKfxLokk9qUqad6Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJL4sD7Tqm1MGK4N8CrcA%2BsdAq2%2F8p55P44jC7Bl0kh2WzAIS1BHl490M1koKEQCOt8mv0PHEFuCKssZpvtGPKQC2dioSTUxaIPeQDLt%2FoWS3tM9UzYZ%2FtFG%2Bxbh5Z8lyobdB0xm6P8V6W1%2BSoTfbHknNBFjhwN2Mpz37V9JfCb%2FBn%2ByCoxdw4GtfGqO17pBJ5v9jfMvdpKqIAUz%2FeWi9yzKlnUUFUoDjEMjJSINVw7BxL3eG2UhyZcJuVp6%2FyptXkNhtcPFIBYn8eUocwrNHWL3o6j%2FDfhTcG57%2Fle7CKrfaLC6NOec%2FDmwL6%2F6OlWmr%2Bt9e2z34T9eJgRe7BvA5nkWTyINPwfX4FKQsOatNPOcil7D%2FySnxPOK%2F8PG9NpwxNVfltUSB7h5TfE9JupX5pC%2Byj40U8Uz6ZczLjXghgcEq4%2B6Qjg7vwQTaEgKWfC1eYOg8eo9fN6xGilRtk9EZgZqecJIHIQtzLLmUTCDTqILGXrZ07nemKfqdc9iPZpecl9HNcRMLv7cYJTlqvNrploVnooQZOeCZIZU%2F9J62vMZqYwfSsl7Kng9Rj1B1CcuQD%2BvPqmHdcYy77Ny4K%2BrdrUh9UUCvTKw65NvlCJavEkhCYFqlBpC29FBw%2Bk1B5rjbLEVx%2Ba%2B0qfR1grkMI%2Bsvc4GOqUBBYL2gRGce9uzU3QU3jzWdVxhzP2985E3VOkRDehYAa8uCQ3clsOCn4vqLU%2FtmNNa7iAmqOWSJ1ITCoP0Di2l5BHzDngDnslxNfMW88ol24pdFIjdTHBDV%2BiHM2g0%2FSkNaocjJO6kZsvO%2BkUOzuosE7jBn66IVO39YtcV8txuZYV6hK5e6joY4S2Gq%2BAGSvf0LGoVnDvu8fC7r1bi%2FnIpHUMVwWRC&X-Amz-Signature=c0e2ebf788b84cae4145cbf3b88b68c066e8ed8985b27bd767aba93734ec35c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


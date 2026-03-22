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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AW4HQIO%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy%2FB0fLU9er7T5mUN6X3veEVO9hsa00G9v%2FlMw458lZAiEAk%2Bfq8jH5ZVKkqbT%2BYGZ6rvrqkVVzjEnRPzt1uSiTBD4q%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDE3GI0SorNiOxVuT9ircA127bQmKQlZQOwHhmcVe%2F2CQutVvnO13bxZ%2FbGFE9dE15zIpXJIsLPpr6c912CpaEtc2SL%2BCHY3Mv2%2FVGJ2Y0kmmK%2BlP2bG9ZQE1n%2FqHfBT2nqZU7ZAiUF6n0lxKXnM4XD34htVMDxj4gT2ftgy397PRP%2FZumq1AlhDjRvMV8KnnByZJgdz6%2FF8AuwJ136Pc0Ws1qjP6Hf5J%2FQw8xs2arzhTkYQi%2FLvkfxre1brR8xzV1obq06CvKjMs%2BDac2uonzW3Vlz2kIqrYMxt1%2FAA3b7nyDgULj%2BKCbsYuTFmI6z%2FnDsJpCO3Dl%2BCD6UqEcGbG%2FATbcvLv59tX%2FX1u4OCRXMIH4vQf429O%2BaHGxAPVRtjd9c5ws0heYQJ01kuFfFPUSdfF8rulCRmBuoNHzLzBf7S3iOq20xXGmAkv6sktq9opWm71t5rE3ybU15Rt9NdyWCaY%2FnvkkoiY3Du61PGpigcA%2F9rdEU7%2B7UXByLjnVY9UygMvd4qPbf4kq4qZO8cO4i85RNKlx0PszOB1UttlqbyaPbmyBVsKMTpYU87Ykt1Jfv3ei%2Bx9SfaZCeyrmJVf9q7yy%2BHxQaMljT7N1wwgH%2FlfG%2BHKQWCoirO%2Bg8mdKLvY4XE%2FJKF4qYyprm7pMKCt%2Fc0GOqUBymaE26j8gZZpp8aZqN8xPHuAvdcJYXsMYZUsooNU1mY3qZbXmmX6Nvipo2G91CjOE9AtDJCbvNw%2FHV%2FG9OeRmbOBp%2Fag1majNhTvmkqMJOPlehuEl%2BMAmGj9FZLqpRdGiTIVHRl%2Fc0PXqyjLQO1dz1c97ltyW%2B37fBfGFVsAkkUhUphlLpF7oeu8lfbIWAeA7Xk4DaBYJ3YPpwgzNl0Ilx1CSd5r&X-Amz-Signature=85d5c8e75c4795586a63981256dbae3b99de44fcf42668606cd6a7d92ac59a0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


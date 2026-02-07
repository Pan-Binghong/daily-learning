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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIBUDOZM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG3IESpcEa1q2jAJ2nGZZ69pOf3AnHd%2FWdl91lLt32x5AiEAy5oNSUnt40kbtGP%2Fhxqxm7mN%2BxFguibXXbCM6Y6cy%2FUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDPipWHe7yRJGrME32ircA%2BYRHrSXP454xQhv3ZTMetcvsvsYBSjiqyXlkY5ad7TObPM3pZQZK99Pu5qgSbUzjSUYQGrPfveyv47NbokJ5b%2F4fFoiLwl5IEGjHPOVDFEtk89x3k%2F%2FJrYLGKw7uEBZO8H7%2BRgnPibvfxPYjHuLhoc3V3Wn%2FukU0WNSFQJ%2FZVkloOUfoGUraP4SruOeLXq33dCbO8zNDtrKnWxz2hJBDhvVEp%2FsDkaFxORBhgii2f%2Bl7o7OvygQ4kmE73ox4bIKK47EOLJLm12hVECnwwlvFW9JtBinh3%2F6nq121EkVHtdTKLNsD0G%2BrWxtr5re1aTBBWm2kztpptZQ5FM15iH3mpJbm4%2FcHlTikg4%2BX3%2Fvtsg6ex7gGFiTX3o8oh2MCnQAKgThsJvN5ltulsSmurkNsAdpHsFQFzEpNkoTgahe9%2FWk5LPPppkdeBa8oBLuvFNzRRlAGals2xxAHe37Rd1EJBjkx%2BY0zOY9i0UmxkYJDkDmi%2FQWQCiB1E564GGZMlHuetYoAfrZ8Yh3Uy0hIwGH00pzF7Xta0PkOYA48D20d7mQlsoGlsBQo1hQ0Noe3LhkxjclLXubcgfgJCs1ZtuNmVTdRcy5qu0hBTcSr2LkYJfIb0g7G%2B5EqyZYnNvGMOXDmswGOqUB9rS3uXOk7xilnilowO8H0u5BdiskITpzgXz%2B50CCbCYR2LCASl%2Fj8PY%2BseaEbwybKZwQiC4lC4T17GrpeYufuQS0xdIKs2jBjxAkvr4xou4ndFLpQxCfRYD4mZmGH8Nm70ZOdbCCVWi5IyfWYeYYM%2B%2FHXFhUHK9u1anFzltwN2gcO4EYe%2F03OAiFyHPZnin%2Bl7ynD2IlifMyGQ%2Bj0XwNs%2FS7KSiS&X-Amz-Signature=0c87f4729248656fa5d8622d5c59caa7b45a18e76abb3b2b4e08c6a602ce9e0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


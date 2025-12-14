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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PXER7AH%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCINwgwvv4%2F2K5PFOKQJxX3JI%2BRVv2AfQ%2FK0GvlGNniBgIhAOV42l%2FoIQzGsVqjAaWYaaeqlYeKNd8wxgXi%2F4U55KPXKv8DCCsQABoMNjM3NDIzMTgzODA1IgxbIFBhDukT28hGJ0sq3APCS8y8XB421muURlFb6OE7NlSbj2UhyqHXgOOuL%2Bj9pKovJLTT5QiVj9ykjsC5MmIaL%2FFW%2F6YTeZVxPxzb15as18%2BVVzFOT4ERegiybGn4MGRCTETyJhYLyUrUhVtXr7v6xC%2FCLJotnn%2Bov%2F8Fi72whV9DMle6p%2B58XdtLD5hS1AXPhRdX9235nCOfWw6h5cmbArmQKD4cmW7MIFnKSQE0RxQK%2FKpEv7uhx8eZMVqq%2FBOvhIflnO4kB7sNztT7UKh%2BemilMLxxgRy0siMna048nuMW1u%2F9QYX%2Bb%2FEmrmtzL%2Fgw0F2aTnhmJUtlqLOaptPXne25w%2F1UIAQrPem2M%2F5MmO82ol%2FJmxQYnI3a7KJ%2BXnI4pMm1akIswirCYs3sFYM15VStQtEwsksfomg%2FbIsS4n3Y3n3kRGKZngTMMdLYvaa0Z39W4HVOx3SUVMGyWN1v8EfD0bq8EfI8fOYYStbsGA0s88HuHsyslfUb3mP3Oi142N8DRCxvs6LU18L9KfWZEzZ4XE5PNKvzdyEHwQTeGesxKzzAIZQLMvjq6p5kppPJa9WFaBTeOjsL5ROsGv9U9DirC5jCg5EdW%2BbE9413WVn4p68d9WPrATYke5B726Z%2FgvCoOfZXJOSs4TDKr%2FjJBjqkATxtSIKwYG5LzLVDhmcBLFgpCFKoP%2BtIeT72gkaDp0z%2B3iGrUqkGZSQjKhOYULXBHl1Oa9%2B0rpgkKIIJ3JjfyZ9CYBKYuAzlCjRrcFQMmalK5CHiqTDxH8ajdMGbYi0z7XYhUPke13B50%2B%2FDwsm15HR5u2KHLwCwhRKl2XbNx9qO4m1aW94KFORpYCUPRN77k3lIzkXdDI5hOrNP9iBqWRVhIUup&X-Amz-Signature=0d104fdb12a6339a45c2bf9c0017bf6143e91806eb83499d9ba27c3273477c0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


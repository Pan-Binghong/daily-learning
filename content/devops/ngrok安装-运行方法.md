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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3KHLKZF%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzH%2FMa5xHbkqCd%2BbkJVVkcNUfSsre3ztg8zP32DCKCMgIgFYevS4xP3r74m%2BED%2BOE8nyqbGoYelZdZmBxcWod%2F%2F%2BQqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCgzIOzdaHBoI2jGircAzF18udRwGbzcpLaQqSsVZ6yQJm7YvIylpX3CJzTqLMPrdIfNse%2F1s4Pg4QAxg7VQuBhbJgqXRelymO4J7DD7zTEIEr9CKa7%2F1yDP7MYCM4nFWIdbp%2BOmU08cR63i7d%2BtolQQHjyH2QHnsiDdim8%2B2Mwad6%2FUKFqaF4PP%2BAFQNVkGjPorXsNLjNDBO64kUlEvfxrgeIZh8dBNGNDAkLIf1VdMzkw9CZZpsv8%2F%2FHJP2GgyqKOiLhDmrvEeTcs2l9AUtEuPRnN56miwClQRDaOZ4wBAV4DDHUmVm%2F2vzzDOzjcY2Iuo1tHVqnqBX2jjACLj6rXDo2Lc3wcGTnZtEcaMyo%2BJNLgEd0SEPUkANoID9TRxZvkJ%2B5zJTaDRMpjWTETQVDTwr6G9aRh%2F3LiCkl2FcdfjaR%2F%2BR%2BRC9EhO3pB%2BMapsFelYF9rNu6RyWaX8weoXW0W1PRmO6t0Ji5txF15AzT%2BsJBQKoV0l92Zaq3OmYdAWJPuPTdMYf%2BNCXWh9qU3GhQmvgMLQbHH9PFgybGELed%2BXFBc5DBiX3neUKTnux7VrotZDiudUQg57h62krcThbw%2FGHc%2FF1Hyg5ecTLmOxYTqi49viGN5R3xcUhBZqQgQtbx00Mvgcjd1UQIwMPWY78gGOqUBvdudRIBQ8DvaAo1fJcv7oZiRFWGvzZJBS2bB9rZZs7pmoMIxgoHtr5YsVkxFMrdSlplEtOo4OUZml0uPlNwcK8NnPbxtIbsAPGe%2F9L6BatnQyWYBqEwcpfNj5RYSshBteCSIBNURUv%2Ba7ferBvWJ67wG8BBvXpcZKZaFJJe3UQG0wWdRXLcSIYi00gjw6eoG4%2BWe%2FQNh05%2BhjgGj%2BudewOTfCu6S&X-Amz-Signature=92b12638bcf1852ccacb767cd4ef847f26c6a79d27814d73da2169c084af0d52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


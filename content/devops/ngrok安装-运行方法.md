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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKP5XAW%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBtQKUTtLp5%2B1IlwVxR%2ByDIaxsCZgs20ALZXMpfD5PwyAiB52UcYDMd6huVBZPf4hObPaqjJeTnj7SiBI3Y%2BrUrDkSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdk8vRMFjnNecwS1VKtwDZ%2BHOpLRpVlfWkaxInEtetWPmBaOzZywzUwEEqhrm0eyq1mPh75%2BUEY8HXGxQBesHujFhFRJi%2BkpODZKHxj%2B5Oz0RKM0T%2F%2FnMrC7%2FTRLNS0URrMoIJile6o70Fx3kOkGWSmycvURlUgeFtwCZjSUTBESqgvn19OzOwElaYGWt2vtNzvSbYHOUaJ8v%2BWgmnjv21oT5i7ZfXuP8QBOwLQhUvvze7dWqyafzYF9GWd3xwj8CKTzILwvWwBVANwQAPPcuvmZfJDcAawu0TMDP9ddnNa1KkA8Y8ZaEYED2ue9PFzuFur8wJ7sPy6K5DG9JFIMJ8cvmuRLvVV2uEcc4RimKakvafYNyH7HRxdgZ8ZmTRtOxQHbbrM6FTKa165TjPXdnrEi5zF%2FUlmqNN%2B3jZ3Pg8FMxU4jQireqKXAbam9TxLsvGCxm2Fa%2BoipHf2ivl1lvJ4wMtPXNy0GYEHMmPNWsmP67qg%2BKbGUDV7BMrxwd4rKzjYLHKJiDFyvz%2BFgdvjQ1dmQ%2Fy1MRtfEIlQa99TSJBCpwysQPKDn%2FcYsqWU5r3t6v8769YYh3LgakbAjaf2VXUxsi4FdUJ%2BeQngRHcsJMk9mlgSSRw7DoXVzU9Yeee%2BVUSnVca2MHAjst0S8wlf%2BiyQY6pgHFnMiS%2BByswbExUDs8FV5SlgGFMLz0GnJ1wAoCWJDxo3QIx40H7r3QduXCu9QqHtdwv7Bba1p5HjDeAT%2Fk%2Fj4v%2BMKcgtN7zitxtYcpOlNJ0X4QqcyoopUgpw4ZMTvJbjBuS%2FXc8n5a%2Fo7qD9mG9HY1NdkMnToZ5s1wtXBKqnOqjo%2FD9EXwFugzprB%2BWHCCeoFtllLXYh0jDElwiLcDU45n3Oj3C8CC&X-Amz-Signature=5a9a9da1996b46c3c4dfc3aced004e0160f1fd89b9307470706b3794217175d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


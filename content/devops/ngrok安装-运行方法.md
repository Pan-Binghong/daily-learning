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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKCOMGOZ%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBAMmUZbP3xfI%2FLbOK13mHcWCE0lPxkoJlh9xpNbdhWAiAGUQry%2Bfcn6TshWF3njv1PLDR5O%2Bk2kgL7eY7TSqjIsSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWLqxlfiTC%2FYOeOvRKtwDTe6tNQRFdRQTV%2BF720qlQMbn1ILip5ksJMVQ%2BNh7455z7qbh7OwRjc0ZIiL3Z4YTr9CP%2BNUxF13acCZAaYqi7W%2B%2BNbtkcfhv4eF2sJjfES6TADVPmBi4Xo6%2FCj7fMJeQOx2eVolb8blF1Nz2Yl%2BzKSveka7l4puieCmzQWuQ7TfttHuXCpWQYvfQ00CYNUi3vwJmUSy%2BQj4GQJV3Src%2FufFj9Efl59fDRwoijc9MkBPCWdil%2BDkAg0dS4bNQKJYA7bh7f2arpBvsCj5%2FNGEy%2FmRV99ujchbqpCwhokoxFHcMO%2FCVed6Bl%2FYZwiK4eYoy2xifboQHUU8WQbIwcK4h5ATEf2VR5w59kGq45fgGCxZs%2BSMwOiSrzpvuSvx4UExrxsm2gbs0UG9XgwqqmNf0RGQz6N4PyhIyYAo7IGFUTXjjFkfmPVs5t4kGv72TyPgtWRub89mT1fH1BHAsNBbn7W5%2BLDOCX4Rme2Ux%2F1lnbFIfZXFH8wNNsUQd3ZarLrDVS%2BViYTeAGuQYIJCR4s2E9UaQwoGz3N0b4cdk5Hfrxt9%2Bs0Deys%2BoF6RIAOzCrqo2Q4RYe%2BhOXbX6730lPMSc0j7wuqh101TBOyczq1U0CXHAluxaZuh4taQ9UjAw%2BsvpzAY6pgFN3z%2BlWX8R9scPKup2XuuaGxv7aix2W%2FmAAiqHWO0KwjeDBjtVb0Twu%2BndPIyT5ihHGweBnR3rDXwPSzJe6%2FCxvJTtnS2pXXb5P1QYRqtspx6WVjdUnVCOxBOru0C%2BV0xiS7derVbBw3F%2Fi0MpP%2BvZQSNUtfC4RCfYfDYKVp7M9rUWgdlJG20aEM6Ora8adARR8UCEAFCtFt9L3UzH5KNh4I5p0rTR&X-Amz-Signature=727bc0e0d582c03ff3e683a9da5af07917a62957c5920f38669e90fba1346ca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


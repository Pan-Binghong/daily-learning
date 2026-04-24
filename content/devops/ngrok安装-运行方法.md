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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXLDCAOX%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWvxAw1P%2FyMh8B0ih42OdQDarReEaiWqMwYg4mm5DWwQIgdIdH4CF4Fzy4%2FA7CNl99r%2B1%2BzGWpvIZ7ieDm0lrsY4Mq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDDojKrMsBV75tzGQmyrcAwaLMcMcqEy8KUIN4mwg%2F0Vr%2F7Y0iOS3NXvmKhshP3M912EfAk6%2FqNFTRA5Z7pOb6vouvePHB3iyDZgm75Zyq%2BtSGq5yrqWXbbUbB7b4ql5xv4Lr%2BRaVljdEK%2Fz2WpKey70D%2FomHlzOnM0IdLlMYZJAVWf8sykz3M5QUr7LEEnhZhANBMr5TI5NOiMM9Qw%2BSLBFnuITYV8gkEMgrGXp6c%2BgdIepVg1gYljPxFHoiQy7ksVdtw4WJ754avJj2SpeD02L7hSRhXrf5zjcOTFy6D1vJ3n6lUsCHdjzmsGCLLF2jTpIHG4500tt%2FNSaj8gV9rZxV8VJGrasUcTKJDEmHMR3UvX7sIVZVli8k3rSqDX2rVLGjJJ8ljGcflbrl%2FIQs72fyeSL1tQFNpB63tmzhlm2ZNOPoiqt9LeGZ7GPbD7h9gxE176%2BIybnaIqtwnQRtZ0KoCCqSK5NsD83GweYP0ikr6Y8IbTID87QB9AeMVazzJUx1nS1oFh41BwGDhqVa42JcdDD8OOC0O%2BJYlAgPZ%2FiFGbK2kCI6DkyNc4P0rKWhKlFZ8NCfXtOJVC5ov2wfj4zxX0wv5J%2FIP%2BBiwrBCSoyiPb8hQNxsZrw4v5naPmmVkzLEMMeLaOQHZscqMNiwq88GOqUB%2ByKqJtKQc%2FD0jHSWELhiCs6NZR1s85gVJoAEAnyQvDCDPjMHlzfN5A%2BmXOVQTES79UdSXsmxD0wvadSNDbDfcCYSa0CA2cKgZvNn5ZfYi51wRtTDGXF20GP4MoThD50KjKbDlte8l4UCobZFrK3aXiwqsJUJhyX%2FRgmDLimFc%2BAgCyhfDWC9e%2B1mMd8Wdb%2FNXGL5VaGABUiyv%2FIgE6HWMeCQMEjl&X-Amz-Signature=3216968ef286999282cc552253dd02b98f0dc000664f284b253b928930c09c79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


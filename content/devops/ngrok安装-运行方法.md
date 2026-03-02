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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ44G7Z4%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGDulm3wSt%2F38jpLSCAeGwzlXM3onE8pxKks8I8EEgAAiEA6%2F5feNBvPbql3hkeLgBAjMEYCV7YqTGLv5L%2F3WztQTcq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDC5L4niMvMskkPL4WyrcA3QhfKuvqMRCOOKFw5cIgGd%2FdfcgZGTLG21Ds6rILEkFP%2Bm60LDTD0Kp9Yc1LzfuKB9iTYFE6QZdh6i%2FsThbjRK6OWTpS3%2BSOhfbF43eS7cz6Cd0ZbEzrXn70vy9%2F%2BVTayNGoF4fsWl72Z7FQNBglj%2FvPPTxMmrzVebmIjeULL9PCgz%2BMA1Sl%2B1cIHfu6stqvPyeLNf5B6ZKpbOOY5kLnKPQJ8KaXjylx9MdBonM5h2d7%2F97i2J198toRN9JIqpn%2FKUwvcrrEfLQfC%2Bc1eamvr5idWCyU5WfyMdHGuywUz0EUgXwX01ImwYupi8f7%2FAjfYOsd0ZJA5i2olQ%2ByWwsTkeaam4wNq2%2BhR2ZsSWFjKcZuIzvlwP2bTOwemepA3QTzcLXOr6MAAXZubO4yUhh93Nl9Uw7Tk17ReInvF4jQQAA1EZKcPzeI%2B8xnyDSSQsPPBjjWGmjH2VktcATaOsdl9V27mb4IhPt02mArYlQ6N%2FnHKOaaK9RMaIv%2BwYe%2BQnJK4clX7sLfA0m9TddDPs%2F6%2FhSwtGu4su0rApyYCIRspAZqnp9PnIE3VVO5dadTSbGSnfwBasj%2Fyq8MlyI7C3mflBArFdwAmJtBpEFtUizMtnvMpL0S0OOeNY83HOwMMb%2Bk80GOqUBaBoElZo4QULu3MZ2Dbk0T3dWPCtGyr4L4Hx1m08FENA6HCUvQQRj8rbWE10L4RFdV2RgVVTJjB3FTPqCxJFZ01e1CGshDjVHAEVcGihGsUKRMuK74XiCuNZwhNEEM9M%2FJxe8wS19EjOyMr6MUgrXPtpAV1vjrV4IbFIIeqSn39zbDD635NllRs9zZ7ogw2qUQ31uUQDexnEFQGHd%2F59bQOT33Ltj&X-Amz-Signature=305135099a0d01eb05bbab8697407357d8e2a884569a5cdd017ad4753ab432fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


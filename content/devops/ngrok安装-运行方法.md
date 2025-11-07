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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3266B5Z%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEz51ZfICBmDpF9anqm9p8cZb1eaxF7ClgLSG0%2FhtoZCAiB4YLli7Gi%2FP4VwTXj5IAILKdjOqi3pMQrX128v3DCqnSqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMIkFqbR8wGpUV3ylKtwDcpsFheLBTFRcUxNnpv4kdk2uAS8FUn1adIMGTyho9UUWcHboHjcfsJcmuz%2FLeN06E0AkQ8eQaAOrGR7rqZ5H7bcWZ%2FIEob3cHmT9g%2B96YappxSGazt0Jja%2FBbnuYyK2SIYZ0z6nxpPmnlGacv%2F%2BYGTN7rjeghE7MUZ58f3LM%2Bx5S3BOeO8bsnFZFSfPagoDNs8dpU%2Fc4C27ey1QmxZ6rASb%2FofZKAVM1ZFhEUNOht%2B4OQz0ieEoWRlG232sNZf2dCky4PDnoMAVi2NGZq2IAmFQ7jVU%2Ba6jXsqiPiPALVz%2FMrpI%2Bz83FaBmQCsvnRyfJ04vfkQcdtM%2B7hIHvRuLQAtuIIDl0UQSvDDvYCUxBFz%2Fta6y%2Bob1uF0wyF8twvp6q7W%2F%2BKlX8%2BiJgA0c5AK8AWmOajTdatWcWWSN8hI8MaBQMbz0VY75euIWta877MlmZ5Zn961SZOK8B6MTsl44GkImG4egYsd4FCIeimljwnejn1GVbizTj0gsc5rqb0%2FD4P0yCUqrzPwSaHcO03%2FCzlDiHCshjkB4JT4KCEd%2B%2BrHUmuJ7dkQTyP05spE%2FWXXK8HHUl3s48XcucW2R1leHIWR9F1SNTiGfyZYsIV9KO1GbABdJUM02Mj9qBT9ow7bW1yAY6pgFN7W1Q66rq%2B0UHMM%2FNmQihB9HtU3yjusQlBqvcTqXaFXDQJvSgoVj5Uu11o5di1LRxfTwRlTid8Vm9Yvlrq2ratdrbPg2CNQ5h9K3yVLDGpiQrgn3HU3FxjHTIHKX6QKMDPEDernQEVKbCT7w29U0Sz5fwQiFW1wopKNYVdXCIArPfdkvm23hGZ4lVVNOBjSHBI%2BRnOaiy81v63Ummw8BguQcK6vYs&X-Amz-Signature=254add2e6f19d60c7f6c22a6d4faa602d37e6416351a7d07ee0c703013e59f3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


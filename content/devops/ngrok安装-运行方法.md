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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVPOTOLQ%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCyAd7vefB4mbuZXPxvQLjEI2B7EA0FV062r1czLsh0JwIgO7gKwFQX%2BMExzxZhVntqxKvE8DfoXxj4GrXzrp0Kv08q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLzReACH1kWV0O2ORSrcA4SND8c0bUgzgysQOyC%2BPAPy4bCoLiM2Rb80%2FcHPRo3dFxBpL8xU%2Ftq1%2BfW3pIFl4EoIuCalEXJ%2Bs9i8nbZBcQiAUWRlDEXX%2Fa0fTlS%2FSvKBGqlz8OiBI0ErL7zHiyGjS5TQqsHpIvGz0hsbMoM%2B8BjqeyItXljQ8%2FgtZ2DIK03gQ61eH6pprDa5KuHVlPRwYeD9LOl8kJEm55FhcJlE4O%2BbuK3TcjLKPk%2FuJV79cDH%2BoiLTDvknMBZok2Zys4PzcaRR90XeIFaiJncsac3Mczh%2F5vgJWS6RsGkXwNXM8EOJ33n9N28%2FKvKtBSzcwYawBuJVo1uA%2FtDwod4A9BYw7q%2FNKmRIXq%2FnDJ%2BNY08RXpDd2G6NF7Ga6gkpbqTOpBstAnfYCPgwAHUVkR9pe4vKNO1MjIMPiZhdVlwSDkD0UD7ZpL0uc04bhgdqO2cpZjgQ42tS%2BTUeOG2waGs%2B62R5TR8TR38vSRmDBQtfbaKMpnwgD5dQkWcSL5OkgoK7YktG07T0viiqKobkFVqyjE%2BqptiY6g8IuVva4fUaDN5Vi%2B2CYx070tLdtZm%2FYrBT7KTDkdNyaMPL1roU%2FHATAQbrtcqIH0mLiS5TMvW9TGyICK9ExAyACa21qZsymOLjMLCP%2BM0GOqUBZ3BpYlLBgfOJpcZHPsVI6PQRg9V1wtwx9V45gxdjDT8WPEN5HtjSo9esGcYHW3SplVBFyS2YXaJkUwQ4pe5mE3bhMhni1hzOsBmTydZ9WUeV0GPdCkQfCyWfQ3Jnbn5ERZG01VUTybm57uKyIAm6yXHc29J8qFDRjqaSZ8dJD%2F0%2BhMCWFRProBiNmSgjegSMVbriCbyOlf7uiVjkWRZd0InpxNOw&X-Amz-Signature=f349b287e0e4066a0d73e735ff95c07521cae31753668067ef43f24c08fe9dd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


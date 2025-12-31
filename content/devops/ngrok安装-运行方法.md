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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YEHX4D7%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpfgjgoXpWgbVkC8UZEn0lCBJkT2LFz2wo8FtijvZUCAiEA%2FYpP03PJQ72e8l1atcuSLuklo3fdWDuSz0RgFcfVin0qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3Es%2FinHBMrg5fa5SrcA0ysGPJUXl5gys1P0q6gYuc%2BcnAzHMLOQgsoSqoSu5QB9fheE6G3%2FNPZNhd35p7qmshUph6HkjMeCGhmUcf7Ty5T7d9LksCw08o0AjW92qt7%2FXv5sYdLp7Dqhr9d90NchbeUFu9XPy372MnMAJEyW1NvAOzE2jdpoM%2BibAzrT9Oqdqv4T9GeEDQ4KwJAYRmJhE%2FZ99xZMlVHtiDqc5rEbMHXK2%2BZ%2BBJioSH%2BKRYnE52hZBaJyKWmhx5Ff19dCsF%2BWr%2FOg%2FPb9vH0xfL4OjPSrs%2FX8kaqw%2FzCfxNiYrEXePh9QzXaPKoyZxRtvznFouk%2Bcp%2F7oh12RhtkJJWlqoB%2BqIyg7F3hBeoRHMPIeY8L1KOTgwt1wdOhwKQrfsIAiZXVI5%2BRV7d9vEd28RVnZ%2BGH2JGz67I0bLTsvOzn2M9DE5GdliC5bjRUSzvs3NMpeCd1VtmZGfm08Gn2U7HIuHKH9mXJMc82erSA%2FPHmyVwb5uMb2vuVAJmJ77UN7CnfL1DMmlvH%2FQSvzcBt%2FNPtIpiCJ6YVs9mvTZGPXar1WQzZ2WuOo8TSnHayD4CwojkKgRIdxNsbBq5pvTeKGPUeyxjPnMy9Fu3aMFpdwCt%2BuaP2epwwhD0cdUW0KFmrHzo8MLDz0coGOqUBEqrWXhupXxGpyBt%2BZ52qzbYZtdXXc1de3z6MtGDa5KJhCwzEAmjflCSDhiFyuREjCk01KsRLsYNO1jcUgerKb0danbFw3FGPDygqt0bBGjmYh%2FchnDQZUJdqQ3RyFtrze5Hn6IzcO%2FH05TsVWoRsCRzs5QvkMbsgWvHwUiGtT4Q%2FXY7F0gC6UbY63Z9wwk%2B4Qjv90dcbJxhM4fyj8%2FVsyIsCDvVb&X-Amz-Signature=3fa9a52ed51f7fc656833f2338075da69f0161b17cbf5b04ba06b5bc183a9bd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


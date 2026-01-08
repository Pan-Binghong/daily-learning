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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PJQNJV3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERe3S5zqcPbllu5CKSO4AFur8NxUdY48sNw%2BZl6DkvvAiB%2FDD0vGmMKpUJHsrgf3Y%2FPABOvt41J%2B5tfhHqWjdG0WSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqdz17Dt%2F6lkerS8nKtwDpR0nZjmj5zkwl%2FMScF%2FewnuZs3UfLmcM5wYGbkSspik6Kqyohs4PJho9YfkCF1ScepwyR0QQRVw2PBTeUkpMScsBZNc2czSYiZm8kuR0Jsez2ofU1kMsxEEx6%2B3uTdIDHuRTgNgdAMcP%2BPELJvTKLhQdXYyOwYy%2F7T5NzQQ15wtqO14Y7DVet9vgONDSPsnqCZ2x1hT10UcWRVkJY%2FIy3PnO6ZGTj3Dr0vWUJ7Xdnj5ZoPi%2FsswvtCwcoMH5JKz58yxqu4W9XhRKlkEGrRv5QsEx648pRHAYwkUaUFFHpylqOLCMQCgFf49dIb9xqPnRLS%2BWACCq%2F7E%2BlWRkkdZm2NJFIgTnkwvt%2FO9GmVxRif1i2%2FoOKBrJsfaw%2BB9vaMFu7xIO%2FnrRN%2FczCWt7BAdq%2Ff2j7XZ8mgMfYy6hC54EH2C2C0xd16aXAe%2Beq07%2BA76gAG2vCtLJistV3uqngq4ZUcxW60a7r227UY6PraRfD3%2Fx%2Bktk9Ga66xXT6%2FAk2epLu4nfaZ1XS%2FuXz6zKccII6OcqIEwEKL4OAw%2FP8PRdX2Xicyz6Xg4RbTRwVu%2BLhMd7zvcE1v7n5QIk9BjetAB7FtZxvMAv4uK34c1tLljhUw41Pcg6s%2BmoNyZVhygwian8ygY6pgFZwaA4RUFkquALE07XvrJuIonJup9cm8OfRNypUcbHEHJOAsq0ZwXWRWKqL1Hhg70SatcsBY%2BZVhVLmZjwRE2g2e%2BM4sglU%2BSMK5z%2BAQiR901ulOdqgeRMtxEMbyK%2FnJqt3n44%2FYNF2oYqQXXwf4iPtitkk58PdQ6SlaQPZsho34r83%2FKn5hXC0Qg4SeLnLmBmD6iBxxnHFpFEEH8G9uqpfKrsIPAI&X-Amz-Signature=2ad9188ea8f473904cb7799f7ff0f3bb12c1cb04e2629b4cc789dcadd1229370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


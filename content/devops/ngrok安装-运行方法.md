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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSEXKFHK%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAcBa8SUa3h5b0PerS8gm9pp8TXoTveixFumq4ugZpnPAiA8Ul2gzH6tPoKz7SYWLq77E2fwwKu4AP%2FaLvKDlmvGFCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIM1Wzq6MSiUH6KgMdbKtwDTlokC4hPRzZG6K5ez8KonKvEUTf8JaKFWqp7nO2FlZpNw%2BWDrnq%2B%2BfKgYUzfTasx%2B9s4OSLldxVCrXnbfe7ybGg4QudrQJD87eP9fUpE24ItaP2EHzmNcvHgKBg%2BnKb0rA9w%2FzBKEWxDY%2BBBi%2BgY6IUGtGbyVYZxkyxyxGzSH%2BF5Wdu0BsJpK5K75Ktxholphc8T7%2FD6HFfH24UDIT5QJMlp%2FXj4843LQa%2ByQQJ0QHCCcY4VkKjJv8Ta729nw%2F0k15ZvVQYlBI79W998Bhk%2B0qRBuBSqseAbrXjJVzBvGF%2BQlV62PYKK4bvdRRpzz2hdMiacSpDiZXsXmloL9zo31uGDmR54lB1F9%2F3HkoKEVWv9N7cyZiYqIvXlyEY64D4iyOvN1FnHM%2FASnh39JfWL5QMOp%2F%2FwOOwyTPGcr%2BJm8EjU3ICIVYj04FSenpcVbRVEGvnbmm%2FROBaLZ6lw0Kk6RGOBn3ORRXiMVW%2BbTZgJXAlIUuoVSMug1g0a0HwVgvXPGykXVFh8%2BqZn5wrWquVduOnncBkv0cCurgRR1lbuh1FHP748MSMGIVDFa5zrUIhqZt820cJ4RRdENIcuqadfDwa6kyeqd8vJIVagIQ%2Fshi%2BGwANlRIIyax7lLXAwyLnCygY6pgFUn%2F7EaxUgALrCidB1DRcTHJH9BaDDdL3XsmH5OQjAOHSWJjxa%2BM%2BI%2BH0Mqv8TTr69TMBPcOghefiBm8Sfr6qOo1KpoPekOnOV9PrXl2dmoDwePTrrSyjr8pvbHNDBdcJ9eXPTwCN8c4hfy88U51Jj6%2FMM2I2hBqVcJfPhirLZfSQRWmSOcfdCruo%2F8a02J42PTfCPRzceJq%2B8Cf3WMGAYCA%2BhrISi&X-Amz-Signature=210a806100f488719d36f20bb6942fcba9ad431bd86b0dcf9d95632d90887cf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


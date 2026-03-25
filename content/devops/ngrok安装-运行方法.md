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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7KS3KR5%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbBCx9BaemARfituCBA70Zp%2BTGXJlN%2FHW0juCdDlGJdwIgATDId%2FxPXc%2B7yRVqsNiKJdhoo9jtiraW%2B5G6pO6kgs8qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBewSW5%2BlUNBBipoOSrcAyszfGFBnv%2BbbRlzUuFF8P%2BWnPplliwb0cyFl5hpRlCQ6vFNbrTFvurXCOtNOXIVd7Jz8VBvVpIvtRQVFNvCFg8QSCfOF%2BuPq1IvnnAmFZbsJMxKgMrV711RpSkB9ybKWo2MdGYnx3ZQrsTDVOoXSIF5VLsAXQriH5LkdTDf4QC%2ByRhZbCyoqu6qS0DnpM3azdVXmLDZuKhTgFjfEBl7%2BUNloxCg49JjIOlB0OSxUB%2FXMEE%2Ba8c%2F9OoEn0u5luk%2FkpQ0qtZg6qtDetIKoarGgjuKR6On0ioYB%2Fl1DLoa%2BEw6JvVZr6KnIW7UpagBpnrTVgpzPZe3gKQli0MhEiYb8lae3nuPyo1fv3Y%2B6ZzTwfkHuxqbvCSsooExBdkerzTU7wGqmZpdGQ01RMHa1Kakrz55roYI%2BpxTr3gGSSNbQG1uT9X8JGFzXTPU5sO9wnI3lHtubbJF0B7g%2F%2FPqljYHpafeuzWpLvkFzTIDPLGvs0zx0F0p4CnbKE7N8uX9AdXuWABCd5IeP1e4Uji3X2khqe%2B%2FGBgqUGoJPO4D0EHkZeAf63CXITj2TxwK28X3EcaOwM4LsO69qaXyhf08bQAKmBCCmgU%2Brsm7Xzc%2FLlQ0m0a4jgXxbZmar6jrFh21MOXXjs4GOqUBC7uOr9ZGq4e6%2FohvE0OKAGes%2BEDeZulYP4ta0defuDPzLvozIOhhSdxshhTIFE9jbmPAmpIwGWOL64m4zZ94%2BjfYZfB2qvIVredG1m%2FLc%2Byci4uQd7Dslglp2ERTx%2FOcmm%2B1ICfIFF3EWFmvaYwg1DT5v2fIpDsrTNkC4xgM6uQQmCNTsLhmlykjTFn2tF%2Fi1r9C1S%2BqpOXaH9HM7uDE4b6wPgt3&X-Amz-Signature=99e581a8b550e2e5f6e68eede5dc5bb78b8c6aaa64c239a442e0e77ff7efc96d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


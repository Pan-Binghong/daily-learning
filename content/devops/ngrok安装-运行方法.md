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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNP3GHH%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6fsLOc0vzrc%2FRzrqQzk6JCY%2FaXS8zSErRtUTXkLe1cgIhAIThLdH%2Bv9IThmSbB1Xm5D2FEHs%2BCXwvXaJokVORJ3MhKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWFQ46%2B0W42COpno4q3AMF5Cv4d39yp2h7dD7ZNbA583T%2BMvmTNn6d%2BgYA1A%2B2f4k9u9AhKKC8uTjhXp5Il13UERqBqNMPgSi0a5nQGC1wpQLzaxR2XZb7VKSZ3rCgZF6iInGBY1v8Mf7OD6IsHzwV9s%2BqakX18PrvwbLsn6%2Bjw0rontZydKdGJLdWL4jFby85uhkvPRYUDWdl3gL%2Fbg1Wrm09iEILIo3p38hdVOjjYsVlD%2FVGD3z4Ihy41HuPRAmS0cSPy8BdnZ23A07mNnWQqLKalR4B8O%2Fvr86pWxft6v%2BRis2yTwts8PPWPTmsFdk8jlJ9KO6Lw30kfzjafWHvVygUOzwPb%2B35F3H9E1KLsNtUcpIDIQkAhvN2RSseNX4aBOYH4umFmYQR4gDCDminKuRGcCd2pzFbgYbIXAdz2jctHUTpE6D%2B9%2F%2BkX57JX39LAwqRhOaPHIGiELzwLZk9GeXB9FW1nY34zIPxsSZTcnrzEI0PtIxMj4yXcjVelP%2Fr%2BVXD4bOSwW158CLkcgpFsNlWtnlqp%2B0yJaOAP4LzusWgrqTZfam20NBU6bgCaQc3FxFA%2FH7giK4ejTj9bDQftpxKEJ84iQhKTt1bq6YENq23g7MmxnGNfyYDuVaKopLiEgSMlWxAeTqeIjDGy57JBjqkAaQekYXjc9BBsSWRV7nW9Jtkmq%2F5e3wDx91O7W3Mbt37dwkeCuwGEuyVxF4sue0i2MYrTeFjvd0Zv1lPfCh13UC4tos1DMFtXY9xARn3fM720a02EByR6zD9REDfEpaqiJre%2FeSamMmGvE%2BZXxpi6gjvXHCVE%2BnyXxAeigBkNG%2BgMHhPVNZvJqeEnd2Ec%2F7ogi30NGkUyiA%2BdT4a1cnsQ4dzIbGV&X-Amz-Signature=68fcae98b6100b5e13ed12a2290f0e77b828d2e12c930ce1e18bef1af254184d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


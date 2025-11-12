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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NXFF6CN%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC73ItqyhitkUyCvcTKI7v6jbDx8JSrDibj78tkMKqWHgIgXrClfRROHyFbsqsEs%2BnbqIeZWNZH9fdF9h3qhB7PhL0q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDBiwClJFRtac8I4aEircA1FrtPuUtkAK6axUxt177x557PebA8J0XSExUMBEJbsJze%2ByARXWbPbSTwlNRd3mnnE%2BcLwmR7%2BOqnG1JYQRt9S8ik%2BH2O6TAoj%2BCf055xuEb1rT1Eyo9ZKxVg6WHIk0Nn7bWcizEAWjgFqpKyGtp9Ny83Jf0MyA25iRliCe%2FiyWXCTu5DFAujAUi2q0eIL823A16Ts%2BSpoblP4AkMhHTyNT2rgPJ2w4WnoVy1O71XGOQI5cSg%2Fv4%2FIaMvEBFfuCuYB562QoiTAnOfZM19PKDym64gv8mKWStIlpIznC0LWk5uDUgp%2BoAbwaPDAlxExhXHsj5D%2BIk6g1sDL8fWeTb8adR36eYMBlgULeRbb9h7QbBoiueU%2FioJDvTUW7QEXsTCbnokvoLDS9TBJSPFtUjgudB%2FsLg7gO%2B4rsccC7jHT%2BaYCkscP5hEfpCiTxrltR92VI4lf3RbnSJvp%2BsiUZTSJovidNIhBWZbw70bdPd4tjKJ%2BDMjt3Kdew9XuCsJr8KACsypHQ3mHWrYzMGl6Cu1MIVwefE4uk%2BYYKEkOGtv7kiMe1wFZlG7RTTsfAdqG3ExOcIvVXMz%2BX3hqSgGIM5wZqFJ1rEL8%2Fs5PNWU41iaPm6jB9xCsxcNfR3ecDMMDjz8gGOqUBT8NiHWrXEHLgiUzDLNCeE%2FOocn64asWjTHAbpkTtejJnOiVyv0G7DqiegAe7rslfjxxod8QhqoARNRAsmbnasYXZA1VEkKiuMPenDBvXcFFe40qJLC9SgGqsjSWQ51924L9j%2FsDpLrUNj4aof6IVd7j7bunODWXlj3uMQOor9fU6X9B6UEfwjx%2BUY9vHD4mgNLQKSPzQ48S4yqtRaQFNUTXlFE4H&X-Amz-Signature=89b05e4c478170dbd7698bf53e0f9a0435578e8b6f34d6a589a966d99ca8b0de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ADXDVL7%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4tXlqNpIlElkoa5xjRLX3C5hin%2B4gctm6Dj2OTc4baQIgH0z%2FfPuf%2Ffpas79scbb1fHOq0LJWPB25jSg6que9qNwqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkGDuZ1vM%2FINqkTMSrcAxDn1hJgEkToMHyL65veQSDZ7CcWdy%2F%2FxZ%2F2HFJO1m2RgvaayebiLMHsnmkczVAIbHcf1fW9TZwYknFqUgaLI10lU8tLOSudT%2Bu5t%2BayvQn7D9v5DUiBEp1g3ThVcqDwaP3MHzD5OVmm7gs8RNaxBhC%2BiLLQTzDWj%2BuYOlW%2FySODnhgArlweKg%2F3QdulrlMFGFXxWH%2Fb81%2FcStjPSCcmVYMo%2B3x%2BrLg39AWlMlx8dg4PzVsJMAU1dJbgiSFHuK6nuLH6L%2B08RSqPUnrl9r%2FMDuI5ORhiL1fOPJ5mdEH7aToEbEEaLl4sSK4UZVI%2BoUQ%2Bj9IzxR4R8aExeYHh3qLhvZi9Hf2FxqBjNOVT8vhl6cZFRvqDaFo%2B448Rar4prowhhlVJUA5TFHfuuj9Y6tLvtr9O9G3rQP3nm3gyMzMFHJvt2M37s9ByD%2Bxpuf0%2F2avzfysXnpdPmJGUFnnr8kYnif7fk0qIvLWHtNtyEVNd48iXQCoeCDV3dTCcGyDUsf8RriQY4bn5gYE4JBnxXZ1htXZKy5x%2FIquwcIrcAwun2qealLu7QRTqI3AW%2BzHAoOIpuxr9cPe62ubRe57CSQnFIxs1SukfdNYVMVtDSsjdioov00eoNxPQ61CSO0dUMI6zzM4GOqUB9zP%2F84cR7cNDJmnJ5pQKX4H%2BGz%2B1HKzPV17vxZQXQome3Hwh%2Fp4j4z6BlxY56V4Tqre4NFLpkv2AhBk8C7iknjp00Hp4zS9BntAcHKk%2BaeJTrTc1jSjSxqjXk52mlSfqs7uPLXA0%2BmHk6jR31KtpFBJxOscOcTaC7z6Osd1%2FkXrbguvTk2z76ltP9NkjkrscP7T34hepJ825FTWsLiMc3in6iCZX&X-Amz-Signature=9dfc29c5a4a13f9cd88c2df90180d05740a4bcbc0bdb0c82fdb55f94d8affadb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


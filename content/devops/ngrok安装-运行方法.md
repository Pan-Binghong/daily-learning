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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RP2XWO7%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQClTkM2wOignXYPPN6hwQZHLRSYB0juKWsEq3t1rJaRIwIhAKx3tBQaQCMHBYMNYtRLKNebN7q2mpf3bQl83p37h20KKv8DCBwQABoMNjM3NDIzMTgzODA1IgywuXkdms3ARoMN7v8q3APw2T0hlglcT7uPlz4uVrN18RU3MpnvDf9T%2Fyf9tn%2BRLrok5VtkRlR%2FWQuximw8%2F6TFHJa8j8oS9583vq%2B%2FxXWKYjdoGvc3yDxdu4%2B6ZFh9xwjDjHWz6trusvVIYjlqFHqWnt6TI7SOVNiZHEAe00u5LlzM6ll%2F%2BGj1iqJAKjkwer7EDDvQn1cD6iYWx3XNL0fjAbxKYDrHfQ0WLU8X0UMJPhQQNe%2FHxOmX9achM2LzUe6Dgq0ENvQwWLyRKHCsJlYsywOa9CZL6VmAbWIu3ze6DiXmCs%2F6XcCkNorumc7zf5kSP%2FDBPCv6m7byzAZARKqmpXpAvOowp%2F0JiGCycjsFz%2FMG4PeQ5fOpB%2FUpqwI1RacDSwb43SpJyHWizaERkPeED1yuKmFQlYANPssZWbxwASVRSsBfQiGmdAJrEc8nfTbnpF9q0IWEP%2BYDV7U0bX%2FzC2XQCwIF%2FbXHMM6Xz7FFRDQow3xNmRkLTQITzzW%2BoQi7ySSsQpG6GL6a1yJDFXtgPNikz4XByb7XMSr6lAEwsBtbBmAMmVUQIqC%2FmgDtdr5oBv33exIUE3E4mcPAQ7x1VHExcAhy3wPfiOdp2GTVib%2Bo34IZ2NKq%2Bn2ShaRIH1IfIuwpL0QYKUG3%2FjDGhNbLBjqkATNZJ%2Fgz1FQrgyw0hTJDI%2Ff5zGVMEOcWcvlbS5eJT23S12MiXylji1hgSrWA42tD%2BRCSwsIyhr7s9E5Wvj%2B3R%2FZSKlUM75ACbqKSOOki77rBAB6Q6JskS5Chw0JkYp5yxrkMgsmL8HkPp35BmYqR6T0UWOU393vZVBm4ZJdrXMDdEMorGBCLX0ETbQbCz7kI9gyLJdFSgc7S9tkw5Y5ZxjlWfeoy&X-Amz-Signature=09b7039427ba83157303be1413f7d8b66c5c0cd8f9a9579d1802452bd598ab84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


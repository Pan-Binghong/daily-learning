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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5Y5HCMX%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIA63Is2NCtPf0qYe6YGA38Mnr7NsB2OPMm6f6OUAxybxAiAwiQ8Ud%2BhGmz13AN5rYQ3w7hbdp07dPcJl9wdPUkrHfCr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMQg7tDYuzyIMOVSHyKtwD71D2ugREegmhvGwB%2Bzha2cheRDkCxqaCKL8mGGR%2BRCVLP7KteZ0w2Kw7kyU5xuZLyizx%2FodAFQAfcNzeBUlWcF9Njrzy9VQULTs17x4pONredcFxn2q9i%2F2UojPS4LjYVcqXoq%2BUtPyrVsU9LVaibZwYFfr5HJj7rCYEkAmhgNlynGqpb2dwtzHe3aSvLxvLlofY2piVbQl5%2BG1NcWL%2Fljxj%2BNan5lHWOvEVLcuO%2BdKGD%2BdDoFjmWOuBHW86pB2L4eXfbF%2FXvrxsDRvkJiWkHSmpg4rCk17ZFjaE4%2FkbxxkDstBjuP5Adb3A49vO%2BHI3JNDwBOr9lyKe5YNQAp8tfMbmM3Cbi7RPsMGZj7UH4S6deHJMkXBA9OlxPQM%2FwmE%2B%2B0lRILCbDpymFwChLKs%2BwWwUq7%2BioBxWJTQuF1KQB%2FHL67FzSgCxot%2FPQzGq4oXPQnc17Ph1Q2Lp5TzUb1v2Vmnvf7uyHzvDtGNtCv%2FHxnlFuW8leJw6HI7M4JCQKtOmR7%2BOExGUZzcIvfMWUIXCeqG%2FB2Dz4vvz5NbGp6qWUrVzjW%2BI%2BQ8tnff5qQl9ZrkI4oO4C6sSinUoKaNUqchEJbaui1k2cK8aS6J%2FoYBC%2FE78Z%2BDz1hjbrZEVWy4w5M%2FQywY6pgEWOB9b4axewrYB6mHZO%2FVDQCAFLsTuZvIxwWwTTX8Q5DoVjuRuwkNjYxu2TuWpnIHwDJK99eKyVX0rkvRtqjCetFuLp4sN6Cyxpo%2BZMf9SoohJIWARitfG8ikxJJIB5fOduUR7caDesPYHDX0iVyJmxiGFERPrugZIF3UERo%2FfbYrp9feaIfrO3%2FFkmZmKSfG8HpMiVnOg%2BfDpuHX3BGcQ2BQlZnEm&X-Amz-Signature=22e45f497c1f02b151bb5dbf1936be2aa998802f86dbe4d2219768abe5aab71f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


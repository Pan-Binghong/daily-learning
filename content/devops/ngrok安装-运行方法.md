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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KGTFH54%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIHIXq3YG3z2ivNeCrTl12hU%2FNBRf0FNiZKpyFXpLvdjJAiEAhH6%2B8ON4jeMBGUQCY7XDmwpqBm2loLNPCHt9s%2FYoi1cq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDFsfweTRTzm%2FsHIhJCrcAzACMNH7ImK4gdI%2FSBZh%2BHsP4RxyGRsKhPMl6GQTOBd2Tw8LPDaLx9q8Qrq7UYooHxyox7W4cLvaLZ6Ne%2F%2F%2BklriNUdb9s%2BAR%2F%2B7MMOBNK2rr98QFw8E%2BcAKyEAhydVeNWEozzaNayiJSuHTBNIxCCpweTmvGBE6Lm68x1BXuoQEkxKzdRuC9wdpt%2FiOiiYpPKzeoiA0j8Tc0vuD4PHGDwH138qQ%2F4kbagpRnpe8ARRe81uJzYVw8sExPlJLxIBqm69QndDh2oJJYNvosKG1jjlr03wqsQb6mZM33UGQQkwTeI2qp52V56yzITc3WDxLmIvTRuihMqbT%2BKCttK6jLaPNwZ8rQZNfosxJiJMiSgvEhE%2FmtWyUNe1DQPKxwoDWTAWTR92HesT7q%2B%2FHhPLjDjrz0joLZK%2B6Lv3B19FE01k6CzcMCmNI%2F6EGDt%2FLWRoAcTAvvtjam53UR797VuDULhx%2Bcy4F0tS7MjVzRk3FBLvNb1amDG3Zk9VsGHrfffJ%2BnvTk3%2BHejn2xa4S1W%2F0VZzOOeNV%2BKG9APOy1kKWk3wQ6LbMbiuuQaNDu90zzrmJLXTzXUAQx25fN5TwNqSCU%2FeqBZF1J%2BPyBsfnaHX%2FGE5jGmk%2F0UKHg8KFIxjifMOuy2ssGOqUB8AmAs4kXy9KnWf0mzGzh0t3vUG4u%2FWYQ3J7LJyqAw7pDgQ5ZkRLTVIOmF3MW3nlZ3WsJzbts9KvCK3cCjFCGs86HEhx9HrW4mj3fl20%2FQdvHohmV9%2FnRnMKS9Qupvmtq51hIxBBGwjpjEzqb%2Fu6uzAbE05ojIurng0fcIcIYSRbD5AjU4%2BHXAL6dyDszNlHDWJKOijzSrSEcR9FDpZc%2BdJQfRZs7&X-Amz-Signature=b6d8bdd3db6d8b11f0b9a6067dc8006a87746809c76d3ddffbe436f3b9fff3c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


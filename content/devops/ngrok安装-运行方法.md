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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAKPJJRM%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIBFoxGYLaGJSs12C1nippoQzE9WAv%2Fn%2FdL0PqNKdTNOMAiAfPH928JsIVldzVpqo85UJTw91DZHRcAUiNSTirZzMDCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMSN4HOBVjTReKwNY7KtwDeP050pAYnA9tkY4Ayc8%2Bh5NJ1etISna2L30CE%2FXITbgwA4VAkgNw6oBL1BujlhWZYYPi0klB9ANEfGn3CiUKSgwNSulZI7dWX16kDDdGgIRABXZ9FWEkMn0cLQ5BC266FlCRmOUjszDMp0icn9qWw%2FBB3F9dG4rCtO%2FHrWoSyDeRMaKrl3r0AjF4P%2FcxgpR0tPHZIAT0UqkigW3TZdpTnVVAnKGI5XC2abEw%2B6yKlbXrYuret4%2BfItPpkNMCwXj57U6m2L20WZMncRh4RU2nKv4llMmibkuYnEIAI%2Fu9iZPnIB17pTNSP0WinRhloCvQVlVv2rp08pzvJj%2Bz4mCbtUrCHCiOWa2%2BlB07b8iNkB3nZC7MDStPRQMzKdKFNUZEG4yGj7i0B2TPoeYwrM4MzLobjWoKq4wteU7lQBYBpO8ctT13e35lkBGqY%2BwgOdLylahDhwKzi%2B0kAdms7kUlasktwnYdMX2qWR0lyGqkrHVIlCmr6gMi0F%2BLT8kUBmasa98gChGBa2BwjXUn561COGqxLWML0aLdYoyqO340%2FYDNnx4cbQ%2B%2BCCVFPJIoe7cpVPk1kSyZmiXuVdLL6nD6MCK6BsISrgSFn86Zed0Wd1NQWvo%2Br136s84%2BPpAw4vT%2BzAY6pgE1SKWz3Jt%2B82XMPr%2BMC1%2BnLfGsfpZbTFqXfYWRe4KkvkGkBx44mfQWUgZgDlJU6wcf47%2Fzk5GwEVKzQu9TobLZvLAQEcRYIZqiYY4owdGs5HMDB1aEOVHEBeNZ8%2Bi%2F6kZ1DKH5MUGOj1UOQldd6wDiygrytKDvQnUataAo3LLB89LXrmU8JpqlvAy6Y9SUbqUCC8R6gLEIq%2BwLwLEf8kHqQ7XwSYlw&X-Amz-Signature=a21a2be7c7dfd36b20d18a2fd8fff1e853f194f4872f3ab8b40ddead855f14d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JRIVX34%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChZvgySj%2FajErrgV01uPNiiUioJHqX2pUCoyD4OwVdFwIhAL5UuY9q7an3JUHhMnPQQiZpalKB8DSqxDM2SqyihJ7tKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxlMEL1VkcGOlvfG4Aq3AN5r%2BqMSmnP9cXAzEdWsgkRkVQgAI6DOMz7q%2B8HgXAwaMipy3J0izmAPRmjEOwILspy56fLTPQOISHHKdABXy0oITAY6hEpERID8iSrViG2atskWhoOtsrlwrVkmUqh4xGh9o6oSL16BcUNLue8YOEIQyUYISkKNlgdc%2FaMcNnop4m4xf2xx1%2FWViujaIuh5WylJ9CKCsrCHPDdV4YoEl7lw0kS08ALJ3QXAJngNd%2F09llzCKnXm%2BXOWHygUuibyGwowEsafuQgI14DMPWhcMIn2H7UaUfmGGXhBgDTe4hMdFfyeY986dbFNwTeIqZRxGitJJCQy8Ec6BjyDtAgTlcgai6MEpx6RGITCMs69VkZywlbLQl%2FVFI0J7yg6nuBJ3jjXJLYlISxTyaMDwONNW9sbluyMQQk%2BNbGT6TwSqVpDN%2FJTpT3sM9S8x8QkxKWxZNGhqCm26oLofWQ5Iy5GOMotiCvlgNvspupOVXIH3D74pbCrvsYc%2BPxb66mKgfagI9jMjqHp2kv7YZmaKatIdg6E1aH7151Y9%2FjRNaAAng1A47RTMgv7pHbfST%2FHmfZ1QBTkHRPnAKt9ndMgPK6XoudzWpoTHfVF67cdDHfSkGhkqhmaFPLyhkehPjPDDDA7tjJBjqkAdvZksX5K%2FDPdtdrfYGWs9tUGSBl7mTUn42WK%2FwW39Q5b%2Bkqy47hM6NK6AxE4hKT1SsfdddlfPunxbLCKlrgTQFCxWQ6Yki5Pb5dGqbJ0r0lTA5%2FbnQGVd%2FznhBAeR0wzKbreWJZILwcJv3%2Bn%2Fm5JGiwZNuLPw4TCXoLTrov8QDhoES6XFxtWnaywKLKo2Re0uyFYOTpLVc7kkhsNSXoaZWdV%2Fxd&X-Amz-Signature=e3856d6fef47d0533456ab617132959363e8afbaac235953e6ac236b39ad79d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


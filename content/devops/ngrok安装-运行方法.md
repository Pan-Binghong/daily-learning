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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJTGUVQM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FARcmSJ%2Bm2UZ%2BIqxbBxITJAdHURboPyLS7CjStMSZdwIgTaN0FEHT%2FjEhq8BjnleDG0WEr%2FSKmsHMxNftsP%2BlpWwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHb98YN6lQ1oXyp6ICrcA6PW9WaYg1jYoJkWsi%2BOfyC0LvjQso3kVh87qCsOie7j%2F45nCg8iDCM%2BkrWFiNPTgOyV3azX2fYLhLTYHJuIRo3bxCrnHxW1Ath8Wj6Qf1Qjx1WIL6cSMCR%2BKcOlTz5%2FaUyY56KSIM%2B74Fu%2B4RmZtuwj4y7%2B%2FFjYiG6XrnoYi%2B8cJjApIAuCmksi2jbrBYCcAljy6pBC9ppwdUIqgnlaePC2Vvt6Vi7W1aVJfl3onrX3Y06pQVbYqx9rbS9YzKS61ewxdF1EY2UqrjRiHmLqLVjZMdWWb3ddTe%2Fsgg6Xjn1kzBmTycUT7E5BgwVTU6MAGVkHmk57pYK5NkACBvEwN5P%2FzdahO4s%2BtcH%2FRkJhNpeSzEiPtXL1O%2FzIkz5Ce3GkWoFVqdS3vLbxU%2Fg521XBKjz9Rk3DQcfDCtbs1SrQeX9i0OG2AAm7qjCzXZ8IwhOXy4ayxbeLX2aPB7EAiLa4zQTssIPMSbTcAPU3%2BR90ThmdCXpCOgGQxRQ5fbJFUHcNBdPa4An0%2FltRr1EBWRfJpJzEIgOYqpTSlVLw49SFjNEK8WXf3BJ6Qh7K%2BmmnpNoG2bRPfeQM4p1AROmn%2BqqNXy7f%2BlV%2BcceHLO%2FiaEop0Qz1iPQD00Xb7vrCdFReMMTwr8gGOqUB03qqM5Zh6OazS2nSjUWS8jEWN8b9tt58UNk6muwGGRjJxyG%2FGHGKhgZaXkcLVBdlidDg35J0n5%2FC87Q8HqXHRr%2Fnicr6oT7arLptTlCsrj5ZPrUOp4F4iJStKJUsOuX8PR9omPnW%2B6VhCqrhdCip7uj%2BXgn0QIhU9uNkwaYqZSXSOMQ5RCE9ANWds3zMs8JlcAelQ28qVl05jsqi1MApbKs%2Ff2Pv&X-Amz-Signature=b940c8018c5ddbd37698f57e5842144f559498bd446090e46675b8ffc4f43483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


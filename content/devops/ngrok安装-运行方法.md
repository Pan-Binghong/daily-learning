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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIOTYQAZ%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICuo%2Fuc9r0LXHh4NELOd07m2zCjGT9z8Ie5%2B%2FrpTj03oAiBljMCnCV4IGq9McGDQg6ySVjW2sWu3XX3fAZorW63tkSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F8uwt7YpOKf189X9KtwDlv2CVdiSnAf1faEPkfoCBfOJohqcU%2B76slfvTFGr1XkaeP7oj630X37kVXeiDXVfsncuyCfBu4cukZIVBi%2FkUcmKrwVjQYPvxV7cRa87DBkD%2FR03yGMIhPjJJVDYFbBH6v4ewezsuq3wwBgrBAZfGn5y2WT%2BtNZvlKgT1pzY9JQxOgeyX9ipMoeHCJtHbDhmvRCuGS19LKWf6f%2BES5mY7OJ6GZag2D3yYREZzfvECcEyf9U2ALOXdHJ%2Fhgu5VVu8qi5AzmEBx3fOUIimVTs4o%2Bxca123N8ngr7RqORNNgOraKyalMz%2FES9xg8QH0w2WcRpWXH8kBdYDEogT6SDvvDjaxXx6Yk%2BLsGS9Ety%2FzxOqP2lI0Kw1MWSZ6H8FTu%2F71hW6xQlE%2FQJlsy%2FArviNXvmtW1oAGdpWaaN095b0k7UcUQOso3yOHVUki0jE0El8QASYzE3fN4dFC6tJq8ASd2NBAxxnhDseSxEmX554gkc9EDQnKX8Z2vIAzZS8g3ZkUvdyMkIBDrhi%2BXB6%2FY7xQiVNIWcWnSx5opJxCNzwWv1GZgjRUs4gkLOd6Q5JnD55hUq6frolRTcezYgWqacm1%2FdBkqD973ihZOODNkfHynbyr30F3jF2HQ3pGZ%2BMwhYaYygY6pgGuq39BD65ac%2FWzuiTF5eczCxmMMMzgWcOarTMGLfrKKvbdDJz3%2FvRVb1DOjmvjlNd8gT3rnEHmyrNQYjdYxZu81O7FuW3Ctb31ALQFe3zKOMCmGnXsLkr83msR0L07x9ykaW6zp0JZf8Fm6E4ZXNlQQ50hQAAaltmkDi3w8xsw41OSBz2le5vuEZSvZSaZ0X5Qpn3Ta%2B%2BKm8DrE%2BqEhBaWpCbiEscg&X-Amz-Signature=3395579f11b8253abc75cf11685b38677a0881fd49322acc5f559088a3eb392a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


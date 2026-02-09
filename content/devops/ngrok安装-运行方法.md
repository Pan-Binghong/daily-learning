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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRFSRPTF%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGTasVxTvYIAppkDrm%2Bwkj6%2FLzl%2B9Yj8hKkOYkpuQDAgIhANk8ArG05DEMSQ3O5ZHnHb%2FUnqoZQGriz8NsG4Vu5AD7KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw62BfzCV%2FLm6MOH%2F8q3AMc90yAVJoPnxTqQloasveZfCXDN%2Betv5gwcLr%2BZ00SDFN9LahAXYbhTtBbrLbY2nDc7NES84SgwI%2F%2BwB2bShF4HeShTOSi5mcKLYdHVE3%2Bd7kZ2ZrLE%2BV6gTj510FOTxw1RIlraFMvp1f04lBXe6mirE4QFbmEOx%2FYc5%2BnGS5QXEyPbq5Hj4UOW9ZuiaOCuGsyvY5Jwog6ok5pFlyEJMlhEkJHpZK%2FF04dVeM1eH1X95XWrZgXIV82ZZba8O1ViUu%2BEg%2BbNdjLvKtl%2F60RUTiT1jN9Bc3g10c7JgqR23Fj7BMdLwtKEjC%2BYYFodFD9ZSZncvNB1wqi9eL1S%2BkBvO4JbHbRH0zCShaMwlmOydfy4MWsbI9yR1eUtnpU0h5z%2BMWnlstIXvYRcv7iNkImXxmhs1TYch1Va%2FlZ0mGIPnw8UiEi3SG2L7Kr5Qe%2BdEjFkuTBU90lgRI2v8cGWKSodVhwcgfBSY38zW%2ByIn8mb5EkMkAe%2FQNFhJfiecIewijX1J4XknrUhUd1X8kzKkozPIXLfD0kvyYUJWhluskuwLVanWVXHKXdHvltgYe14DU7uYxZ%2FLBEEu0E8Q66Q2s1PI%2B7wWdySE0I2NWUFnrAW%2Fr0YAi3aIh57cJTo%2FWOzTDrlaXMBjqkAdw%2BErCJZS6GzB3uVdzPvOE%2B3SAnkKgZRZwlta2QcteY8zA8CLMAwbXfdiMpLqXiINUqZqIZUFaI%2FR89pRYAME7EPIMLe9TCTyc4fXSnxkPHYJ9eqypL0669ItxYUM3LDBniZRZcLi85kax4XCDyYZfZ2B%2BWDFod2Gtpi%2B8ICCj%2FJsHPEZJ4ezTyeRdLe5en2r%2B2sy%2BUpIpG%2BDCPdVV%2BtPV7ZyrV&X-Amz-Signature=0fbcfa1abe14237fe505c510ffcdb75935466a7d0563321476ce2b1f90c836a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZMQAOZL%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6Z%2F2wbykJfwOAPdm%2B9ci0rcQLSx%2BX77RhI2EJyc8c7gIhAK4Jj8lbJxLo72Bz1asBiMFsJfjDjC5k31W0OVE96kkZKv8DCG0QABoMNjM3NDIzMTgzODA1IgxEAlrIT6364joTA%2FIq3AOl1C30KpR80nFVHbJ0%2Fj7cRb5djxMkJF5eX9evUZSLXtUm0dowwyqPr5CcXXmQwqpiwi8nm0QPpya2eYUrXjDYEwfSagaABLC8BjJzXlF0eNJoSbPNkAvq5Ed%2F%2F%2FJM6gQqF8Xv1YgWZfd0WfHD0oVDYUNVNVsZmB5xe3YXIVU%2FXZXkjVZl7GpEd9yn4IddQvjtueyuZY1fbFAafXVVWdIizzm%2B8WUyvRdj0xXJUb9Hv4dlFc5ZEMJsLywLUn4HygEmRsuhjKtanDjp3TQ5RNFjWVSN74hz4Q7MocTAzE6JqrGx7jrvn%2BeNLrU86ZUExI%2BpCLCBV%2B%2BgGz6gQvnHdb%2B2fuVNta1rM9gtVouJTvpKQ0ehiRLRvQqMoAu6dKZHQmc5Bykt%2FmVczdlfttdKbyCyBROEZfRq%2BQ4%2FRqQugI%2F5J%2BoWIwiC2Lbn0mHj0yQ%2FElp1%2FquqlIEPOljqqdTBJQ4hNQXi78cCYNBXbWzhEHqBbkggvlzmaXGJ%2B3SFjiBI2xn7T7DaE45nwMNuI%2BbBIEVm07vQgHzKdCKPwjLgv6jYwQFHmw%2BCYg%2F5sO5aSZ77JANePJQOvaQNO%2FIqm%2FAk1ej%2B4JGRNvA%2FpU0rqkkYoQTcaqgjWKnwyiPR2JYI%2BDCJjKDMBjqkAZhoVfeOeAarfYoLJoci8ShIavPhUn8VIOmzoXvh8T%2FbYJ1fYhQQJZmrDP5NK%2BzYgdpiza%2BlEm5eszHnVn1qOKTn2UQSA1MbwAPw1n0j8QutL2BuMUH0oU8b8z9I3JQVNYmMJ%2Ftxw6xJuYv6GTv6CMOqlT21Tn8FLVkgu8mdhUsdJE3JQXaq7AUsLj6rileq1J2hffFtQ3jsnAYi%2FqedSx3SSjFz&X-Amz-Signature=4b4d38323c05326ed3eb973d64baeecce7489b1da9bf6898fbcc20443d60a5ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


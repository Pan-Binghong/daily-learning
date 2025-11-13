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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLYLQUEQ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIFIOK8T8i4cMPcPKEZyoKAxFpaiO0dS4uC1d5kV6rKgrAiEA34L6DYUeNZX4A3i24BR%2BqNlO3ObZn%2BGbITHuCHpfYnMq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDGck1x9%2BH4gTPznspCrcA3RVkFDCX0E46Ru5OQCHVFp%2F5dGLFxZpHTnKG6wmgObiyRbfdC5W6Cf0ciH8W4MWYSVIzmi6qwNqKhHwItQW14OQDrT%2BD4rzSUnjfZsNNVO8LrF43TOoWTGAK2stv0PFaQRXkua0%2Bh2SILH9UKCocMHpyaW9fmoaSvfpyYJv95vdge1hUt78CObppq0bX1NlvmtKkaaBG2KcM74lrgTktRnM0FcSGnN7880WZ1pcGv3Ncdd5%2B9SwPHv8kx9g4%2FXvKxEpLmDeQTGSY%2BPG0dhK5AIOyP5BRl0x49TtHBhzkECrFDerUCBYg44tSXzOJgj6t95zdhKOecipvpIM514FmnGZ%2Fom59Dohx75Atdxn99XHbLbA%2B7NlyHKTmthB0e%2BJzy%2FhTdXsTGUFG2pM3SgLtgCGfS14%2BQYSV0aKyi8997moAphW5BRZMTlG33FO1aR3SCpNbAyTAwJVLM3TjWC1sx0bke3fZl%2B7db9Bam%2BlFoUCOroIn4uDH9v6JVwtGd%2FhpKYq9yM0ByFJNJ0vCyf%2FxsNkGYHCZeo0ABnJrn3ziAjK9lWpu7Si1CmffaUXMpYHrfIX84ppeNO0xW7NG4HB5f1xT83qZo1FR3bdn66ET%2FZ5bweXsjVkX2dtKGYFMOTx1MgGOqUBi%2F4%2FJ71mLLSyge0RxWh7HLcoG7NoWgrzoNRVay68UKQ0BBzBlll1yf6LMujx1JkAKOojjOVf7eL6fNsytiN6Tpc5xN88mKR6rNJFeqZpAPGhCGGOBh2%2FDtdLjbdZzFwqSnXdX3HTvxrAtlRbtsqJflpPgCDceuQAdr8Ff3h40zyESsEl5uO4aGbuSLLcsVnZhYaRmKYgLpadHhDiJb04mE58GEoN&X-Amz-Signature=c4235dd91d48debb90f80c3aefaea09879fc358407556ab9ca492396f6f4fc08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


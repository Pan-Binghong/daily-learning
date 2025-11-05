---
title: Ngrok安装 | 运行方法
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-29T12:21:00.000Z'
draft: false
标签:
- Ngrok
categories:
- DevOps
---

> 💡 前几天帮人微调模型的时候，使用的LlamaFactory的WebUI，由于服务部署到他的内网环境内，做了内网穿透使得可以让多人访问。刚好想着了解一下，在此背景下，撰写了本文章。

## 内网穿透

### 原理

又称为NAT穿透。NAT穿透技术是让NAT背后的设备，先访问指定的外网服务器，由指定的外网服务器搭建桥梁，打通内、外网设备的访问通道，最终实现外网设备访问到内网设备。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MHBKIYU%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAINdGJztKoNwnViv9c5RG5vGhLUBu2y0ZAHlEDBSCumAiEAuXt%2FDjvi3qomNpVnPU8VupCD6zi%2F2XaueLlLMoGIV%2BQqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOPpus2ghX5jM2phpCrcA%2FwWA6ZGbQxqYF6mz5mG3r5ldjOB%2BbW0QzsBoIs%2Bjwb9IlNV1nYtGvcQkqUyVpMPGtvMC1grVcgYF0xEeb82CjwCVXDpDyjsa0Isfar3UbEIVvOKBmbjbxkrWjhmT9sfIWMJX3Pfg2AlG%2Bv6GsHRVNjs%2FCpiCssNi2KGizgLhYIxVP4Uz8kDWZopgIb7RgNuN1hLI4pMIZUxRvB1Eewgs9hK6frAxdbsTxff0VJyAPR67JYx%2B4QjZr47aM5XoS4MPn4N17FszRioba6wcaLqttBQZK%2F841MO2QPTuaJZPUvqauAInI04JD0uxZyhldCkg2lGvViTXM5T4XbUh3rb7SJ%2BN8%2BkVfP9CRMjN0ZS8%2BwNmzNNHf9m2Gg7Ux0PkDAXFYXRG5WoBDfCIFARUPagv6ihFQUXz2N2hOAYGJfNeTU9rmrrmhtBvpyceQaJR5288xRnbKPOjkkXk%2BidA3nsfRQ3IK0KDFMSrOntz0R06X59Ol5Vd0WdhBt1L%2BCcHE%2FmgiIB7hR90vj%2Bkkum4yLxHTwBzzm7YWR5viVX%2Bph38JACzU6glZJwZ5iF3DPb4NYxHTdkr1ync2V0WDufz0lonKO0PRkPD7trCP6uij0LO%2BHoq2ODIPIYaDd7ZE%2BOMLyirMgGOqUBH5VMjuw681JJG0QfFUXbzLhLCd%2F8iD6PrtJp0ZLdwAsj5LzopnVVvOycftNiFxo%2BM3WUBS%2BNpAq0UMP9mlFbHSH8YCgRBPzMIA0HCjfX6lbwjcglUJchVyGxRBgwIGobkjvicoyh54AywOpMYSsebi3hPRun2o2VpIrP7d5TFtKuFBWusJhNy5ibtuigtNJiyf50nguYqYo3ILmqJsGcuIq6wQDR&X-Amz-Signature=733f492e5b6fe74a3866d42c2adbb93d279d68f8576ef2ca00f25f659993ac51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


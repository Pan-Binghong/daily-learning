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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663465TJWS%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjUOi5Saa8rSMNZwdcdP6ziYCrH5n2ugjH1sZwbrfbMAiEA8fbE9DfG5zj194QHgbcTciBVCC21SSKF5JzSfk6oxdoqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2BpHEaqg%2BJQwzakaircAzdTiEGR2y%2B4W2wFBk4vr7OD0FbfzA89wrir8d4PO8bLghaKOegjeqOQb7GWcsYWTdvc%2FVEfdx9wBgDHA6Cd%2BFY9kWCTahR8Y5mrA7nZjYCCC3PDS%2BxhjwIZ8wtgMOJKwXhnnrFt8NCDTlYnrWtxxCSFvOp6IaGCc2e6VF7A3VGaylBp%2FaBWooXmsgtHFF%2B7VZZB4%2BKjlNS0IcS2X5N4h7V89i%2FeiQOeRki0n3OQCBi7MjgaYdc%2FJZoj0m6A9JXZNK%2FIJeiopskpW6ezVs42bf2vZ%2BL%2FE1RB7XngoLly9TNuH2%2Fto%2F8MgNMFaIWf1A59y4tK%2FNw5SOn4XSWdONZVKsmOMMUVNZYqZ5nWBVgCgjOHWBS6N8AZLc0BR8awjCaXRKuqmvCWFwssCEeUh%2FX%2F63tOwZ8ptvi8iVmVbzmdtLS7VeCyMjvVFiHRuVFbhWPHp5iMigZluFf9urv2jSTVOHOKYgGELfJtzBRNlgAekXzgku1KJUCxgb8OdmP8e%2F4gW5KWn58dHHVoKwUrbtJQcrYJfu9B0eGmJAEKpcdtwu0%2BfcuBEu9urztTIaw%2BUhiQBNLQLst0x3IHKWGmduSzrrXpICVM23N%2B89PFH%2FRDlc4G9hH9Vh4y9JXTzKGTMNLI8MsGOqUBRmq%2Frwx%2BHSjpMdq2sl0FcClEYGPcN7KYSXxmpuv3W8EDr9dhRlBKLDNNFAWL62eoO8%2BO%2BbqTOrBCQ7ZTG%2BKUzW9Vv7y%2FWh0%2BIBKhbPEVPZhsJeyQ7d3ytnssMEmbf%2Bg7TuvL5mRMJIMJ%2Brc6QQPOTMsRg6y%2FxH5QhwPEcrV4Vv%2BscMb5PZjYGKJlNFtN5KvpBXWxK6oOBS3B2xTj3K%2BGkIM8KasA&X-Amz-Signature=dc1ab53f7f6d683275f50fb8abab4f6cf05c2b08554f046aea2578616670eb84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


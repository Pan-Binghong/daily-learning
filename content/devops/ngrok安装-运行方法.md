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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFRIHYWX%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQC34bYa41AyydFCKlppNT27Ptg1HhH9nya4uT5XQivsTgIhALY1oPxWzJC%2FCD95ojFhB6PEkSYBsEHVmCHQcXMM3brbKv8DCBQQABoMNjM3NDIzMTgzODA1IgyZpBaLkBZzvsLtzRkq3APxRy1%2F%2FrOW6LcaZXqsde058ZM2ffJLHRc5yw%2BAx6NI3wK8Ds8Czb8vg2P9YWzGyr6QACDWMks6W4Gv62RBKp5Dwdd1cl1MdJBonn83juR%2F%2BcKHgdrxWhKhFLtRKTpI060HKm%2B9jiH4FoQpu4GidooXvaeg0PC75mXV7FIb5zcBpzl4JetCZyhVa66AAYS2QjxGEpnLX0pc7A1G9n3XsGMgBYVZmd0tvSR3qJGfjLn8g9DisIg2PFeVnRsWgf6YKBs3db3urO2GtpIlT%2FsoVfH5gYit0aJkDhZCVBs589lsYR5k0SBtSEyqiOKKx4BaRz8A6hJIPhSxtpn3gWpnVM0pw%2BH3L3VzwrPPaCM8y4SCJQGC1QM0lirG95ziPw6zkX806ww2BGdLJP6Wiz2JV6vTfUVWyjFf4FTFo0ql6dba%2FwzxrGGVA%2BnWKjHa%2BI3pelqukMerdElFeRV0QsdsHnzrSfk8Tol81sE9wcpAMLL4eRFXuCH5gNRfUNV3Z7lBtrWv%2BisXwjDBhlMJbF6zn3LDGVT7sH8XuqQZ1n8mim%2B0NUO5myeApWKDiFMMXY8s3vzl5gD4Ldwlp1xh8iWJUSDpNSA%2FRjfqYOPSp2fyhNSEuUqR2jOVT%2BoLi9fpHzCpj5zLBjqkATB0Hm2GelgdMT8lr%2FWINi%2FRSnfMw5asxxuqHGLL%2BCX%2FbjBCzxtupr%2FHraXX0CeQTzA%2FhxQWMXlsgG3Is6L96PzD%2F11YsL1N7YVsdRTr2RRzA%2FjYukrKwQcs4WxhJc6Lhv3Xq%2BLjy7KbOoPt5jvkM8A%2F4oSBZApDowBYZbptGxCzSgDVJR%2FJJX3sbZ7rEbSEFVjV2UWS00IdRHUMeYOnYwi6ITGc&X-Amz-Signature=faaabef61c4964709c60c968b79d9f32bb39e173fdd943f1ba88f48fd1b2dd89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PFV7QPT%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCICTP7sZzhIKVOJHPLgXA%2BV8se5jXtRVCUb%2BeY8UHC0%2FOAiAqpKQpgKuJHTOhFjI4%2BzexPIPUOjy53LixYN09%2FbGYRyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMP4UGwondhHn0JjxZKtwDU4c7wvuZWIE8SLTXgKgQd7fcgN0wXSwnzAPr0xTPDS5wKlU%2F6qqRd0RMPoG52O5456pbm0joV2p1qC2g%2FJPYoOdACDwKCvUtXKtC6pKL0wsc%2BHHfImKySw9fQz4EqkohSbzonBCUL3x0LaaEyIzZ7WEIMN06U2Z7StcoACjBgae9efXVIZxDENpc6QZMc72p6wWQ5CP8%2B0Zr2IocryUMsth7FsI5USnXPfIzlLLsrc5TrT07AX66j8n45z2JDSzwm2KiGQglk2tPjhHeQ5j2AXJzelzkd%2FqXR2T%2Bi8uAQIGuAshbFNTB%2BxarWfhOQKA2Mf6G4vfI3IZ%2B8ZnXj0JKZ9ZGZVdCLDTV933Jsg9iFBtq7pPLK7KS5ucFQ6pbk3d9FgFRXqjw0aQIO8VNtBpzM%2BuyaPXNBC0lg%2FVPNiq7yQZElFWAyLR1ypWNHcUGlF9hTMEyMgFrHgCUHJRJuxaq5m2sUEQBUise9wZPZCpXxgUF9iEmo20BrPwSFkpxl2YCn2rtYm7eavoE4vSAdm7smfm0CcMel9eqMmUrL3vpNImqnbjFIgwsLHgFT117FJaSDd%2FuWrFk7M1Y%2BDZeZcqVklp7e4gOm9LG42m4cHxRIbRs6zVnKMR2VH2rnwgwrsjsygY6pgH6C5Sv61apxKneOKEML7glbsTLYXdwEU3D2J%2BdVgMdD58lZpEtQc8OgWCV8cHZv8VQjz2fD8u6ptxwJgOmPNVyCxF3BrLMJte%2B6%2FIY1D%2FdvMkl%2FG9bjTJTjeTKN%2B26IzkoLfdEbPV4kGEWNEy%2F03z4nae3DA4LNXkyiPFw3pTZ9fa1siSu8RaenEJ5isa3gTfOBWEkb4TwL5hdZwgGMQ5fNalXxsoc&X-Amz-Signature=e31e007613bcf9d36abc753013b8efdda50cb3c71989e441d6f70246a80d2c2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


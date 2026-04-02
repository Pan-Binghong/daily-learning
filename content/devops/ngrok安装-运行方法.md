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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QENFKHG%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAaGR%2FAtuAWJFeRlDrHugQNxd%2F18QUfd95xhwDL1LlYKAiEA6knKr1Vt8yo5xTvZEHXlQCwuaM3jDNI7xZnal5GmaWoq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDiQqcR%2FsuTTvAjHPCrcA9GIrgWCGS947mUN1nD7562RIUDHxUGacSF7vh2nL1xIR3%2FukVsIzNFaXu9yItRc3%2FP0SLMeTd4pSA98s1d7Hzviy0GXFsaj62xjPc%2Fhxgq71OTgH2MUuypkc5Dzx9ehxF%2FVv9Ax3XuI%2FLF26LmN8G4GXypcLck9aZ1Wu3v0G52PXLZsJPR3KLEf8xhpeD3VEEG3NMt2EsyvY0RWrL0ZE2AQXUGATA%2FxbYCGKSj8akR27pUtVgVqqN9yE%2Bscdfko%2FgOfVvIFL5iX8X74kKnw5t53LLVQE%2FXFf5AcX3cdKaOoBWkBLo16nYXzPkCDY6BeEyNQAeHqSAGPfOhtWwmeKt2ejrKqTOL5gdXnuW%2BZ1OR%2F13tJvjC%2BGheDdzmv%2BscnDnb9s4M0QmkoB5rIbsoojj5IR4Ha9299iIsOm61gZfxSzYwDH3gLMN7B5uZO8hUW%2BcfFaL1d%2BDiSC4qxU40zeTI%2F4KmljT3wSNATXhzLhEVAmK9%2BtbH8qgOIr%2BWOb4E3agEonxX4hqxZDgrwdP1rWcI3YlRhCtasB57Iqg6kB2j8tN3BSawxE9yXMmhyxSvkjwGgXWBiaGrhDMPPqAjzAyr4Enh1OfNjnkwDuSh3eKD3r7Fo2yU3EVegxQkbMOiut84GOqUBtw89vvIJxbYQipiU0UlhDmJzRI5A9Qeuvwx81p%2BYfKw7It1It6tT0TXv2ZnlRI6Ew%2FA5al%2BeGgJd5iGLxOj6ekdVEQFbO3liNkPlm9S24Z9QuHc%2FSOGSZTRw%2F8lFe%2F1CjXWsHckOJehVoMsX6HN6JhXMdarSkcNEmaZLANZbZky91Ct%2FxEnPzOFXMFDnsCd7RXgstZLQRoXdVENpQUAhsKNxyGUl&X-Amz-Signature=cc9fcc7073f8d642fdd7456a8e509616475b4beb61f62613432f8b30f5476a7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


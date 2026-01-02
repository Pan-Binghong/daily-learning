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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466366XJPT5%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIBL5AotR2uuEwv99kKDK5a0GdvEfB%2BHl1qnDkwpdhtciAiEAtjLbv555f0vL87a61AeXDqmfxzHOBzmmU8dTwRpEGtEqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFlqrm7%2FAawPvAc1ircAz%2Bn3yOCa1El13FIg4T12fCiHj9jKIRiPH40xFAAHCnPAixhZKlrLdfFvxqUw336FW3sHuFT7mnQq8IgswJtz0SA8d1InZuCL35UEPMt3HAA4v7ADIrl1vIH19i8zeHCSbqqGwW8vP50ekG8RKRlrcy%2B9eeuEcpzjoCN%2FWstbNUpNHf31pEyJwoEytO%2FlBeQtaAYg%2BZf1s1Tx3tacabRPpXn%2Blc%2BhgbQrt6VHCvDahga1hLIWemDjcuFkcC1XnRAQnxa2VjSIxRIaK9EuM4s9tPn8W3sCUYrLgPdDb38jSVXwcp4TgsfxyHVERFLVN8VeGZ0jOX2ArvKAUrNgnb2qFaQ6kQN7m3TiRnIi%2F3cmRxaxWU5y1EBwLIEAcQ%2F4zkrPdLH3JjYcd9W1zBdwWopX1%2FUw80GTZ1%2B4Wi7Gtbt%2Fu5A9aIGjSq0cCiUPP%2BWsjt8zhexzBaCpyuGq7X3PVBh%2BcW3DtzIcEFhayYJHjSfVCRwTxS83T0n94%2BMFgKQeNtrnQ4nZ4FtGaACEHKHKI1zTfwHiPIkgTp6lT4GRGZJWVN2Oh7aUJeTaubLPxhi0neUfBPmk%2B1NDsbmB7PyJj4%2FpruB30tb%2BBMwkLJPfyJYE4C9bZecibhQTMJl1EwCMKC13MoGOqUB2MqayT9Vyhdd6Y9JrnFj2ku8Nzdp5HAW5mjac2fD%2FrRPsfzC%2FapWx3u023EOiNlRVrYykGmDSJkg0PlKENUPDX1tYtmMM669QdstwFIysSrhI2Zg6cq5zGADbO%2Bf6M9Anj1kz88Pv2n9HeT15MdDkkZTExW3jzwx3cfzg38OBu9NnslGF%2FSWhLsO7mG5uoe7eBtZl5JgU%2Fi%2FAkrQftXFizuC%2BLtU&X-Amz-Signature=0394f84881b0cd50b43e722ec55d59e5f4b5385be0f9ef0b1a996f14c1b867b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674EXUYUV%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5m%2Bepr7PfPH3KnZvtpBzTKVdV3UPfXgaWLy0gChFR4wIhAMX9t9byujJtj60ZFOEDquka7QNBSO8gRTeKJwHh5G36KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnKu8rajAyWryduZAq3ANpTBO3MVc3uFbxC9inKoqhwpymwI9SuN2IXN1Vv4OPa70vLU3nEHUMtOqJyCK9l%2F89XzJ4W1gjedv5yQBjPhRvV4jZlofiLBbGjutqzzkXD9jx0YOaBptvG%2FKncNomE0RgUUspgn80ZoLiTu8w2arwdLYcNQcy10PAvRvCwM8Z6XASVr14t6UwER6YHAe0EUvhWks9%2FxbXiSWUsvRed%2BfIFw2QPED1%2BuY4qg9s7%2FOrKHJgl7vkmBBzap%2B67ipErafQKGxqwM%2FtlU107WCNT1DCY70p0eCnQiGX1DN6m2xFPN5s4Q4Vu9pSLePqJjFU1OryahQvp1Ssos07Hq9rM0w9EuNNRv6E%2FJ5kbCIiu67Vw%2Bsm98cQQRB3%2BU42%2F7GdPIBff%2BK%2FUKEflua04kh%2B1nrf6I1LoR8Mju4eYZgIPlI1al9Gq%2B2C3Ovk4LYWzOIjLnHA6ufDx3gf9LCMX3jmCCEB7urDPSTmMKKyrRLJK0q8jdgvfvfcClvK2H3BdaPo%2BngF2Mv3ydLvVx4LcZlIiR7oPucJFSZiXC8n%2BpVayitBbZUOvDBximbqc934Rc3ejGFZAonuzYL6iET3yeV5vI99GPHCYYHpPYx8LsLADd%2B0Q1%2F0YX7XkGt0azLwiTCY3bXLBjqkAdWvz%2BSvIFzA0d5rDGDwbNHAcn2NVPMgGWZ%2BT6AM%2FP%2FRIF5jZ%2BUxj7876B3rSm5IkRC1R%2FxADCrzPv8Fg%2FqxClXE06SX3vz4U3P%2BrbJ3q3otur%2FscNczfhSAOIAzcHi9HUi%2FaM4NkpVOlSY5WjUwoTRW%2BMDOR5QbD18rvlo%2FZhhLSoQ2gUuCEzhMPIsvMkL%2BAId%2F0Z61TzLGhgGwfGkg7l4BIhsj&X-Amz-Signature=1924ac9e3dcca492877ba1f2aac17264984b623bfa98f0f5dbfcbbe838d654d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


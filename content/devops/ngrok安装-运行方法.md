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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUQJGI5F%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGi1Icgmf%2F6VuIxmz77zWSZuiBro7OZDpt0pCE9bwROAiEAoaskFFRy%2B2CgC0gQG6M350H2sLGT77BRQ1joohsnHC8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfILz0Clqjjnvg5AyrcA6h0t78vtiqK5SuRDcQ6glH%2Bbj10nNwx8hbcxq%2B8LYJmF%2F6sZpzlyqLUFEgJIDiwgLLrTYmROaf7eqNebYqih2NJMlaJzqf%2BKhql%2Frv49kA%2FbZoml7N%2BmQGDa%2BDnpOT%2FvemhuM5tYLsQV%2BRklkfB2G97b3rW2%2FtK9MS8u%2BjycHbyNvu5svvqw5EQXkEp%2Fi1XBQtN%2Fwvre3c65sN6a9h2FKEefgnj1Dx6tFhUGRbv9h7Z473%2BXI7TjR6f9zV%2FAFCJ9%2B%2FHtDWXjdZwAxQiqNgS9Kr3fX7jqNHHR453%2FilwFsJm6%2FRTpWTqxSon%2FsH47c7rFszZ74abBnRa1CHhbvrABbMJQNNWhFiunjYBRi57U%2B8M6TafYArTvGtZGBjXsqGifCS7h440u8LADiNYx8%2BtKEgoVFaGsJcfuDL8DiUZmfrPyMF4s3ofjcOi6UXUmVHbSnEBL1JFEADYGS9LchtB8oUny14vufnyzkR5c1VDvjQ6%2F7UUvHvgkRRB6zktfEjqHatBW%2BjkfmMmPY7Q0BHAGAJBtoLRGrA3GfD%2F7OuFtXOh3iVR7zvA1Ht3ku5qBi69yHLRM2VO5kY%2FG20cpJXDQj1jrYyNTIiUOhZA34UcBQT3ZXxf%2BUGgbx5xdYL1MLTJks4GOqUBOPQSGyo8tyicawRFMncgGLId5AX7MO1GLHIRs%2FjPrstZGz1NQBU8pEmddwBGqHlxPTxmCPelI50Kx9DRRzBDeipMSgaUmLI1F2sRTQN69ZSgRp%2FwQztAj7HM7QflWJnGFbf2SB1T52SU4EyXootHA39UUzMz%2BdnQwseV8j8S9zTSVCALV3rM9JKdeVEOr2T%2FXvYCHk8AlknyIZDTO7D%2BO2%2FCSxf2&X-Amz-Signature=c2fd36962d4c84c011b44adc3f4095999c6b953434846eb139fd6523adca52da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


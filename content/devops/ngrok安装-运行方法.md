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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NEZP23J%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIF9fCr7uNkpQl23LsaBvjKpyNhWTx7d2SroKS8R1DWx%2FAiAnMc4wkoloh2s%2Fu9JxY03NzHn5%2BbI3UiWZdfDWcnck4Sr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM7SpNuUezlslwAlimKtwDI7y8H2mnPe9pYeAC4NpZkHJLFqQZUloZRnmwqYmeaNHD0wPUpJFADlbjYpLeDhM694N0dQnEji%2B1Uf33gQ5zyaULXkt7am5eqauIKhtvJJ3A6LM2%2BSqQ2xsfUTfa9TMKHIEQX4GtqTOWFjNkV1OuTB%2BJWjuM7R6xuiyasXyVXw2TbASEpJtxgQP8yGXUh%2Btt8HzQ28DXIohpyAgtGCjproG6g6mIe%2BO27J23x6983EcFkg7VXH7GXxDgFYGTTa6cyKSAeOL5fhvUTyTWFSn4G4C3gYq3Ck0gJ7ia4ZPAt5dtxMl05gn048flfl0RrcrEqW6jGOsMXSFDUe5qQ5QaepzTwlUiB%2F6ddzW9CyX1UwzvC10WB5PHACXsTxV4zhFF5VNiV9pruBGu7PuPaddayycaAfTIywElcp6zmCakqZEGboFC%2FatKzPNpkw4Y3%2BEm5U0JU1l4XIFwi7LDYVdbB9WeBgFDZCb7fOkD9TDQ7fWL%2Bsugf4OshRC1CXW%2Fu50xfdCJM4nksZ%2BXjr0y3UX0qK0sK3FxSmmY2EL3WOz24V8jwpsNc3ngUlqlvipvBFOb2zkhumjfUL%2FzsinMN%2ByWZ2Z1yW4boiqVkgcpCZ3NiZ8%2FHmyCIiAGFnmFGHYw3vmgzwY6pgGx%2Bpdu85Kqe0knJk6gK8iucqeaikYHsvHEGIJEh2cg36anPuKGlC4VBisBIG%2B9ohz6jBrno2ioqPDsax6s4F%2FDnaDkJCwb%2BBrfOZezDkpWBmFbJgm6ETG%2FCawNyieQ7MZ0KqPPCE%2BVDPsLIxuozilOthxxXtLEeC%2FTQ04NY47csUD3UCe26QEFB37BFveU3Lt%2Fl0MOYbG1ATl2Vhfv5%2BHvL8%2FryGuW&X-Amz-Signature=12b8d9013c0b80286a6306950f164523d3272a9659d71e7b862eb2345ae4548b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUVQGEL7%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQC3WPegY9%2BlAM4dIEwF2jJPzHiY7xPqHYTbt%2FNuAQxDogIgcY2v%2BG1MkG7xZ9xCP150EF3bdNNioaCeKW6V3HfgS30qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcITdCw4KpRFVkC6ircA7v02h1u7sOXtV%2FYPco3RxfzKuIe6pSxXRLeQdUP%2BJSGREUoK98euddC7zD6NXNuHd4djMS5fEK3G%2BsZoc8y827gxErMvgjk%2BkYu8i0OBfk%2FQfTlIEhf4NjcWRPNpszhCpXPQA4xVAFaMQRil%2BBJG%2BRk2qyHg%2FNKcGDBg0YJHd%2Bqp5fK%2B2jQVm6mSSOVwI0ubiMxC1twr3fCq2mx1PdHCWbJdnLzmo6nfgz6guV%2BlJXhTA50AySAsxGhZD8bk6pAe6cGdehZPq7thdrt0BwbAnkcny0YjERWXN%2BYKAo5rgnnajjZmJIvch1SP6zw2RtgPA2W11QJ6WTjNgeLjfZE1n%2Fr7C4%2F5PtjKlG%2Bfn0gVNWvAUbCjrEg7XPNoKQwH14X5Kms%2B3lOjb6yBg6VWlGt6t4BEubYSwUxBzzmjXqPhEBmWoZLXdmCrSrs%2BUQs4Sm05EIyr0zG4Pqzw1xqnQJ%2BXYuc9qknIkzW8YSUvthANoBz%2FUFIGNY7C%2FjnT8V8gWiUGZ%2Fe6imbFRI9fcxagv71oYz%2F0evZ%2BNmnE1b9%2BOy04klSJmxPKqZbnowyuFaT3ZxX8%2FwNTXRWrpO2bxX1RTx5V28%2F8%2FnK6scAVds8QYlIVvrY3pe4kelDzZcc3zVGMPK16MkGOqUBNPhFDXyWKjJEhfZZpG6E6rXMiE4obVGh8gqWpev%2FpgT6iASf8jOs1Lo4cYGTN46wYA9JPOlUzOEEYqjmCzdu2ryYfP0kXOQGFk0ZbOh1SmSPWUAAj6FFH%2BRYaBv8Et3P17AVSaSYJHgnDbQk6VFT1PkQRbbUSJjznK5ivq7iNIrMibhwtDInhVQC8wL%2FxDiiqbXLf6cipe6O5%2B1Eva7mUyPXNcna&X-Amz-Signature=34ba068c26ebc1d7ef5e89e6ad6098fe0626d260ae063acd042e1928583d0564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


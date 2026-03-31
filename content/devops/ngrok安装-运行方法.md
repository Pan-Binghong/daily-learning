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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663QFSADG%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCF7ZLmHd%2FkKrpPVbLDcl0ddVW%2BFO15tAqt2bJlQh61lgIgVS9jh%2BSr86qlbZTTsC6%2BBwN9dGUgq4ZI0cy5uAuZvz8q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDFDmu2kbFN%2F8sdtOgircA2oCqoNnfGrFs74JI8urdWHlKaX04U%2Fj%2FZDKOop8vjUHupDCSl9r%2FdU8HPG5Z2vV%2BbMbbziJjBZZhqlzB1QmbqWYVixA27GpblLjxQN7wDtnVWy6CsJN%2FtRtvUqicTeqvvSSRJ58%2FtzOUqynlGsHkF%2B2vtTnhHPjThAmAnIhfs7aXZV1BaXtzoCyMbuN8hkmsVwo%2BDb0Vy4C%2FnbA%2FP%2FJib2Juo6VV5qM%2F1ZTxU8WqbHErqfX%2FzmzwmETIwTF7JOk%2BE1ELLQzXNN%2BiMp7n%2BixvvwVmBKVxdMFlFvrqiD6QqswdKSWm%2FxAGkZCVHDemJLu3RbFvT%2F53dqJu2xxtOEvWubX85fmPfWNbnDhz2IgSuXTygexU7epNmW2BVXTKesAnYZN5qbQiTRaGumaCt3l68PcrH8iPJX%2B3NlqcjfEX5BYoXST07D7EtbIw%2BiumO57B%2FIDrFuziZQgvnZbFXqBqFbKuhZW828H7FVd%2Bg7iOC1Wtk6z2sPm6MOT5MfctkY%2FyEecRUOWhdhdfMO6tltL9bg7nJlRfqLnLeVVjtcE6MCXhl%2FfDci6aEiyPeKxkrI1q3cb4Elk%2BBr3xE3qRft03OHYY7lgYQ77K7w5CkFHblhkQUvp4tly7zUBp6FsMNzwrM4GOqUBOcevdakh06T%2FH%2BiLyPC72qJ7SpQ%2FqutFp%2F8AFNwTQxIUWk9A2jKpb5a4oOFdKUC8%2FbghBNWoYMTiVl4tu8T30Q%2BSQRA%2FCbI8cIzW0mKFAA2%2FLaDettOcPUyYTmI3%2Fy40nYic3p8iq8pMhcDS2nWA9Cdss%2FTgRNDFXWdi2G4CYFXYuXlBUp%2BceSQZZNzVnathIOB%2BgZe2I3H5Go1FChzv04ul2Ye%2B&X-Amz-Signature=8a14ae113dae57fc07437f15c747698d0823712cb976ecf505be68d83969bf0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


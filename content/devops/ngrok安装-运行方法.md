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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRK3OX7J%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMwFsCAbCkQk%2BG4xGnOHSdZJYWANrvM%2Bszw3%2BFWqfI8AiEAr6cOd260WOY1RrDBH1HcrrLlTn7EhexuoaBFnXt8y%2Fcq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDIoiv2H6n23U5p%2FuPSrcA2I7DOTFwl6lg%2FdY7LVehB%2BsydeNucm6whKlMfvS1PIlEktciNIhnIBo6YS3oG6um%2FdiINAR2T2OlRuVUjDYglUn7ohHzhaUxSAXAWBLFb984MWB1ewG3KN1RDjWaDS4kX9nW8HAJag%2F5Y%2BWJRm9otvwmrTcfDODfnKHqP8N3TVZ%2BYvKzsVFEfL0QYztTmoJfA3xp6af8%2BESu%2BblLppKT6PZjqs5uyqWN2WkIb7Wubvy6KU7tAjFa3sEZcNN%2B%2FyBrbDwrD338sD98KDsFQu2F4hr5ftEhNTJnjngU8lkTrBUEoCae97M5jcigP3YE7I0S46bAEP51kLHM%2B7ddB9bWEArobMUCBbMvHKvsFzTesx2wBKKQTiPOJC4UFLjYGipF54E2wTVb8Lhln6Jf10ylFlvkiPq0uJcZrqqUQSKrYf7425Lx4kh118B5a4RHZu7fFgCYdlvtetW5i9glanCL9PUMiatjK85YACUI7liIsc39RH73O0Hl3Cy4ytMlJEfR4%2FALJAvdnJv3%2FNhFgQnNRRQ9G5wiC9ZYjWRC9B%2BOqCMl6ukuQ35pcyOEwMxxqnM5sHevwA7Sxz41pb%2BRmAC7Cl5vvHcuEbAa1hGRaopR0IQMIfzdqqi8jwXtUonMMqnzskGOqUBtsna5ilLqSadoqw1I8Zf3rLVbrWj%2Bnp3J2Uws9eV2t0To9dXNFSyfjSsLQhOxlpXK%2F4cHypuWDENOPoojV9Dx8rYGi%2BirBv04zfhj4Slvcf6DgSUMtfocor3LMRot3nRLqOJNNfn33byZc8AlP5VVDSicPgrLVjqOVWdG4AtnINcbjpEcdBEjd4FVutuH0OVv39Ue1PMNbW%2FXXr92ookDFeZUHRh&X-Amz-Signature=2ede47f29415df91a5c4a9817164011565194816b8c891c216888bf188103127&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


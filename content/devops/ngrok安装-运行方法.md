---
title: Ngrok安装 | 运行方法
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-29T12:21:00.000Z'
draft: false
标签:
- Ngrok
categories:
- DevOps
---

> 💡 前几天帮人微调模型的时候，使用的LlamaFactory的WebUI，由于服务部署到他的内网环境内，做了内网穿透使得可以让多人访问。刚好想着了解一下，在此背景下，撰写了本文章。

## 内网穿透

### 原理

又称为NAT穿透。NAT穿透技术是让NAT背后的设备，先访问指定的外网服务器，由指定的外网服务器搭建桥梁，打通内、外网设备的访问通道，最终实现外网设备访问到内网设备。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDMDLIPW%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9n2begaxvmj13G4qasIMteKhvMo0Mb5AtdIeFRB2h4AIgcvpvmRQHCaQLiHUSddalSgddE%2BgAqGyORp1We7ZL6zQqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBssCQ1W61DM%2FOwlYSrcAxQ1JhDOAHPPvzqMZl%2FLoHL0s7ngDqwd7OxL9DvQSF%2BretPHUVyR5%2FRx6UWlrQ4AAGgHrlpsOCeZ8L6W8F%2F1H7Zi8oolIvqjBGv%2FYx%2BgoKa%2FrYS%2FSW%2BR0R9N3WPNk3zooh1VlfLkmeGGD1xfGSJBakObHmzgjSOfqmMfqjDOPqDJNZyJvk3uuFfPYH1Le%2BcxRsdnDvvDWfHN80132%2FB30Fp%2F9L4uIvQatRZ5BT3Vu%2B5nUYVQwFlKbXERe9aDH2T0mEddst6jKtil2321jPHvP7nzdDvFvAsZFCqNwZN04zkcSvPaj6sS24zWa2hZW5QfMOD8sZ8egMLt1QICqvYZLTnzhxgJTTNvc1PIy7Egn%2FYaxmMWBsOs%2BZf7YtkuxSu8%2BLAYsgR54tEFY3%2BBHuZ5bOZ47NtCDBJXdxtlYfFmeBzDcIvC2%2FQeI%2BhiW4XRA8DnaelMLQbjqhJDr%2Bb7zIEU59n56aTECqflCzP%2Fyu9TvFP1sFEffD4oyrNRoKa0lf7W9DCSyZswKiBxEfmPjSkMVAMpjECYQgWy1H56TayBSaantcOpEM%2FMjYdam9dJuE%2B21MTtUBBER9VUmKWnlW16YTlYkaIHYqNlPXd%2BhFRE4U9MZ4m%2BAV5kk9ANAIKtMMSirMgGOqUBvhTfW4wmWOHKgBXb%2FKc7PPpDTc7BxNv5OhG%2FmZ44Pa91V9xAfsLgWKj7NpZu0l0HdqtfpUaOq0Ob9Bnb%2F4fDawJnSBRkpLsgV5K9XYSLIdoNFYzUfeymB3Ez5Ugc4qK3US5zLCcfCrmOhQRjY%2Fw8IPVUUm2z9JuzPdJVQrQAPoPUSu%2Bn4sn88Xr%2BdCiZ%2BfQ4RPFBk3tphg68rsXe991uGhUIHE1m&X-Amz-Signature=b3f7cedc42a5233fef99d319a0b7eac242c73f11e7c6f864c41e6b049697ec14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


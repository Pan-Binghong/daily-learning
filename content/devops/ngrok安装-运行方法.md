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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WRY5BR2%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHj894yvaTjFh8V2xaeF0Eqm1YZmS%2FdvPnZqlAOw5KIAAiA%2Fhosb1el4eD2tTBYEjfcHGvweqMRw3BtSQj%2FT1dvQUSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMsAqW3aOt8A4jMUIWKtwDu%2FdN9hzmbi8ba8Xc%2B3wdPh2hUygpqBaPRDjJldwkaM3UwNq09Ux6w8cJwd7S50O4I1F6cmnhbQkZLuH0iy4LbaVmwIbf4TDzQx9NQVXWCaDfjpzZJxUlWTLvsJIvaA3MxJcxjYHs89%2B0D4UJhQy7V6V8FsO1SmxJn0ydk%2FF3P1doCPYbjyGFz6NQNmVNKYOC%2FPA%2FZao2Qwz7j21L3XA7El6Vj%2BNuAO0jNF8KroRC49v%2F%2FKCKYtgh3a4yjWkP9wKFj60bTduG6w%2F9hWI%2FBnUuUBrgfIMW4ChfrUM6obdjvqM9%2FiEVbKPqXz%2Frsu0sc3HMBW1QMxTIPVifuhpsQy4UK5A%2BQCZk%2Fd4mir3XC6qSNqPwsPdF1936aCtx0o9LX6z3%2Bsn7g4NO9CbB3vPGqz4XrWWUMOLpdy49yiWTo0aCHMM2kQizgEvJA7StFTnJ4hsVkQ0mn8Eb0G1VNePhQxja3kALceqRTOPBn6nTR0sfzsQzZGPJuhTtYCBlkRARjARqYF8K4VLCaZ%2FCsr2rEfh6%2FavGv4S250aSYTWCE7UToU0TbOLE3N3ZyMlIhJz10tYjfVKpStIqinvWoyL1t%2BjKGo5OysOjI7GYGr0WEujSmNxB2lQaVScdDwIPEzww9oWEzQY6pgEcaVKh5wD%2F3o6%2BeQdK%2Fn2IdWopZuFLXkja0%2FI2HRqwZt683NjH2dScTZFkV%2BpNtWUa%2F6ancB1SI%2FvUL5%2F%2B8FALPeEmWTN5avYbVjwBl1LSKI%2BQNVhdoUaO4g77MdbYwxnAPwnswbRSmBydPQf0NKDLERvQnWb8I76ltg09UgGapzyyYykkXfgz7m%2BhuuWLb4gygM2arxykpwHONflhdFoYvEOOAFaq&X-Amz-Signature=688c3fd8186eb202d718a0559737d1c57ce2ca1fd9c8ffc79c76aebe1c9c706a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


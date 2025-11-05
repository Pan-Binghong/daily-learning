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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5MBAT2S%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeBqogGhgLPOluZm0RSpDwhzfgJsMJdvjLkgE63cMsowIhAMOkoITK%2Ftnp%2F0wSQ79Y354awfEs5oUSriaTVqBuT6gUKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdxVMJFb9P9Z5Pt3cq3ANXi%2F6rtV7rhp7ne4FAuVoNMgmzBn2n%2FR4D0VA3%2BjuKbbcd1RlVfaGbn9WDcOYoyPhXyy8M%2BDM5oMe5AiudgGL3JlxJdKDBbaHosZ1ADzqP4TlTfhLOz5TCv7FfrA4A4r50DnHPOrbcSirh6hLC7PtgFxG7F5WAfpnH0gIz%2FJ8YekEZLKRgXxFFPmVBpTKENC%2BxwrKe7bo6LyZS39BvhAAXWdtcl4ICVl0xgknWI%2BzG03hvnIyDHKXCgA%2BArgpgT5rex%2Fbi0iwKEHaMhiOrD4831rFLWVjgyLHHoabyyc2UxsXxjYtbHpdRlSNWok%2F%2BMFKXHrP9jbAAGLeBZMpMWgylra%2FA0ZbFjCqb2UQs8WeT%2BIOnu%2FNVt4I122dBHjMFKOe6YwThcZY1X4jMNYoK9042srxOdmBAXuKCJbxsRnXf8Se4aWaRy79mqztnpNrEdECe%2FKDTOqdj%2BvoncgKg80A%2FIieL8YHjAvOY1kyIvp%2Ft%2FMl7i5SoW7JmMCQ%2FiatUu%2FBslW%2FhRZfTWmpBazSm4yIkEMHF831QvSxNRU3jD4HpIon5OIHfRRpZwJywypR8FXTr1hK3S0bdRl%2FynO%2FugcElLFt3BMVj8MpXJzgD3DKIz5LPNsNr2HfIgf9YnDC9oqzIBjqkAcz8GgsAgGradfPa0SVm%2FGoeYt0RAUgugh1b96UL3nj49G1zXSyvhrLPtQ5nnNM5Rk31x03h5KgFKTZfjupGMXPHJcnuum9Kndf3fJlJtgE5WR%2FVffswSbKp9z3KAVjag1jLC84bRhm82%2BSSiFPu2L%2BGtaY7KRThNQddB67yqdqTplN59lgjcvQGTlMaf94%2BQAZvbY2Eglkc8etef0WMU6vFSZCJ&X-Amz-Signature=603e16ab6e4bb986a60b8ac1bb7a05f33141ccec63ac64b16c459b6e07452edb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


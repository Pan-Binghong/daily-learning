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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGAPPBH%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4srOI0oAap6Kye3pGpQVZabd1EMjfpnNLkcDXi5YB0AiEA%2FwtZ%2FyLtX%2FbZgX1TYL%2F9z16oY4pdP0aYmJU3FKJ%2BTWcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKdTOxlTirIUjhpl9SrcA3zPT2d4XqpAAGi%2B6tyx%2Fn0JPFaP0DT%2F4c1E7lj8Gzs1R%2FsQxPFq7iSyZqp84BFY7FqNEiJPrioEZIDFT%2FVJ9BGb8%2FrO2%2B7qyftDJ8UC4Qh67vsfdXaEgGh5IL5sh%2BRO6A1oSMM%2FlEeUyaszgXB2%2BYDv%2F4z29D0hMSeskcGK2nj1VcPvqMS%2B0LDe35kb5ehKv%2FG442GK4ummMOTfgCnNBk0SbLr6C1xjkC3OH3BwpLWWLwXcoJaJSbv%2B7hzCy5z4KC3B%2B282Rx4j2nYurP0y5%2FXbi9CkZJmHrrRqd25RYMhmOWMd6PRrefbjQymH0F%2BBgkK%2FcCOZRTM0SaMSExZu2rGza9saJyErhu%2ByMHumc0NTQOHFtZ0wr3ZGcCPY%2Bv9LdsoT0w6W1Iawt9mRsQFft%2Bx0GV3LsMoZLzQ7MW7lW8GKydcuyW%2Fa0Yg55bvQNmaq7hxvIlV8ajApzewWj1QzO0MGq9V3cqxaqXDoALVlfrwmzunG9vMemouZyHzXJuvr7oTk0lEmMI3aQ8dmHhdeDdcLrCVEsPOGXVPlTnBWZIn5gDboLRdNv6RTXqtiz9O2gpr%2BKhqg9gDum6EfAQk1w1pG3Jidm1Jvhw9KCG0LQ6rBoFrw%2FFLZlcx1bAtEMOXXwMsGOqUBy36IQXvTyY%2Bv9zRFgKVDQosGSG6syFDSQscZWVx6RDqJbNFoEAlAFp3QrorTeDUWfEylK1x53F9SUloJUSfIuzVFbz2tSMaIQyflz%2Bl7N2ziw887ow3BOTDOd31LG5FKSEmuYM61YXe6xqDi8O2He0%2F3UETBl7RzwhdBjuyPG6Qkxa00mcrStfHabMtYxoQ2gDjn6qIz1xOSjTEZzXdjpXRl5bgU&X-Amz-Signature=274736d0420621560c439d9bf3a7f1ff156db9d5a2e41512b3dfa52c4ccfd665&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


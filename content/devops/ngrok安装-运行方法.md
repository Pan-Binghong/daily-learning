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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677RWQ4MS%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIBvNiaSQKhdr8%2B5JSviUxfLdIG95kToiur7dH417HPeYAiBP3uRLLhicRDD%2B5XJQ0LQDiLDcBNMTGsQ2VqD4rkUbeyqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHFklLqE4n8JlqkgnKtwDRLKVxi%2FZ7KC2lgu66F1s1Z5UxzdeybFirdeUN8ULZ9sNo%2BiX3gVPVgdg7AvTaTVZ5aHR%2BvB4BCl6mubq4BtGN0ZqU9f8bO%2FVDigmNE7%2B0z39yQyLNuaBKITXrn%2FlkSJgiuNNs0w%2BbzVL%2B6Yid2Iftgw73CBHChlByUZHgFCtkbsBYlpM7DPudfNbtPqYbQgbMBp5NaIy1Yw%2FzGe%2BULjkGozLuR1VTuIryCHRbuTFq6pMBs3c3BVRWYHgrFeXnGCa5TF9EAlQgReZ3AlkwTp3KmddYQtPAPv91hrmNeWvx9DSpey47u6AF976chGIjryx1vkKXMKAY6XtTOQZ60NelVqC4dNKeyvkuyPTHLVRImHsRqPArBeRvRbdJa2QXB9Cc%2FuHKlo9TUZQcQtcElySgCJOjqVnC%2FNImOd2RfFdZdyq4jKhmURGXuecLyxxCQDt0VfpoTxfZ5vPRigS%2FqFA2wO9xUVM6jBJxahL6tLbGg6kshcSeTQlOkrWRl3RCzYZpbHXitdNCrZrK7lOrjN4tcHyIpunlVpR1NngYyTDPI6hHRFM03%2BWMxjKKLcElXCk64j37fZXLAVXErrib5mXOwfBEfKItuYoyOhd6hT7a9vye101nL7Vb%2BKYHNIw%2FfOWzgY6pgFABKxcFzSCI6qznIMJ3t2JgKtNV8S%2BzV27wx5CdvEdn%2BS69gMxvMQW1OUqXMwOF2GI5LPInbk8W1LNrtbqaYh%2B7uuqeBoB82VuzG44Enu6pVgsa%2Fu6P%2BBMwYTtnzAq6gLYRPSGJiTspNulC9SYUi2UwvnCPv%2FQj4PsL8v2CBzsRVthhlJdpPTDhPIwTVvwJzo%2ByY5qfvJ4%2BU1budIbf1yfJARntePu&X-Amz-Signature=81ce6c4c418914159a370215b7644885be83d1a17b03d848b451d4f42c64bd65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


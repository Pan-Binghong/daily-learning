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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMJZ6B3P%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIBlR0YEHi4MAkX%2F8CC4IFH8dPPbmlpSUDoigu1dcknpyAiArgNdoWXgxg8xxDCyx%2F5ncnDIKHqc5n00wP9ti2E9ejiqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsWVUT4hLWdhZAZYSKtwDUiFLi6gy6IRUAHRBe0JuaTUPdZPvZvveacB7NMZuPAY6A8fMp1%2FgnQsz5p4N0Wl3kMHnsIUEUAoVNM6d%2Fd0a3B%2FfFCm%2BSn%2FnViWZucXfpMKSO7jKmKzs6gGWqnUa5vVVwBCKGJhLtQ0GIod0%2FDOQcu%2FbJzzGAJApNpyDloszwj7i%2BC5r1%2FqfUB2O1XWFPBa98TOOXNfNXDAiC7e3YFo4QbqXHscy4k%2Fh%2F5y0qKuW11YbxkvzfwX1g7lIKG5BeZ8%2B9SuOAOPHQfZ4mK%2Bwfv26XKs%2BGKiIDctSVasJVACfQ%2Fd%2BkMLlLxGVlLMcUPJNN9wTIHCs%2F5csB7RH1Ne9GkXyJOQb7xGg7uly3VXCplB58jy7DEOLnn5LDeVxzVET1pevwsdPmzBRr%2BVlV%2F0Q7rIt5ox54srBd5wpvTyb%2BQifCdj9vystPOnG7m2ekS3SIh92AgWjA7Jn4OogNpXC92VCUPFbSs6GWxPP%2FvFdCIDisna%2FibCz4c0jdiQr2lecGEW%2Bxv3Tb5Usgr1bLj3IAEldY8JURC0g4jDrlpxAkhaQrIcvwPgwueTKQlmdAp07yE94qXsvPD3%2Bjxyp1DwNVtqi8q%2BedL6DcAR5r6bG%2FjGp04suLoJe2Hmu968Y5TEwjPXRzgY6pgEsLRiIEGAQ%2FoDKVFWGtK0zPAuDokf11iv8r8zT64aN9hSzn5GIcO1dC5ZeOLXExV%2BnFn3ljOXdxzKfRs4fBlEa8Uzi%2FZL0QrMY61BCCX9jS4b%2BTIGT7U3SmTIj%2BJKBFJrZ80I7Z2Oj%2BD0w11cprM9Gx%2BxPEkc3tmL61%2FvJoVYrNIQ4yNrnkfv3NtHRb%2Bqeyl52w4QTk5YIsY4q9JkI03dN5klCJsMY&X-Amz-Signature=2efdb05b62e4bf4f52f55f0a35f20a72b98eba2e4512003e6fefb11f1209714c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


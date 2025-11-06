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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MTMVXNK%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvfNXECDPoLfeUN8mgIQmBuBHfSjyQQLQMfC8TFHKT5AiEA4WJgS8EhLswbY4mYFgxo%2BWMvXD6t%2FFUD5pJ5gOpWlLIqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJd5HB0%2F1K6e76gVGircA5DGtKE1sDLe9FJO%2B0Llo4q0jjOx1fea%2Fqe3XoqzjAdbrazRN2XH%2BjRNdlhdhStK9GL4snlNg2siJGNMkFVCfR7L8SBs5P8gw0arBo9yN%2B6t8oGthePLiUm9mKi7F0bRS%2Bewl3r4VT5LI40jHIHNu2U1oigEypfxiCp6VW5%2B5xm4zK933RkqehW%2BSI0ABXSv8%2FQ8T46SMV5zE6N6HqzhFXQm8Z1WjF4%2F4TtiXdwclRYpwE6QgtIHv4GQQaiptnmOM022Cysxuo1j5Y7zDnaom891%2BmL4y2iEBqkiiTXW22Q9Li9WSOfs38Fdp6VmbbfaznB47vAR7Lb1xygYh7ZNVU9kYPBqJzYTBytAm8lhvfsQLmZlBMR0%2FtyimISvOZjanemE%2FdZuZuZe7HZCjS16hoFTGbebJCUgeSxYqI8T4MWjOMwzbU8cb%2FDUuRkNHwQpuDkeYiZvtjRVjtS4EXoDB%2BGA3lAZ8ZV81RJG6WM0y4Xhg7Jh1eXBowFjqXFrU74%2BnBcTxt6NzCEXljuwt3LLFQD2yJ%2B6fV%2FDLkKlaua3rSjnbY7YvhJMStegS7Y3inHOaW%2B2mRBRLFK2dXHDreWLS9IwI6Ur%2BM2%2BHVu9fmmsyDFqPyMM0M1tseND%2B7q9MK2VsMgGOqUBlH9hCVA4NeiijT6lCW3EPdDEpKZC3MMf6NpKJEd4%2Bgqz78MGiC%2Be5g68Pp27NeNaUAdNl6m5SV5aIxui7q6uV%2Bsa%2FjjU049rUZhbIRwTYmGT77p78yqDgSHOVLiNfdd5jrmy8OM92cn6qW8thxrPMXgQSmEy9K83FVusBP%2FXMa%2FG5f6m8%2B0Rg4%2FWbjOuqV%2BZ3aghQdFaI9KCSS1hxvTeVxbl0cZ%2B&X-Amz-Signature=8bf257063629fcee05ea1817a41d82859d7799b8e8803fa1ad89e0066b6a7194&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


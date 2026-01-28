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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UZCXTU5%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSFU%2B%2BWXEOpVfzvfARmUjuk4OuuNKX8ctw%2FRYP8fzh3gIgGma9CvTMnbCtacBDlEwgBcadsL2B6uWX7rnsqtcqAcwq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDKtBOxQ8G70Aw3G6jSrcA2uuVSJ3kCmF62k36tqS%2FgVJXuzb4g9riXGVrgt02ZrQ78rG%2FEahvvzMHDDgI1l5I%2Bg2yP56AX%2BA2nlpkRZqNURJRRo0m23Tppvk%2BJ%2BhqwXaSjnl%2Fajegp0bPqiqyO7Ct7XTkpZIVe3pQe95rGwzeiMlJyCLGFgJ83PZRF3RG5FkSsovLjxc04FUcrJyGzSao5yPD32mQRGj%2FAE3k7T5ezmKK%2B3eAXV6Oit704UbKJOeMoDgujX2s23nzkQxTKwJyEWrC3kWthqP%2F1ctT4wMpUGeBRXxToJs4F1iUy2gR7Rp6Y47CipsdgJDdI0FGiPNA5nGSRqI8t9u3vLBUV8RONDcnOY8z4cQjunQlU4oNE43XJK9cBypHiuHDmAHRm8ZW0J4q6wZ5QmS7OPovUG3rt7vnkaMPrSVSnYP6DlczPPhMEleUTfbrMpD8Ar3i2WUgg7kmBwh%2FVH%2F7Q82iM8MtflCjj5t4t0d0LkvWu%2FAo7l4YjhbGKHh5OhQ0S2z5vvNwAm%2F8OXk5GiLjKzr7Zp0RnB29RDt%2B%2FIUJSehl3ZxX1el5%2BU%2B%2BxhgOA7EGvuJOWSZkhPGHpcstxg1T5ogBAkGFVyWm9Nep%2F6tNq%2Fqrxwow5v47dPjVbhRBW7vrGNaMJyW5csGOqUBKdBKOkqDMs2LbKmE86dX9sOJMa1mI%2FxwAwJXaIdRccxyWXNbhkezbglDh2%2BluZt%2FPewG6xyXBxuOf5JaQf5geX8TCVc9O3%2FUqom2hcNlZzt%2B2KW29rxyVr1yv1ttdPnglO1e3WhO4V9P2Yqt1%2FmJc8%2BlnAqe%2Bx3h53qX345Q9jrEO2uUVb6SORkpYVKINmRiMNZ%2FNCOYqPii%2FUPlooQJa%2BVqQ6Vy&X-Amz-Signature=997d8bdbc637e69d4f7889533b45c6a0a16f1f71bdbfc4ffcb744b1bd9337625&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


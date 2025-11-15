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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHE32STW%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNF9sOAmVe%2FRU02WuSc95SME0UyCZX2xn7FRr6szGBVAIgVm9rppP4TQMIIH%2FFUipbAt2mhHN%2Bu99UVscI6SbDjb4q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDI%2FsVFU83%2FXJA288nyrcA8kFQoMq%2B%2BLC4xnAf4sCNibo8QDrIC61uaQuu9spfiaNyKfDWVdvnAFQuLAN0GcWZcXzqDzSVG13961VB0VOLQ5g4PgzXVbGOEXj0YzYTdcAWCBx4pbAym%2Fn%2FVYhuKyVmPOYpsZsQQRA3TewrOlxEyhlUn6KPNq80hvf2MJziuH0IZDqenSlPyuylrc3xZMvor1TmO4c727sHTN7J0RUf7qQZkbv%2FPaYhGPl7CTOfgAwrZpvU3xTdgBGidN53BxEIQttLSsUkKtuCf%2Fs6Gew%2FA36OEhDQ10YJOoKZIPx4MD57kNjjWmelqrphBLxO74osJsK%2FTFPYAxsBV26LA8TddnUG2%2BeMmEwscvvVYK%2FZltg70wLxtNYEfCHJjueRBW6I%2BpRjGbRPIrJciWQjI%2F2HgLA23ZdsouteHMFtKOzz3bIwFYG0klK3umjQ2gLMVV%2Bgn%2FSKlHySVkLyR7HzZ1KwnxCcP9zujcvcwhhhxlLfZa%2BYnLLei09%2BzX19KbHw87NWpUhyO%2B74bx1MzGcM3vymCA2s3xh74W6G7GUNxQvKRM260j0rBQRe%2FkOOvLG9kASyV6Mxki4wZVDeIr1DIPzTge29HIykhb5btC20pSr6%2BDsRo292qPhNP4dkdE6MNrA38gGOqUBCLiOLsn%2FrXgTD6WgIgljeTPYIKAioW1dZdzDwWJzBDGCuJdXEYLoUQJohwHWmQOi7BL%2Bm82UxxlcD0Xa8Z6EFaV%2BhWeLk8tIQ20W6dekw3YWQlHD3uOJNSlUq3MwPXAb64bxw0cY%2B7fyuQ%2ByBiC6dzumC16uRVmQ0vS5bn7fHsOKnRRAbZbrgiumQ3RiqU3G%2BS1MHXiqZ766k7imLhhaC4KbSoae&X-Amz-Signature=50a6fe9d9e4d31035c8b046fa0d44d07c9a3f9c1d7b5f8fcffbe5fe0c8ab4208&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


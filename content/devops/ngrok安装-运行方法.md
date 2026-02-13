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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UBBUQBQ%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBM%2FrL0lIl3cWvTj4h5quuo1NNuBtY4%2BDgeaLm5nM6duAiEAite9RPTUrpK9axOtQ4fyFwnuxFSz2dOV6e1Ts0Cqvd4qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3%2FvGsh1Xcs%2BYqiGyrcA1lKnh%2BKn0GBmcLZ4PhJzmEmu91nGXzzzlD7STgh0WC5fT92MOiTk3t6nZAlDMhnp3rQB5WAkyza9A6LFBpJMNQAzJx1S135sc4RjB9rwD%2F8rIhqlLQyZzw2L0kJpHzeM1RTSDCo2MOX8dvCO%2BcK%2FgqkTHrm92ca%2BzASx3E52cGgaZ6nf4iGaj7AXvaSj2A89WV9uT%2B7a7fIIVsKBsgeSCpDPlQQgzESXw%2Fb9WsjM2fVvoHHj23VSFx2we%2FGR2tvzU953LFCjkOmArxgV4fLfp%2Bna%2F3clsRFs58TKQCuW0KweuR8BuziS0j2PpO1CcfKzRt1I5QBbbv78Y7q%2FaOAQf9bD%2FB4n7W2To9QDmwpkeRKGnbNnm6pq%2FZTEduXHOAhpGHpt31K0lXVtm9ZT%2BvFqBTUPIRajfg3eHIaLjZiSo6C1uH1aQqfBhAQllNAM6%2BsS59BplhEXPIVQ7z7kwjCGYmbNmdM7%2B%2FMsAewG8O0gsOanOyXgKDBhuJBsIaZa32hgPTZXObP%2BuvWSc1dighHpQ0aIdZ7lBCIOW4rC0x0SNyQNyhOXWSQEGld%2FosC4Yl5faft3T828vRT9vQWFV0v0pt2%2FSBkCKihSUVyYT2uQF5BI4dXXxp7kf2we5ekMJuTuswGOqUBd1E9SWFBRibNV9aOnz6ts2LvxKHr6%2F1GXVmmHs5AUJJq6%2BlEDkCoyo%2BnTr60epZF1xBbDrfrXOUyueq%2BQMr6Udofqu3%2BUSGApEQptUZR5Q9Qf96CrGmn2pgicI7yQKiA6Gh8kPCRMi%2Bh%2F%2BrNNE5SM4MfJUpVaB9GMbH1ksyimAWlJ0U7QTiuzrjaV4GV5ZyEzPqOEGL6HncKsL3kYDuM1%2FwnbWjj&X-Amz-Signature=6bf1feef245684612fabffb438f233c5063217b6590d6eccdc54e4606507adcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


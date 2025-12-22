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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOYXNAGZ%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQDWDxIzbHMmGwEQ8EMHDySyd45l0qJynRuReQlhUd0rpgIgTsYLoVLBbdOHYYH%2BK4a82zzlqhU3B6oJQ9ObjQAi7tsqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMEqpKYiVvGGAbzjByrcA6%2FllXVNkSP4TACZry%2FHsETIhzwhiMzpNKn1X3JbaLxVF27d1tHacnXEuz90GHcMzhHtoOYZyLAnPVuIbM3xCiHZN%2BUcdsRGqpzWysGbtjsmHPxsapArWAaGTPnJeXbGRvgelFfDJ0xSi8q54by0YNMvkC%2BpAjlz4jmlSkZDdAHUTioL%2F0xK3yqnzC7af%2B4kvWFQsewhv3l%2BaIxWOrHbfxca6OBBUActnRAfvMTmQtdVAiqMJwVHmLBSc52soJvFOruubdJU8GfX5B6VPR90%2FtIqCl0yWRsQLsaRIBn2e3yr5mGVUqg%2FR6Mv1N%2B3OQEP%2F6Fni7LckIRWLHgGYO6%2FA8zNKRGl%2Bzg3GxIaPg7St6rVI0FZJ0PFcM2ykL9tBI0FtX8aLyec4rJ3JG3hBvwg2iGXy%2B6%2FuGNWxeNGr09fCGtGYSFjZVCISyZ5BfMpOetu%2BSTc8N9HnslF%2FPSk8FAZEDS00Rn9MO2yD%2Fvu26K6kT%2BvmFUPwvtyGVSZUPc%2F1TszGrOqkqolz00i0Ma%2BPhP3iejgIajpYiR3DJyhD74aSfLhGoI8BbprXbnkjV8hjyI6UKZI8sKajchWWiiKWqODMAoG89fgAR%2FTkSD%2F0fDdNtf8PjRuJxnZ%2Byk65jsyMOHkosoGOqUBBViCBhsJvOOjAVUfoIZNmmNVQzfcAEXoaDqfMon0g0Fnu3KjDH58lIVHNONCR%2Bxef7tg5EO3sMtDsCqUCAKhjhq3ifUleQ9Cmg9ujtfhJak3lw7aQlcNhibcMkwgcu4oCrWlRGjss1v8O1%2BCJHPAMBLJg71%2FYKmzj6fp01AhbobFR6PuLRdOQxpyr3zmP6qVbj2HK0tNXyhxmBHF3jE7rwOVJ2LK&X-Amz-Signature=d41d5a61286c3612d231b570f2dea7cb57908c331ff5ddab07925ecd40b8e861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


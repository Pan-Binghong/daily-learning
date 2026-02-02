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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXW2YKWN%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDPo6vXlR32weUrMGbUcWGYyd2cxvVKZ58Pw6Zs6bNjJwIgdzpQlNWimD6tX1iZBXo9STb4hrVVi0mrwOkT4momNRwqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBbl1ZZWDvfrKEogircA44w9btNVo%2FzdnPrkZJ%2BtvLt9Il%2FhqJQGX20bnkHiiJI4%2BdQmHOKPcSXaZdUPmwe22gkhdR8ijD6q9Bz0uskLNp6dX%2FcMl7BLG4QS8nU86vGv3DsfQlmFOC1Qfj0H%2BRJbw1RqkYXDLTBRUh68nBMxkW4Cz7zrLsPbO91aSZvwqEa6MJlDIqKSVRbYCi4kforPyI75bk4LbAoOTfk5wHqFuA13Q4Pecv%2F%2BVeQ37jyKJ4EecssEwkYtKbzE5gejrvVYXXYUUR%2BOUNZCIxKMVR%2BNtK2euAmcooWc4NFEjP19%2Fo4DXZ3NtcEnph3nbzsVprRj4dquKh4Q84HDvCi45%2BR6IIU0HfJlxbdrS4x%2FBbvfx4uVwk9YxqIixRto3gzJC%2BKuC9BOK7tvsFWLLbN8zgiaPY845bQnbnYRo%2BJOdAr7xL7melW26elLaArsGRChX%2FEytteb8dIsSFUpCvai6ewY6w2YHixp90jIwF%2BabxVzVUtIuI6NTul3OzIY%2FeKGwormkytHulLCNdb4g4z9e7IvQnV%2BXFs4WdQbBy00hTQZuSoFsHEnD11Bmv%2BlJUS%2FbslT2XNU6EE4i4u9iLwl784Fn%2B352fLTNnNpddnvOXBNlAzgPzIslDvm1naDU07MPqGgMwGOqUBWmFZWX2en4jXA%2Fj6bYWrTXWKSPfzcBukANcr%2B8MA%2FTCVEfj9NYHwTwN57do47nCWN0ja4NckXPSLkS4AKEMIZWA5HUstAL3M8fMFsex6%2FnKvMpV9vhw6RcHrsQF8e1VAZF7vNFMkobMU%2B7DDK73sWhAI2QuFVaM1zn8bnZlF9StMUGimPVmMAjtjqzrT6VDAiVGJF8WwsPOpAzlAGawes0bVo4RB&X-Amz-Signature=9176fc0bae6d11796421bcfabc57ec5afd5a2af3562a26e79691eb1fac22f61d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


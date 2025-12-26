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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEI7CQCY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3dkXNEciTEvRgdo8SXUps4VB4SUPpy9Q1zBUtSxE8uwIgPjMpR9zm6reaKnyf%2ByyrbQK9GMbjcYLysLRAnsDU7wkq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDNUTUWUgp7G4eLfpeCrcA%2F%2BQtqQawoIyxDE6lz%2FmA318YIv%2FZIWP3GbhhB3o9MIwtqaiu2xM61WgqYdUsWkJMeprGQ6qO81T7FwtMdM4DfQqyg%2FUUrdBBFxrAa62oQzj6mHNw%2F7a96Z0ShvtOKuAzdNYZdkV27t3xirimPmYC0kmvkwnKh%2FP9XUNRARgx2JxNw7YKIlqCnMvtuyHAGRJzcjf7dUNxXC8Dzv2TqylRAyxxQAiyxjCLtGaPFZeiqTutk%2FRY75XCpxICJgH7N0lc8ZCJoGq8lIpFBp0J1%2FMNjmmDAdOFOKcPzyJSeJ7gwTWQWpZffX%2BGNDYx2kxBD52j9ja0E0RNEQTDpnkc4aIVISkhVsYg86NWatOsi%2Bw13S%2FrZ42%2BZS2L53pt1xVAZ4G3NEeu%2FxkNm9U4BmvcNMs9JHOOcV3se7L4RmdePGbrHmbDwjinoF1KcyRPBRunRpq2r%2B5jwoLBC4JPZ4e4Ad6DwUrizbFORCeF5GiVN9MVM%2BnumB9fZtt1MDwUUupGDdpz5nLFgyAkK48Ykh83VTB%2FIEcA7bImRpG6016bb34DJyDfNNCLiXR137Vn0RDtOd69h6yZRhnFsBVnDvMJdNNPC63k%2FGATd6khh7sj7Vp%2FMHSZj0%2BniAsvb%2B0daneMNLQt8oGOqUBZxWBZdlJb27J0prgGid8lrnQBOk6a7pmIW2fi29SKPfrHQzL05OO%2FvdO1oNs09%2B7X4m%2F1kpSEBzSajD2yD8Byv9OmNRKVg5YW4S%2BU4zTP2TwuYzHFUEfogcfm9Wegg2lJL7x%2By4rQjn76O3ROekAkKITLU3Bv3AOq7J0dpOKXqVH6B6jIGITMbGacMBXOThXyJ9qZstvU57PbxRyBzkrGFDXD%2FW%2B&X-Amz-Signature=acf9dd5fb29ba1f4d13a0accd68dd1e80ed4c2b7a23f93374ff43395b1662506&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c26f5ed-10b0-42bb-a8d5-ab7b8cebba88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLGGKPV4%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIC1KHw7EFUHCS7Sc7O%2FGWO7gBOKPrCie7D1xB5IoH9BUAiBIl02lRwqpQTzw3XsoWQdmYDX5u0d4fnYxltEqUDOA0yqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbWU18oyOSJFv13vgKtwD%2BJKHZys0hejSnZOEJObFQSp4qdVZxSjs%2BLaHLrEl0QS4pFOBQXLrq%2FNVJI92sYqYQdume%2FMhuFjC0J4Jq7DNFrpxyrSRkVgPPUSHS6J2%2FVuEqNn6jKOOdntR%2BmisTGTHS5YjS7OjY5YEoN6yDyImHeNoX2UqlzyQEyrR1t3eW37RQlcIs2Ubk7UaoRe1Nt8EfgITf0lamXZAWK1WE02uDDcHSyapY1V8dCF6HmVieFxIQrUocJPyBbB77XGuzrir%2FsczObnkvoa5nDAsJ2x8gqCUZT6k6H0mrp%2FONHApRFJN1Q5S7s3Xx4Frj2z4EywH444LbZgI4qeCjUrRRIN8nU4eLNYGaV5x%2B5fR6ZTLz%2F%2FjcOsft3Iga4u8rfg2aLuhlTijmkxjd9fDbIIJPEChQvhUPtTLZOrWWtasJd9rGHck6M41EEkFJAHf%2BsUXPXa%2F2nSdlN4T2x2ojmDWo%2FsTr%2BZgC5woR1eOeX2s8DkzNMmprRPn1Z%2F%2BSEtIqzZg6XZy22NNAeWjJfHRSgCy0yfQv70AzKWLgSR16FAWWW5EgP7bcrjGycWVm3VS08CuzKe3JIWcOLUGP%2B3vwwscYqPFPhLw2QYzERbWehmdxRmBnTpYDb8RHLmTeQCCqqAwvKXozQY6pgGihGVVXhLrFAMah2xQaJodeygIRVdiP%2BD10tUFB%2Fu2YGFL4zXVhO7%2F%2FDSCY%2FjKPtZyzCvnXVaJsNl53eekH96x5sASBwDy%2BoH8VGNA3YTIDOh6dUxKjjaPSyn7MKmvgbKalu%2BaRcc9ADupuuD0HlXe3EqAUf5cshbnXUBCP4mmkiaXmhsUed0nmB5F78C63ehwz5nayLq5vV1wXIdYyVO2N3loGoWh&X-Amz-Signature=e94e15c7562fbaafb94bf46cc99b3911468f8c42f424ae5a3d22cbbaa005b8d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


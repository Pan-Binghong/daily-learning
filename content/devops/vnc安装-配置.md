---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K3IDILP%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAg2LSIohVUMtof7dcNrXSa6JuBBpcVAFLPsVPeVmA2QIgXoH572liGIPrJKJRGq61Nh7Dj2ub9ejlXJU3y1QC%2BdMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpbKagoU9%2FHchY0RSrcA6P3Xx5jb64bsUY6ia9L6oxuD49zsjpqspl8VhwU9TJAtuixMrb883ojZuj0zlhT3zSBWytfn7dBkdkgy33pLjS5rG7tPQqzaqHQTSO9xZRDzsEr7NUZ7%2BNJ2d69DYHrrAHAlJPaThParTvtIE6gH49jfvd48bydUgLwslzOuW%2F82T0ZSfWQkbDQgtfQusGr8A4BJreBP7Y6GARWqGLtwSi6a1Tbjj8GJHlmrjOMuggZq4I7VD5EXr6vsjXuf0AVycEN2HG6YA8oYPSVlrmhnEMSz8pdz9lBmceoyZn2FzsoNBuA8h1aZrTHaXyY5szaL88IzVz85uSXfYz2b5%2F7ZsK%2FHDR%2Bbhcf%2FKrH0NJWT1DEWL8D5sVirBUjCvyRR9kYkWNSQYGei3Hg9p0al9H1d8%2Fez%2B2t%2Ffvnbeyu%2BQW7jZDIlCWw%2FISuBgtyh%2F7pwBmCl6%2BZzjfXffM4RyM6FDXrQn999O%2BIJEs8Ca9o%2FBCkRpND%2FgWO0GaUsSFjg4iO%2FMZ19PJAf6I9esKIPGp5gDxRgX6YY5BFH6VRkCb55FXuQv0%2BFBMqWQdRMm8cIk%2BF2aIaniNjv27%2BRBq1tqjtTXNmnhuiojLeHxuOYS0TTKXO%2BY%2Bjx69vXjs41D7GtWHhMK6D080GOqUBVi8DuRGqcrhU0WZ6z0OeUdUC0AdIdGIF2Z0MUGn%2BBb77XVIbILSJZ%2FIRTiF9%2F1BTqTeNG3Dl%2BSOsTuRX9MDHdpIvsHGf0bpr20aWbz9ZJIznBftEveSwXzXWGbb8ad%2BkIyFR%2B%2BachZRCpSBPTSXMv5W17UFdyOoFQ9HI572LDjFVyMcZ70KTte8tlp2QM5lnwC7WfCFhE390jQcM%2Bnu9lixLnLe0&X-Amz-Signature=275d852c5fe48bcf195b65c7a53523bc26e92b2d448e37ea452866fef8d6921c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K3IDILP%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAg2LSIohVUMtof7dcNrXSa6JuBBpcVAFLPsVPeVmA2QIgXoH572liGIPrJKJRGq61Nh7Dj2ub9ejlXJU3y1QC%2BdMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIpbKagoU9%2FHchY0RSrcA6P3Xx5jb64bsUY6ia9L6oxuD49zsjpqspl8VhwU9TJAtuixMrb883ojZuj0zlhT3zSBWytfn7dBkdkgy33pLjS5rG7tPQqzaqHQTSO9xZRDzsEr7NUZ7%2BNJ2d69DYHrrAHAlJPaThParTvtIE6gH49jfvd48bydUgLwslzOuW%2F82T0ZSfWQkbDQgtfQusGr8A4BJreBP7Y6GARWqGLtwSi6a1Tbjj8GJHlmrjOMuggZq4I7VD5EXr6vsjXuf0AVycEN2HG6YA8oYPSVlrmhnEMSz8pdz9lBmceoyZn2FzsoNBuA8h1aZrTHaXyY5szaL88IzVz85uSXfYz2b5%2F7ZsK%2FHDR%2Bbhcf%2FKrH0NJWT1DEWL8D5sVirBUjCvyRR9kYkWNSQYGei3Hg9p0al9H1d8%2Fez%2B2t%2Ffvnbeyu%2BQW7jZDIlCWw%2FISuBgtyh%2F7pwBmCl6%2BZzjfXffM4RyM6FDXrQn999O%2BIJEs8Ca9o%2FBCkRpND%2FgWO0GaUsSFjg4iO%2FMZ19PJAf6I9esKIPGp5gDxRgX6YY5BFH6VRkCb55FXuQv0%2BFBMqWQdRMm8cIk%2BF2aIaniNjv27%2BRBq1tqjtTXNmnhuiojLeHxuOYS0TTKXO%2BY%2Bjx69vXjs41D7GtWHhMK6D080GOqUBVi8DuRGqcrhU0WZ6z0OeUdUC0AdIdGIF2Z0MUGn%2BBb77XVIbILSJZ%2FIRTiF9%2F1BTqTeNG3Dl%2BSOsTuRX9MDHdpIvsHGf0bpr20aWbz9ZJIznBftEveSwXzXWGbb8ad%2BkIyFR%2B%2BachZRCpSBPTSXMv5W17UFdyOoFQ9HI572LDjFVyMcZ70KTte8tlp2QM5lnwC7WfCFhE390jQcM%2Bnu9lixLnLe0&X-Amz-Signature=031e4648759c37d10815d08163ee409cc2d73e65ddba21278b8751a0889cf24c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


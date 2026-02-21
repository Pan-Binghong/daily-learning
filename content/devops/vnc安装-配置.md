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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOKLSOL2%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVqmkqfS0Dz%2FtAZcGPL39nE8NfLoaYNm2NtbJO5sfwQIhAOk%2FVx0627UWSMA7UFN96NxfAonUmIq3VNl6eZbmhF4nKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIL5%2BdFlvYVCvhcIAq3ANpFNZbGMLFwpbXYogHPFFuwXMUsB2vvDkhX6tcspnHUWPkBGrglhhE5qBbr%2Bpwr%2FGtXNbj5s%2BipXY7OcmIum804xxqaNh3z6WwG%2BXRMp0iIPMELn1XBImbFKI1aQDpLwaHpUWwoQnmZYoi7s%2BPahNzd2WeD3Xxaw36JSTFrHBAsckueFaY3Q0Zc0LvzDGHzTRSIyMVjv1fbtcrzOe3xKO0jdq1soeaLtIzCUdVLJPJ2%2B%2Fs22OMLsrqu1e5XIBme3z8TYr3sDsCtCOSVvU%2Fn%2BwY48unexmXYxK3bdUkshbaqE6Y2lJ7UuDAcR5IHh0riu2JrbXPOXUIFzh1ZrUEbgN4Ny9rJNu3Iom4EJqZRldftZ%2B9uwl9E4RGw8mMGVjCFBc%2BUCu%2Fhj8Me3dyRF1wZTu4n%2BmeLF8hHxxDr4CGCsdq569aE32IxbZZlgbAJ6CuQdkg2NaQrPcRw27%2B4gIzmNH4NdHkZwZwQliGTOhjq1G3r%2Ffuy4Ew1xYijcoLT1FZ0tWh3Ko%2BdpvwjVRgOg5rksYBhRgz%2FTwoSRNdbzk0U0toHP3UAcgP%2F2ryVB08kC1rmNnYi47%2B50W4ei90mOtKuNVFglFggzpaCclBV84q9G4OIL9Z2TiFL8Bsn28sDjC2veTMBjqkAeWW1izig5uURIJRb14sN%2FbsunA3caElJIHtjm65wxsvyOsUCIs2GceTyswUn6ZQvf%2F9khauU9cZ%2B76lbDSWHTApzk4Qx48wQFHCUzbeUzA2Fign7qac%2F0IKRAei3QiltnWE8wZPeSJnpo8daCY1zICIjaXNpEV7yxiGEZY9PL6bBAABbSU23XlT74%2FVSwZGqgqJV3zOmDFjX6CM1s5jj8wOH4wq&X-Amz-Signature=272a54e98e484e835a129ed9cee4038775893415604cb43aea7125f31cd3abae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOKLSOL2%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVqmkqfS0Dz%2FtAZcGPL39nE8NfLoaYNm2NtbJO5sfwQIhAOk%2FVx0627UWSMA7UFN96NxfAonUmIq3VNl6eZbmhF4nKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIL5%2BdFlvYVCvhcIAq3ANpFNZbGMLFwpbXYogHPFFuwXMUsB2vvDkhX6tcspnHUWPkBGrglhhE5qBbr%2Bpwr%2FGtXNbj5s%2BipXY7OcmIum804xxqaNh3z6WwG%2BXRMp0iIPMELn1XBImbFKI1aQDpLwaHpUWwoQnmZYoi7s%2BPahNzd2WeD3Xxaw36JSTFrHBAsckueFaY3Q0Zc0LvzDGHzTRSIyMVjv1fbtcrzOe3xKO0jdq1soeaLtIzCUdVLJPJ2%2B%2Fs22OMLsrqu1e5XIBme3z8TYr3sDsCtCOSVvU%2Fn%2BwY48unexmXYxK3bdUkshbaqE6Y2lJ7UuDAcR5IHh0riu2JrbXPOXUIFzh1ZrUEbgN4Ny9rJNu3Iom4EJqZRldftZ%2B9uwl9E4RGw8mMGVjCFBc%2BUCu%2Fhj8Me3dyRF1wZTu4n%2BmeLF8hHxxDr4CGCsdq569aE32IxbZZlgbAJ6CuQdkg2NaQrPcRw27%2B4gIzmNH4NdHkZwZwQliGTOhjq1G3r%2Ffuy4Ew1xYijcoLT1FZ0tWh3Ko%2BdpvwjVRgOg5rksYBhRgz%2FTwoSRNdbzk0U0toHP3UAcgP%2F2ryVB08kC1rmNnYi47%2B50W4ei90mOtKuNVFglFggzpaCclBV84q9G4OIL9Z2TiFL8Bsn28sDjC2veTMBjqkAeWW1izig5uURIJRb14sN%2FbsunA3caElJIHtjm65wxsvyOsUCIs2GceTyswUn6ZQvf%2F9khauU9cZ%2B76lbDSWHTApzk4Qx48wQFHCUzbeUzA2Fign7qac%2F0IKRAei3QiltnWE8wZPeSJnpo8daCY1zICIjaXNpEV7yxiGEZY9PL6bBAABbSU23XlT74%2FVSwZGqgqJV3zOmDFjX6CM1s5jj8wOH4wq&X-Amz-Signature=06c7e8b9fa5281fe5643dce18fbb50bcd4fcb820c81918a988f567bd4066ba47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


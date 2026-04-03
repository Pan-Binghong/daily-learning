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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LAXDZYB%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsTu6LyoHw9wsikH5wMTvNtmYlcEy2qnB5IPiAumsaxAIhAIIBvfgJxH1xLlsWwqywWYoJTIBypxCgTTn8HTk74YKuKv8DCH0QABoMNjM3NDIzMTgzODA1IgysHM3uAuNEz69X9m8q3AOsNBgzj6tyNEkcSh2bGZeR4RxsR41Uy4bThIHOS4SdKhYIOJ5dDjG1cNZNlRvbSmnNyMSzmNyavSgDMZoI6L97j1WDTKRpkQhsTbeVaec63Z4aSUpT6krB7tLRtA40szdT2yZQKMCVG2J8%2FOWvneqZrJ%2BtwFehV0guuZ3M5nwuiLebtoHMtIV65OgXZb9YKYP5bJH%2FWGR2PaPVt0QvmNLXGEwhFMgHXRP6VNMmseSnx6Ulw1%2B5Ugb053NhChkkogzlUcINF5dGlECqhI8gSqWV2BB394NBDSjAsWRgylNrtSjP9BhpcDGy2LhMnNpLpmFUDHm1E1onfOXTeIp3JvJnp%2FT0Ma5lwiJdpFkao0YJifwE%2FBtW39jpK08tLAjahDjXYQPUxfa1963PwyL%2FZBGZ3U3JYgAhlzSU%2BUoeBIL3GLfJ6gK5j%2B3gIekBOnB0gS8MXfNmk8dKomuHGRrE2VISaOp1TjF%2FbZGdvct9uBluUBot%2BIzbM8GFDBiaVW83a9yuaGV29K4s1sXYU5tmm%2FyCdcUMBF%2F3pFNFMBsfGUXNM48k7kJzsg4ga%2B65bZLHnjHFRASKkgCbQkClJz1U6W9eDF5%2F4RgKI2Lkcbd7xooMw12%2B2WXIOXxpZGdqOjDE6LzOBjqkAfG6xT7L6zlbZDDDoaX8UpXRZN4uVK7WhJTb37fL8k%2FCFU%2BsLDro8csp1uBM94NjyZi7EFm4fwQc7t%2BUtCYeAigAu04nxtNrP6EiThDtSH3%2BfsS72QbmJFK4pp%2FuSK20EdAvHkwWlhETnyk0HAfh43YDDo8ahwQyvdYeEWpUQN4nnXqVq%2BWOCm6xADGqeAuUWxKNQeMWLn95Lt%2FlSsf0626j8nB%2F&X-Amz-Signature=d05275b7f20b3b8758adc2fb6ec05479f195a718dddf3ab9baca85f8fcb0d356&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LAXDZYB%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsTu6LyoHw9wsikH5wMTvNtmYlcEy2qnB5IPiAumsaxAIhAIIBvfgJxH1xLlsWwqywWYoJTIBypxCgTTn8HTk74YKuKv8DCH0QABoMNjM3NDIzMTgzODA1IgysHM3uAuNEz69X9m8q3AOsNBgzj6tyNEkcSh2bGZeR4RxsR41Uy4bThIHOS4SdKhYIOJ5dDjG1cNZNlRvbSmnNyMSzmNyavSgDMZoI6L97j1WDTKRpkQhsTbeVaec63Z4aSUpT6krB7tLRtA40szdT2yZQKMCVG2J8%2FOWvneqZrJ%2BtwFehV0guuZ3M5nwuiLebtoHMtIV65OgXZb9YKYP5bJH%2FWGR2PaPVt0QvmNLXGEwhFMgHXRP6VNMmseSnx6Ulw1%2B5Ugb053NhChkkogzlUcINF5dGlECqhI8gSqWV2BB394NBDSjAsWRgylNrtSjP9BhpcDGy2LhMnNpLpmFUDHm1E1onfOXTeIp3JvJnp%2FT0Ma5lwiJdpFkao0YJifwE%2FBtW39jpK08tLAjahDjXYQPUxfa1963PwyL%2FZBGZ3U3JYgAhlzSU%2BUoeBIL3GLfJ6gK5j%2B3gIekBOnB0gS8MXfNmk8dKomuHGRrE2VISaOp1TjF%2FbZGdvct9uBluUBot%2BIzbM8GFDBiaVW83a9yuaGV29K4s1sXYU5tmm%2FyCdcUMBF%2F3pFNFMBsfGUXNM48k7kJzsg4ga%2B65bZLHnjHFRASKkgCbQkClJz1U6W9eDF5%2F4RgKI2Lkcbd7xooMw12%2B2WXIOXxpZGdqOjDE6LzOBjqkAfG6xT7L6zlbZDDDoaX8UpXRZN4uVK7WhJTb37fL8k%2FCFU%2BsLDro8csp1uBM94NjyZi7EFm4fwQc7t%2BUtCYeAigAu04nxtNrP6EiThDtSH3%2BfsS72QbmJFK4pp%2FuSK20EdAvHkwWlhETnyk0HAfh43YDDo8ahwQyvdYeEWpUQN4nnXqVq%2BWOCm6xADGqeAuUWxKNQeMWLn95Lt%2FlSsf0626j8nB%2F&X-Amz-Signature=f9fa9add81e649ea534859ac80b28eefadfa5f686e89aaefa2665f2e9f7263d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


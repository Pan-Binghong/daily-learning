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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOOEWB5%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB2BsaaSlM5LbI6nQLWhgbbKnJ3naGFRvNrRSKUROyilAiBD7KneP1Bs9J0BIbPnqWCKqecrYH9n2Jq5xFIShP2I3CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK5mC6KngFeUAQ3HyKtwDXWSXUF2361UzOQEKSG%2BZq7kiiH00glslDpQSObT%2FXvVT2M1rgCLOmeMay%2F8qm1zJTsq4Vu8UyHaSqDH43IBUoPASMYiunfj8arKRPKCTeVIu87rdMcL4pjfnYgYGq9ebYUYZmJjfAPly0KOE2aCAGcSXxGLAI1ZdgeH2wyTY5mBVGYuXp889PQ%2BZZbefKZ5zZ3XZj9yhxgzzRecZd3clZJ9qvHKMaUajlsfCNDcOJYrd%2FGN%2FGIw9sRRedNYDJE4C4ubDs5GhRKiYCJ6vV78xTVBRl0e9tRsoSf2DXkiWlccDNMfFxSmoTwIIuUvxObY0KYJcFuFPu8Q37lV%2FqxX5RrivZUh7pevgnB2rnu9v6fkE4K69%2FjmWlae9M9cdc2SJVCz2EoV0ikjRqinz%2FgPCpc4VwHTEruYetXBW63twT7MSUBKMnSE7ubwojtEUr2FQlFhMvFcxJWLR27d%2B%2BHiFQW2JCXXG9OU2miAXqvf0%2FhdWTvWBtM28eANs4SfRueM681OKHFGgtokj56IvOllySiqj9fP4iHxQRdl%2FNyL5sz8%2FNzQWCw3JZ%2Fs%2BLU4izxyJVdDIpFnjzRQWSPkJ8Z9H1Is9XZLuQvQs61tE5kTvEy%2FGTRedM9rElfHyQKYwoMz1ywY6pgH5ABvF33ylttihnvo7B0FItr%2BKGn2W8sVdaX2nfizo5burcMHgWjmecCpAUNM4on1DXHL%2FnhLtm6Tl3IvcX58iUcEMwclM6Ift5ALFmOUpF9k5tjrkyUtfcHNZ4mmp1Rk0%2FiqJpHilzdNEDEiH8BPJG%2FuHU%2FgmOERY%2FyZBplfQvNv0THsmKB5Qm%2FEZ486cOTguFQQIvHcOvPYpcq13gTG8Z6j1gagD&X-Amz-Signature=0baecb11c0fbbc30a5650688f858f48166eba8e0fbc9bc1fb48723a35578c8a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCOOEWB5%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB2BsaaSlM5LbI6nQLWhgbbKnJ3naGFRvNrRSKUROyilAiBD7KneP1Bs9J0BIbPnqWCKqecrYH9n2Jq5xFIShP2I3CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK5mC6KngFeUAQ3HyKtwDXWSXUF2361UzOQEKSG%2BZq7kiiH00glslDpQSObT%2FXvVT2M1rgCLOmeMay%2F8qm1zJTsq4Vu8UyHaSqDH43IBUoPASMYiunfj8arKRPKCTeVIu87rdMcL4pjfnYgYGq9ebYUYZmJjfAPly0KOE2aCAGcSXxGLAI1ZdgeH2wyTY5mBVGYuXp889PQ%2BZZbefKZ5zZ3XZj9yhxgzzRecZd3clZJ9qvHKMaUajlsfCNDcOJYrd%2FGN%2FGIw9sRRedNYDJE4C4ubDs5GhRKiYCJ6vV78xTVBRl0e9tRsoSf2DXkiWlccDNMfFxSmoTwIIuUvxObY0KYJcFuFPu8Q37lV%2FqxX5RrivZUh7pevgnB2rnu9v6fkE4K69%2FjmWlae9M9cdc2SJVCz2EoV0ikjRqinz%2FgPCpc4VwHTEruYetXBW63twT7MSUBKMnSE7ubwojtEUr2FQlFhMvFcxJWLR27d%2B%2BHiFQW2JCXXG9OU2miAXqvf0%2FhdWTvWBtM28eANs4SfRueM681OKHFGgtokj56IvOllySiqj9fP4iHxQRdl%2FNyL5sz8%2FNzQWCw3JZ%2Fs%2BLU4izxyJVdDIpFnjzRQWSPkJ8Z9H1Is9XZLuQvQs61tE5kTvEy%2FGTRedM9rElfHyQKYwoMz1ywY6pgH5ABvF33ylttihnvo7B0FItr%2BKGn2W8sVdaX2nfizo5burcMHgWjmecCpAUNM4on1DXHL%2FnhLtm6Tl3IvcX58iUcEMwclM6Ift5ALFmOUpF9k5tjrkyUtfcHNZ4mmp1Rk0%2FiqJpHilzdNEDEiH8BPJG%2FuHU%2FgmOERY%2FyZBplfQvNv0THsmKB5Qm%2FEZ486cOTguFQQIvHcOvPYpcq13gTG8Z6j1gagD&X-Amz-Signature=ef6933a488cd48a02d6d9c4d974cc0053cceaa196fd0c2a5671ea73e7eb73cb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


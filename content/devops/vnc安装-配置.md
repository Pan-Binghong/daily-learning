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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QMMP4AA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF0bWSrEeDELQB46XqsIs6YYYBbbM%2BsVKaLvEZM%2BKxCyAiEAqv7GtnIB0BP5Bxv5Hxj4deNecimrJWJN2bxwsAoNDugqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM4Oi%2BjbTNXN91oVNyrcA%2F7N%2BoT2HKEBOK0NCQFqpCfQDhZ%2Fm41PXpps5w3ymuxfbQ47Ahn4b2%2FvLlbe0fpJO4vIwGLV5WzrWmEZSdTANYNoMCRqcrRKdjtUfrjTUcSBGrYzrqWL4oZO3Su26%2BfYaLEgJGu%2BcvLdH2AH7CNu7l%2BmMEt7Rzpo6glZsa754%2BxRral6ovVLaOjazL7u5hGOhjYpSLSuyTVP6%2BMtwTJrFZGG0O3vG1BdEVOr%2FMRVtetxCPw4XYHo0z2Cmyh%2BGvpExcxu9p5oMxFTzokyiUrTc7TYZ6bygy0YCU%2FEv8KSWo4g2vxf9NNCEiygTE4nOLTSQ2%2FRz5EiWZyVBxmE1K1UApSiOPZPFlUGBIbefMZkd4%2FjO30FpRH5S9rsO9vRKTU%2FnSqin5w1Yjx4r%2FHek9Ox3XCbFHqeCvx3umXMEfu%2Fbf4lQmNESGVULvrukeEbhhVhYKA2iSHr3s6d82%2BAVREKrvQGJWdOx3En9wRbxMcyhLFaLcyS9MF4FCmudElDp%2FUhdBbkZXrpsAFePSZYs1YKsrQYePXVU%2BE73g8OIDFvNjJ0zNzciv3ahxnez0WDnNEKv5AA%2F8Xtz9C2q0t4tsnxHQzl056orJLrDxFLUfMP1olsqFhGw1245qsad0qRMIryr8gGOqUByKe5lDrEIWuUrr86wKK5JfwtatSf6YMBScnDys5VjVdICGH4fd6mavljJytiDMUr1BKyn3ua6w4EKyWzlnTl9MdcINTSYHgvM7IYLVkpll45zGTT3eU9eofhfeuQT3Sx43SGjinZ8J%2BJrwhxNO5%2Bh2vtuttm6er1U2GlaaFsHJ74sMEkvYO%2F7lGf74TVy1EXpFJslUkzbd89bzCrsop%2Bgp469ftk&X-Amz-Signature=3da8b0e73d5f94f7c2eec18eeef67facb1eca69e6b9aaf37f9aca5141cc85739&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QMMP4AA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF0bWSrEeDELQB46XqsIs6YYYBbbM%2BsVKaLvEZM%2BKxCyAiEAqv7GtnIB0BP5Bxv5Hxj4deNecimrJWJN2bxwsAoNDugqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM4Oi%2BjbTNXN91oVNyrcA%2F7N%2BoT2HKEBOK0NCQFqpCfQDhZ%2Fm41PXpps5w3ymuxfbQ47Ahn4b2%2FvLlbe0fpJO4vIwGLV5WzrWmEZSdTANYNoMCRqcrRKdjtUfrjTUcSBGrYzrqWL4oZO3Su26%2BfYaLEgJGu%2BcvLdH2AH7CNu7l%2BmMEt7Rzpo6glZsa754%2BxRral6ovVLaOjazL7u5hGOhjYpSLSuyTVP6%2BMtwTJrFZGG0O3vG1BdEVOr%2FMRVtetxCPw4XYHo0z2Cmyh%2BGvpExcxu9p5oMxFTzokyiUrTc7TYZ6bygy0YCU%2FEv8KSWo4g2vxf9NNCEiygTE4nOLTSQ2%2FRz5EiWZyVBxmE1K1UApSiOPZPFlUGBIbefMZkd4%2FjO30FpRH5S9rsO9vRKTU%2FnSqin5w1Yjx4r%2FHek9Ox3XCbFHqeCvx3umXMEfu%2Fbf4lQmNESGVULvrukeEbhhVhYKA2iSHr3s6d82%2BAVREKrvQGJWdOx3En9wRbxMcyhLFaLcyS9MF4FCmudElDp%2FUhdBbkZXrpsAFePSZYs1YKsrQYePXVU%2BE73g8OIDFvNjJ0zNzciv3ahxnez0WDnNEKv5AA%2F8Xtz9C2q0t4tsnxHQzl056orJLrDxFLUfMP1olsqFhGw1245qsad0qRMIryr8gGOqUByKe5lDrEIWuUrr86wKK5JfwtatSf6YMBScnDys5VjVdICGH4fd6mavljJytiDMUr1BKyn3ua6w4EKyWzlnTl9MdcINTSYHgvM7IYLVkpll45zGTT3eU9eofhfeuQT3Sx43SGjinZ8J%2BJrwhxNO5%2Bh2vtuttm6er1U2GlaaFsHJ74sMEkvYO%2F7lGf74TVy1EXpFJslUkzbd89bzCrsop%2Bgp469ftk&X-Amz-Signature=615ffabca6eedd59578d5f9f9a7ed26748a06e861d227c0bcfb2a0bbaf6b0956&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


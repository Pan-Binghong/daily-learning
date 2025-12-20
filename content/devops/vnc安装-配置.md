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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPARQFQM%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyae8%2B8GmdkBaDPhVH0s%2Bv2scBCC4c%2FZJt831M%2FzT4fAIgHMlgZVWOlzcYWGLcGfC6u4YwUkArTH5pPeJCOKqKMNkqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM79TL501m0IJodiBSrcA%2FUG4v36KDaAYENVbpoJATdmMtGbjs806gi7ny7yH%2BAkNBX1s7zIpOClhCM3g1oQo4%2Fvm%2FprJIvObpd%2B19agy558MgzwJT%2BipE29smFWjdEJHtuIKdG1WgMFekbfYwLhE%2FpqM9hgAq3%2FBWOgSufzSWFBL6On1IjpAQDwUbQr76zF99BlWJHblCszC9pIhWO2iNARPziTsWmRUcpZuh%2BiD2%2FQ5Fk09O1dh8w1Hhi0fEt1HA2ogdGscrVLL5y9mPmTYOTAkFr412W4dSL4T0sBmRbX6n7Kt7VAl4T1Q7yeD6YVpGFuLjfIGsQLHAAMlBNQgm1jw5eXh2RFZ%2F%2FVX0u%2F4GQ5RDNn4WDiIVgGg4xZ1w54aJhzVzsBhdFWUjKUKHY082HnXE%2FzT4884rEqpF3jrdPhaLj4VAsNfHtW9KMsNzLg95FXeSOiSpGAF7Vsv56r2PzkmSIKsLZZo6NZmC8aVllYG7j0lAPwsrgQ4PbieMbyHCGV8EyKmj%2F6G5R%2Feaez0DMyP5QuBnfQE4Zcez3UgboP%2BUEYcnh8GxU%2BgyixF%2BFOOdFpwtyCBkhkcLlXOOCK7N6He%2BnAFsJbVBlxB%2FwD8fGKeSTQzPR%2BS637LPBGaqR3Kq47yLtxUjlSLCmOMKmFmMoGOqUBjzt7kiCwwHg2x9RW3TSSebxp%2FUneRZuWszr74uj%2BfpxYgQnevZ1cPcnswLKIPmYTdllgNe7aJlfkhbUeZgZf%2FmRlZ9mdsfyYWkfU3nOq6Bk47%2BmHt9t9gh%2BqHbXNqSjZWJuwldGLdszeWJJUWJbxc2TPFz8tcYyex6s5ZEgubzjuDDHEDNWkUuTnjpb6ZivBU5Aanejx3UfKM7btWIM6n7PZTXOY&X-Amz-Signature=ef0979eff2923166f4130eb948d6972e03f77bb34fb53b4cc0b4b635fb094787&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPARQFQM%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyae8%2B8GmdkBaDPhVH0s%2Bv2scBCC4c%2FZJt831M%2FzT4fAIgHMlgZVWOlzcYWGLcGfC6u4YwUkArTH5pPeJCOKqKMNkqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM79TL501m0IJodiBSrcA%2FUG4v36KDaAYENVbpoJATdmMtGbjs806gi7ny7yH%2BAkNBX1s7zIpOClhCM3g1oQo4%2Fvm%2FprJIvObpd%2B19agy558MgzwJT%2BipE29smFWjdEJHtuIKdG1WgMFekbfYwLhE%2FpqM9hgAq3%2FBWOgSufzSWFBL6On1IjpAQDwUbQr76zF99BlWJHblCszC9pIhWO2iNARPziTsWmRUcpZuh%2BiD2%2FQ5Fk09O1dh8w1Hhi0fEt1HA2ogdGscrVLL5y9mPmTYOTAkFr412W4dSL4T0sBmRbX6n7Kt7VAl4T1Q7yeD6YVpGFuLjfIGsQLHAAMlBNQgm1jw5eXh2RFZ%2F%2FVX0u%2F4GQ5RDNn4WDiIVgGg4xZ1w54aJhzVzsBhdFWUjKUKHY082HnXE%2FzT4884rEqpF3jrdPhaLj4VAsNfHtW9KMsNzLg95FXeSOiSpGAF7Vsv56r2PzkmSIKsLZZo6NZmC8aVllYG7j0lAPwsrgQ4PbieMbyHCGV8EyKmj%2F6G5R%2Feaez0DMyP5QuBnfQE4Zcez3UgboP%2BUEYcnh8GxU%2BgyixF%2BFOOdFpwtyCBkhkcLlXOOCK7N6He%2BnAFsJbVBlxB%2FwD8fGKeSTQzPR%2BS637LPBGaqR3Kq47yLtxUjlSLCmOMKmFmMoGOqUBjzt7kiCwwHg2x9RW3TSSebxp%2FUneRZuWszr74uj%2BfpxYgQnevZ1cPcnswLKIPmYTdllgNe7aJlfkhbUeZgZf%2FmRlZ9mdsfyYWkfU3nOq6Bk47%2BmHt9t9gh%2BqHbXNqSjZWJuwldGLdszeWJJUWJbxc2TPFz8tcYyex6s5ZEgubzjuDDHEDNWkUuTnjpb6ZivBU5Aanejx3UfKM7btWIM6n7PZTXOY&X-Amz-Signature=daf3c6b6945b64467f5830a6a889b0140d82242740a6a026696863b1f950a997&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


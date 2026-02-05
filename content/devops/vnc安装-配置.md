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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BMWUZF5%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQDpl5sTHLuKDMZk4PXn0W25iEYieOcm6yvUJwdw%2F7QHUwIgRJrP7LN11AkqVFurSW37qlSwzpbq%2B3Ztqo10ZUdjjigq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDFz3O3oXNBAwxSZ6CSrcA8wZmXVwjMREyJ6twgYWyQrIkXUaGLF%2Ft1%2B20cyLlEEkmX5YZ7t45UltRGGkHqeDmTcFiMPW70C%2FMOJUEqbrQmuwZachmPqgb6IEzh9Eq20%2Fg5qdOf3Zkif55JI%2Bk1YSw1GE%2FtEfeoZUtfhETHrXoZ6DFYsM23OJmC5HrRW4zPxzS4UK6wcQ4IMkNLt0icN13nP0QSiBiP4u%2FFOmHGPA6gM83uDb%2B1oXxdAd53cIjXOEr1AGPIm%2BLrNVet8RPz6XK%2BID6TiSLkuSqlXJeWsarvomrYiO5e3r%2FCI79Zk%2BKmj3gMrqdxg2KxNHf%2B%2Fn7iFyBAH662KAXIgsWebNJdl3APToiMXaSOgFQNbR4WGDvfm89alCSPfzKRe9fo9%2F%2FoIu8N8A6HnDWA%2BOhkO5hHJkxPQ84d8Mnm5qMEnhpzYm7SG1XwDN%2BkfMQXTJvDn8uega6%2FXGz4CGZ9InDg27bgHJ4VYpJbZiionBL2jABZI92tjDs%2BI3zrmTd4b%2FDNTHKqIu80X9lnAbcFrmaSY4E1L8sxYdWVUF45aRFm%2B2l27cpmC0PxCy3Ic%2Fr4ovDfgSDSz2gCqR71KtpaG6v39RXirqwE%2FRg6t4Zdgs4VK%2F%2BeEz2l8a33RmU88JN9bYrtGMMKSTkMwGOqUB1IiCFdP5TjL%2FmO%2BuvY3Iuzs6BSXT5%2B7Sp0vd8M3HsE58UFdjcwUcS5QYKhOC5%2BjAOTZpCKw3fgoRLUefTJzyfdV1sVYX9l2gNavgXmNu%2BzpGqqv0kwgab6STqj6Nji%2FjHpQdkCaMjN4wu1YR3qam9Iks5BMhwk2ZV9fFIuiCSrGitAuP7hkFjl%2BjRXFGf1SohnvSqoCbw5m3PUc3V2F%2BNKUIyD5y&X-Amz-Signature=e6932c4d98a8f39d2aa8408e29aef6ddfba2c335f514020d48a9b63d46d53f2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BMWUZF5%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQDpl5sTHLuKDMZk4PXn0W25iEYieOcm6yvUJwdw%2F7QHUwIgRJrP7LN11AkqVFurSW37qlSwzpbq%2B3Ztqo10ZUdjjigq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDFz3O3oXNBAwxSZ6CSrcA8wZmXVwjMREyJ6twgYWyQrIkXUaGLF%2Ft1%2B20cyLlEEkmX5YZ7t45UltRGGkHqeDmTcFiMPW70C%2FMOJUEqbrQmuwZachmPqgb6IEzh9Eq20%2Fg5qdOf3Zkif55JI%2Bk1YSw1GE%2FtEfeoZUtfhETHrXoZ6DFYsM23OJmC5HrRW4zPxzS4UK6wcQ4IMkNLt0icN13nP0QSiBiP4u%2FFOmHGPA6gM83uDb%2B1oXxdAd53cIjXOEr1AGPIm%2BLrNVet8RPz6XK%2BID6TiSLkuSqlXJeWsarvomrYiO5e3r%2FCI79Zk%2BKmj3gMrqdxg2KxNHf%2B%2Fn7iFyBAH662KAXIgsWebNJdl3APToiMXaSOgFQNbR4WGDvfm89alCSPfzKRe9fo9%2F%2FoIu8N8A6HnDWA%2BOhkO5hHJkxPQ84d8Mnm5qMEnhpzYm7SG1XwDN%2BkfMQXTJvDn8uega6%2FXGz4CGZ9InDg27bgHJ4VYpJbZiionBL2jABZI92tjDs%2BI3zrmTd4b%2FDNTHKqIu80X9lnAbcFrmaSY4E1L8sxYdWVUF45aRFm%2B2l27cpmC0PxCy3Ic%2Fr4ovDfgSDSz2gCqR71KtpaG6v39RXirqwE%2FRg6t4Zdgs4VK%2F%2BeEz2l8a33RmU88JN9bYrtGMMKSTkMwGOqUB1IiCFdP5TjL%2FmO%2BuvY3Iuzs6BSXT5%2B7Sp0vd8M3HsE58UFdjcwUcS5QYKhOC5%2BjAOTZpCKw3fgoRLUefTJzyfdV1sVYX9l2gNavgXmNu%2BzpGqqv0kwgab6STqj6Nji%2FjHpQdkCaMjN4wu1YR3qam9Iks5BMhwk2ZV9fFIuiCSrGitAuP7hkFjl%2BjRXFGf1SohnvSqoCbw5m3PUc3V2F%2BNKUIyD5y&X-Amz-Signature=f27f89fabab614425460024cb9dcf328b19bc2cc8d8e8e6fdd72e0a954c59cfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


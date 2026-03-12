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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIPAPUX%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnLOr7UgXipIvTM99pF8at0KbdfwUYtV4sYgNqg%2BwaDAIgJ9HGqfhfPZw%2FIaVAA54xoGH0Tj5FPSSXaJxt%2FetUrS4q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDNyuE8nmGMEDUCTAyircA2JgnkTx3EYkxUK%2BhlIVT9dKXm0gUo9UYW%2Bjz%2B%2FWG47xl6J2r2FdyJmLkku66Ly3x1iZl5USJS64dhFtPFormGdjTYW8z81z%2B8fhdI1eUgoB%2FsFr8CBY02BoMrkinAvU6LXNeQqwrqOtukemSAOatMvW2CLr8JV9pKsxAe6FZJschkFL6BoCA%2FhrLlOX2Ggxv8ah%2Beauclsm06LWfFroGxiTcj77FGO7zaEn7XFE4S6ZKD2ZZzUW1XHzgb7hfqeGjTbSll85rP5ufLACvF5E0mI8Ucphg9jrlak6HQeX4zZeYSBax%2BWXFXLooDSAs%2FdIV5W%2FG%2BGZIzHUAY71iSRj94YtIbMcqzIqYd6r8kwsAeXbEyk9A8NfFKXit9jMj0EiJzl2EWMVlrjWES2xjXONwaQ50ccRFvqdzNJ1%2BCnVuQT70OYj6CCUfXkXVj1WiLVu53jE5s%2Fsl1diBKEd%2By7%2F42kB9yNL8TX2KHsysBRmB61dGp4rVPr7ILftRVK9HPhRVHouMZJBEFNdeFSTc2a86o9IFsvGb7OCUZAZWw3bs0AX21P%2BBzfXEzQ%2FSFuUbprcevIZ6M2Tf1H%2BEILYgaBHKw5Vzq%2Fi%2B4g9dyijYhQ4LxmsEAGKQ8qkqdiKg69HMN%2ByyM0GOqUBbDGklF5lmXxguVs2c0U%2B05uk9UkLwsJunBCY2N%2Fn2g4MvIURcqy9YGacrJoIgqc%2BaDA6RMb7nfb8bQQlAXBzfNI3WTsXlelyxD0jdwJzbS49NXSt3YKn04wAKbUlohIIoSggBxn6KLjDtTIQmEuxsBs2Eck8oNATmovyJAdHsGcKgllQaDnzoSfQePqWAETCs5xKcznVXWXhpvDFnGlzL9dxEHld&X-Amz-Signature=b1c60dcebb3bd2c973d80606db89261e597a095a7df177b13dcb188cd3937fc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIPAPUX%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnLOr7UgXipIvTM99pF8at0KbdfwUYtV4sYgNqg%2BwaDAIgJ9HGqfhfPZw%2FIaVAA54xoGH0Tj5FPSSXaJxt%2FetUrS4q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDNyuE8nmGMEDUCTAyircA2JgnkTx3EYkxUK%2BhlIVT9dKXm0gUo9UYW%2Bjz%2B%2FWG47xl6J2r2FdyJmLkku66Ly3x1iZl5USJS64dhFtPFormGdjTYW8z81z%2B8fhdI1eUgoB%2FsFr8CBY02BoMrkinAvU6LXNeQqwrqOtukemSAOatMvW2CLr8JV9pKsxAe6FZJschkFL6BoCA%2FhrLlOX2Ggxv8ah%2Beauclsm06LWfFroGxiTcj77FGO7zaEn7XFE4S6ZKD2ZZzUW1XHzgb7hfqeGjTbSll85rP5ufLACvF5E0mI8Ucphg9jrlak6HQeX4zZeYSBax%2BWXFXLooDSAs%2FdIV5W%2FG%2BGZIzHUAY71iSRj94YtIbMcqzIqYd6r8kwsAeXbEyk9A8NfFKXit9jMj0EiJzl2EWMVlrjWES2xjXONwaQ50ccRFvqdzNJ1%2BCnVuQT70OYj6CCUfXkXVj1WiLVu53jE5s%2Fsl1diBKEd%2By7%2F42kB9yNL8TX2KHsysBRmB61dGp4rVPr7ILftRVK9HPhRVHouMZJBEFNdeFSTc2a86o9IFsvGb7OCUZAZWw3bs0AX21P%2BBzfXEzQ%2FSFuUbprcevIZ6M2Tf1H%2BEILYgaBHKw5Vzq%2Fi%2B4g9dyijYhQ4LxmsEAGKQ8qkqdiKg69HMN%2ByyM0GOqUBbDGklF5lmXxguVs2c0U%2B05uk9UkLwsJunBCY2N%2Fn2g4MvIURcqy9YGacrJoIgqc%2BaDA6RMb7nfb8bQQlAXBzfNI3WTsXlelyxD0jdwJzbS49NXSt3YKn04wAKbUlohIIoSggBxn6KLjDtTIQmEuxsBs2Eck8oNATmovyJAdHsGcKgllQaDnzoSfQePqWAETCs5xKcznVXWXhpvDFnGlzL9dxEHld&X-Amz-Signature=48d21c468dc65d5229b750805fc5f4953d46d43078428f6e409136fa055ac19e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUZG3KES%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCCT3neT5xhiUgxXav7qIx%2FUfAO%2BFsmRMgoRCjucykjCQIgRixjil3mI5PDXQWkP97%2B%2B2IY1rpFgKmgt8L6D75iirAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCfmXAr%2FVZgClysfwyrcA8Y2S6kVuT2ZemSAhtCRgYKkzaMKg%2Fo1jVqFJcMH9p6ZZjAJALh52BKg3fwwFpx36Be15XY3AO8BWsJlajJR5Q%2FYGjk8etQTs%2BAhn8HNtmHTQmcr5CH6WfnX%2BSDj3iyOuzP2QIjl14%2BJuJLdXsqkVkwIewwhM%2F9rBmPYXuDzoT%2FaJERdF4Ba%2Fxw8nL7GrqovKoF2chiFp5XPd2ko2JTkiBCw9aqu86iWmQyNXPf8bHZkn99hVaVMsyrsnV6cpj56X5d3meB9You7EDzZgdVpBZPeM9ZvHb7o5o5XZCTdZFOuN9bCnS38faoZPOgwU%2BtqKUCEluqTqsyFP2ieqTmt9p7cdfobxNdNoKCGjfgJ68DCeeC9kw5HChsG1hiGugqiuDZGp%2Ft8Qu6V2RBSHxnJPRle25OHEn8xWPMbPBWFNHVbALqCHbmEHzT0Lz9xeroZGZ%2FG07TIIpRhSNVOZ%2Flu0y6ZCMr%2FMoyguE%2F4CJrquSiKyLTbU5SvJKjRInccGS0mjhH%2FlzGT%2FxLK1FfNqynXbQ4faOcwTTc9T0WmQcFXmDgy7M0xlXRJN6v5c677btGc04IgvjoaA5YrM2BxFr1QwC4lk%2F5WdaInKbga5A7STGO7PCT0cEUmtj%2BVjAddMJa7xMgGOqUBNGujrc8D7e2wiAvTZf82VS9uhLAJRWSsdfxHfgogUp%2FXY2Ba0x%2FV71YO9b3E0rAK61Rj213vAtCLP1B6dCK57Sv%2BBnllHafgEOiambuz%2FnEM8eyhNquPCwLkXoHMRZfvL7dQpX5Tj7FmGeRqQiyyIFkJg8DgnvmZ%2FjPMl2krZX5dwY9kuy81AThU1C4yYwsD3dNgOTaKDxo4XPVJ2%2Fgl1Zl5iaCK&X-Amz-Signature=a9f3f6bd5d86b4cdc3d970845185d1e2784fbbfda803b0020c9441edb7722dfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUZG3KES%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCCT3neT5xhiUgxXav7qIx%2FUfAO%2BFsmRMgoRCjucykjCQIgRixjil3mI5PDXQWkP97%2B%2B2IY1rpFgKmgt8L6D75iirAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCfmXAr%2FVZgClysfwyrcA8Y2S6kVuT2ZemSAhtCRgYKkzaMKg%2Fo1jVqFJcMH9p6ZZjAJALh52BKg3fwwFpx36Be15XY3AO8BWsJlajJR5Q%2FYGjk8etQTs%2BAhn8HNtmHTQmcr5CH6WfnX%2BSDj3iyOuzP2QIjl14%2BJuJLdXsqkVkwIewwhM%2F9rBmPYXuDzoT%2FaJERdF4Ba%2Fxw8nL7GrqovKoF2chiFp5XPd2ko2JTkiBCw9aqu86iWmQyNXPf8bHZkn99hVaVMsyrsnV6cpj56X5d3meB9You7EDzZgdVpBZPeM9ZvHb7o5o5XZCTdZFOuN9bCnS38faoZPOgwU%2BtqKUCEluqTqsyFP2ieqTmt9p7cdfobxNdNoKCGjfgJ68DCeeC9kw5HChsG1hiGugqiuDZGp%2Ft8Qu6V2RBSHxnJPRle25OHEn8xWPMbPBWFNHVbALqCHbmEHzT0Lz9xeroZGZ%2FG07TIIpRhSNVOZ%2Flu0y6ZCMr%2FMoyguE%2F4CJrquSiKyLTbU5SvJKjRInccGS0mjhH%2FlzGT%2FxLK1FfNqynXbQ4faOcwTTc9T0WmQcFXmDgy7M0xlXRJN6v5c677btGc04IgvjoaA5YrM2BxFr1QwC4lk%2F5WdaInKbga5A7STGO7PCT0cEUmtj%2BVjAddMJa7xMgGOqUBNGujrc8D7e2wiAvTZf82VS9uhLAJRWSsdfxHfgogUp%2FXY2Ba0x%2FV71YO9b3E0rAK61Rj213vAtCLP1B6dCK57Sv%2BBnllHafgEOiambuz%2FnEM8eyhNquPCwLkXoHMRZfvL7dQpX5Tj7FmGeRqQiyyIFkJg8DgnvmZ%2FjPMl2krZX5dwY9kuy81AThU1C4yYwsD3dNgOTaKDxo4XPVJ2%2Fgl1Zl5iaCK&X-Amz-Signature=2244c61c3f646b32ca9c355312fe3eb319e5b987a4c3d5fd78c073c3a211c13f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


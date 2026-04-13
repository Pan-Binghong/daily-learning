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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXAHVWGR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC32hlYS9TdIp2Fh2VeUKP2xjAWx9l3raw078gl%2BxaZ5QIgbc6d7RP4WOptbCW5f1cf3HBacmZ4X20hFj9BSF%2BcNjgq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDMfZF33rWcZtRBKifSrcAw30Ta2v%2Fon6FXEefolnIvbRoTn1AQS2e6T50i9hwS0U%2BTdGoNVaPvra0FHJb7HS92MeN2LXlysks9KgMAqe1%2FkKYQ3TqS91nxduZLeHgPioadH3LdQVmPm9JE01kUyMolXACxC89ASijKRmvOic%2FoSaq9uT2QQaIyi4uu4RnOfW0mY2bCU825rjcVm6hlPOQEzIMWjLW97gGetN4NJuzyxGOkul4o5iZ%2FCQFVWkCrK1C%2BzKebk6RK%2Fd8vzmtob%2Bi%2BMA87T3E%2BajD3o1e25v%2F9%2FPlcBOm7iE9y4by0b9WekSvhCUR8Zwt7u3eL3u0f2Tc4KpfsvICNfSImeX1GsyzWXRWW5KJzujuR1XFuaOPsEWv4%2BKpueVaGiZnM6KESaIEjVaxmmo7vuC%2F4qXaRir1qHPzmtO2W6yniKm3JRbgNEVNdOn4hm21Uhcfu63ZK%2B84xFEBTCoqzx%2FnLBnpqcWtuXdpNwC0kOoeSZDjmnRSV2DdSxuBCVh2n2zJ%2FnBPnt6QfdXAkeYkBcoGdjdDI79LNZvJybt4DxF6g0At5SaoXwW8q1sjebwdToMG5HuH4Tf35xvBYyGYZIHDoPpXu8psvEYpQK2etawee3V%2BFVT2vkDo7Aey%2Bglc7CW6t5TMPSw8c4GOqUBGBBWKyz8JybW5JWnq%2FoP%2FCCtixF0FEy96VUairI0Nrc%2BK%2FK9fZ%2BL0PXqeZCEoOXe2hZLNiqxhXBNwWnN%2BuZXqIb0aAChdP%2FvYmpk%2B04GazMXri%2BvMtXv9oYWTlLAjY25xt95zvDE0MM7YWEIjbGuQ%2F3%2BWuoavZ4FrHV%2FUxQRlVIodnEXyHc5Mg2Q6pgbfAeklAz4W9PlKpJjuV9QS5QxkZhVw7GC&X-Amz-Signature=eb9784f2aa0d729067baf4cc46d4af4b62430553c7946551d4cc8ad4fdde8afb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXAHVWGR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC32hlYS9TdIp2Fh2VeUKP2xjAWx9l3raw078gl%2BxaZ5QIgbc6d7RP4WOptbCW5f1cf3HBacmZ4X20hFj9BSF%2BcNjgq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDMfZF33rWcZtRBKifSrcAw30Ta2v%2Fon6FXEefolnIvbRoTn1AQS2e6T50i9hwS0U%2BTdGoNVaPvra0FHJb7HS92MeN2LXlysks9KgMAqe1%2FkKYQ3TqS91nxduZLeHgPioadH3LdQVmPm9JE01kUyMolXACxC89ASijKRmvOic%2FoSaq9uT2QQaIyi4uu4RnOfW0mY2bCU825rjcVm6hlPOQEzIMWjLW97gGetN4NJuzyxGOkul4o5iZ%2FCQFVWkCrK1C%2BzKebk6RK%2Fd8vzmtob%2Bi%2BMA87T3E%2BajD3o1e25v%2F9%2FPlcBOm7iE9y4by0b9WekSvhCUR8Zwt7u3eL3u0f2Tc4KpfsvICNfSImeX1GsyzWXRWW5KJzujuR1XFuaOPsEWv4%2BKpueVaGiZnM6KESaIEjVaxmmo7vuC%2F4qXaRir1qHPzmtO2W6yniKm3JRbgNEVNdOn4hm21Uhcfu63ZK%2B84xFEBTCoqzx%2FnLBnpqcWtuXdpNwC0kOoeSZDjmnRSV2DdSxuBCVh2n2zJ%2FnBPnt6QfdXAkeYkBcoGdjdDI79LNZvJybt4DxF6g0At5SaoXwW8q1sjebwdToMG5HuH4Tf35xvBYyGYZIHDoPpXu8psvEYpQK2etawee3V%2BFVT2vkDo7Aey%2Bglc7CW6t5TMPSw8c4GOqUBGBBWKyz8JybW5JWnq%2FoP%2FCCtixF0FEy96VUairI0Nrc%2BK%2FK9fZ%2BL0PXqeZCEoOXe2hZLNiqxhXBNwWnN%2BuZXqIb0aAChdP%2FvYmpk%2B04GazMXri%2BvMtXv9oYWTlLAjY25xt95zvDE0MM7YWEIjbGuQ%2F3%2BWuoavZ4FrHV%2FUxQRlVIodnEXyHc5Mg2Q6pgbfAeklAz4W9PlKpJjuV9QS5QxkZhVw7GC&X-Amz-Signature=382d5bcdbd29f45b7fb9761b13bf358341ffdd573462deacd2b11b461857e56d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


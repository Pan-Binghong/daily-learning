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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGBKVRI7%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEcx8VkwUK4ZLfS4qCWGA%2BgKC0MtQmbS4irvqAPbcUqNAiEA1wMnxgeV2Rjo7shvxF8EBVXBBKXzMHHqj0B9p60bCvkqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfQj2FPCz04fHvahyrcAxMjWdhn79h7%2FzaH6TIHad3u%2B%2B8pbNkxeuLsnX5bwftYk9Nj5PjTCx6PEveRa8iOdwV%2F%2Fjhxcy%2FgXVABs0Q5LDWxIk0%2Fra0clu%2FJwYSn5nzTKIX8dc204pzchYWbp5Zr75jwCb3jzyjJc9xWxq%2FVYOaFnJac7YmBN9Zh4HqlUjdY22vmDWuY0Rd81zKCcK0AxpqYaqMJ6JOgUar6QmKWIUcpHDrd3vsaDgWmQWCMKGRayhWqEn8BR0KrODjG%2BwvI3Xk8HuFWWJmfBDnBlLRbJLqr9g0zGpAyc1IrYtHPQ%2BMAvgrzJiqk94eZGrP4Xz9otiUzqd1Y0ZmfGRwVBvyBxOJUgQDO9L3POE4WJAcOs6p4ExoOYILRKtCJfO8ylmBAq2KfE0I7LsKaS%2B1RBP5M0iyyFP7e%2FKvZpzjuljU%2BKYwwybZ6TyclDWCNZyRB49oL0fLMy2L8BpfOtvEWlc4%2FW71TNnj%2Fh2XT0F9SRjzt%2BVorWHJEX3h9vc8BuGqj4gSyuiSpp8J1atssd2BTxmw0NZZx2ZUM0Ghcf7Bw3AacSCNDRvxV6YaqNMbpyNa93jGJlQ6PaXSFiNFOXFiiJBes%2BH3iWRvGht%2Bz%2BD8rVnc8%2FTlgtgfybnmjoPDZbBmyMOTEgcsGOqUB8d%2FSJb1JzysqK8rZfECxugtz6RX6QnI2dWFSbJJDu9B1H6vvE8Let4Cb8QVOK2zQAnoZYzG4nz9%2F%2Bmh2JkldyVzoMCGTupwQyMzbE9YrAXi2jYaxeZ6r3MweP3%2FtRmvAkBR%2BcPpB1KxLbRrTfHfsCW20B4kdNKIszDLg9P3JjaFa1WxcCsvluVbUjyXVC3Y4NGinJl71SYIaQzcaMaxydqJkDt79&X-Amz-Signature=4297dcd3a130d8279ced1988a69a5823e05ae0723650f3fb0d0ddf5a74636a1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGBKVRI7%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEcx8VkwUK4ZLfS4qCWGA%2BgKC0MtQmbS4irvqAPbcUqNAiEA1wMnxgeV2Rjo7shvxF8EBVXBBKXzMHHqj0B9p60bCvkqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfQj2FPCz04fHvahyrcAxMjWdhn79h7%2FzaH6TIHad3u%2B%2B8pbNkxeuLsnX5bwftYk9Nj5PjTCx6PEveRa8iOdwV%2F%2Fjhxcy%2FgXVABs0Q5LDWxIk0%2Fra0clu%2FJwYSn5nzTKIX8dc204pzchYWbp5Zr75jwCb3jzyjJc9xWxq%2FVYOaFnJac7YmBN9Zh4HqlUjdY22vmDWuY0Rd81zKCcK0AxpqYaqMJ6JOgUar6QmKWIUcpHDrd3vsaDgWmQWCMKGRayhWqEn8BR0KrODjG%2BwvI3Xk8HuFWWJmfBDnBlLRbJLqr9g0zGpAyc1IrYtHPQ%2BMAvgrzJiqk94eZGrP4Xz9otiUzqd1Y0ZmfGRwVBvyBxOJUgQDO9L3POE4WJAcOs6p4ExoOYILRKtCJfO8ylmBAq2KfE0I7LsKaS%2B1RBP5M0iyyFP7e%2FKvZpzjuljU%2BKYwwybZ6TyclDWCNZyRB49oL0fLMy2L8BpfOtvEWlc4%2FW71TNnj%2Fh2XT0F9SRjzt%2BVorWHJEX3h9vc8BuGqj4gSyuiSpp8J1atssd2BTxmw0NZZx2ZUM0Ghcf7Bw3AacSCNDRvxV6YaqNMbpyNa93jGJlQ6PaXSFiNFOXFiiJBes%2BH3iWRvGht%2Bz%2BD8rVnc8%2FTlgtgfybnmjoPDZbBmyMOTEgcsGOqUB8d%2FSJb1JzysqK8rZfECxugtz6RX6QnI2dWFSbJJDu9B1H6vvE8Let4Cb8QVOK2zQAnoZYzG4nz9%2F%2Bmh2JkldyVzoMCGTupwQyMzbE9YrAXi2jYaxeZ6r3MweP3%2FtRmvAkBR%2BcPpB1KxLbRrTfHfsCW20B4kdNKIszDLg9P3JjaFa1WxcCsvluVbUjyXVC3Y4NGinJl71SYIaQzcaMaxydqJkDt79&X-Amz-Signature=6e0de8b435a8ba6357e83ba057794d01ba63913701e3d7f31cadc7d14533d6d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


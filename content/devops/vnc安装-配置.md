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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMAIQ6C3%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDLEIL8ngAcMnc4653FVvalyGS0aHGucYdGr6rp8h5O%2BAIgXb7HOuSySz1k3IngqSH4D9nLmLQ%2F0Ti%2BpK39LFLia8oq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDPTH2HkddCSFezndvCrcA%2By9M4YXI%2FA0Cbq3vvo3DI7Y7P5LlKFr5riA0HszlIuZcSRTSe9EL4gryQb4GOVNn9PdRwmOA45HfuHcdYMWc7WPAPLrLCAI3g0VTL5nhEQwXSaWj3OLub8vPaZTK1qKiDDsnFEle7VslE7nmKaB4NU%2BQWWdwaQNmohgCG9BXEhAXIlXhd9cumyelvZsZVykv846nsLrja3kXIIa%2Fyz6hfHXfXoQNRYAMcQJ66mjNQmPpUpoCSVS%2BJFcrFLh%2FyMDhsPMLw%2BfNBtow83TGhM9mEnhyk2sgAx9EVCzGZSYgbyTkdtRcGZg%2F8EezRedbCQzMZ7jOAuCY7RuynhcZOBlSrTlDn93qAH1b7HgIFEOnGkmX9wh0mOYj5OnqRKORcbytEPm8rtBTYrklYjeScXPHLA4gGkwp53bkjjXzYMPNDzwkC9pbhvXAJpj48C9wT705P28fpsdGsyKNhwRCcWHICAjjHpWH%2B7z12j%2BSH0bJRpvU0jBrlzbm7GsWmBc589lu%2FvHce%2FA2vhB8Xapk%2BKv8hmOrYdovbE5r0ddo%2FWvAuVD2FqNdtTSq16WKIhZ3KwYnjNGVg2SeURzYgWvz3mbLqN1g1ZuPCBv6djduI57tPOBz07SdWldHn7VQpi4MMveuMkGOqUBBJcGkVyENE4cUm8RhKusogB%2FIkbyATWGSXa2e1DDtWe1ic0K0GdMFOy9zH1mmAHbtiXg1oAa6DQ2Oqsx1SPVWzNjbf1pvWXZCwhEzLSR1Ja6qg%2BRTT9TfCDoIddkx10s%2FOZvQodmoHBpl8OPUDHOVrxSg5ZnVrNaWiKABt9Ee6RiAwwK2ZK9zJv%2BoELgxCgJVv0YteG6M2O%2FyLL44yFUONaoBvpp&X-Amz-Signature=a98945c3818eb0a3037a59b89919c2ce671b1a0652e4d3675c19bc5d689b34ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMAIQ6C3%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDLEIL8ngAcMnc4653FVvalyGS0aHGucYdGr6rp8h5O%2BAIgXb7HOuSySz1k3IngqSH4D9nLmLQ%2F0Ti%2BpK39LFLia8oq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDPTH2HkddCSFezndvCrcA%2By9M4YXI%2FA0Cbq3vvo3DI7Y7P5LlKFr5riA0HszlIuZcSRTSe9EL4gryQb4GOVNn9PdRwmOA45HfuHcdYMWc7WPAPLrLCAI3g0VTL5nhEQwXSaWj3OLub8vPaZTK1qKiDDsnFEle7VslE7nmKaB4NU%2BQWWdwaQNmohgCG9BXEhAXIlXhd9cumyelvZsZVykv846nsLrja3kXIIa%2Fyz6hfHXfXoQNRYAMcQJ66mjNQmPpUpoCSVS%2BJFcrFLh%2FyMDhsPMLw%2BfNBtow83TGhM9mEnhyk2sgAx9EVCzGZSYgbyTkdtRcGZg%2F8EezRedbCQzMZ7jOAuCY7RuynhcZOBlSrTlDn93qAH1b7HgIFEOnGkmX9wh0mOYj5OnqRKORcbytEPm8rtBTYrklYjeScXPHLA4gGkwp53bkjjXzYMPNDzwkC9pbhvXAJpj48C9wT705P28fpsdGsyKNhwRCcWHICAjjHpWH%2B7z12j%2BSH0bJRpvU0jBrlzbm7GsWmBc589lu%2FvHce%2FA2vhB8Xapk%2BKv8hmOrYdovbE5r0ddo%2FWvAuVD2FqNdtTSq16WKIhZ3KwYnjNGVg2SeURzYgWvz3mbLqN1g1ZuPCBv6djduI57tPOBz07SdWldHn7VQpi4MMveuMkGOqUBBJcGkVyENE4cUm8RhKusogB%2FIkbyATWGSXa2e1DDtWe1ic0K0GdMFOy9zH1mmAHbtiXg1oAa6DQ2Oqsx1SPVWzNjbf1pvWXZCwhEzLSR1Ja6qg%2BRTT9TfCDoIddkx10s%2FOZvQodmoHBpl8OPUDHOVrxSg5ZnVrNaWiKABt9Ee6RiAwwK2ZK9zJv%2BoELgxCgJVv0YteG6M2O%2FyLL44yFUONaoBvpp&X-Amz-Signature=7837b6222657d1341732a1564681b5cf4f8ec1cd506700388079d82a86146f97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


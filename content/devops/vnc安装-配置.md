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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ILEIAZO%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHAhw6%2B3gwQ9SIkP7iA%2FZC49o7HO2PBdWpgDZNexJZpaAiEA6UbMHQ60aI1Xn9Co%2FuTyP46pUowbHBYb%2FqUpQSYeuOUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDGhZ4r5qEVZQcRqMnCrcA0y4R6R4NoOrIH3RcfmBjnB2jPBC%2F0jK6pmKBGhMUolXZCJMVfs0vqc9BujuIQ%2B8vXMbQAMbgUIAEThSV3MVNCxWVMEFD9VoCxrl%2BuOLwmopnqCnDttdDTGB0ESfxXbXXnbzpNW7QuAopA28wsLARR4NLmXGOC3kIJmkZof%2FsNhnf6FZQ0UCASi107DLzJ3KzIPFGtMXI%2BItwzZonrIiKJqasFljGcYfWZmYuAUgqyyAVS35d%2BJjz4rxjR6YtpXbHlPcGtnFJmryg1OHtjArmbrStq%2FZNT7pcjq6MDVuZ5Xiht4H6DaWbJrkA0tu4GsLNqpJh6sa4R4QX33tYEym8OMn7gIwEBJ6nWrxpw7l84l4UpI%2FIhElAV456xyBeBCCpbwBlfLe7cOPjnrJYD3%2Bg4xa%2BPvYNjcO9XHjTGrCpVmOwa5ay6zBxvtF69ZLieun%2B6Z3WdSuUS%2FXWwrm5YOezVpP%2B4AVN%2BT%2BPG2wqjOvQ6eM4aolWO2h8IFhvo9WKM%2BsZ0S7R3fdmcEUjKYw67PZqoYrIqpCkOcGfItDNnBlvxXJBMsrgqaqPta5bMgTlAozzwNZTYSda65E24Lb1wgUjA4SsIK1eJBCgAjro4iPksiQdSHSyFWqNCjcOlJsMNG%2BysgGOqUBI%2BMqUEVEvQCGoAb%2Bqxd9oLyOeDdt2mt%2FcBdv5RM4T6oNf%2BfUP3fpPuaR4boCcKFLUQejh%2BOE68FRD8FqPokhO5M1G9t9tCjX15RghXwzVjfGZrcBnoYdWfrAqcNmxtWtaJZKZNla0sIjKlMP4Tb1XdLG8hf9ZwaLH3aQayH8f8foUkWCx52WMMI89xoe%2Bsf9XaEMA7Q%2FpeptM0VNt6d8mXppYMIw&X-Amz-Signature=949ef85263b9116ae6e79c79df454e5b192ad18daac32a17c84611308713580d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ILEIAZO%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHAhw6%2B3gwQ9SIkP7iA%2FZC49o7HO2PBdWpgDZNexJZpaAiEA6UbMHQ60aI1Xn9Co%2FuTyP46pUowbHBYb%2FqUpQSYeuOUq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDGhZ4r5qEVZQcRqMnCrcA0y4R6R4NoOrIH3RcfmBjnB2jPBC%2F0jK6pmKBGhMUolXZCJMVfs0vqc9BujuIQ%2B8vXMbQAMbgUIAEThSV3MVNCxWVMEFD9VoCxrl%2BuOLwmopnqCnDttdDTGB0ESfxXbXXnbzpNW7QuAopA28wsLARR4NLmXGOC3kIJmkZof%2FsNhnf6FZQ0UCASi107DLzJ3KzIPFGtMXI%2BItwzZonrIiKJqasFljGcYfWZmYuAUgqyyAVS35d%2BJjz4rxjR6YtpXbHlPcGtnFJmryg1OHtjArmbrStq%2FZNT7pcjq6MDVuZ5Xiht4H6DaWbJrkA0tu4GsLNqpJh6sa4R4QX33tYEym8OMn7gIwEBJ6nWrxpw7l84l4UpI%2FIhElAV456xyBeBCCpbwBlfLe7cOPjnrJYD3%2Bg4xa%2BPvYNjcO9XHjTGrCpVmOwa5ay6zBxvtF69ZLieun%2B6Z3WdSuUS%2FXWwrm5YOezVpP%2B4AVN%2BT%2BPG2wqjOvQ6eM4aolWO2h8IFhvo9WKM%2BsZ0S7R3fdmcEUjKYw67PZqoYrIqpCkOcGfItDNnBlvxXJBMsrgqaqPta5bMgTlAozzwNZTYSda65E24Lb1wgUjA4SsIK1eJBCgAjro4iPksiQdSHSyFWqNCjcOlJsMNG%2BysgGOqUBI%2BMqUEVEvQCGoAb%2Bqxd9oLyOeDdt2mt%2FcBdv5RM4T6oNf%2BfUP3fpPuaR4boCcKFLUQejh%2BOE68FRD8FqPokhO5M1G9t9tCjX15RghXwzVjfGZrcBnoYdWfrAqcNmxtWtaJZKZNla0sIjKlMP4Tb1XdLG8hf9ZwaLH3aQayH8f8foUkWCx52WMMI89xoe%2Bsf9XaEMA7Q%2FpeptM0VNt6d8mXppYMIw&X-Amz-Signature=a4665d1b01838ac8779893418a3f39dbc4831802509d4998f75746a24c6150e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBU4CLE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDVrEBj%2FcBZFimydBUNMR4H7oS7OA%2FgrMinfhmBtNFEZAiEAmCh%2FliCra8gXUjvA%2Bos%2FxlaEHTicCtDD6pUOfPGdUgUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFE9ghm7GW4s%2FvRtkSrcA53uZsNcnkfZf5CChL24988CPP3dA8%2FfgtESoHnKKXgohvNukA21Wepbnqz9m%2BjV6uLYoPJ2iaZg3dP4QsMj6ZsP5hCjlZn4%2BhpWTXQICQxP01byAcSkU4QQrVOrYxxqJDZ443kzXOHLfj%2FTKTEioA13dYddhidPiKAg8%2FeH7jAbSLJz26jR82gZ7%2B36lnUc7q4H3Xpd7%2B4E%2B5iGoQBVPzcwnFmnOgai8ZkgNeHPwRj%2F1I9AEbxO3Z21eti7WRmdDaXy22nimzq5EV8tf6LTZicYyB%2BfO0xL%2Bhm4qAPRbU9Tut6ESRdFhjzVn%2BpeMedsaeVS7Am%2BnYx1Rr3aUMRiMP9I9Jpylghl1N8PsYzO%2BzKISOpNpgimkaK9g03UCCLXg9eGlOL4fiHORjiUBfmTuAU5mIuzDv4ci2smDOxvEp0BkxrEy916HkyVcv%2BhlMwIczvKQTse4jBphNnLnLW5FVyH0VkaKSa6asN%2FIUvF7yGXrgqJjgRL4w4n42qUmOwBFM2lNJ7VTdmfRwCut9TP59zn1Rj%2BExRMxmfc9n4TbCXkDaPBmUgBi4kpB%2FGtE99VBIVFjRa73IVQo55cKWxPDSCf5Wyf8SayQZ2toTzRjNygwmeooxTSaNwDWgbEMNTvr8gGOqUBVI3SyDnt%2F8NNwmwoBbVmo7ep5xU%2FoMVMPYXM05elaRgTo4jYf2fmoHb77BgTOWS6TAIvqP98fY9qHqkvcTxAJlSSbZwR5yfusuq2BHu%2FLLHNaHjs93m94EBOSj0kIo2qkMn%2Fvn2lLVfMF%2BgbiSC7i10eU5v3OYQ854wJFxhUOPx5kdJHxxNAKN7tZrRK2ad5Xe9mDHPEfHqL9UWETJrWXksf4bf8&X-Amz-Signature=78aa8ac7c8320eaeaa83ab924587c331bbc4e2b29dad91c8efead34b9a0850c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBU4CLE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDVrEBj%2FcBZFimydBUNMR4H7oS7OA%2FgrMinfhmBtNFEZAiEAmCh%2FliCra8gXUjvA%2Bos%2FxlaEHTicCtDD6pUOfPGdUgUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFE9ghm7GW4s%2FvRtkSrcA53uZsNcnkfZf5CChL24988CPP3dA8%2FfgtESoHnKKXgohvNukA21Wepbnqz9m%2BjV6uLYoPJ2iaZg3dP4QsMj6ZsP5hCjlZn4%2BhpWTXQICQxP01byAcSkU4QQrVOrYxxqJDZ443kzXOHLfj%2FTKTEioA13dYddhidPiKAg8%2FeH7jAbSLJz26jR82gZ7%2B36lnUc7q4H3Xpd7%2B4E%2B5iGoQBVPzcwnFmnOgai8ZkgNeHPwRj%2F1I9AEbxO3Z21eti7WRmdDaXy22nimzq5EV8tf6LTZicYyB%2BfO0xL%2Bhm4qAPRbU9Tut6ESRdFhjzVn%2BpeMedsaeVS7Am%2BnYx1Rr3aUMRiMP9I9Jpylghl1N8PsYzO%2BzKISOpNpgimkaK9g03UCCLXg9eGlOL4fiHORjiUBfmTuAU5mIuzDv4ci2smDOxvEp0BkxrEy916HkyVcv%2BhlMwIczvKQTse4jBphNnLnLW5FVyH0VkaKSa6asN%2FIUvF7yGXrgqJjgRL4w4n42qUmOwBFM2lNJ7VTdmfRwCut9TP59zn1Rj%2BExRMxmfc9n4TbCXkDaPBmUgBi4kpB%2FGtE99VBIVFjRa73IVQo55cKWxPDSCf5Wyf8SayQZ2toTzRjNygwmeooxTSaNwDWgbEMNTvr8gGOqUBVI3SyDnt%2F8NNwmwoBbVmo7ep5xU%2FoMVMPYXM05elaRgTo4jYf2fmoHb77BgTOWS6TAIvqP98fY9qHqkvcTxAJlSSbZwR5yfusuq2BHu%2FLLHNaHjs93m94EBOSj0kIo2qkMn%2Fvn2lLVfMF%2BgbiSC7i10eU5v3OYQ854wJFxhUOPx5kdJHxxNAKN7tZrRK2ad5Xe9mDHPEfHqL9UWETJrWXksf4bf8&X-Amz-Signature=35fe5d13d5b57760a5a8a77578f9b0f7a4b1c26b974c5862e928756c476e6939&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


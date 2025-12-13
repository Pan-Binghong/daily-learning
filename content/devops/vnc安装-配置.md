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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D7KM4AB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIEpQrg%2BG%2BdeLb5m5zeakiXlWky9jqLGRdrlq9R0mDrKbAiEA3KAE%2FLk2Ca0ejtR0MAf1ffVwg0N%2FKcKJ1SHrPz0lzDUq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDMXEQOb%2BUkGL2gSzDyrcAzJCBOKuVeppCesOfVJ3IWu0aTgqW6qj5zjAdq2vz7gyztRiRVfjhuC0Zh7jZlcaSeeJ4DRjEXLGf5ZCqw%2B44IPOMUW4V9NiGzAmnPlPEzAhpqJyV31iv5VLERdgZzhiOp69SlOM%2BDwPONSewdJnbApXczjLFfYeP%2BLZWdSpTlYUimVPAVLqxr4xlcTt66Ax1j60yGg4Xgfg7ksxorUUAfrWOOqHMOs6CCNwKNX%2FK6xswHJxh9YQG%2BRwd5BcuFqRTCrBgMaltYRfvW8aThWWciKJoNTl%2By2vF8HUloEB7MC4ZakEcexOf%2F1l1vpStFqbmS1Q30o5Jjn%2FQOrT1%2FwAHIFCPZwyBPkLClihHe4M7g7VS%2FU3gLZkvsd09x0uHpkYe5vGE1WK3biPpnsgeKNGUrw3dArccBDExTyYQHRIGFBEK5LwPatPh19qeEE8HeqQVjAQH7wVr9rR6SR4MH547DbQbZ6Be3WVDQulomb%2B%2FzSux63O9S6vTjGp%2F8KACtPFrU5cDQ0sdgFqpvhUbzir68CMGj7HrA0NoKJP4ipr5O95uaUrs1cpTox83T1eB2LIzXQn3g1x6vYSG3KuKy4jgKFJjde8U%2FI1K0%2FnxYxqRgbYLjBJfYhSCt6w6E4JMMeM88kGOqUBAAv21sTdol1nJZBdH0iDsIsZmhGCXDPEL0Jkty%2B8BpjHkOnke7N27QfTrXYgdHlGtREOKCtylyK%2FeYyAMSH42SWcAz%2FWC09ZSpEvk%2B1oMzytosmp1kC6wlSHGD2MbCfnAutRZ%2FX3WBx%2BWyJ9T0BW6KfgR2gKjYlbsvuh8hLDytpXa00Wtg4zyW54OPngnwDMGCroPZ2ZnFgUOV2RT7WdHgUcfh4G&X-Amz-Signature=db20cf6497962939a88c132ca8ed3f9a758e60bd65d1358875d8a9e84b7cc245&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D7KM4AB%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIEpQrg%2BG%2BdeLb5m5zeakiXlWky9jqLGRdrlq9R0mDrKbAiEA3KAE%2FLk2Ca0ejtR0MAf1ffVwg0N%2FKcKJ1SHrPz0lzDUq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDMXEQOb%2BUkGL2gSzDyrcAzJCBOKuVeppCesOfVJ3IWu0aTgqW6qj5zjAdq2vz7gyztRiRVfjhuC0Zh7jZlcaSeeJ4DRjEXLGf5ZCqw%2B44IPOMUW4V9NiGzAmnPlPEzAhpqJyV31iv5VLERdgZzhiOp69SlOM%2BDwPONSewdJnbApXczjLFfYeP%2BLZWdSpTlYUimVPAVLqxr4xlcTt66Ax1j60yGg4Xgfg7ksxorUUAfrWOOqHMOs6CCNwKNX%2FK6xswHJxh9YQG%2BRwd5BcuFqRTCrBgMaltYRfvW8aThWWciKJoNTl%2By2vF8HUloEB7MC4ZakEcexOf%2F1l1vpStFqbmS1Q30o5Jjn%2FQOrT1%2FwAHIFCPZwyBPkLClihHe4M7g7VS%2FU3gLZkvsd09x0uHpkYe5vGE1WK3biPpnsgeKNGUrw3dArccBDExTyYQHRIGFBEK5LwPatPh19qeEE8HeqQVjAQH7wVr9rR6SR4MH547DbQbZ6Be3WVDQulomb%2B%2FzSux63O9S6vTjGp%2F8KACtPFrU5cDQ0sdgFqpvhUbzir68CMGj7HrA0NoKJP4ipr5O95uaUrs1cpTox83T1eB2LIzXQn3g1x6vYSG3KuKy4jgKFJjde8U%2FI1K0%2FnxYxqRgbYLjBJfYhSCt6w6E4JMMeM88kGOqUBAAv21sTdol1nJZBdH0iDsIsZmhGCXDPEL0Jkty%2B8BpjHkOnke7N27QfTrXYgdHlGtREOKCtylyK%2FeYyAMSH42SWcAz%2FWC09ZSpEvk%2B1oMzytosmp1kC6wlSHGD2MbCfnAutRZ%2FX3WBx%2BWyJ9T0BW6KfgR2gKjYlbsvuh8hLDytpXa00Wtg4zyW54OPngnwDMGCroPZ2ZnFgUOV2RT7WdHgUcfh4G&X-Amz-Signature=5b627de202588fe152151964d791ed11c13bf3a5424f25c8bbe8d3b8577caa25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


---
title: mstsc.exe端口修改
date: '2024-11-18T08:36:00.000Z'
lastmod: '2024-11-19T08:19:00.000Z'
draft: false
tags:
- Windows
categories:
- DevOps
---

> 💡 mstsc 是 Microsoft Terminal Services Client 的缩写，是用于远程桌面连接的工具。通过它，你可以使用 Windows 自带的远程桌面协议（RDP）连接到其他 Windows 设备的桌面环境。通过 Win + R，然后输入 mstsc，打开远程桌面连接界面。

---

1. 打开注册表
1. 修改端口号
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp PortNumber 为 xxxx
1. 防火墙设置
1. 启动服务
1. 勾选设置
1. 重启电脑

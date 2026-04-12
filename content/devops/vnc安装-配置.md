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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMN47F75%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE7aFj7VTG3ulZGeMA25YiGXepANyPvpzVBAEMzMtFWgIgOxqrW4e8T6SSLmcQ0OEr%2Bph36j1uLgDajZkLgIggjfYq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDCDk6Gz8CEl%2BLV7TeSrcAxtVa%2Frih86whIVvr2AMLYdSVRkClb%2BkHr%2FsnCjcjsF1kcp6rTUoWU0kLTqnTH2nPE832mIg9lyrMGXZxGNVlRDV6M3D%2FRKqjdr1XHYlHzIhHDWW9fOBK%2BeNc0%2BXNy%2B709YVqWZyBShjZ1TtBUWMza1LX1kH2yno6%2BuBwgUwCj4Z7brZRrzNIxIPS6KMo3CoNnZiaDxfqTbb1ZhAeHiZYY05%2F8cr%2FsLwxB1IAJp5gsX6QH9GL52hcmxuFOEujTTD89XNBW9AO7CQrMN5gEA5SkhaVK8raspPUmlx1BkRDDSKjldKpE3wtBU%2BTfUSDp5qjKaP8wmmYK1%2FZaU5WY%2FIskPTirps1TlCosZeOBR7hznhW3cWqs%2F0VeN6YPebwrWma150c3i7ZpB4epNc04IB6T79eP2fQv8F9MwcAFQHxa4sqb83wMc8zSCj35fniQHJWrMbndY6Gis91bIdRG4uWtzjJ3jr%2B2as5wdFt4YAQnzB8c0%2F5dlTzon22aCRAVPsIrHOlHaed4d5hV4h7Wayw6ut9IaGrGcCGsLgq7KmgTQ6mShxTG60NGdc7mHFhNwiiLJb2S6F7%2BALX5z2LeLNCGAIf%2BRb71xmMat2ZlPB13UOA2QwxC2yKOLlXmIaMKKH7M4GOqUBae8XOkOKqhyDrKDqlJ5evyt2b1HV%2Fe54NL%2BZBGM27ycRSiEMUZLn45NkT4w6DfVoMFhIODxEcz%2FUcP1daT2LCc%2F78qYTb%2Fx3Zg8lXm9%2FkJkZ69cFlpNLyMuFlxn2omOOhRsbWK7iNAj08GO%2B5KcpzJZorF2RX1ofnui9Ssc8jVzcML%2BNTNYNfSeLou2sjTo9Wthb4GKZUAZImQBe8vRSwbezBS08&X-Amz-Signature=d89f330c3695533d1a6d8bd65e0d743a679ca7b0af3eb90ea2c3730b56e86d37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMN47F75%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE7aFj7VTG3ulZGeMA25YiGXepANyPvpzVBAEMzMtFWgIgOxqrW4e8T6SSLmcQ0OEr%2Bph36j1uLgDajZkLgIggjfYq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDCDk6Gz8CEl%2BLV7TeSrcAxtVa%2Frih86whIVvr2AMLYdSVRkClb%2BkHr%2FsnCjcjsF1kcp6rTUoWU0kLTqnTH2nPE832mIg9lyrMGXZxGNVlRDV6M3D%2FRKqjdr1XHYlHzIhHDWW9fOBK%2BeNc0%2BXNy%2B709YVqWZyBShjZ1TtBUWMza1LX1kH2yno6%2BuBwgUwCj4Z7brZRrzNIxIPS6KMo3CoNnZiaDxfqTbb1ZhAeHiZYY05%2F8cr%2FsLwxB1IAJp5gsX6QH9GL52hcmxuFOEujTTD89XNBW9AO7CQrMN5gEA5SkhaVK8raspPUmlx1BkRDDSKjldKpE3wtBU%2BTfUSDp5qjKaP8wmmYK1%2FZaU5WY%2FIskPTirps1TlCosZeOBR7hznhW3cWqs%2F0VeN6YPebwrWma150c3i7ZpB4epNc04IB6T79eP2fQv8F9MwcAFQHxa4sqb83wMc8zSCj35fniQHJWrMbndY6Gis91bIdRG4uWtzjJ3jr%2B2as5wdFt4YAQnzB8c0%2F5dlTzon22aCRAVPsIrHOlHaed4d5hV4h7Wayw6ut9IaGrGcCGsLgq7KmgTQ6mShxTG60NGdc7mHFhNwiiLJb2S6F7%2BALX5z2LeLNCGAIf%2BRb71xmMat2ZlPB13UOA2QwxC2yKOLlXmIaMKKH7M4GOqUBae8XOkOKqhyDrKDqlJ5evyt2b1HV%2Fe54NL%2BZBGM27ycRSiEMUZLn45NkT4w6DfVoMFhIODxEcz%2FUcP1daT2LCc%2F78qYTb%2Fx3Zg8lXm9%2FkJkZ69cFlpNLyMuFlxn2omOOhRsbWK7iNAj08GO%2B5KcpzJZorF2RX1ofnui9Ssc8jVzcML%2BNTNYNfSeLou2sjTo9Wthb4GKZUAZImQBe8vRSwbezBS08&X-Amz-Signature=e1e7365685718548aa9d23d07d21fb41dd0f3a11c1e6b9453b7eea52d39a3210&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


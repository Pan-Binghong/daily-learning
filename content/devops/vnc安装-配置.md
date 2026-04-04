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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWM6RXAY%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAV6Kk8C1xvquGfHhJ8p1AhB6iZaDoQtvYoGODn44yEBAiEA1TPxkhbN2zBPnpPzcaSnhC8ixOiUP6X5ON6S0frwXnkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMvajvKnvRculIkcircA4gVdkjvCFQaFhIwAtEnerXHE%2BClooGmHvLerTH2UvW%2Fm6ge%2FmT0OH4INmflKJ8qCKP2Lhje%2BqwdlmxdniLZtEAVWjwyRaeQgMWru4anwr1cAZ7OSponNnFVkkEgvEPxe2uCyT7FK5%2B4TgfDjDg8AD1GYq1KPCa%2FGgLd%2B4%2Bbe%2BIUL12%2B3o5%2FoWne057nQf3FaP%2FSLg%2BnhAHd5B%2Bh2R7%2FdSfdjQaPZihAhr5pAz3nF9swdAsi3kq%2FVYe7LuA0ViXy1%2BwScmfAs8gVIhZ9uSA%2Bmaiu6XJFjM3ZEoJfbcY3oqc5H95msOHLORB74SGlHorRbsNXfjaHcMABS4Ya1nQ9aHDbrW4xwcvREYUySEsTdq%2FF8kLUqXLSrHwNCgRvQPVQG2gJaxy28uTpO67VaHr9AeT8PMfS%2FG8aaSbm%2BPMkEvC1HlwTUNKaF806gjWv%2BJqYf5fQsnWN6Y4wwNmWE8NVtdr%2FrWE1uyR5pCFlhatxcDjA0fLZT%2BKF4ELAN0p7nkRB2euzUrhYDpsDL4J%2B%2BIMiYVA4eqAY5V%2BMs%2F2L8YgTgrruwBEt1yCjipNdJOCKC%2BIfFcZtGk8uY8Riw8RyUCRSC3mAOL%2BoCLu5Ok0CnD3IoTf1VOenQH4ICgDG5DRcMMiNws4GOqUBn4%2BA01WkzE6pTeTj86o4HEBvPtpGprCy2rzvNtGYD1IHMjLXjJsFaafdcEeF2HmI94sGW0UsMBP7F4TM9rtHLOGfTF1vGjcFczr2kRY0FEWq%2B%2B0GmdI30lsNNxuikGSx490CGZA%2BTRdLowJFfwtuCc8Un%2FmhNb1OAEb1TcNRQ5bi1QiUJ3PY6y1TXyjj1k0rg%2BpF0LVZDMJYGbZy3zf1owLlXoNu&X-Amz-Signature=dd9da8170144797b3b8e2964489342e71cc219c6d1bbf877c4a17972f4fa54e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWM6RXAY%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAV6Kk8C1xvquGfHhJ8p1AhB6iZaDoQtvYoGODn44yEBAiEA1TPxkhbN2zBPnpPzcaSnhC8ixOiUP6X5ON6S0frwXnkqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMvajvKnvRculIkcircA4gVdkjvCFQaFhIwAtEnerXHE%2BClooGmHvLerTH2UvW%2Fm6ge%2FmT0OH4INmflKJ8qCKP2Lhje%2BqwdlmxdniLZtEAVWjwyRaeQgMWru4anwr1cAZ7OSponNnFVkkEgvEPxe2uCyT7FK5%2B4TgfDjDg8AD1GYq1KPCa%2FGgLd%2B4%2Bbe%2BIUL12%2B3o5%2FoWne057nQf3FaP%2FSLg%2BnhAHd5B%2Bh2R7%2FdSfdjQaPZihAhr5pAz3nF9swdAsi3kq%2FVYe7LuA0ViXy1%2BwScmfAs8gVIhZ9uSA%2Bmaiu6XJFjM3ZEoJfbcY3oqc5H95msOHLORB74SGlHorRbsNXfjaHcMABS4Ya1nQ9aHDbrW4xwcvREYUySEsTdq%2FF8kLUqXLSrHwNCgRvQPVQG2gJaxy28uTpO67VaHr9AeT8PMfS%2FG8aaSbm%2BPMkEvC1HlwTUNKaF806gjWv%2BJqYf5fQsnWN6Y4wwNmWE8NVtdr%2FrWE1uyR5pCFlhatxcDjA0fLZT%2BKF4ELAN0p7nkRB2euzUrhYDpsDL4J%2B%2BIMiYVA4eqAY5V%2BMs%2F2L8YgTgrruwBEt1yCjipNdJOCKC%2BIfFcZtGk8uY8Riw8RyUCRSC3mAOL%2BoCLu5Ok0CnD3IoTf1VOenQH4ICgDG5DRcMMiNws4GOqUBn4%2BA01WkzE6pTeTj86o4HEBvPtpGprCy2rzvNtGYD1IHMjLXjJsFaafdcEeF2HmI94sGW0UsMBP7F4TM9rtHLOGfTF1vGjcFczr2kRY0FEWq%2B%2B0GmdI30lsNNxuikGSx490CGZA%2BTRdLowJFfwtuCc8Un%2FmhNb1OAEb1TcNRQ5bi1QiUJ3PY6y1TXyjj1k0rg%2BpF0LVZDMJYGbZy3zf1owLlXoNu&X-Amz-Signature=f265ab6c8d87cb104164900ad78de40420fcbad8e1ea214a02f423bfb3c05313&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


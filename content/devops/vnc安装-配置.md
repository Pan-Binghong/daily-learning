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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR5F5NAP%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQC%2F7bXjJW2nFlMgB%2BRhQ7y%2FsnvY%2BrbSARwm7yzh90rZ3AIgYjki85Kn2Jo1ueje%2BCaXnK6H2GcrqB5ykYhUnC0t0w0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDMPLHaI2gwmWg0muhSrcAy6AnOkx%2FJOGlIUz4mynS8asY6IaZonWC7SLzKJDf92A0cX7mevRK4XlhhwRMbqUybjGTzGrncNnPMAVtzEeRJd4wRxn0Rxuw2tLkUjCttsZu%2F41%2FO1DEOFn8Jyk2bkrO5LJ5D59LPWcRqce4TudnPOZejIEVMFQK9pM%2BN4vtqFeRaAqyLUG6ptZNod70YdqwWrRcMGJsl5Fowr6fV68VSSQ1wbqNSxb32lagAezbgSUR%2FDtubtAWQ%2B%2F3ftxr21%2Fh%2Fffqj9Ls1QafB%2FHtsGep3C3FsftVpnfAG6M7KfAQeOTdEetNB%2FrmJWWbER6YyQgrW5%2Bp1gwJAPgp2nOshIBqEbN5J%2B72%2Fo2aOVAsiVZL0MYyUeQsyu0%2Ft7WRUIU0gVfUgXvXiWtcPCErisPkqRszQgJ06MNdmTg6zkqSPeaJwzKEwrh7cdfAcKWJlHUMGUhIxblnSP56FK%2Byto1iv52IuVPsW5eP%2FpZ8kkEllEx%2Bti2EJg8eyP4YUFPKagMmygztd1okClRDIurNaFR9DwcAvB0x3AcwZBNri%2BS2Zrw%2BNga7D8UEwpcqTnlH3wws2RKma8s%2B%2Fnvb%2F1z9nHbIGNkwhSrKSU%2FucMY3hsv0f5XiA4JvgSRMW2IUCophpX%2BMIn1%2FswGOqUB6V4qmPNpLh%2FFKyukKcJQsj4aPahTxmt88Ljihts1xBfN7KKGFMDoGhQ0uwT%2BFIkgOsuylHDfiuOli51kK0yDx27GG0L9QMzr%2BkuUlJR6kIAAwuR%2FGU4P1ZAmBSI%2BDbYXfLeF7LF1Qh0J%2BWyBNoEDpurD%2B17VyslKdqytrsc18r4xF1nZFSeoZJpsrdvimM5GkoTHAjG0fiNYJw64tZTgGIqXG4D5&X-Amz-Signature=d274f6f8c424a225cef3f863bc7dc8ccd471a29a846afb85923759c171f4b8c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR5F5NAP%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQC%2F7bXjJW2nFlMgB%2BRhQ7y%2FsnvY%2BrbSARwm7yzh90rZ3AIgYjki85Kn2Jo1ueje%2BCaXnK6H2GcrqB5ykYhUnC0t0w0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDMPLHaI2gwmWg0muhSrcAy6AnOkx%2FJOGlIUz4mynS8asY6IaZonWC7SLzKJDf92A0cX7mevRK4XlhhwRMbqUybjGTzGrncNnPMAVtzEeRJd4wRxn0Rxuw2tLkUjCttsZu%2F41%2FO1DEOFn8Jyk2bkrO5LJ5D59LPWcRqce4TudnPOZejIEVMFQK9pM%2BN4vtqFeRaAqyLUG6ptZNod70YdqwWrRcMGJsl5Fowr6fV68VSSQ1wbqNSxb32lagAezbgSUR%2FDtubtAWQ%2B%2F3ftxr21%2Fh%2Fffqj9Ls1QafB%2FHtsGep3C3FsftVpnfAG6M7KfAQeOTdEetNB%2FrmJWWbER6YyQgrW5%2Bp1gwJAPgp2nOshIBqEbN5J%2B72%2Fo2aOVAsiVZL0MYyUeQsyu0%2Ft7WRUIU0gVfUgXvXiWtcPCErisPkqRszQgJ06MNdmTg6zkqSPeaJwzKEwrh7cdfAcKWJlHUMGUhIxblnSP56FK%2Byto1iv52IuVPsW5eP%2FpZ8kkEllEx%2Bti2EJg8eyP4YUFPKagMmygztd1okClRDIurNaFR9DwcAvB0x3AcwZBNri%2BS2Zrw%2BNga7D8UEwpcqTnlH3wws2RKma8s%2B%2Fnvb%2F1z9nHbIGNkwhSrKSU%2FucMY3hsv0f5XiA4JvgSRMW2IUCophpX%2BMIn1%2FswGOqUB6V4qmPNpLh%2FFKyukKcJQsj4aPahTxmt88Ljihts1xBfN7KKGFMDoGhQ0uwT%2BFIkgOsuylHDfiuOli51kK0yDx27GG0L9QMzr%2BkuUlJR6kIAAwuR%2FGU4P1ZAmBSI%2BDbYXfLeF7LF1Qh0J%2BWyBNoEDpurD%2B17VyslKdqytrsc18r4xF1nZFSeoZJpsrdvimM5GkoTHAjG0fiNYJw64tZTgGIqXG4D5&X-Amz-Signature=5f25af6532d15b757ac95b9fb8c73e9c1fda58e54d7b795d09f4e95e439a55eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


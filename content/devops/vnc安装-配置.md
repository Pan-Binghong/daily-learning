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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBWGPRY%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3KCFJv3EsJE059AGGTrwmZIJAWfmptjvc9AuuFQxkCwIhAK2vwNMD%2BVhGhgdz%2FHozv77p5DAPzhHiGdV%2BLs4njyXiKv8DCE8QABoMNjM3NDIzMTgzODA1IgyguYFUsjg7td2tYqoq3AMnyXAW7rBs314WwWlZmctcaAFqhHoUUs07GUYrraO%2FKpxNdVguiBVMa1Qwk5%2FbBab630P7YeAvtRhmZwDShzOh8rX1oMeJQzdT89%2BAM6gxtlo4i1lyQyjdBsHTKRXERUhPcGEVW2owPnX8spFk0q4QHY8vgkwihivcGBo6QA6%2FAETfSKK7c7AAsYqr6prh6AAFoQb2ZXMq9hSmJ2atCpIHz0%2FlZjS%2BlGhcKVubgHye8PmuTjiP5yYtluMOMZaOZB34XpejBJ4yeuvoHVCR%2FcgOk2frnb%2BySIv2bJ0OUtCLnpP6MmZf011xlAQ6wQZhXQc0ruf9bdI%2B7jKM%2BQhuhVKV24vjo7mXgNhvf9wLMObO%2F10j3I%2B%2Bx5tqeltppP1Gx2QsGIibVbGnlFmOqofqPanlPeiFza2bJixpYxECUW5pR4HqW01ntYIRDnL1rQbb%2Br4CpiEexNQvHMGAcDOG9eD3Xr4ob2xUXPsV1TWVmJvzmp0Ys8paJsnNiytRwG2KtIlhZ35S5ak8D1YAlUN568uzusfSrrM205anXdYqf7xJYGDWLrTol8x%2BmrS1MqwkttwIfOEE82LXjkucMJEZG5jp6%2FXOxL38qVXa7JRH4JcZmRP5bmAjmBJgn0zdWjDvi8jJBjqkATB%2F8CtUNPnB5yUzbeBWxXYhPznribDh6S%2Bj9ToNWaPEK6qSWn1Dzc75hmGTuw1w%2FbME8ZX4a8Uh1Lay0g%2F1lhYdaIlGXe%2Ffs7vrBWXptpKai0v5T9U4xz3DJ4g6AMTtTmWtm%2F9wVipJs9J2nOL4IQuJQ%2FE86qb2jTGJhbSSVXoEW8KWEXuOztf4asrtErS639EE%2BGewv7HBmT4TWCSHeqIcC%2FoW&X-Amz-Signature=7fccc507e99a5e34b6cbed71bfb6d0e5502b6f9ef18e3bedd70a2c6cdac2544d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBWGPRY%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3KCFJv3EsJE059AGGTrwmZIJAWfmptjvc9AuuFQxkCwIhAK2vwNMD%2BVhGhgdz%2FHozv77p5DAPzhHiGdV%2BLs4njyXiKv8DCE8QABoMNjM3NDIzMTgzODA1IgyguYFUsjg7td2tYqoq3AMnyXAW7rBs314WwWlZmctcaAFqhHoUUs07GUYrraO%2FKpxNdVguiBVMa1Qwk5%2FbBab630P7YeAvtRhmZwDShzOh8rX1oMeJQzdT89%2BAM6gxtlo4i1lyQyjdBsHTKRXERUhPcGEVW2owPnX8spFk0q4QHY8vgkwihivcGBo6QA6%2FAETfSKK7c7AAsYqr6prh6AAFoQb2ZXMq9hSmJ2atCpIHz0%2FlZjS%2BlGhcKVubgHye8PmuTjiP5yYtluMOMZaOZB34XpejBJ4yeuvoHVCR%2FcgOk2frnb%2BySIv2bJ0OUtCLnpP6MmZf011xlAQ6wQZhXQc0ruf9bdI%2B7jKM%2BQhuhVKV24vjo7mXgNhvf9wLMObO%2F10j3I%2B%2Bx5tqeltppP1Gx2QsGIibVbGnlFmOqofqPanlPeiFza2bJixpYxECUW5pR4HqW01ntYIRDnL1rQbb%2Br4CpiEexNQvHMGAcDOG9eD3Xr4ob2xUXPsV1TWVmJvzmp0Ys8paJsnNiytRwG2KtIlhZ35S5ak8D1YAlUN568uzusfSrrM205anXdYqf7xJYGDWLrTol8x%2BmrS1MqwkttwIfOEE82LXjkucMJEZG5jp6%2FXOxL38qVXa7JRH4JcZmRP5bmAjmBJgn0zdWjDvi8jJBjqkATB%2F8CtUNPnB5yUzbeBWxXYhPznribDh6S%2Bj9ToNWaPEK6qSWn1Dzc75hmGTuw1w%2FbME8ZX4a8Uh1Lay0g%2F1lhYdaIlGXe%2Ffs7vrBWXptpKai0v5T9U4xz3DJ4g6AMTtTmWtm%2F9wVipJs9J2nOL4IQuJQ%2FE86qb2jTGJhbSSVXoEW8KWEXuOztf4asrtErS639EE%2BGewv7HBmT4TWCSHeqIcC%2FoW&X-Amz-Signature=d3f9a95ac59aeac2e59d1b33951fc23f11d02348260cf84c01d9262b7ae009ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


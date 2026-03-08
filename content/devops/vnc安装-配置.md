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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV5U22HE%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIGGjc%2B3Vah%2BwQkb32Z%2FgPn9f%2BwPpQwWGP0W2O4LaiXw9AiAHqU8HU6lwT1tK4js2JlV39W7Uor4mIdqPRAxO8XAvkyr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIME%2B5XvdD4GGOTKjplKtwDIbaIUrUGIvNl%2BrHOuqhiOUEqV2FtsO0CRL%2FT9HITJLHKyVvXS6UN8BgtvwLW1biHnE9359pZvqyRSyChJcrA3%2BOPtQIBstLC6joI9wgmHVWUt4KrMi%2BmME39fzoHWVdTLJjuD%2FDKLaDXOUI0GYi75pVxiNwWbPItgQhstQfgC%2FMozTEJwm3kLMdFVRKZkps7CqYz4sAERVAo3lhVZ9nSqG4f2LYqdw1MlRagM4RWjwiNFA0IlT%2FPYhBSAzmE1rR8dju3S7FQtdiauHn2ymmphZULqIudU%2FPgQhyeVyVJrU7uyuLdjWVlh1p73%2FDrYmkMrhLh7Ygc6mKAj2a5PnVXYtOh3UVK8YSwPm%2BvTWITNv%2BkUDCW6Fn%2FBDF04fsgEn%2FU879%2BDF14yO1QuF2iVxtO1sUc8NV7OOA9VtK1gBXX4rWHBaepj94MIErlKGUf5pPNINifPgYtIqjFqDu%2FwrGPyGu0kYM9lpiWPf0iJvGD6vc1mzvAerWZTPA4e3hgorHZ3bTkNidfJO3zCZeiuKqnbqzRAMHZ4ldG8EEnuW9KA%2B9jB%2BS0K%2Bf7P%2BPenSGHV86grie%2Foqafw1opijQ347ABp%2FJ0bmqG9SM1SFoln5yjX10%2FRgZGAdtf9JnodD0w58KzzQY6pgFl0a3NTr0qhDu4fRt%2F%2FARiNtL%2B4xGUkPzejvPjyrq%2F7ynSmzjAQ8%2FuTbJ6xbrYUwZolmixkNZe9ZYDDwImQs8w3gXplCyuvB3cNDYK9Au6CLeegpmYJ7xoZ7OXEn2W32YbRna613ZzjoWDOBQsS5fjSMrb7MCaREBz8ppGc318KAcj2h1UnAPXrCljk4hgZ%2B5wQc6WDmpuPcgJcfXAfxDR5b%2B6soPi&X-Amz-Signature=a9ed8e3e5e1f6e88edb4c1750a7322ce581cfb093f887e30efa12f80c7924ca8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV5U22HE%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIGGjc%2B3Vah%2BwQkb32Z%2FgPn9f%2BwPpQwWGP0W2O4LaiXw9AiAHqU8HU6lwT1tK4js2JlV39W7Uor4mIdqPRAxO8XAvkyr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIME%2B5XvdD4GGOTKjplKtwDIbaIUrUGIvNl%2BrHOuqhiOUEqV2FtsO0CRL%2FT9HITJLHKyVvXS6UN8BgtvwLW1biHnE9359pZvqyRSyChJcrA3%2BOPtQIBstLC6joI9wgmHVWUt4KrMi%2BmME39fzoHWVdTLJjuD%2FDKLaDXOUI0GYi75pVxiNwWbPItgQhstQfgC%2FMozTEJwm3kLMdFVRKZkps7CqYz4sAERVAo3lhVZ9nSqG4f2LYqdw1MlRagM4RWjwiNFA0IlT%2FPYhBSAzmE1rR8dju3S7FQtdiauHn2ymmphZULqIudU%2FPgQhyeVyVJrU7uyuLdjWVlh1p73%2FDrYmkMrhLh7Ygc6mKAj2a5PnVXYtOh3UVK8YSwPm%2BvTWITNv%2BkUDCW6Fn%2FBDF04fsgEn%2FU879%2BDF14yO1QuF2iVxtO1sUc8NV7OOA9VtK1gBXX4rWHBaepj94MIErlKGUf5pPNINifPgYtIqjFqDu%2FwrGPyGu0kYM9lpiWPf0iJvGD6vc1mzvAerWZTPA4e3hgorHZ3bTkNidfJO3zCZeiuKqnbqzRAMHZ4ldG8EEnuW9KA%2B9jB%2BS0K%2Bf7P%2BPenSGHV86grie%2Foqafw1opijQ347ABp%2FJ0bmqG9SM1SFoln5yjX10%2FRgZGAdtf9JnodD0w58KzzQY6pgFl0a3NTr0qhDu4fRt%2F%2FARiNtL%2B4xGUkPzejvPjyrq%2F7ynSmzjAQ8%2FuTbJ6xbrYUwZolmixkNZe9ZYDDwImQs8w3gXplCyuvB3cNDYK9Au6CLeegpmYJ7xoZ7OXEn2W32YbRna613ZzjoWDOBQsS5fjSMrb7MCaREBz8ppGc318KAcj2h1UnAPXrCljk4hgZ%2B5wQc6WDmpuPcgJcfXAfxDR5b%2B6soPi&X-Amz-Signature=75783dd05398b964f5fbebdc77cbf3014486c107be6a5e63ec2dc0fc0f114002&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


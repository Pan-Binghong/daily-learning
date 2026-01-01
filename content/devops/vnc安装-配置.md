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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE4SKECR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIByb0UXHtrnm444W0F4EMC8vAF1bfpJa6zdon5ccfQGqAiEA%2BQH1DasXPGSSw2P8rQHYYElhsEGhodAODHvsCbRltYYqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgOB9WfT3oZ6w8UayrcA%2F%2BxL7pdBS8DYTRzSQQe14VZ%2FdZrx1mut0B5iuibkTgmPuVnGaWFXh3MEk%2BIk6CRDjp4hnT3Ftbn1F%2B%2BkGnsrnfIdh0Dj2BFPae%2FUovJ4GhEgOGaXBk1KMOSOO9rQXhhQk9mMcAbQNVYclojJo6rXHp3lB243NFM%2BZJQ5LByQJgWJYSZoAUSpFddGBkC1Zt4pBJXV%2FJqAnvHkLG%2FnbYmcyJ0r3swuEIyqkq%2FL3NtQlRohTgCJjJAt%2FCTzr2WG0KOtUCy%2BxTIkIi4hA53hlDocrf9U2VGGjYsvyf1GECp4mjVzlPK2dwKHqRiPqKrOCz%2F8x2G4UtbozW3mo9h6dMP%2Bcxf8x9s%2FF8kThxt3vYcrHLhAfEw9dgKcUBBCuAuI%2FuZHq8whMnTR5RKbLIBPx%2F7dvXXLEkrxdjH33h2WsXiN45BB5wAMSLPS73PHeOdKQYHI2s48nzPdNy%2Fz%2BVmu%2FxSLc6632BPI54Z7fVrCHyjXw99PN6E6I3%2BwAMaZVW0VZ3TIlY7oitMgnPIQaUcKdbWfM0mEjHnpvjhVCzsttER9EhJUILfekDSRB%2BLvwtKyFzHJv2QOSq3%2BQjouqraXaPjzjrnHyiipdCo%2Ft0mlFgLYg8%2F2wfwgMEDIheMO%2B51MMmi18oGOqUBalmqZNKDg636uCmrMU29iLMpnoBN3s2dKIC3RB0r1PKS48mvrecRuDWu5JeueXKPrISZMB3UHmwW1%2FH4K763fckpS3wKbiy1KrGe2XU7paqxZNAAu7xLj2l67EuSPUNDEGuMITUcTYYndcds3pOmS6Vx7QLr2Ik8EMtAQzAUm2xJRj07a6ftEEa59UO3pb1SkAZWXy4PA0ZrPE1gToHc2FkOCO0m&X-Amz-Signature=3916a7bc334b4fb70a9856aefe8a57a2ec5e87e6877d3b80ed372ca896c63c47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE4SKECR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIByb0UXHtrnm444W0F4EMC8vAF1bfpJa6zdon5ccfQGqAiEA%2BQH1DasXPGSSw2P8rQHYYElhsEGhodAODHvsCbRltYYqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDgOB9WfT3oZ6w8UayrcA%2F%2BxL7pdBS8DYTRzSQQe14VZ%2FdZrx1mut0B5iuibkTgmPuVnGaWFXh3MEk%2BIk6CRDjp4hnT3Ftbn1F%2B%2BkGnsrnfIdh0Dj2BFPae%2FUovJ4GhEgOGaXBk1KMOSOO9rQXhhQk9mMcAbQNVYclojJo6rXHp3lB243NFM%2BZJQ5LByQJgWJYSZoAUSpFddGBkC1Zt4pBJXV%2FJqAnvHkLG%2FnbYmcyJ0r3swuEIyqkq%2FL3NtQlRohTgCJjJAt%2FCTzr2WG0KOtUCy%2BxTIkIi4hA53hlDocrf9U2VGGjYsvyf1GECp4mjVzlPK2dwKHqRiPqKrOCz%2F8x2G4UtbozW3mo9h6dMP%2Bcxf8x9s%2FF8kThxt3vYcrHLhAfEw9dgKcUBBCuAuI%2FuZHq8whMnTR5RKbLIBPx%2F7dvXXLEkrxdjH33h2WsXiN45BB5wAMSLPS73PHeOdKQYHI2s48nzPdNy%2Fz%2BVmu%2FxSLc6632BPI54Z7fVrCHyjXw99PN6E6I3%2BwAMaZVW0VZ3TIlY7oitMgnPIQaUcKdbWfM0mEjHnpvjhVCzsttER9EhJUILfekDSRB%2BLvwtKyFzHJv2QOSq3%2BQjouqraXaPjzjrnHyiipdCo%2Ft0mlFgLYg8%2F2wfwgMEDIheMO%2B51MMmi18oGOqUBalmqZNKDg636uCmrMU29iLMpnoBN3s2dKIC3RB0r1PKS48mvrecRuDWu5JeueXKPrISZMB3UHmwW1%2FH4K763fckpS3wKbiy1KrGe2XU7paqxZNAAu7xLj2l67EuSPUNDEGuMITUcTYYndcds3pOmS6Vx7QLr2Ik8EMtAQzAUm2xJRj07a6ftEEa59UO3pb1SkAZWXy4PA0ZrPE1gToHc2FkOCO0m&X-Amz-Signature=8e997be54d7fecda895130725e4b5b8b2de0c2035c670bee34979ca376b931c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


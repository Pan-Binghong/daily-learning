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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF2WXKT%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCICtUCwj2%2FGfEb8lwon18L58zglWojRf6W1FbAzedR8t0AiEA8u2gxMwmrSXqY1f%2Bq6LlD%2BL5QPcak2Z%2BLCtOArXrBw0q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDPKh54c9u6DfysWRhCrcAy2b3GoPOz7CGMtLhmpJHu9Bz1NlEY8FYFWahkgAJyUf4CXe4DP%2BE8uyLF48iKtWpHaFTlZfXkFQAadvkx0rqTbYSWEMiGlX%2FQUVHBTw4EGZwLtj%2BJvXAjZw9NIrtNNwoOoT6c56EUa4dGI0A%2BVlpsLXnVJoxkRH6F2Fkx2wmT947a9aM7d0M5k%2F0cGhYpxAl%2FfGhrxYqibvi0nI3BXlW1kw%2BNe86Qlj4HSNAPFZT5gL8HoAFBgF788ywDU7PxDsl6TUL0GYNeoW%2BWA4iVPvdK6nNtixBL5ChPhgzCjyvv9E2ZFLYIxjWGc2WZDwKdDKB1jkfbFnfOPtKhPhqTBHdgMJRIb95nXKguKlPU2uqz26g%2Bmb7dPl1CLepwaLzcohnmqlc77on%2FsbidaoB0NgMQL0wAJf5wwQRwSH0LsWBaF6a7Tiri1KXy0G2%2F%2BYXzSs29UPuvKxmzmKICh9QkQgDb3eSQlMH1C3YuWnygCVrtwumZSB3TfumWtPuxsvYsPmYBh%2FQ58Cre3cNzbkS13uRmwLF30sxnybSSe6Z7rYTjVO%2Bk9lpmmDRbIJkFuzqDDaFLgkbK1OnaCK1Vf067GlDDUVimcmkY%2FJVl0Yt2aqHMcUUMFSrlUjJFEAELlcMIm%2FpssGOqUBRVWFi0L%2FTviZ4J%2B%2BOjb5sk5aUFHcPDSdJwaUvtcKBMXVXTIJkUc0iFosm4QBs26HRa7USlGb4oD0MktFqFIvvD1MBpix9Hcxof7ophGu3idi1tC7c%2FexIN5A7kr7vGx7Fb59eBXNq%2Ft5lo1pUCvDST8P4oa4nw%2FO5Gg%2BxCw87N0OQQD5Ou3drXX6NhBTY2v5mjezcucUmNjmgGNURtW%2F2m4r7AoI&X-Amz-Signature=5f75782ca50f84c02fcf5e02f567dfa4be2394cc8d74c8d86d0c6af12b327cf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAF2WXKT%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCICtUCwj2%2FGfEb8lwon18L58zglWojRf6W1FbAzedR8t0AiEA8u2gxMwmrSXqY1f%2Bq6LlD%2BL5QPcak2Z%2BLCtOArXrBw0q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDPKh54c9u6DfysWRhCrcAy2b3GoPOz7CGMtLhmpJHu9Bz1NlEY8FYFWahkgAJyUf4CXe4DP%2BE8uyLF48iKtWpHaFTlZfXkFQAadvkx0rqTbYSWEMiGlX%2FQUVHBTw4EGZwLtj%2BJvXAjZw9NIrtNNwoOoT6c56EUa4dGI0A%2BVlpsLXnVJoxkRH6F2Fkx2wmT947a9aM7d0M5k%2F0cGhYpxAl%2FfGhrxYqibvi0nI3BXlW1kw%2BNe86Qlj4HSNAPFZT5gL8HoAFBgF788ywDU7PxDsl6TUL0GYNeoW%2BWA4iVPvdK6nNtixBL5ChPhgzCjyvv9E2ZFLYIxjWGc2WZDwKdDKB1jkfbFnfOPtKhPhqTBHdgMJRIb95nXKguKlPU2uqz26g%2Bmb7dPl1CLepwaLzcohnmqlc77on%2FsbidaoB0NgMQL0wAJf5wwQRwSH0LsWBaF6a7Tiri1KXy0G2%2F%2BYXzSs29UPuvKxmzmKICh9QkQgDb3eSQlMH1C3YuWnygCVrtwumZSB3TfumWtPuxsvYsPmYBh%2FQ58Cre3cNzbkS13uRmwLF30sxnybSSe6Z7rYTjVO%2Bk9lpmmDRbIJkFuzqDDaFLgkbK1OnaCK1Vf067GlDDUVimcmkY%2FJVl0Yt2aqHMcUUMFSrlUjJFEAELlcMIm%2FpssGOqUBRVWFi0L%2FTviZ4J%2B%2BOjb5sk5aUFHcPDSdJwaUvtcKBMXVXTIJkUc0iFosm4QBs26HRa7USlGb4oD0MktFqFIvvD1MBpix9Hcxof7ophGu3idi1tC7c%2FexIN5A7kr7vGx7Fb59eBXNq%2Ft5lo1pUCvDST8P4oa4nw%2FO5Gg%2BxCw87N0OQQD5Ou3drXX6NhBTY2v5mjezcucUmNjmgGNURtW%2F2m4r7AoI&X-Amz-Signature=86f02d850b93e13e86436ba70fc2476ddcd06a114e2e5d48736710165350b141&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


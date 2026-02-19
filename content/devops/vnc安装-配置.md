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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYELGF6M%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmxPrtPamx8QZwKeV5ULYRSIjihFMn7EdZN9vQORqoRQIgfVcqFs3p7rKJVzLoTmkbTFMtiVfvfQh%2B6z5G3MNei1sq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDKYUDE2A9OBsvm3bACrcA%2FNEWpj1bI7PlApyFcOutlgumqUR23qSAbOc3zgxDNDKcpgjdoVHiAKZDSaqrWdQKyi8bWdibrcyKmRqm709xy1TM%2FJbgPTLI2u%2F6GBlZsc10kwVwXhiNZoqZSSchlW4W00IbUEY0bTuicT8TiThPMmG2NTBqLaENgAqxn3iO%2BHZMCSovFklXbpJEj13OrFZxZLbjS0F3ywTNAAyITevbFl9ssGMeDlmkJPeKn9PGkhKPEK2ootF3PvtD%2BGY%2BCqAHpKPi19z2GD4Wk82byoNB3rYssy09xSxFOgj8uQ5HCONxN6dewiHSuq%2FH5JBNxwp324LDfX97SqWt2dI3zTBeNTY1wbOtwWpTKfRHcUW%2FFoOptJ2lP2%2BgDksgkCWWS%2FBrN0oN%2FDdX5fEnBjbFy2fv%2FmagbNLhajvrmjRSUPg%2BLI1eu3m8bTAfGMmgS0Qr8AfOEBV9R3TVxXFZKZL%2B82Yp2NAw3Bxrn0KYLsXGVDhHCyDepFm00p68WhxFiUzDfV6%2By6O3E88dsdK92tl1TIkSe6ftcQB6XHOPUJ8FE5zkoKCpwPEZ5TkA%2B1rmwdOLizVc%2BKJPXxL%2BYQYi2HRWYLx1m3WiN4YXw96y%2B308u9t4uqoQ6udE%2FPmwmOrG55LMLbx2cwGOqUBsGjEyqb8QrmJnLGC9QQHBwPwftePVczUekKpWAGfqU43qZZ9ZkBXLkD0iCGsaHiCNiJvAFTnsOa1AZ1KpHQeoqdomjHWQ%2BUdmjkZzyeIQOGZWgM4y2QG2vzxZv1z%2BL2oU%2FJQ4O%2BwzRTkE1DwhcVGafystuJE8HtAKsCmGPr4Elg1SvEXrIPhNOTG7PXGt2nXfBJyhZDM%2BZeYZ9uYNmwnG6g9Mnoz&X-Amz-Signature=3742a54c1e77bd1f9dc585a7910982f9e61e514413339ae6250e8765c9a32c6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYELGF6M%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmxPrtPamx8QZwKeV5ULYRSIjihFMn7EdZN9vQORqoRQIgfVcqFs3p7rKJVzLoTmkbTFMtiVfvfQh%2B6z5G3MNei1sq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDKYUDE2A9OBsvm3bACrcA%2FNEWpj1bI7PlApyFcOutlgumqUR23qSAbOc3zgxDNDKcpgjdoVHiAKZDSaqrWdQKyi8bWdibrcyKmRqm709xy1TM%2FJbgPTLI2u%2F6GBlZsc10kwVwXhiNZoqZSSchlW4W00IbUEY0bTuicT8TiThPMmG2NTBqLaENgAqxn3iO%2BHZMCSovFklXbpJEj13OrFZxZLbjS0F3ywTNAAyITevbFl9ssGMeDlmkJPeKn9PGkhKPEK2ootF3PvtD%2BGY%2BCqAHpKPi19z2GD4Wk82byoNB3rYssy09xSxFOgj8uQ5HCONxN6dewiHSuq%2FH5JBNxwp324LDfX97SqWt2dI3zTBeNTY1wbOtwWpTKfRHcUW%2FFoOptJ2lP2%2BgDksgkCWWS%2FBrN0oN%2FDdX5fEnBjbFy2fv%2FmagbNLhajvrmjRSUPg%2BLI1eu3m8bTAfGMmgS0Qr8AfOEBV9R3TVxXFZKZL%2B82Yp2NAw3Bxrn0KYLsXGVDhHCyDepFm00p68WhxFiUzDfV6%2By6O3E88dsdK92tl1TIkSe6ftcQB6XHOPUJ8FE5zkoKCpwPEZ5TkA%2B1rmwdOLizVc%2BKJPXxL%2BYQYi2HRWYLx1m3WiN4YXw96y%2B308u9t4uqoQ6udE%2FPmwmOrG55LMLbx2cwGOqUBsGjEyqb8QrmJnLGC9QQHBwPwftePVczUekKpWAGfqU43qZZ9ZkBXLkD0iCGsaHiCNiJvAFTnsOa1AZ1KpHQeoqdomjHWQ%2BUdmjkZzyeIQOGZWgM4y2QG2vzxZv1z%2BL2oU%2FJQ4O%2BwzRTkE1DwhcVGafystuJE8HtAKsCmGPr4Elg1SvEXrIPhNOTG7PXGt2nXfBJyhZDM%2BZeYZ9uYNmwnG6g9Mnoz&X-Amz-Signature=f44a2273c2047c41d6fd7db58bc7cf32e9cd74a92e79acab6edf31af9d6fb2b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


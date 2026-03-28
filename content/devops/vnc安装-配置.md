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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V27G53SN%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCICQbKZ6DZkd4sJiaXzo8OE6OeGYvnjaVuyScaUyUpb0yAiEArZS4LsIT6BstAHWbHSa9RUbZ81JI87OpqIhPfZTxsD4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIxW0DRGZu0LQ6gcaCrcA%2B3dP8LeU2Y%2BWwoKZ6kPr1HNhcocHmL%2FFqiFGbEhwC1zGA%2BkPE6SpLSfusRWDgo9Nz2Yu6%2BWW%2FqEhrD9DGRgNMRfZrg86IfzPsB4vUsvTmlmCtG9CpAP6UbPGAfmOb2bDBonBXERSVNvzhrmtPrxdsB6RMNtO7pgt9TWiZ5c3qRs32%2B5tG8%2FZNvnDLcql2b01LKleWErGQ5yF0AkbY8o9ZSx2141VXiTajjRzbqWT0R6ZFTpRQExN0%2FmCLC5ifGrQ01DWGx3rh9ybzvo9uWrUy7s%2Bw0Qa0IIpXP%2BLzaeal0bwYkRzXAkcz%2BTSmghxrCM2uxgG0ZLH7mYr0FYFzGrIaoduC1rVIoyzqOpXKLZ4OchstTXlx%2FDVUEFuqvReuH2jHsl1CcUzEd1ILSQICMJJNrZAUN0Bdu8A77z98F3r0wZdOKZB3HizYqTB1EHIuRqIZCiH7DqUAJxK%2BzAWObTkkstAkMGne0qxJVtPq%2FpaEuO1eRncrgx6gDrusn4gPycWjNBhe8s3JkI1MK0BaLwyDCik8i%2Fivef%2F%2FV404Ig5nq6BE%2FbzVMF8ti%2FQUGf7zhOz8gtZs2vKcaQsYYdJPLEUTfwV8wq9tyCou0WC1YlfRHz7p%2F69KBO3CbXwFPbMLPsnM4GOqUBa%2BcYBAONkni4R2X%2BnAgnBDiw0bS91rQp8TDDSRTmE%2BQ0i7plng%2Bz9NqmVtlYcLHRb68kgCGRJsuaWde5fBvIsjjfzkqhovMIFdkaY1YxuPa22TMWe1Z0aS2p7tXyrmhb53A%2BLf71YetCWazPjR%2BaKzn0UZq2yIh7YGsPyHDPvJpftMlWKpMpgmkhWsHOnFswsuzG7PfUdIp2rEwC4juvqXI44vtF&X-Amz-Signature=043685fed9af2fe5c192842c97236569b51d5015ccb9ec3383fbf975ad087232&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V27G53SN%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCICQbKZ6DZkd4sJiaXzo8OE6OeGYvnjaVuyScaUyUpb0yAiEArZS4LsIT6BstAHWbHSa9RUbZ81JI87OpqIhPfZTxsD4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIxW0DRGZu0LQ6gcaCrcA%2B3dP8LeU2Y%2BWwoKZ6kPr1HNhcocHmL%2FFqiFGbEhwC1zGA%2BkPE6SpLSfusRWDgo9Nz2Yu6%2BWW%2FqEhrD9DGRgNMRfZrg86IfzPsB4vUsvTmlmCtG9CpAP6UbPGAfmOb2bDBonBXERSVNvzhrmtPrxdsB6RMNtO7pgt9TWiZ5c3qRs32%2B5tG8%2FZNvnDLcql2b01LKleWErGQ5yF0AkbY8o9ZSx2141VXiTajjRzbqWT0R6ZFTpRQExN0%2FmCLC5ifGrQ01DWGx3rh9ybzvo9uWrUy7s%2Bw0Qa0IIpXP%2BLzaeal0bwYkRzXAkcz%2BTSmghxrCM2uxgG0ZLH7mYr0FYFzGrIaoduC1rVIoyzqOpXKLZ4OchstTXlx%2FDVUEFuqvReuH2jHsl1CcUzEd1ILSQICMJJNrZAUN0Bdu8A77z98F3r0wZdOKZB3HizYqTB1EHIuRqIZCiH7DqUAJxK%2BzAWObTkkstAkMGne0qxJVtPq%2FpaEuO1eRncrgx6gDrusn4gPycWjNBhe8s3JkI1MK0BaLwyDCik8i%2Fivef%2F%2FV404Ig5nq6BE%2FbzVMF8ti%2FQUGf7zhOz8gtZs2vKcaQsYYdJPLEUTfwV8wq9tyCou0WC1YlfRHz7p%2F69KBO3CbXwFPbMLPsnM4GOqUBa%2BcYBAONkni4R2X%2BnAgnBDiw0bS91rQp8TDDSRTmE%2BQ0i7plng%2Bz9NqmVtlYcLHRb68kgCGRJsuaWde5fBvIsjjfzkqhovMIFdkaY1YxuPa22TMWe1Z0aS2p7tXyrmhb53A%2BLf71YetCWazPjR%2BaKzn0UZq2yIh7YGsPyHDPvJpftMlWKpMpgmkhWsHOnFswsuzG7PfUdIp2rEwC4juvqXI44vtF&X-Amz-Signature=a2ad1bf63132402dcc11c2f3c5859b7e803fc3dcf50a88e3a471836462a6ff44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


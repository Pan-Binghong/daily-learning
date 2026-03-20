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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEB66JER%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIET%2FGLdYF5aVU9vxdi80QtnnGanZSdExfIsi4%2Bc0XMPyAiEA72%2BUYBdxHTxD5lwto1lRNpbONqW0oFydz5EtlQBh6iwq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDIcq5uJ%2BQef%2FmArAxCrcA9%2Bw5Gvzh4lgDk6t5%2BX5GTknLPaJwS%2FRtR6HrCK57fh71QHRSUbjxseyxEvxa8eBYeyzp%2FKlSA%2BqX1HnxfUxmrG%2Fao4Jzd4NDMznXiUN8iyOAnV7iVNWwW3xQRkhxLkWVsvfTI7kmPJ9ztRAsxe74o9Y75CPVyLRgjHxTshK57OwTIb03%2BUpHWYg29GQcDNr%2FpNPW80EhWik1q7KFkGUEqpT5gCUD0eTxNCu%2F%2FL%2FDEDd6b3Y8IKN5Y88Z1b9xXzttv%2B1THMLhcAwB7n9G5Cf8mQ1sb0pwx75Yzd4wBvnNXfvjWp52ZWrw5DLDDmkDMXJlrCrOl6%2FhU1%2BTSB3mVTzRK4XjrBzpLargIR7lJN%2BAykAosTER9ZUXA%2FHX3Glo8223VwzpwGldndvsvSy%2FzIiD5AugtrYgcIud90xpu1amJq7xzLp%2FeC74wV4wLqjhLzEIyHnDUh1%2BZbuimG%2F32Vb7pRzacKqDmdNh34jHzekiTkuk45rxB4S9ooFDRiXE%2B35wsaokKK2ozCDabn1gAlbN7oppPkcfQdNyqdNBh3oC7Mb7kwdI6sp9Y5%2FvyspQTDwss2AjWtSB%2BvpHfGwxgaasiYJhJa4wKPNLMqvWj3awwVGmrVIfEDP1qwMm%2Fz6MMi38s0GOqUBcsBLT8ezJuvkEVXg4t3vAbPkEBBtVDtTwm2oZ38H9xH8lrnndxGULdC8%2FrH4XpS9Dq2L7qDctQn3h1mrpSo64HHZ9Uu40%2FpCM%2BHScbBRRv1h1KgcBFTL69Ym4QJkszi%2BTSYrDW7Nby%2FD91N5aLsrwFgvY1r9z%2Ba%2BBzcg3vJ38nFtJebLiO1NZ6sD78K7NYPjZDtzvJIkuDd2%2FiCtMDHzYVoCwHmW&X-Amz-Signature=2474a5b8820173377ad29803c4e64052c64b0f0105a44add6b04248e2284566d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEB66JER%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIET%2FGLdYF5aVU9vxdi80QtnnGanZSdExfIsi4%2Bc0XMPyAiEA72%2BUYBdxHTxD5lwto1lRNpbONqW0oFydz5EtlQBh6iwq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDIcq5uJ%2BQef%2FmArAxCrcA9%2Bw5Gvzh4lgDk6t5%2BX5GTknLPaJwS%2FRtR6HrCK57fh71QHRSUbjxseyxEvxa8eBYeyzp%2FKlSA%2BqX1HnxfUxmrG%2Fao4Jzd4NDMznXiUN8iyOAnV7iVNWwW3xQRkhxLkWVsvfTI7kmPJ9ztRAsxe74o9Y75CPVyLRgjHxTshK57OwTIb03%2BUpHWYg29GQcDNr%2FpNPW80EhWik1q7KFkGUEqpT5gCUD0eTxNCu%2F%2FL%2FDEDd6b3Y8IKN5Y88Z1b9xXzttv%2B1THMLhcAwB7n9G5Cf8mQ1sb0pwx75Yzd4wBvnNXfvjWp52ZWrw5DLDDmkDMXJlrCrOl6%2FhU1%2BTSB3mVTzRK4XjrBzpLargIR7lJN%2BAykAosTER9ZUXA%2FHX3Glo8223VwzpwGldndvsvSy%2FzIiD5AugtrYgcIud90xpu1amJq7xzLp%2FeC74wV4wLqjhLzEIyHnDUh1%2BZbuimG%2F32Vb7pRzacKqDmdNh34jHzekiTkuk45rxB4S9ooFDRiXE%2B35wsaokKK2ozCDabn1gAlbN7oppPkcfQdNyqdNBh3oC7Mb7kwdI6sp9Y5%2FvyspQTDwss2AjWtSB%2BvpHfGwxgaasiYJhJa4wKPNLMqvWj3awwVGmrVIfEDP1qwMm%2Fz6MMi38s0GOqUBcsBLT8ezJuvkEVXg4t3vAbPkEBBtVDtTwm2oZ38H9xH8lrnndxGULdC8%2FrH4XpS9Dq2L7qDctQn3h1mrpSo64HHZ9Uu40%2FpCM%2BHScbBRRv1h1KgcBFTL69Ym4QJkszi%2BTSYrDW7Nby%2FD91N5aLsrwFgvY1r9z%2Ba%2BBzcg3vJ38nFtJebLiO1NZ6sD78K7NYPjZDtzvJIkuDd2%2FiCtMDHzYVoCwHmW&X-Amz-Signature=9f4098e15e75574120926ae4286460a5c8f42de224ed7167f4986065c62cdd0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U44NWC6%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtOemwS%2BDJRilvdWsYvqwerlUqcUBXaARPTtxd4L%2Be4AiEAyYbLNxvCaTJhEwf%2Fc9upowPwkzllBMWZZkgFT0jgiIQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDCIaS1NDUkwSKaKHryrcA1QlUlH%2BJimiWy5BDWDH7Z76F%2F3rdyyUztBEBwL%2Fy%2BUQGuPRj8%2BKScXHM4Ki%2BgKpIe9QfoeIKiHPWG%2FRS9axizLRRMEGF5IElXZ%2FwBfkJv2NpMxiNqpC%2FK7U3%2Fiq%2FnZxKNeMt6iJgD0kpimXSbtoBMlHxypk3J9joT6dZAA6fiOXb6N%2FH3tWIakKWQWEXemFCSa4ppNjXboQ0rD5o8bRreeGrwQbaIXUtkAf7WcK27QaI7UVlrJ74N85JrL0FMaaUS8xJgCaKPhB19aNp3kqNY%2BywuNrp%2FVUiH9o%2B%2B8O3DYL%2BxDofCTFiIiLRehH705IPH2JHtcZmQhlsgqF7TU7xv7mfRinKW7%2B0ZnHf71xY%2B1ZxVnm1aVycc%2FdyEv%2BTQL%2BxBacnGn6%2FCQV8%2Bb4vHF4pyN8tdmhV4DfxuWhmw4%2Bk581VOGNXhTVvLjhMENo1fALWkCLM5QSN1vYIvfxcsYib%2FvAluV%2FQ5Ht8uVLo51zJ%2FIZWld6I7syEFNPhG8RD4eUoNTMTxGPFO1a5%2BLBp9fCwd3qk9x1cExy8YUol1vOl3Lj75F%2Bgofjw8X8CMITyp4fDScS8U%2FemfKNDhiR1GxbhhklMQeBHE9EJYfHwhNTY3wvDxi%2BSHEHeufv6JQvMJWWic0GOqUBeDHpGuEaZ0rqbY0HTxL6VU1SdbONZgM1ZLrS9wtaSpPIbbpI7siRzHqvAdIR2vmGxcrtMTgdegWv9uGb7w9P%2FAw5pOA5%2F2TYLok8CiV339z2tPjuSHy1ued1sVyCaKdw13XsWMK5%2By9O3KHWuDK9Dhc9qF%2B947FVef%2Ftsvwl0mvoXk%2BByYgJF9LcF5VFY3JeMmpDaW68ZLRJGNILo2PlKvueOkGo&X-Amz-Signature=4f916533d61cc734cb2f899530af2b99e2a29eb82083a377b9f66e8d2bb97c99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U44NWC6%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtOemwS%2BDJRilvdWsYvqwerlUqcUBXaARPTtxd4L%2Be4AiEAyYbLNxvCaTJhEwf%2Fc9upowPwkzllBMWZZkgFT0jgiIQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDCIaS1NDUkwSKaKHryrcA1QlUlH%2BJimiWy5BDWDH7Z76F%2F3rdyyUztBEBwL%2Fy%2BUQGuPRj8%2BKScXHM4Ki%2BgKpIe9QfoeIKiHPWG%2FRS9axizLRRMEGF5IElXZ%2FwBfkJv2NpMxiNqpC%2FK7U3%2Fiq%2FnZxKNeMt6iJgD0kpimXSbtoBMlHxypk3J9joT6dZAA6fiOXb6N%2FH3tWIakKWQWEXemFCSa4ppNjXboQ0rD5o8bRreeGrwQbaIXUtkAf7WcK27QaI7UVlrJ74N85JrL0FMaaUS8xJgCaKPhB19aNp3kqNY%2BywuNrp%2FVUiH9o%2B%2B8O3DYL%2BxDofCTFiIiLRehH705IPH2JHtcZmQhlsgqF7TU7xv7mfRinKW7%2B0ZnHf71xY%2B1ZxVnm1aVycc%2FdyEv%2BTQL%2BxBacnGn6%2FCQV8%2Bb4vHF4pyN8tdmhV4DfxuWhmw4%2Bk581VOGNXhTVvLjhMENo1fALWkCLM5QSN1vYIvfxcsYib%2FvAluV%2FQ5Ht8uVLo51zJ%2FIZWld6I7syEFNPhG8RD4eUoNTMTxGPFO1a5%2BLBp9fCwd3qk9x1cExy8YUol1vOl3Lj75F%2Bgofjw8X8CMITyp4fDScS8U%2FemfKNDhiR1GxbhhklMQeBHE9EJYfHwhNTY3wvDxi%2BSHEHeufv6JQvMJWWic0GOqUBeDHpGuEaZ0rqbY0HTxL6VU1SdbONZgM1ZLrS9wtaSpPIbbpI7siRzHqvAdIR2vmGxcrtMTgdegWv9uGb7w9P%2FAw5pOA5%2F2TYLok8CiV339z2tPjuSHy1ued1sVyCaKdw13XsWMK5%2By9O3KHWuDK9Dhc9qF%2B947FVef%2Ftsvwl0mvoXk%2BByYgJF9LcF5VFY3JeMmpDaW68ZLRJGNILo2PlKvueOkGo&X-Amz-Signature=3f1fb7e21fbb143f9c8aed2e6c7f9bccc270758aaf4ff43d1745595f4ace0465&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


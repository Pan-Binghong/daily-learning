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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS7QTIRJ%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGe9h5aMC773mV%2FTuhiX4HkSYqJUt%2FvtR43qX%2Bk7uMf7AiEAinq0Fgugk5SJ2s8OX54ZKuEuLfgrdQcHft2L22b5AcYqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCylu8ss6J1wckO0PCrcA24DGufQuFZ8yyCTR%2FlHl%2BaddS%2FwRuFLlD2ndu1VFROq5tNITPyhYy%2FwjGw3lU7jSXoz5%2BjiBdFk7g2k7TyYKVVqOl6bhNrCRpOm0p0LhAKD0pxEuJNCBSqS3hq40ys8eIo9o8%2FLehLLj1LLRZY%2BshNKwvU3OKOURyUJFVFSt0Hht9%2Bb6VO%2FV8hB6BVCN1HW5wWOIMBGJU6A7%2FECVoTHVqU8b1E2yPCcmgvBv0sRA9Nokpy1ZyCSTwAE2fbuNmrc3fLQ0fgxskz7bEa71HEZlM6pEPIQkE241hf89mLbWolTPO2Dhvhcujn52NC%2BgEa9nFTBQj9DgquBqC%2BDriyn9aG4CiIzuVthQGuVjvmzT3Kn84sGl3e%2FiXtHkpi0oRghfaPzWWl70o4eHOl4KRlnnRlt4D7nan6hNxZkWHzRV879ph7tjRHEQqI1WUnh4qhEZIrY57o94Ul5g0idsG0Np5dSwYtnbzyot8tNeIUZwg8EOGJkawYpSObNxOfoIeVep3aam%2FIFZMTaeBOFv%2BJCMn%2F%2FpnE7YdHcek%2Fy5VYoyU6hPA8uLVJ6k6W13AmpKFCkoqFLDm6%2F2soFsiNk5tB3q2zG7F%2BLX6fg6ZdV8ppPjHgha2nSk2elhDkalgyMMNv5hssGOqUBef5Go9e2CDVDYPM7dvpTl7LpmlgSPuzIpMx%2FN1MAH50cw9wWNwxdLrmrk2bw0Wn6tCPwHDtemdo5phDZH9TuRY1elL2AoIVWbPsw9LiAJn241acdPGXX5z5gC6dnpVne6GreWNArWtAtMNveGgYtZNkpomQryO%2F4wHx9Q4%2F2nYWtVlrYHjU24cB9bkHLDTw8Q0HJD2mYymxc%2BBqzBvF%2F5u0nIkZY&X-Amz-Signature=248769303d2614fc1ab709c8cd21e19afcd81c4e091f04e83db705ca3bcc13e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS7QTIRJ%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGe9h5aMC773mV%2FTuhiX4HkSYqJUt%2FvtR43qX%2Bk7uMf7AiEAinq0Fgugk5SJ2s8OX54ZKuEuLfgrdQcHft2L22b5AcYqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCylu8ss6J1wckO0PCrcA24DGufQuFZ8yyCTR%2FlHl%2BaddS%2FwRuFLlD2ndu1VFROq5tNITPyhYy%2FwjGw3lU7jSXoz5%2BjiBdFk7g2k7TyYKVVqOl6bhNrCRpOm0p0LhAKD0pxEuJNCBSqS3hq40ys8eIo9o8%2FLehLLj1LLRZY%2BshNKwvU3OKOURyUJFVFSt0Hht9%2Bb6VO%2FV8hB6BVCN1HW5wWOIMBGJU6A7%2FECVoTHVqU8b1E2yPCcmgvBv0sRA9Nokpy1ZyCSTwAE2fbuNmrc3fLQ0fgxskz7bEa71HEZlM6pEPIQkE241hf89mLbWolTPO2Dhvhcujn52NC%2BgEa9nFTBQj9DgquBqC%2BDriyn9aG4CiIzuVthQGuVjvmzT3Kn84sGl3e%2FiXtHkpi0oRghfaPzWWl70o4eHOl4KRlnnRlt4D7nan6hNxZkWHzRV879ph7tjRHEQqI1WUnh4qhEZIrY57o94Ul5g0idsG0Np5dSwYtnbzyot8tNeIUZwg8EOGJkawYpSObNxOfoIeVep3aam%2FIFZMTaeBOFv%2BJCMn%2F%2FpnE7YdHcek%2Fy5VYoyU6hPA8uLVJ6k6W13AmpKFCkoqFLDm6%2F2soFsiNk5tB3q2zG7F%2BLX6fg6ZdV8ppPjHgha2nSk2elhDkalgyMMNv5hssGOqUBef5Go9e2CDVDYPM7dvpTl7LpmlgSPuzIpMx%2FN1MAH50cw9wWNwxdLrmrk2bw0Wn6tCPwHDtemdo5phDZH9TuRY1elL2AoIVWbPsw9LiAJn241acdPGXX5z5gC6dnpVne6GreWNArWtAtMNveGgYtZNkpomQryO%2F4wHx9Q4%2F2nYWtVlrYHjU24cB9bkHLDTw8Q0HJD2mYymxc%2BBqzBvF%2F5u0nIkZY&X-Amz-Signature=8ababf0f0276eea7824d79ec7e5aa8d3f022b9a2172956df75ce31aac9491c7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


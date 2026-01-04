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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F4WNN7A%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDEqMjK7NjxAbKzxh5FlBX4SAXS1awsEphDqxEaIqSFNgIhALKcWeQ8gswuVsGH%2FyjvNzy2bgM9m5%2F8yDGb6TpvAMlXKv8DCB8QABoMNjM3NDIzMTgzODA1IgyRK3C%2FjzYcdQfqMUgq3APHg9BuOp0cGT5jtwWgNJGt7vXGVlGJIrYCjog%2FPkVYmk%2Fr1iIM7E7MXaFeI0E5Tv9esVsnldPCXbhDeiKEaKUTstJnW8xNG4AYJDiwOh6SYD4EvSqER8WStXllRU5Yqijbo2QLQ%2FhPOHqYH3jEiegJZgEA7y6j1oa%2F3Qxj%2B4m5fy%2FplJEbW6aET0HZVzB2A95VJESsq7roMjeHcFDdmuikPZyUFXb3OhFmotafyc5O1IaRTg1TuMMi%2BscR1N1WXrpWFUHgkm%2FuOnRM04S9nYfxNV64aUsn2xNejRWTFxlNajY1tqYh%2FxPncWlBRVa0txWfrCEeHSBE7sNQiD2mCcJp6w8fQubA%2FheWdp%2B%2BOvhnM%2FGw%2FD15%2BMMnGv0K7l7w%2FjHqzseinZrQEMbM%2BV3IrfwXaEmPRkQHBTQ3GIudYM36ToQTI3E4U7iVBaoI2IiPQYcag0GuUN9jiCzBVfZBVFB7WyAiRrWhpflPbqR3FIFjIAhPqfZ7fRxR0J66nSv%2FIlTZrccRaro7xhA%2FZgiR5pUbqsFtc%2FqZH29QRy%2Bpsx4lJWKZ5JO9mOAzPc4N%2Btuig%2BuJubp3sQU7BZszg8vU2iYE7GIry%2FFy10f7t%2BU1kNK%2BIJeeEbM%2B367lMRl7SjDYoubKBjqkAcBSqOAmSzbAvKR%2Fs00SgNTthnOcjCZbF%2BjT0uJFEwQ33WN5jHtCdDqVlFsBLzerE7%2BmpJ02P0TpsoVJ%2Bd1osQdQCcRfZTJRS%2FTSdfKXBcaTKyC8bWkWL4rMZjL1c%2BGiUQCIq9Dv72pNbegLtv%2FmkH6mSSKqn4XSq1uIiEXhcq8NDuLj2UknjQR%2FCNyMYHTGa5zuSGCsfWYHnUMSSDEzZGn%2Fp51j&X-Amz-Signature=f0bfcd1c7cfad88e6b34c405938b9f60efafc29093db06ee343e323003e69170&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F4WNN7A%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDEqMjK7NjxAbKzxh5FlBX4SAXS1awsEphDqxEaIqSFNgIhALKcWeQ8gswuVsGH%2FyjvNzy2bgM9m5%2F8yDGb6TpvAMlXKv8DCB8QABoMNjM3NDIzMTgzODA1IgyRK3C%2FjzYcdQfqMUgq3APHg9BuOp0cGT5jtwWgNJGt7vXGVlGJIrYCjog%2FPkVYmk%2Fr1iIM7E7MXaFeI0E5Tv9esVsnldPCXbhDeiKEaKUTstJnW8xNG4AYJDiwOh6SYD4EvSqER8WStXllRU5Yqijbo2QLQ%2FhPOHqYH3jEiegJZgEA7y6j1oa%2F3Qxj%2B4m5fy%2FplJEbW6aET0HZVzB2A95VJESsq7roMjeHcFDdmuikPZyUFXb3OhFmotafyc5O1IaRTg1TuMMi%2BscR1N1WXrpWFUHgkm%2FuOnRM04S9nYfxNV64aUsn2xNejRWTFxlNajY1tqYh%2FxPncWlBRVa0txWfrCEeHSBE7sNQiD2mCcJp6w8fQubA%2FheWdp%2B%2BOvhnM%2FGw%2FD15%2BMMnGv0K7l7w%2FjHqzseinZrQEMbM%2BV3IrfwXaEmPRkQHBTQ3GIudYM36ToQTI3E4U7iVBaoI2IiPQYcag0GuUN9jiCzBVfZBVFB7WyAiRrWhpflPbqR3FIFjIAhPqfZ7fRxR0J66nSv%2FIlTZrccRaro7xhA%2FZgiR5pUbqsFtc%2FqZH29QRy%2Bpsx4lJWKZ5JO9mOAzPc4N%2Btuig%2BuJubp3sQU7BZszg8vU2iYE7GIry%2FFy10f7t%2BU1kNK%2BIJeeEbM%2B367lMRl7SjDYoubKBjqkAcBSqOAmSzbAvKR%2Fs00SgNTthnOcjCZbF%2BjT0uJFEwQ33WN5jHtCdDqVlFsBLzerE7%2BmpJ02P0TpsoVJ%2Bd1osQdQCcRfZTJRS%2FTSdfKXBcaTKyC8bWkWL4rMZjL1c%2BGiUQCIq9Dv72pNbegLtv%2FmkH6mSSKqn4XSq1uIiEXhcq8NDuLj2UknjQR%2FCNyMYHTGa5zuSGCsfWYHnUMSSDEzZGn%2Fp51j&X-Amz-Signature=c9ab08475a4a6e4e4b5da82ad9a1e899cf445aed280e770ec8b0fce9b84adc4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


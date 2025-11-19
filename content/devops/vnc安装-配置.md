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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665R77IMNZ%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIHfQwpRcLz0IJb2NVWjtf7BHB7jrQQhMY0KQOjgaCN0%2FAiBfJoRw%2Fga9iN2CQUutlrfRi0woP0dZWQXjm5QI2mEbBiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLKvNGztXb5OHwWSPKtwD7HpGUyM3xR6Jj378%2BL2a%2BpmPGy1DPgj7QE1Mzzph5NozFLz8vs4xB2leeYPJIHhjaPvPcTlimrmy0g5%2F1uczai4HW0dLnljAamoHqicZELxG916A2lSQoY1iJ%2BKWGykPJumUI1O7kG9JqbJ%2BQYAQXgkjiIlSgDhPCuyyQ%2B%2BTaxrVxhpwr2j08TDNPQBDZcbRgUJ7ZH2hGm%2B0aFXBjtzPo8Y%2F9EUHJ7XMUwudRLyzjHLX0a4uA5Cv38djVxqigySehv9xSif%2FtklnRj6j7bLLvveTMSsRPhjzkisqVfXtcuJQF6sxE7BjoVgH%2F7ZDOgntAOSIsHHDvuvzt7yPyEqPXBQXcoIOCqOJL8RHwQFRut1Thqgnll2haLeXrqn2YWBZeiBRLgXiYI277bjgPHEpUAgvnzEx%2F0Dz7FhsQFKxCIkJ7fcoIftfvuWUJHzenBz5qCE7lGPmhVT7y8i2fY6fVejY92IEmrd%2BWTcBa6xeOY6H4pkVq6da3GNqvHZjS9hIRMXkXS%2FSQD%2BuLLQF4Pfoy2N2OKiKWA%2Fm3iLGmTwOlIboq4v9f4k8KNnz8iH8fLQvq2w9KMkw4b%2BIjbou4%2FVxUb%2Bs%2BlLu7smP1mBLfGWbqocRIb%2F09f83q7gL9iUw3Mn0yAY6pgGLSh5r9jzZJQxVnpBE1zWYkfkZYVWjIwaravyGGp33R4KXRfkPikoBEzm8ABp2TVKozmYl%2Fvc99qK2zlkNrPlBZs3C3op9w1GoZFCscSsY8w7FE%2BHQBGLHje06Bh23UpkL8%2F78QEeI9vzTvLWIwwEpN2agD3ZWLVx%2FomxLY1S2u0u0Kgww4S0JW2tbVGNmvb1ZScNdM%2FAnE%2BhLcD20GgDiaqi5LaBm&X-Amz-Signature=b51a364960ffb4b8f512165df971d289e34ee5686a2afffab1cd0f26e3cecee9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665R77IMNZ%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIHfQwpRcLz0IJb2NVWjtf7BHB7jrQQhMY0KQOjgaCN0%2FAiBfJoRw%2Fga9iN2CQUutlrfRi0woP0dZWQXjm5QI2mEbBiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLKvNGztXb5OHwWSPKtwD7HpGUyM3xR6Jj378%2BL2a%2BpmPGy1DPgj7QE1Mzzph5NozFLz8vs4xB2leeYPJIHhjaPvPcTlimrmy0g5%2F1uczai4HW0dLnljAamoHqicZELxG916A2lSQoY1iJ%2BKWGykPJumUI1O7kG9JqbJ%2BQYAQXgkjiIlSgDhPCuyyQ%2B%2BTaxrVxhpwr2j08TDNPQBDZcbRgUJ7ZH2hGm%2B0aFXBjtzPo8Y%2F9EUHJ7XMUwudRLyzjHLX0a4uA5Cv38djVxqigySehv9xSif%2FtklnRj6j7bLLvveTMSsRPhjzkisqVfXtcuJQF6sxE7BjoVgH%2F7ZDOgntAOSIsHHDvuvzt7yPyEqPXBQXcoIOCqOJL8RHwQFRut1Thqgnll2haLeXrqn2YWBZeiBRLgXiYI277bjgPHEpUAgvnzEx%2F0Dz7FhsQFKxCIkJ7fcoIftfvuWUJHzenBz5qCE7lGPmhVT7y8i2fY6fVejY92IEmrd%2BWTcBa6xeOY6H4pkVq6da3GNqvHZjS9hIRMXkXS%2FSQD%2BuLLQF4Pfoy2N2OKiKWA%2Fm3iLGmTwOlIboq4v9f4k8KNnz8iH8fLQvq2w9KMkw4b%2BIjbou4%2FVxUb%2Bs%2BlLu7smP1mBLfGWbqocRIb%2F09f83q7gL9iUw3Mn0yAY6pgGLSh5r9jzZJQxVnpBE1zWYkfkZYVWjIwaravyGGp33R4KXRfkPikoBEzm8ABp2TVKozmYl%2Fvc99qK2zlkNrPlBZs3C3op9w1GoZFCscSsY8w7FE%2BHQBGLHje06Bh23UpkL8%2F78QEeI9vzTvLWIwwEpN2agD3ZWLVx%2FomxLY1S2u0u0Kgww4S0JW2tbVGNmvb1ZScNdM%2FAnE%2BhLcD20GgDiaqi5LaBm&X-Amz-Signature=c9c3d5530b192b3b7aa31f572403eaf27ca7ef58c44b026fa3e0ccd0bc2feb53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


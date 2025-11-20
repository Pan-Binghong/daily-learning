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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J5ZOCBB%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIAmqObSi3LpQBxDSrkeKsdRd%2BktznseQANxQwsYlEzbCAiEA6RbFM%2FdrNYEv8yInHUri09Uj2Ghe4zEz5kVfIU7QPLQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FKeUy0wyBBe4%2FXPyrcAywG4lqDO%2FuLB97ZacJwgNycx1j5OFNxh%2FZQWJTfnskOQbiDXhCgqERGa9yagbdiPKmvFybIFfERZvtECaYELfPyYo8vhlS6wxb8%2B1m1uOIbAEbbzMm90eD1GQyCy92bS%2FNUffLNQWYev3X8JW8cLbd7m2yXriVMMC8%2BrZijDGWAA3rjOsYbTHibilDHYPGIuz4xaCZqthMq0UIBSkNk9YX9GMhluA4%2Bzyiz2hzg2BVNpEHsiXH1Jw1gi7BX68t92bchbwpY9Ka8dxEgWSdMKQBT6OG1dU3J3PUWzkAxSba7SH9q1PySqN0%2B9moJ2z1iA7CmfMtxf2MKatD%2BIHpe4Z6bYunQ2kW54%2Fg6mdpDiKy73T58bOzp4FOVh3OB2nkqMnCMxBAyorOyGNXdijQAyc9rhUryqExATxGJ1dR4E5GW9ah52Qq2ylmTUIYfirznfZiP4qjsymQl3XIhZs1h7oRerfkjHI4mA7oltMwEZGTUovFAhqAAry8R82LTwLddXS3GImL1IJNes7Qjzqma%2BxvtdSN39MttYiJe6p316%2Bme0B%2B%2BHy8Tx0VDJOOl8LUHIJsw41yCCaHRLywicGwOZ7r7cwDKAAJFLQmFrUbYPOs08559AUfjyeAE5MgJMPLp%2BcgGOqUBcEBLNR56R8L5m6Dqww4Wir8GXwOnS%2BPbKksPq0raO5dAp4A%2B%2BIfkJmjV4Ba4M7zsJ07SV8giuYY3tmxkaMpdXQwWgGmXpl8F6MMF9ogF9WNeTKILJvhTjbeE%2BXxejOGb%2BO9FYwFZhR9LNSTqugbXNLf7xkIX1H%2BGPWRs08H9o1E0R2grwVTnRFtlAtGLULunzQfwvwBBoLmr2RW9uoODMPeRHSS8&X-Amz-Signature=5b299cae838480fae3d9c07da4a5064af09448a60b02ea5fe52295a380f45646&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J5ZOCBB%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIAmqObSi3LpQBxDSrkeKsdRd%2BktznseQANxQwsYlEzbCAiEA6RbFM%2FdrNYEv8yInHUri09Uj2Ghe4zEz5kVfIU7QPLQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FKeUy0wyBBe4%2FXPyrcAywG4lqDO%2FuLB97ZacJwgNycx1j5OFNxh%2FZQWJTfnskOQbiDXhCgqERGa9yagbdiPKmvFybIFfERZvtECaYELfPyYo8vhlS6wxb8%2B1m1uOIbAEbbzMm90eD1GQyCy92bS%2FNUffLNQWYev3X8JW8cLbd7m2yXriVMMC8%2BrZijDGWAA3rjOsYbTHibilDHYPGIuz4xaCZqthMq0UIBSkNk9YX9GMhluA4%2Bzyiz2hzg2BVNpEHsiXH1Jw1gi7BX68t92bchbwpY9Ka8dxEgWSdMKQBT6OG1dU3J3PUWzkAxSba7SH9q1PySqN0%2B9moJ2z1iA7CmfMtxf2MKatD%2BIHpe4Z6bYunQ2kW54%2Fg6mdpDiKy73T58bOzp4FOVh3OB2nkqMnCMxBAyorOyGNXdijQAyc9rhUryqExATxGJ1dR4E5GW9ah52Qq2ylmTUIYfirznfZiP4qjsymQl3XIhZs1h7oRerfkjHI4mA7oltMwEZGTUovFAhqAAry8R82LTwLddXS3GImL1IJNes7Qjzqma%2BxvtdSN39MttYiJe6p316%2Bme0B%2B%2BHy8Tx0VDJOOl8LUHIJsw41yCCaHRLywicGwOZ7r7cwDKAAJFLQmFrUbYPOs08559AUfjyeAE5MgJMPLp%2BcgGOqUBcEBLNR56R8L5m6Dqww4Wir8GXwOnS%2BPbKksPq0raO5dAp4A%2B%2BIfkJmjV4Ba4M7zsJ07SV8giuYY3tmxkaMpdXQwWgGmXpl8F6MMF9ogF9WNeTKILJvhTjbeE%2BXxejOGb%2BO9FYwFZhR9LNSTqugbXNLf7xkIX1H%2BGPWRs08H9o1E0R2grwVTnRFtlAtGLULunzQfwvwBBoLmr2RW9uoODMPeRHSS8&X-Amz-Signature=d6367d89a22118da6ef4e5367c8c0d522d3b7fb1418c7744c694f38c3ff8d85f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


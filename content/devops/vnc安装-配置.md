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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYI43N73%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEvCDchFxTYPrfvBqBc41vlyxwwlPtrjyI%2F3P6z8Y1wNAiEAoIGHjFyVekb%2FkN4ASOx%2B51B0%2BlHSVGp%2BWT%2BnIgurDsYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDLT1QeOX4QTLkuZZYyrcAxM8cgTZWPl20ZDxOXwygFSaYDs8rVtQ2k9uE86mulMM%2BnmgGRRQ1xuQvzQ9WgG1y8%2F191QD4Nd76dk9TYjsln2lE0fncv6GEB8hCCd5Xhk6ECdK1%2BHOf9iJSvcKV0b1TB7ghxJo%2Fz0mfOMcbLRHf%2F%2BeBPf9cVx4BBwOo4leOy1hdtdTcFZ4Z4mPQgZ9SeTMQbPFnGLvysBTAO807HaY0xOamJyKTj9k4CsfhuMXCq%2BeC4yx8%2BkhW3j%2BeGq4TrJPUpuqta%2FHMyWt%2BeJH57AGEc2czVJgRyacBgYUlBh3j5zzXQJE7lJUh7bwq59Saralzf5v9OjPXnVSE3iWBRLUscvZMdUeBo2uOixdTB5my0ydkWz4WF8%2FruNmY0bORK6feXpcOphVOBsmqF2%2B93EgU9dZGy107k6nCP1xwx%2BBUyOWcvYktDy7HBSaOZfs0g6hcWvw4mSa604AuO4ZkuSehCMyHGPEeRehfVam2sfPDfK8M4tsGdZuE4Y1nhGFYwUMy4JAvhghRJk2zlXs%2F%2BEtZdbsQ75MGOAJiMJbDigYs8AYS6u0GLPE0tG5mQwOzXVrm1GvARB2wM6zZQ8rM9V8iRoi90CS9XqJmygfBOc7pI9h%2FXCKp%2FcUaRcfD5JaMN6wmckGOqUBLt9dVKd33RIGV2Dl1ngglLLFlImlJPZaOcX05ihdicoh%2BtAU6%2F0%2B1vDfsxoXgar2%2BmQqVQ0cGAPoQRAoPLgeJ7Zgib0k%2Fys8MXp51yGmY%2BVRRPnfY7aFggoKSrKBxf1i0M4CdV9C%2B2FkTF2JbQJHg3fpH2eBShVlTRaSBOxXMOkVCzJaAymEyna0tiV2FZtWOack8%2FfSdcCzkLimysZjLWr9xjbu&X-Amz-Signature=804ab40638e2881fac86c95c3efb50e107d08aef8ef33ab06be89a8920fed576&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYI43N73%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEvCDchFxTYPrfvBqBc41vlyxwwlPtrjyI%2F3P6z8Y1wNAiEAoIGHjFyVekb%2FkN4ASOx%2B51B0%2BlHSVGp%2BWT%2BnIgurDsYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDLT1QeOX4QTLkuZZYyrcAxM8cgTZWPl20ZDxOXwygFSaYDs8rVtQ2k9uE86mulMM%2BnmgGRRQ1xuQvzQ9WgG1y8%2F191QD4Nd76dk9TYjsln2lE0fncv6GEB8hCCd5Xhk6ECdK1%2BHOf9iJSvcKV0b1TB7ghxJo%2Fz0mfOMcbLRHf%2F%2BeBPf9cVx4BBwOo4leOy1hdtdTcFZ4Z4mPQgZ9SeTMQbPFnGLvysBTAO807HaY0xOamJyKTj9k4CsfhuMXCq%2BeC4yx8%2BkhW3j%2BeGq4TrJPUpuqta%2FHMyWt%2BeJH57AGEc2czVJgRyacBgYUlBh3j5zzXQJE7lJUh7bwq59Saralzf5v9OjPXnVSE3iWBRLUscvZMdUeBo2uOixdTB5my0ydkWz4WF8%2FruNmY0bORK6feXpcOphVOBsmqF2%2B93EgU9dZGy107k6nCP1xwx%2BBUyOWcvYktDy7HBSaOZfs0g6hcWvw4mSa604AuO4ZkuSehCMyHGPEeRehfVam2sfPDfK8M4tsGdZuE4Y1nhGFYwUMy4JAvhghRJk2zlXs%2F%2BEtZdbsQ75MGOAJiMJbDigYs8AYS6u0GLPE0tG5mQwOzXVrm1GvARB2wM6zZQ8rM9V8iRoi90CS9XqJmygfBOc7pI9h%2FXCKp%2FcUaRcfD5JaMN6wmckGOqUBLt9dVKd33RIGV2Dl1ngglLLFlImlJPZaOcX05ihdicoh%2BtAU6%2F0%2B1vDfsxoXgar2%2BmQqVQ0cGAPoQRAoPLgeJ7Zgib0k%2Fys8MXp51yGmY%2BVRRPnfY7aFggoKSrKBxf1i0M4CdV9C%2B2FkTF2JbQJHg3fpH2eBShVlTRaSBOxXMOkVCzJaAymEyna0tiV2FZtWOack8%2FfSdcCzkLimysZjLWr9xjbu&X-Amz-Signature=e8f912cdd32a9b88ff3fdc65c52255b087b85498abef5fa47ffeb29ff03a61d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


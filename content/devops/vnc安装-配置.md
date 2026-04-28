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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW4LZLVH%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIC7jzb7XKRi06VDzODeNixOLejb3kYbBuQuEWAHHjoubAiAkN8QIp%2BSbuUStZIzbNDCNmnFVgLpHjlDAHoaQorhyPSqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BIBo26ne87aOpHVQKtwDE8A2u74VJNaeUK8FnWBfuxoSfik%2Fd2QGRtfZuK2Bn04cwFTKIax3Ftrs7Sy6iN0vSHNT6fMmDzpYyJZBZ%2B7SyQMewZsvU3bMOGoMc9U7U0iV2bCTou88maU2naDfuEihGgBXRN%2Fm7zuFJ44S1pN9jTDjNwQPTNtMdCdRjRphXyVAx1qh4HEuIFekyDMkzkyjxL6z3U2oxIw9S4ftTAqPtaM%2F8ILiiycBe9RyrFc%2BNy7fTn2%2Bj%2BitXtnD59OU7lcE0pSvVqMPkrrpyWIMN2Ds3nJhkK8SVCpuvBNPtGRsatqYrHs5DGYbOVcp7uQmYCfAXLYbbZLJEllRbKgc8ANUA9y1KjojueoEambCO0gypRRQfvJkzc9wYylmdSybK5enucHLt%2Baqmt1dy9T6D20FtF%2FX2qhqCGR4pBiqxnHWliSIojtNBHqVWEkJcBk2N9WwKaCuA248aMfzp7ElBDzEbVkcatPQZ1Kt%2BpsMUjTAmSBrLDQc8Lue9Bs0mC3tCkJKHidcp4sd4XnaS83B8XyuHaBCNr3Er%2F2y9F7POFTMQrpHqXscX2o5hqwQdLfGCfFAPY7nz8fk0qkRWHdFNBer%2F6evYijhtSLogst7PFON43y4Fg4V4jHu90Sswvow9%2B7AzwY6pgG1U%2B9CioICnXRbyOWBDoay%2FBhVOqsb3YP%2F2o6iMhxx8dqHTZVPKmNh84TwwpPYTfX2MxfWtQzPphp%2B3wM5RXDc3Jbb%2FAM87QF1z1mivFb9P%2B%2F5DxLYerWXOvWiStsSBI7Lcko5%2FVOD06hXIO3ANs3Fd6stny0jBsUmFPek6iJp1e1zGdJ%2FQqQqk%2BZrHb1CD1gvj0qKiTHsTPDV5Uc4JTSF0t12hXIE&X-Amz-Signature=ac066b5eed72465891f7156baa372489f0d14f6651c8755ce3d35150323812e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW4LZLVH%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIC7jzb7XKRi06VDzODeNixOLejb3kYbBuQuEWAHHjoubAiAkN8QIp%2BSbuUStZIzbNDCNmnFVgLpHjlDAHoaQorhyPSqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BIBo26ne87aOpHVQKtwDE8A2u74VJNaeUK8FnWBfuxoSfik%2Fd2QGRtfZuK2Bn04cwFTKIax3Ftrs7Sy6iN0vSHNT6fMmDzpYyJZBZ%2B7SyQMewZsvU3bMOGoMc9U7U0iV2bCTou88maU2naDfuEihGgBXRN%2Fm7zuFJ44S1pN9jTDjNwQPTNtMdCdRjRphXyVAx1qh4HEuIFekyDMkzkyjxL6z3U2oxIw9S4ftTAqPtaM%2F8ILiiycBe9RyrFc%2BNy7fTn2%2Bj%2BitXtnD59OU7lcE0pSvVqMPkrrpyWIMN2Ds3nJhkK8SVCpuvBNPtGRsatqYrHs5DGYbOVcp7uQmYCfAXLYbbZLJEllRbKgc8ANUA9y1KjojueoEambCO0gypRRQfvJkzc9wYylmdSybK5enucHLt%2Baqmt1dy9T6D20FtF%2FX2qhqCGR4pBiqxnHWliSIojtNBHqVWEkJcBk2N9WwKaCuA248aMfzp7ElBDzEbVkcatPQZ1Kt%2BpsMUjTAmSBrLDQc8Lue9Bs0mC3tCkJKHidcp4sd4XnaS83B8XyuHaBCNr3Er%2F2y9F7POFTMQrpHqXscX2o5hqwQdLfGCfFAPY7nz8fk0qkRWHdFNBer%2F6evYijhtSLogst7PFON43y4Fg4V4jHu90Sswvow9%2B7AzwY6pgG1U%2B9CioICnXRbyOWBDoay%2FBhVOqsb3YP%2F2o6iMhxx8dqHTZVPKmNh84TwwpPYTfX2MxfWtQzPphp%2B3wM5RXDc3Jbb%2FAM87QF1z1mivFb9P%2B%2F5DxLYerWXOvWiStsSBI7Lcko5%2FVOD06hXIO3ANs3Fd6stny0jBsUmFPek6iJp1e1zGdJ%2FQqQqk%2BZrHb1CD1gvj0qKiTHsTPDV5Uc4JTSF0t12hXIE&X-Amz-Signature=dddce6c09ef783059a42eedc5f1db28ebe2a574dfaa48f3186bfb1c2374e02bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


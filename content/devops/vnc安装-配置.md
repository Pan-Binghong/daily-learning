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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXMFCBZN%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb6vRdKtv%2FiiZKZ08nGU%2B3dxy%2Bfr6Jesq%2F%2F3YrAiImrgIgEHf%2B5i0nk5JElojfvWW03%2FaaYRDedFFdcg2yXPtsB0gq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCLPqPqVM9%2Fsi8qjRyrcA3Otm19wPd83hsWS0ud3vqYLdhmGJS92IE6L24XY1H4JcedB1le%2FHw1%2Fm42IbCzUW4cOrT7EOO3t%2BBUW09ZkXGweEgdhBdmEB3q2Wq3CeTn%2BFyjxJL5%2BnwIQG8Vqy70RDSCrT9AMie7x3yZImGktsyiuPVvhYr7c1GF%2FZmlefwwAn55%2BJ8My1AR2vjcukExfEf5KSvZmtXvCziqlc61R324JIRD%2B%2F5THwzmgvfCJgs5l4nithGacXZZFXGzG1t2JGu4qEHgEfdGt6U%2BJ7jK2kBw0JiJ9jR0UTjcEMDJ8TI3eEmMXhjrh4L7bM4dfkcEmbgGA9wSNkxlE6M9Ttb1rJ8Y7QkTSnMuYJgzbReyz6au8gWjkPTAePPSit7z6d6NRhsZiVlFR16ld59SzuHLe1wO4YP11NDID42KZkSbsRHZy%2FH97desuC8VQrLYXQjPc9cN9kjEdd5C%2BjU7HGl1z0qMuPeYLxXlFzmNJA4H55NCgNTVBWJNOMrREBZD2%2FuVf8b4PziiUaGYpLZpo9iz%2BOLzBZZbBnRnC6IIvsabAKAW5jk86nR%2F2X1f05lXETuVPghNEV1XILXtKO3zyWNyv83QKeG0EHZnu2VHDoA1GCv%2BNugJaZ3%2FOKyeUoUcyMOOulMkGOqUBXvTuqDN3eSh3Y2sIP8UUzXWx39qzja%2B7ddam3GE3MB3sIadVkUqGTimTUY1RbhOwdl9XWf91xcUQ%2F249zJcHujNuLqr0TyDjEsc13o1TSsGZN0Hte4OL%2FV%2B4%2FDbhVmw3DysPlHysKcpr2TbZNuFNmp%2BcuUCFtMKEffTE2%2B0OV1EW1bM0HXr0Yr5nA0lsCPQSLz%2B5xJa7FPuoJpWN4aKpbDrYFubk&X-Amz-Signature=01b495c9535e337ac5d9ede8f7af46ac4e1ba54694a7f01c8d6c35b87b11753f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXMFCBZN%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb6vRdKtv%2FiiZKZ08nGU%2B3dxy%2Bfr6Jesq%2F%2F3YrAiImrgIgEHf%2B5i0nk5JElojfvWW03%2FaaYRDedFFdcg2yXPtsB0gq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCLPqPqVM9%2Fsi8qjRyrcA3Otm19wPd83hsWS0ud3vqYLdhmGJS92IE6L24XY1H4JcedB1le%2FHw1%2Fm42IbCzUW4cOrT7EOO3t%2BBUW09ZkXGweEgdhBdmEB3q2Wq3CeTn%2BFyjxJL5%2BnwIQG8Vqy70RDSCrT9AMie7x3yZImGktsyiuPVvhYr7c1GF%2FZmlefwwAn55%2BJ8My1AR2vjcukExfEf5KSvZmtXvCziqlc61R324JIRD%2B%2F5THwzmgvfCJgs5l4nithGacXZZFXGzG1t2JGu4qEHgEfdGt6U%2BJ7jK2kBw0JiJ9jR0UTjcEMDJ8TI3eEmMXhjrh4L7bM4dfkcEmbgGA9wSNkxlE6M9Ttb1rJ8Y7QkTSnMuYJgzbReyz6au8gWjkPTAePPSit7z6d6NRhsZiVlFR16ld59SzuHLe1wO4YP11NDID42KZkSbsRHZy%2FH97desuC8VQrLYXQjPc9cN9kjEdd5C%2BjU7HGl1z0qMuPeYLxXlFzmNJA4H55NCgNTVBWJNOMrREBZD2%2FuVf8b4PziiUaGYpLZpo9iz%2BOLzBZZbBnRnC6IIvsabAKAW5jk86nR%2F2X1f05lXETuVPghNEV1XILXtKO3zyWNyv83QKeG0EHZnu2VHDoA1GCv%2BNugJaZ3%2FOKyeUoUcyMOOulMkGOqUBXvTuqDN3eSh3Y2sIP8UUzXWx39qzja%2B7ddam3GE3MB3sIadVkUqGTimTUY1RbhOwdl9XWf91xcUQ%2F249zJcHujNuLqr0TyDjEsc13o1TSsGZN0Hte4OL%2FV%2B4%2FDbhVmw3DysPlHysKcpr2TbZNuFNmp%2BcuUCFtMKEffTE2%2B0OV1EW1bM0HXr0Yr5nA0lsCPQSLz%2B5xJa7FPuoJpWN4aKpbDrYFubk&X-Amz-Signature=5cb879e4ce5950ea2041a543b10ef19ba664086c2b088cc3eecfff0b8162fb9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NPCKI5U%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE7CCSzjmYlRddTqIan2otKeg2W3ZwWzqlm49EPbG%2BgKAiAFQnNqT3hMhB%2FfrfY56Gs43S9HHvDQfK3DMmXbzDbbmCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMKdG9efFnbklCmganKtwDjr2AiNogLW5ciQRp41EsQYysLE8Vxlmq6myC5gNSjVp3YKyX1qrCL2%2B3Fk6aCPM1bwwyrWXknyZy5nkaDTqbjWdXDWFhQ4dvPO8rGj%2BCo9gNE8bglQggRUHiLb3hpm883fd%2BUjwGOQdyJmmSUr4%2Bh5iRi2TQycLcg3VVOycTV0OJK8PvW95bKIicyXUC9ZFBLQEqFlfAGGzJVw13ZcLviZS8ndaF%2FITCRHmTnhyoPjims3UgtRgZRhDl7mjlyHK%2BMDyu1sWEbr04Dshxc2X0yagQJ5k7DTO%2Fb0U20dKu1qd3bQinBtH41GRVwLxfk9Q%2FEaXIYhTnwYDPz4vEo7oim1SQz6hmUpFt5Y6VV5SyGpds6yJF7FsYKw1CJItWExh0A2yPtok2tVw3j4s9hv%2F%2BsvVIFsRtnOzSMRpLV2LHUuaavbyA28el6beqoiJSBB84AOUtExwkOmx1te8pzT9F4KLVW0nur7CKkkgsJ04kDM8zmkI3gyTKkN1s61lOPuNNZLgjesjtPoc84dclxhDxe7quiP19SZS2S3Q1AwEdknT52J9Ro2EiI8I1yL%2Ft0dGMxBBblLFNeU5qOsZurGp7XuvoFpriP4KYb5Bgwr9h4yl3UZtp5uS3KHtVzwgwxq63zgY6pgFWg0Xrs%2B76dUZVF%2Bsu%2FHS6q5vCMkuU%2Btfb%2FhwntpqmsD92jgCNcjNCTE77TLYf51qpc1Jtko4KOI9M%2BB%2B4NRw3SNVIjVoXPOiRg5M0%2BvDoAk%2BVpsuOjYf3GWWF2oDAQjNMKnqAZJZ7bT%2Bays9iOADQfAT8kf%2Fx%2FUglmBrXUbW0AxiugK7uhFT2nTJVlRyx2AtP0kmlQ93EAvSppo%2FSSpGO7WW2YAnM&X-Amz-Signature=3ad709648e320ed2768160f73b9aa70c6f6a33927adbcd17a4e7871032ab4ba7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NPCKI5U%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE7CCSzjmYlRddTqIan2otKeg2W3ZwWzqlm49EPbG%2BgKAiAFQnNqT3hMhB%2FfrfY56Gs43S9HHvDQfK3DMmXbzDbbmCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMKdG9efFnbklCmganKtwDjr2AiNogLW5ciQRp41EsQYysLE8Vxlmq6myC5gNSjVp3YKyX1qrCL2%2B3Fk6aCPM1bwwyrWXknyZy5nkaDTqbjWdXDWFhQ4dvPO8rGj%2BCo9gNE8bglQggRUHiLb3hpm883fd%2BUjwGOQdyJmmSUr4%2Bh5iRi2TQycLcg3VVOycTV0OJK8PvW95bKIicyXUC9ZFBLQEqFlfAGGzJVw13ZcLviZS8ndaF%2FITCRHmTnhyoPjims3UgtRgZRhDl7mjlyHK%2BMDyu1sWEbr04Dshxc2X0yagQJ5k7DTO%2Fb0U20dKu1qd3bQinBtH41GRVwLxfk9Q%2FEaXIYhTnwYDPz4vEo7oim1SQz6hmUpFt5Y6VV5SyGpds6yJF7FsYKw1CJItWExh0A2yPtok2tVw3j4s9hv%2F%2BsvVIFsRtnOzSMRpLV2LHUuaavbyA28el6beqoiJSBB84AOUtExwkOmx1te8pzT9F4KLVW0nur7CKkkgsJ04kDM8zmkI3gyTKkN1s61lOPuNNZLgjesjtPoc84dclxhDxe7quiP19SZS2S3Q1AwEdknT52J9Ro2EiI8I1yL%2Ft0dGMxBBblLFNeU5qOsZurGp7XuvoFpriP4KYb5Bgwr9h4yl3UZtp5uS3KHtVzwgwxq63zgY6pgFWg0Xrs%2B76dUZVF%2Bsu%2FHS6q5vCMkuU%2Btfb%2FhwntpqmsD92jgCNcjNCTE77TLYf51qpc1Jtko4KOI9M%2BB%2B4NRw3SNVIjVoXPOiRg5M0%2BvDoAk%2BVpsuOjYf3GWWF2oDAQjNMKnqAZJZ7bT%2Bays9iOADQfAT8kf%2Fx%2FUglmBrXUbW0AxiugK7uhFT2nTJVlRyx2AtP0kmlQ93EAvSppo%2FSSpGO7WW2YAnM&X-Amz-Signature=f5f9c007b245a4d8e02ce09fcc3203c0ffbaba745a7a67b17e2a99dbca16dfc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


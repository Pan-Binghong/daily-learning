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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVUS4SJA%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCICLADNOqjoU%2FUjSp3dEt03gPxcZUNeuG8HhX3TSIjKoSAiEA9RB7IMn4jmEOTd0ertiGQXv4R8Sut65PHYrMYqJBfZ0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDHRH6LkXpzyLcC775SrcA6ooazE%2BtB2Z8qIuBZexRsL6l%2FSxCezNWSSdAQO3jIbhvIm0rLa4VzmgE42ftJmI9FgJP2GeN5F5c3xVGAprqODQitcEmx3TDRTPt1k6T5CMcptdHkMKX3Ya4GnJwZkXI0%2Fp%2BlPES0gZue9NaN9mw%2BCqzA6IOq07nfbflpmYEs6YggnGMcyw7%2BNuh33ZR6yukwE%2BCYiPUkN%2BYwtT6HolYYRYprvqlxWhmf19ipqJG3Qdg4M9jUNwEJ0LnCK2vEDTvtCpCAfq%2FydGY3vL%2F9N%2FEHeR4yWU7rokm9y8qYZ%2Fnb5i9H4UfVWdg2wL83%2FV9TvBUGYRINoAYEXBBTlOeHdihQM2Or%2Bz8ZwygsCAcZ9IQQp3wCu%2FRX0rnl6BLJFy1PQDeaULSQm3fV%2BEjF9QKQyoI4VJF%2Fpzx0b2F2IUpYIA3UxUN%2FDKybAa3BaepWTXsHZBw8%2FfaqWlg3IVR7vMh2C4awUGK6J2dOzcXGhDETeg%2FRjhU6kqd89m0mppHMkM9SBA3tdGHMbPKo1eq7QvoiZJ3045Tm%2BdumwPktX10F9dDvnnTnwYmk973Y485cC8VPnmBEWycuAvmaEqdO6Zn%2F3F7jC4ehaD0OVIYm04Lc1Eh53C8nOBjKpl6X6xeITPMI%2BGhM0GOqUBR3XpPPZ9gX%2Fb%2FISG0tjVDa%2FiEftxsGXh%2Bno3YO7nUXRiveRXhfZ%2FQ5P%2F2yi1oJMafJq0l0EdliWxkSXXkYAr12TtfxUBzejL6Jc1y0QU93fHNuEqsJPb2VW6jefbbN9qqAEKNgy6XqLZTOfV1pqN7ePHqUoE767MH9OiU0WMWj7GPvfOE1rwfibtQAqTK%2FR3pD12pd6qxxIZ0o9Ic9lDEFRpOvap&X-Amz-Signature=04812e7611621e6d8769dd6768d0b9fd9159c34e36cbef90b4aef0cee48397e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVUS4SJA%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCICLADNOqjoU%2FUjSp3dEt03gPxcZUNeuG8HhX3TSIjKoSAiEA9RB7IMn4jmEOTd0ertiGQXv4R8Sut65PHYrMYqJBfZ0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDHRH6LkXpzyLcC775SrcA6ooazE%2BtB2Z8qIuBZexRsL6l%2FSxCezNWSSdAQO3jIbhvIm0rLa4VzmgE42ftJmI9FgJP2GeN5F5c3xVGAprqODQitcEmx3TDRTPt1k6T5CMcptdHkMKX3Ya4GnJwZkXI0%2Fp%2BlPES0gZue9NaN9mw%2BCqzA6IOq07nfbflpmYEs6YggnGMcyw7%2BNuh33ZR6yukwE%2BCYiPUkN%2BYwtT6HolYYRYprvqlxWhmf19ipqJG3Qdg4M9jUNwEJ0LnCK2vEDTvtCpCAfq%2FydGY3vL%2F9N%2FEHeR4yWU7rokm9y8qYZ%2Fnb5i9H4UfVWdg2wL83%2FV9TvBUGYRINoAYEXBBTlOeHdihQM2Or%2Bz8ZwygsCAcZ9IQQp3wCu%2FRX0rnl6BLJFy1PQDeaULSQm3fV%2BEjF9QKQyoI4VJF%2Fpzx0b2F2IUpYIA3UxUN%2FDKybAa3BaepWTXsHZBw8%2FfaqWlg3IVR7vMh2C4awUGK6J2dOzcXGhDETeg%2FRjhU6kqd89m0mppHMkM9SBA3tdGHMbPKo1eq7QvoiZJ3045Tm%2BdumwPktX10F9dDvnnTnwYmk973Y485cC8VPnmBEWycuAvmaEqdO6Zn%2F3F7jC4ehaD0OVIYm04Lc1Eh53C8nOBjKpl6X6xeITPMI%2BGhM0GOqUBR3XpPPZ9gX%2Fb%2FISG0tjVDa%2FiEftxsGXh%2Bno3YO7nUXRiveRXhfZ%2FQ5P%2F2yi1oJMafJq0l0EdliWxkSXXkYAr12TtfxUBzejL6Jc1y0QU93fHNuEqsJPb2VW6jefbbN9qqAEKNgy6XqLZTOfV1pqN7ePHqUoE767MH9OiU0WMWj7GPvfOE1rwfibtQAqTK%2FR3pD12pd6qxxIZ0o9Ic9lDEFRpOvap&X-Amz-Signature=4c9d5b82fa24f5f4ea6b7794f389342005fcce5435eba060a84330b186f08997&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


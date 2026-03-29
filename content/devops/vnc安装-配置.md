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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QESYY3I%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQD5Qf274hqigXVbxnMs4%2BSqMlnhXHlHHJNp7UT%2BvpnbNQIgWLjHJe3jATRwkmn3g5PsSY0vSFI%2FvV1MSOSD7828MHoq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDMU%2FmOAYSA5u%2BxeTfCrcAw8xbjquvaJ93rfmqerB%2BDiHFW5ZYEAb2LHqsOPJa%2FShKD4xFg%2FCNDHbAMCSUZk04TeysRYczjusGInz7O1X5FTEqm9uSTduRtdOpPXuSpRpZIm9JCKgy0jW1B6fpntHdbFg57UxBubJ6DlYvFmYBRZJL%2BxcPbDdpRVMQiO7hLIH42L7D1HrYihM%2F4A5n%2FmKIDPar5nvMJRad9AFzqbR%2BLo8mZTM7Em9i5vdAMPUm7lkJN5yddd8B4Jaelpqbc37iyfUYdM5huWQRIwGKpt%2BJZ2V9KFW8U0bjcZy7Dem45DBS2zAtSAkXO07%2FmvGS3GBFQKYX9LpT3rfH91Dhljtkb34dwNjNQ2DnUseag7ViPU%2BRIhz%2FMmA5nzZkEOy3iRaHVaSnkLWbikCdEMGa4Fo4p%2BDM9zjpwUN2%2FTLWRwHauy77RYk5ULVazvUPRS1qPS5WU3c8xJUvLdmDRjKzdhOPcLruOihNhX16yarzMlvNj6%2BxQ%2FDKpmddBqpKAYoNZCzmORA0dcm0JzxAjEmKhNW7p52PMNZv8UGDl2PriJpb1wbS%2FMMM4Vd6HRmkDxKAIpXW1LDnbaG0VRAm1MmNnw8%2BowtY2h5S2RchSPY4FX3rQSzXzF6zIJAZqqSjvsoMKu%2Fos4GOqUB3BJMUTcTIMUuLRGPWBqGOwtIWBJL%2FLPHkxyQEFHLl%2FmwjKjfjGMSFel9rHfqv7p%2FIPKmgutr0osm5PPdld5M3%2F1q0Dh7NipKzM1j9pwJ7s%2FRFJCE23Tblp0yvjfeJQYMP7LpY7gc1G1SCD3%2FV9lSsiQ%2FXr%2FEsD%2BW9IY%2BkEh1ObbgZfBvaN9%2BuxkDCHNQXMQO2ZUexCYferHHmC%2Bm67PAzu%2FLNQLT&X-Amz-Signature=bea913f4eda74141f42fa9ff94861e783b1a91e1cac2bb3346c41045743e8761&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QESYY3I%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQD5Qf274hqigXVbxnMs4%2BSqMlnhXHlHHJNp7UT%2BvpnbNQIgWLjHJe3jATRwkmn3g5PsSY0vSFI%2FvV1MSOSD7828MHoq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDMU%2FmOAYSA5u%2BxeTfCrcAw8xbjquvaJ93rfmqerB%2BDiHFW5ZYEAb2LHqsOPJa%2FShKD4xFg%2FCNDHbAMCSUZk04TeysRYczjusGInz7O1X5FTEqm9uSTduRtdOpPXuSpRpZIm9JCKgy0jW1B6fpntHdbFg57UxBubJ6DlYvFmYBRZJL%2BxcPbDdpRVMQiO7hLIH42L7D1HrYihM%2F4A5n%2FmKIDPar5nvMJRad9AFzqbR%2BLo8mZTM7Em9i5vdAMPUm7lkJN5yddd8B4Jaelpqbc37iyfUYdM5huWQRIwGKpt%2BJZ2V9KFW8U0bjcZy7Dem45DBS2zAtSAkXO07%2FmvGS3GBFQKYX9LpT3rfH91Dhljtkb34dwNjNQ2DnUseag7ViPU%2BRIhz%2FMmA5nzZkEOy3iRaHVaSnkLWbikCdEMGa4Fo4p%2BDM9zjpwUN2%2FTLWRwHauy77RYk5ULVazvUPRS1qPS5WU3c8xJUvLdmDRjKzdhOPcLruOihNhX16yarzMlvNj6%2BxQ%2FDKpmddBqpKAYoNZCzmORA0dcm0JzxAjEmKhNW7p52PMNZv8UGDl2PriJpb1wbS%2FMMM4Vd6HRmkDxKAIpXW1LDnbaG0VRAm1MmNnw8%2BowtY2h5S2RchSPY4FX3rQSzXzF6zIJAZqqSjvsoMKu%2Fos4GOqUB3BJMUTcTIMUuLRGPWBqGOwtIWBJL%2FLPHkxyQEFHLl%2FmwjKjfjGMSFel9rHfqv7p%2FIPKmgutr0osm5PPdld5M3%2F1q0Dh7NipKzM1j9pwJ7s%2FRFJCE23Tblp0yvjfeJQYMP7LpY7gc1G1SCD3%2FV9lSsiQ%2FXr%2FEsD%2BW9IY%2BkEh1ObbgZfBvaN9%2BuxkDCHNQXMQO2ZUexCYferHHmC%2Bm67PAzu%2FLNQLT&X-Amz-Signature=b6bda6a28410d308f6301aa64ae107cef0af26070b89b78fb33277b2a17ce12c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


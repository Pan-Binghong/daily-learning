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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KIFWNDO%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHorhcL8HMmmW8gBMGE1JDARlbfKZPQRg%2B9nODo2tqFkAiAVdQvVqaUig9CQjgWpvsB3Bpt%2Fg65Iw3hpVNeDMhaMZiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2GZAInnns%2BYLf7utKtwD%2FIa6iL0u9yMzZwNAetvncBKkJOWNfz3EUGUEZJn0FeIc7w7mChbUVWWghvlDQnv2ykZzhXv3y4BjxdTDh1tKXhxMcmVANIztS38yuH51LpUnzJnOarufK2zp3Bc6%2FTjwYWKwyl8wUha00IApzy96o7UWIRGak6lNbfaII3%2BBJpJAIIYpu48ylzW4wHDCXrCYMsRPVUg8aqyWojTnepfhwLdsBlIdeyB5vtCMycmnZsnSKGYRGEcPe3eTEwcGqUGbBfa1ClUtpAequ6iyXmsxMUF8O1XkyCkYWczsIDSrIXbs%2BSfadjoOCbTR%2FXO9KxDw3ahlY%2F4RvAfDCxt%2F6sdg6GrXb0xW9%2F7xw1cWcTAby%2FJccvx4c2pRd8ObYdsTehdKLip14zANCXODo2QxEnkucN7zkd9hfBHL8icVfsOFjCITxRtJhqyHtS0MP7GFcS2HGl%2B1U7UAxCPrOvc03QGfW5Bq1kLZ6wnYN1nrPjboOJzZhF7fwyUS3mWWEyEYwAR7I9VW%2Bjou9FyfpC5YqBGwWXBYlrXtcoTGn%2FNQuuU0y1rpyRHBpmZ69GxcOEYq68McWbruiH3KE2Q3ccIuG6PRomIW0KKtjt%2FlSfz1B07LFzvx13aX0TLCmgOyN3swqNaOzgY6pgFQ7RN%2BA%2BasX5RYe8XPlWD4sL7okVl5dUi7HJgeMLcF27n2G17fHJMbGYIvk25XzWRjx4c5AHlDJiU4uRIq%2Bvp0EkjxaAIZVgkG8MAphB4OFKmuU0to3Rg8weTQv1SHoH7ROwVaKu1Vuzq1RSP9WhylUKqNl5fm9SmkkiShWhuRSOFh6xCDHKT9%2BOOVHJqQj974uDGAGtdU%2BcyMgbf8saYX%2BoWimM04&X-Amz-Signature=44eb5da9d874b37beca9db13798e83ce13911e0bd5bd1ef1d460d5d669ff871c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KIFWNDO%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHorhcL8HMmmW8gBMGE1JDARlbfKZPQRg%2B9nODo2tqFkAiAVdQvVqaUig9CQjgWpvsB3Bpt%2Fg65Iw3hpVNeDMhaMZiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2GZAInnns%2BYLf7utKtwD%2FIa6iL0u9yMzZwNAetvncBKkJOWNfz3EUGUEZJn0FeIc7w7mChbUVWWghvlDQnv2ykZzhXv3y4BjxdTDh1tKXhxMcmVANIztS38yuH51LpUnzJnOarufK2zp3Bc6%2FTjwYWKwyl8wUha00IApzy96o7UWIRGak6lNbfaII3%2BBJpJAIIYpu48ylzW4wHDCXrCYMsRPVUg8aqyWojTnepfhwLdsBlIdeyB5vtCMycmnZsnSKGYRGEcPe3eTEwcGqUGbBfa1ClUtpAequ6iyXmsxMUF8O1XkyCkYWczsIDSrIXbs%2BSfadjoOCbTR%2FXO9KxDw3ahlY%2F4RvAfDCxt%2F6sdg6GrXb0xW9%2F7xw1cWcTAby%2FJccvx4c2pRd8ObYdsTehdKLip14zANCXODo2QxEnkucN7zkd9hfBHL8icVfsOFjCITxRtJhqyHtS0MP7GFcS2HGl%2B1U7UAxCPrOvc03QGfW5Bq1kLZ6wnYN1nrPjboOJzZhF7fwyUS3mWWEyEYwAR7I9VW%2Bjou9FyfpC5YqBGwWXBYlrXtcoTGn%2FNQuuU0y1rpyRHBpmZ69GxcOEYq68McWbruiH3KE2Q3ccIuG6PRomIW0KKtjt%2FlSfz1B07LFzvx13aX0TLCmgOyN3swqNaOzgY6pgFQ7RN%2BA%2BasX5RYe8XPlWD4sL7okVl5dUi7HJgeMLcF27n2G17fHJMbGYIvk25XzWRjx4c5AHlDJiU4uRIq%2Bvp0EkjxaAIZVgkG8MAphB4OFKmuU0to3Rg8weTQv1SHoH7ROwVaKu1Vuzq1RSP9WhylUKqNl5fm9SmkkiShWhuRSOFh6xCDHKT9%2BOOVHJqQj974uDGAGtdU%2BcyMgbf8saYX%2BoWimM04&X-Amz-Signature=276992d749b8c088abf7a28e93ab5b898bc3fa56c4e9b75bb2b58ce26c7333db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


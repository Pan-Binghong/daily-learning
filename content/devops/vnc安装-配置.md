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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TUSJCSF%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCckoZprM0ASYYE47Wr6NNCebyTlnRwIHgKCAl1yAkc9AIhAO7A93Bj5vbI1dyGD6nPs8COKjFpsXDkaR5iFgh%2Fyf1lKv8DCBQQABoMNjM3NDIzMTgzODA1IgwImRWkV%2FCPEAbpeDQq3APd0voj21opCylBQ8FyGg0wRh%2FAUMwQ5M7kP3A%2BaLwCfbjdzMxy%2F%2BZdPVPKz0DhAKnSlUA6eMsIIT7TsIJBnz5XnVHiEM8mGJLSq6aqquT5Mqh5UgkWKkDn6Ux4YhqpLWsvatD4AvuHTbyJJEelGqJmVg%2FOgFSmcXjVQnqe0NEKkUMVW0iQ8NBFSM9yooJU%2BShYA4aYY4nBbhEfn1fJTK1HG82dJuIMAywAt%2FVzkLnpKYGeGvLt8AIBAO8Vus6npWqCq0jRt%2FnsJ6ab%2BB70CGeDcNmTVKoCJjPjAWG4mHSY6roR73piZKoMAeTS3TRCKbDd2Cp9lEcaDlxcR4%2FH6pyh7D3xPbAN42JkXWmoc8ppWPg%2B1zNDdq2%2B5wSg2%2Bka8D7r2e1o32fxaXjy0lMcU%2Bf6YNivGeqdhtIqkA8yF52pcCtUdaCAGOuTEe83IMC91W2buv87WNWkMBo9AaxcaKNoSzSRzBDAIE9OshNuO9HdTVbQfzz%2FMQF2KDJTynblxCgkIJ3cBWOojWCEOgDl3tPRsLRyyRBmqsdT1Ybg5zrPufkwAt8Q35A5lw66tFzROjs8ZvUHBn7WIsoMafRPQ%2B0ZZMb9FxdE24jBKEb4h9pDA1aItOvQWZy%2Fuu9ihDDPj5zLBjqkAURFs1n71nr57sDxXjGfkVVpw4dFBTpL0wwoOBacoPBwi52Evc%2BIqMCLMALQ7Vm6hGsSPsqZbW6O7DKVut8nQabazSPTn0B%2FcW%2BOonYtm6aTbb3U6en4jiB4afWrUMZ6glAzHo7CJSM3CA61J6M2PSkv6Cvxq5l%2BEfbPYEawfllsv6ZjGBmaGVBWdjOLkP6gqrP7BpdUvlylem0jB%2FXxYRHTtior&X-Amz-Signature=f8887b2e545b983ae28b4be7a9ea23f282126f014f659ac878115456657c8420&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TUSJCSF%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCckoZprM0ASYYE47Wr6NNCebyTlnRwIHgKCAl1yAkc9AIhAO7A93Bj5vbI1dyGD6nPs8COKjFpsXDkaR5iFgh%2Fyf1lKv8DCBQQABoMNjM3NDIzMTgzODA1IgwImRWkV%2FCPEAbpeDQq3APd0voj21opCylBQ8FyGg0wRh%2FAUMwQ5M7kP3A%2BaLwCfbjdzMxy%2F%2BZdPVPKz0DhAKnSlUA6eMsIIT7TsIJBnz5XnVHiEM8mGJLSq6aqquT5Mqh5UgkWKkDn6Ux4YhqpLWsvatD4AvuHTbyJJEelGqJmVg%2FOgFSmcXjVQnqe0NEKkUMVW0iQ8NBFSM9yooJU%2BShYA4aYY4nBbhEfn1fJTK1HG82dJuIMAywAt%2FVzkLnpKYGeGvLt8AIBAO8Vus6npWqCq0jRt%2FnsJ6ab%2BB70CGeDcNmTVKoCJjPjAWG4mHSY6roR73piZKoMAeTS3TRCKbDd2Cp9lEcaDlxcR4%2FH6pyh7D3xPbAN42JkXWmoc8ppWPg%2B1zNDdq2%2B5wSg2%2Bka8D7r2e1o32fxaXjy0lMcU%2Bf6YNivGeqdhtIqkA8yF52pcCtUdaCAGOuTEe83IMC91W2buv87WNWkMBo9AaxcaKNoSzSRzBDAIE9OshNuO9HdTVbQfzz%2FMQF2KDJTynblxCgkIJ3cBWOojWCEOgDl3tPRsLRyyRBmqsdT1Ybg5zrPufkwAt8Q35A5lw66tFzROjs8ZvUHBn7WIsoMafRPQ%2B0ZZMb9FxdE24jBKEb4h9pDA1aItOvQWZy%2Fuu9ihDDPj5zLBjqkAURFs1n71nr57sDxXjGfkVVpw4dFBTpL0wwoOBacoPBwi52Evc%2BIqMCLMALQ7Vm6hGsSPsqZbW6O7DKVut8nQabazSPTn0B%2FcW%2BOonYtm6aTbb3U6en4jiB4afWrUMZ6glAzHo7CJSM3CA61J6M2PSkv6Cvxq5l%2BEfbPYEawfllsv6ZjGBmaGVBWdjOLkP6gqrP7BpdUvlylem0jB%2FXxYRHTtior&X-Amz-Signature=143c24db159e4db3991924dddc5332dbd4ef829e63c7b44fe506a2993b53435e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


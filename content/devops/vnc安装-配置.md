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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUZDY6SN%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIFGg9d63JXTL%2BNwpKXfkfQAuyrjieO69IiU7z01r23I3AiEAjSmzSlXWTYdrHX6qmulIgrCyOwHkGXVf44umyuHwl9IqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGWRnz4U2m4ExaIrircA44N49HQqh5fwWeo6%2Fr2Ci2Bi2%2FbT5TVbpFu35UUUftK8jBudq%2BYZaRGMlMTNG6Ufy2PNblk272rihw7Q1Bc%2BKLwsDQfEcPOyD%2FQyw2gdEcAK29EdOYHf2Xp9w2ayzIxF15VyGb092OK2nB%2Fo%2F8HlO612iKOO4FL0CYaQZppVAjUUU3TCco42htkafWoUSDJv7L%2FSSg9U2mlyUBCuDy2GlylSlnx3HCRO%2FrL%2Fo5LYoBUcmE%2F9hkhZRGisZcm%2Be%2FHTpxiaqbwprxO8zPdryGIqTz19fT5DcC18atXnnwutArrVHhsED9wqrVjT5omv4dY8fmTokoZhSjX8rUc7NvoOG9ao3AEdYtpnuUw%2BhL2dvhuyWZMVjN9igI3R7U1ErDgx1NzHQ7pEdoy6%2BhWdxqtnpDH%2FgbF4vG2fWtL4Ww9c89caf%2B1zVhN299QnKqBJWs2kl2Ybvqv5kektscgXMoYFxKvEYdQ8KcPtdI12uXWL6wxItbk1Itf%2FFTtOlU182KXbBC1QMTIhE5blSsAWyM5DoCGz1aQKKsD1vxjhyzvbghfTmhv9pRYCIInQFi2NyF%2FNoqdxDiPoPuUHQSnJspWAkaunxOXneu%2FHLoj78kHDv9GD1EqfrEXxZjjV9kpMK3n4s0GOqUB4odIp0MWf2lbEK1Oq3bmphc%2F6SmCPqpspmiv5olTPH02AuWAsAFFo0cNAFgy3LcnUbmv%2Bpe4ven5AxiwWhznkedxaOb%2BIKzOiUA6bUzrCdQN0fdxS68bwbesLAj7%2FnYrO7F5MaLT9xKyJCGGdEPySlrwfOZr178DW%2BdrWM7CHE%2FZWtciH2vAEukJ7p4KqzNShbmyuO5kE4FMSivnrVVSSUPn4gze&X-Amz-Signature=c6d1461b95591ae072a5e8018a0e2183bdae42eacc89fafcd2f514a0b4568728&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUZDY6SN%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIFGg9d63JXTL%2BNwpKXfkfQAuyrjieO69IiU7z01r23I3AiEAjSmzSlXWTYdrHX6qmulIgrCyOwHkGXVf44umyuHwl9IqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGWRnz4U2m4ExaIrircA44N49HQqh5fwWeo6%2Fr2Ci2Bi2%2FbT5TVbpFu35UUUftK8jBudq%2BYZaRGMlMTNG6Ufy2PNblk272rihw7Q1Bc%2BKLwsDQfEcPOyD%2FQyw2gdEcAK29EdOYHf2Xp9w2ayzIxF15VyGb092OK2nB%2Fo%2F8HlO612iKOO4FL0CYaQZppVAjUUU3TCco42htkafWoUSDJv7L%2FSSg9U2mlyUBCuDy2GlylSlnx3HCRO%2FrL%2Fo5LYoBUcmE%2F9hkhZRGisZcm%2Be%2FHTpxiaqbwprxO8zPdryGIqTz19fT5DcC18atXnnwutArrVHhsED9wqrVjT5omv4dY8fmTokoZhSjX8rUc7NvoOG9ao3AEdYtpnuUw%2BhL2dvhuyWZMVjN9igI3R7U1ErDgx1NzHQ7pEdoy6%2BhWdxqtnpDH%2FgbF4vG2fWtL4Ww9c89caf%2B1zVhN299QnKqBJWs2kl2Ybvqv5kektscgXMoYFxKvEYdQ8KcPtdI12uXWL6wxItbk1Itf%2FFTtOlU182KXbBC1QMTIhE5blSsAWyM5DoCGz1aQKKsD1vxjhyzvbghfTmhv9pRYCIInQFi2NyF%2FNoqdxDiPoPuUHQSnJspWAkaunxOXneu%2FHLoj78kHDv9GD1EqfrEXxZjjV9kpMK3n4s0GOqUB4odIp0MWf2lbEK1Oq3bmphc%2F6SmCPqpspmiv5olTPH02AuWAsAFFo0cNAFgy3LcnUbmv%2Bpe4ven5AxiwWhznkedxaOb%2BIKzOiUA6bUzrCdQN0fdxS68bwbesLAj7%2FnYrO7F5MaLT9xKyJCGGdEPySlrwfOZr178DW%2BdrWM7CHE%2FZWtciH2vAEukJ7p4KqzNShbmyuO5kE4FMSivnrVVSSUPn4gze&X-Amz-Signature=05b7c2a8bbbf90666715548bc83e893a9b29a954cc5adaae4275192537a6908b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


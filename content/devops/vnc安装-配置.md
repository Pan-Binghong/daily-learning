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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JRHISOU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMTYZTc1juUZVADtxVxzBBKCkP9MStPl3Jafz2HdBElQIhANf07JBjsat8vodCJ%2Fla0%2BKjHr2X%2B2v4ELCU8dCZzczeKv8DCHQQABoMNjM3NDIzMTgzODA1IgxntpQLnlo8hTSug%2BUq3ANXmC96rB%2F3zajPZwUJMiwYKI2cCRWbrtJryljBiYcA1cADmeNh1feVpMceoWncaRfSyDTzn81u0RiZbwvXE8sGtAmXD9n%2FR1CLU38yDVB%2B4F8C%2BWbS%2FlybbAIP22N%2F6rTIg4YZFqcAI47QruEeL6DUwoCNSr42lOA6WGp4xFqw95G8Cdfh6AOTqrVbrvkstFEgNwCo85E%2FALmYR%2BaskBJgTY9mfzxBBiqC4ab0DfAe05JjUP2ZuAbU0RMGZfoQF3L%2BI7D19RpsrYQ4BaK%2BKbVmn2C5ftu9Sdnq5EZ63TTIH8ahU2MiOiFFQagUMOp3sHkOA4ontteyW22Jscs0wfhzgst7sOHkSMgh7YbIDvIDjTRpq8dnNyLPDxdQ9WmAo%2FJY9ytLLgFRgygnof%2FH5zy7vkxLABEjDQHnpKuBs9wTUDD89e8L7Jtt11WKijIpMiiGs4wC7NYTGiV%2B0Ry5qBBs2dwNEQDud9syakrfyuapplRIIWMC2ZPqiYYb6rbKYdMvh620EZOi45WCMZo5WYNOvAr%2FN%2BsVi4xbjduvfry3p4IJffsWpEPDW6NISJCZOPmCPWdjbd8DMA%2Fxrc6tVhPXm8i8tv89o8Hrawo%2FiLqfbH5aKIhMj3Om%2FvQtczDv5ILOBjqkAXCbhaQOqVllVj%2BJhtOZNcDEXhAaozhMQCZvyhuBqZN%2BXPDgd%2Bw6gTP0li%2B48tQnXafJ4TjsRMYjSpasX3cXKLc7HlnNAvE%2FFaPEMkwDYfF9%2BypPhnh1J1W9AuQNeijdHTaU%2Fx8s8id4JFbQdCQf2IGM%2BLv6lm9sobNK%2FE18QGujti30y1Am%2F%2FC7h%2FW923ERvilQ%2BpSGS33ZryquibRLXbEvGf%2B1&X-Amz-Signature=175d48d12eaa773d19b13deae10c13d91e49ccaa73850369f8183967521a39a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JRHISOU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMTYZTc1juUZVADtxVxzBBKCkP9MStPl3Jafz2HdBElQIhANf07JBjsat8vodCJ%2Fla0%2BKjHr2X%2B2v4ELCU8dCZzczeKv8DCHQQABoMNjM3NDIzMTgzODA1IgxntpQLnlo8hTSug%2BUq3ANXmC96rB%2F3zajPZwUJMiwYKI2cCRWbrtJryljBiYcA1cADmeNh1feVpMceoWncaRfSyDTzn81u0RiZbwvXE8sGtAmXD9n%2FR1CLU38yDVB%2B4F8C%2BWbS%2FlybbAIP22N%2F6rTIg4YZFqcAI47QruEeL6DUwoCNSr42lOA6WGp4xFqw95G8Cdfh6AOTqrVbrvkstFEgNwCo85E%2FALmYR%2BaskBJgTY9mfzxBBiqC4ab0DfAe05JjUP2ZuAbU0RMGZfoQF3L%2BI7D19RpsrYQ4BaK%2BKbVmn2C5ftu9Sdnq5EZ63TTIH8ahU2MiOiFFQagUMOp3sHkOA4ontteyW22Jscs0wfhzgst7sOHkSMgh7YbIDvIDjTRpq8dnNyLPDxdQ9WmAo%2FJY9ytLLgFRgygnof%2FH5zy7vkxLABEjDQHnpKuBs9wTUDD89e8L7Jtt11WKijIpMiiGs4wC7NYTGiV%2B0Ry5qBBs2dwNEQDud9syakrfyuapplRIIWMC2ZPqiYYb6rbKYdMvh620EZOi45WCMZo5WYNOvAr%2FN%2BsVi4xbjduvfry3p4IJffsWpEPDW6NISJCZOPmCPWdjbd8DMA%2Fxrc6tVhPXm8i8tv89o8Hrawo%2FiLqfbH5aKIhMj3Om%2FvQtczDv5ILOBjqkAXCbhaQOqVllVj%2BJhtOZNcDEXhAaozhMQCZvyhuBqZN%2BXPDgd%2Bw6gTP0li%2B48tQnXafJ4TjsRMYjSpasX3cXKLc7HlnNAvE%2FFaPEMkwDYfF9%2BypPhnh1J1W9AuQNeijdHTaU%2Fx8s8id4JFbQdCQf2IGM%2BLv6lm9sobNK%2FE18QGujti30y1Am%2F%2FC7h%2FW923ERvilQ%2BpSGS33ZryquibRLXbEvGf%2B1&X-Amz-Signature=d9c5abfa27fe7209f635f3fe1e164bf4a413c0d20fe355291e90a344fd1c5bc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


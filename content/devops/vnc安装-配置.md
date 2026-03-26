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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMNO2PSM%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLUAKmFdpoCZHqdqrik1PCHXJdQZAcfpaqyxmqSRG7vwIhAIO1hCJqGyUiUujsecSoQQxUhcnejmtX6GQHcXg0rnwHKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqiehzU8QuNJghGQgq3ANA5iiFquPJDyasvONnpM9wSb7MArHWwGTqbMJKz0DThUT7IQtPCNH4AqDHxYL%2FZxLDUiHucSJY0ZqfQWF9LSRRNeHk%2BU16H8qj%2FyScoEqaxXe2jpqncGY3amZ%2Btv%2FJJzbv0vBumXRypY7MUec6QFv8ynRs%2FbiVtceXMotO3aM41hsmuoX3si3V9osXM%2FvH4ECwwHEhZXW8B9%2FvTm8rhGWv1RhtCE2X8rh1NBVbB9d6lK8bdUb6TvukJw6qmT4BcHUAdfzpw0EwcAx9IKoCjumqVpIj%2FiQLQRx4qfnEWlaDJ91cByCnR0phr%2BuQcKll9dIK%2BsYJ%2B10Sr7xdvT%2F2h6LKkUJE8wLM3%2BbkP9pxmMv4NoucWn2ZpKfrLwxO%2BpOtG5CfEMtog%2BXbowJ0rkeTguQPxGQSexY70gGWHU5V5aNOrX2T736RjF1xIGfpU7m5dMR3PaW28wc0PQFS7L%2Bz5EP04POFFKSylnbg3abaR9o4kuZwprdQkGstceos5qDOm7mSo3IIXRdfM1GY%2B7FR0pRjC8MTxbV3pBEHj1%2Fs%2FFcyGJdjMuz2hGhq9rq0VvtGkvJRG9Vhl9EwZBcxLcRLBRYMybQ3Rff46XZJfyu5WHoTsBpk6%2FeJEOfGW7v7NDCVyZLOBjqkAQlmcYfnAmewjaqM%2B41F5Qa4U2gP4mlvDGLy%2B6bnSJJm9XcygZUGorbWIscoYoRT1bKKfYXtVrL2MWX%2BQm0JzXBK%2BPXZL1LR8EJau0fqcBhAC4XyTH79DydIjGIRxdI2bfVSgKVuq2NFfc%2BX%2BQyUH9b4EzGdxZ9Rp1lZUqosWkClQ6B7TfcnoOzEcAMES0SKWw96C4G43t1nLDDNwusaN5fr6a%2Br&X-Amz-Signature=ed61ed0ba60bf4896cfbb99c49e6e45b75ad32367e771d178ded95ed64754500&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMNO2PSM%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLUAKmFdpoCZHqdqrik1PCHXJdQZAcfpaqyxmqSRG7vwIhAIO1hCJqGyUiUujsecSoQQxUhcnejmtX6GQHcXg0rnwHKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqiehzU8QuNJghGQgq3ANA5iiFquPJDyasvONnpM9wSb7MArHWwGTqbMJKz0DThUT7IQtPCNH4AqDHxYL%2FZxLDUiHucSJY0ZqfQWF9LSRRNeHk%2BU16H8qj%2FyScoEqaxXe2jpqncGY3amZ%2Btv%2FJJzbv0vBumXRypY7MUec6QFv8ynRs%2FbiVtceXMotO3aM41hsmuoX3si3V9osXM%2FvH4ECwwHEhZXW8B9%2FvTm8rhGWv1RhtCE2X8rh1NBVbB9d6lK8bdUb6TvukJw6qmT4BcHUAdfzpw0EwcAx9IKoCjumqVpIj%2FiQLQRx4qfnEWlaDJ91cByCnR0phr%2BuQcKll9dIK%2BsYJ%2B10Sr7xdvT%2F2h6LKkUJE8wLM3%2BbkP9pxmMv4NoucWn2ZpKfrLwxO%2BpOtG5CfEMtog%2BXbowJ0rkeTguQPxGQSexY70gGWHU5V5aNOrX2T736RjF1xIGfpU7m5dMR3PaW28wc0PQFS7L%2Bz5EP04POFFKSylnbg3abaR9o4kuZwprdQkGstceos5qDOm7mSo3IIXRdfM1GY%2B7FR0pRjC8MTxbV3pBEHj1%2Fs%2FFcyGJdjMuz2hGhq9rq0VvtGkvJRG9Vhl9EwZBcxLcRLBRYMybQ3Rff46XZJfyu5WHoTsBpk6%2FeJEOfGW7v7NDCVyZLOBjqkAQlmcYfnAmewjaqM%2B41F5Qa4U2gP4mlvDGLy%2B6bnSJJm9XcygZUGorbWIscoYoRT1bKKfYXtVrL2MWX%2BQm0JzXBK%2BPXZL1LR8EJau0fqcBhAC4XyTH79DydIjGIRxdI2bfVSgKVuq2NFfc%2BX%2BQyUH9b4EzGdxZ9Rp1lZUqosWkClQ6B7TfcnoOzEcAMES0SKWw96C4G43t1nLDDNwusaN5fr6a%2Br&X-Amz-Signature=a84b850816390d3dd6c0858a4793ed6cfc7b2c5563b95178ba726d77a7b8acea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


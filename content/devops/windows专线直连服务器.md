---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKHT224N%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIH%2Fo95Lumij1BcAsO9NuEXQbFdkdUDxSLNK0Cy11JaArAiEAnxVtv0GIaET3bRYxCNkYTfAPgDNETVB%2FsFUIEUAoSXUq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFZH0Sei0HcuTBKsuSrcAwDDmTEu%2B7sEmdrb2fgDjaAMNdN3FPCsjhs4XdliZcqNjZe84W25KeLVzHdwUAMrMlGkT2cTcXAqGGaDBkniCOGoNLdsHYovbiH0W54cLLM%2F8trlGR8pgQAi2jEY2aUw%2BGckxQFUu8LMFTxalZkW6r7mYdVPXXc%2FHsbO6lDqyoSuUHjF1GOnsp7s%2B8tHk8RTucr5Wrlyb3ZXtJj7R2KnsrApjoYgbpBFs6lHIyXxjZnVgjzJc5XTgpxuqmyG8aEiKPSiuiJuSrOrCN9aiBwt3xJQ69dL%2BwGreYJhePYakI%2FkcHXHjVCoI5oMwInSsa%2B9AWuE1yNlNKOEAx11vfSfsRV5dW%2B5RpuXSJF8HhT1rQ%2F6UhJHBnA7z%2BYAGfD%2FAdxXXuJtKIvURtnSkX2iNVd8mjcDRKkLGk79i79kqG7tYL%2BuQG9ndBhc3eJ8mwhgmZdASHm62cYP%2BsbMlimPhFMNax%2FyYA9j62CVSZMSbVgPBfrenMMIp%2FHOF6RMxOiVHkUn2sxGSOvXTRRbF4NTmXW4sXda9GO67QpindvhdFe1v%2F9ZQ2lOUic4mYWZzAybvHgs5KSiXeDzc2omBHoRxFOVqp%2BFoxFwB0UrP496KLpyrUObrp92gkPYklY%2FULihMKSF1ssGOqUBqnGZVRywzjso3Y3pVA7oYWRzp%2F9x9mchKhzEx5DzZT02ePTE72d98GrvM0TwvuSs6%2FI9cs93rO2XDUO8Nw7doEnqpQmvFCvloHnsPxP%2F1iHvNCWBP5HkwUzFfnF%2FgpLWX5k0KuMcPEesk4USQWucSmM8p%2Fq8NsSaCQC91YttQkxkuTzae8UlqAfYJpgRqalkMSjVnGuakFB8EpMbuZzmhQZDtLIc&X-Amz-Signature=834b2b392fee1ba94367dbdee512a12dcd44ac3beeaca0eef27ed4602142494c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


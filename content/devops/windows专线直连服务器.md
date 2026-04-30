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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEBUMBLP%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDg996ATTmhLFWzOyivRJSZWV8HUcg%2FQtRy0S4wqZTTBwIgA7RdJONWPZWimnBZpZaIDka8hkZ3OSVOfhMYtO8r2RAq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDE8a9tZQZu7nn1QK4ircA%2BNpsfaY%2BUYMqy%2F0dZdbLG7lO2Ah4pcX5wDNdwkbtzWzTEprQQuWhxSbSCX2UrwEsXREKovp%2BdmOgJ2PQAh5ZAQetecGG6MqkReJfeDQNTutV4vW4EQXKGdmc5G8EHR8YKv316YKggj3zn5QfxBSBwcb0CIC%2BkAEi15DCJ6D81%2Fu%2Fn1kE1ZL4KBRZhET4iXbKvnnPiyMWzuT%2F8k%2FjfJzwHqHdMROW368at5rPVJ4abGk41EMi%2B8%2BfrErGl8h2BNwn8jXjnztjTuSAIbjxKYH6KUAzglQL4t0k%2BMFzQNmWscwcKlnd6JO6zPEoCCKv26kmD10XnQMpiDa0s4E3XMcs9ESW5M%2BeI57Mv4YEKoiJGk8yfw2OBvVwjVJ%2FX7KF7tWJR3rZeLFp4DFfiILVU3DIJDG9dGB40qjuvdgkUIgRkm0Ue1H%2FxMPZL%2BEUQ18wInh0yqBiFOJz8B5oE2A2LZWargUFnDJ%2B8csRhZaQ6i5eRRCyDKFNVkcDIEcSodXp%2BbwMR5pJ%2FnbYnR587qthmmG93kQhb5XOlyhUvgMijIb1kfyU%2FI8EthoKknvzh2c4%2FoQbAfrul4kQNs7eLFyL1lf4MUms7Fz0WTQ36A%2BmDdOKz4Fw4hWUfZSsYLTRgtiMKaczM8GOqUBWLu%2FEZEjRWVRcmhx2uztDqFhnoemr7OV7oiSFoZ0arLPi1XqrLYoNptxoQzhxoQfLhNxHkMa0m7EMOL2uaA2g1a7kwt2fz%2Bkdq1dQ9o2ewwvAMbQ4eYQv1qwYvr70io%2BVzGDw%2FjM4aluOow9VNIm5kKqZmtHyWaOTkrxGvs3kr78rwRiG0gPzTuAyJqWZOl66ne5fgaevIUvgu0Vzj7Kk0xKthQ7&X-Amz-Signature=d9ab71cd5e28f6ed998eb8fbc9e8bcd21ad06e4b915f76dfe90098c68da6aa61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGOYQXFN%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2wK%2B0uKQ0jV4fOCIWqpfims15OUI5Q8pNI%2Flp7yHDWwIhAINgTx5rOTluul6ajWLBxtGQrbKE%2F8ZZOjZu9hERktKGKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXNJiEqrD6IfhBqV8q3AMADbNZbkOEK31moRLk6IX58UXRlYS%2FER5JDHu4vvC6nXeFPm%2Fc5r5cg5jBMgkZPaV4cUwJI00vOS3YDIAruoQLRPjWGOnW2T2ml7vWKBTqmoE1QHPUVedEm8Kjn%2BnFHyDy8vu7DppNM4wJhYrnA0aB6lDEQTFD75WZE28%2FhB6Q5inFv%2FKDH%2FjlEcD3xl1%2Bvj6AI4V%2FwjFB%2FyuUIvXow2rep5ncC4Tst5C1v2HZxKxWCB8DbMCL%2Fl1E60QfAYowug12QyARnJWu1oSzC80RXs3BeEnEkbDYmB%2FRtaeS6lDAXHM5HTq5WpycCM%2Fv3TRxyT7zfTN6ItZdVIerC%2BrbZAKYugJx325MNVjn25qMO9V6B2U8z7JIFpWJMzOKVbx4HMLkv2PWWI0zE2gXDVTgmOH7TiIVpEqJad514tkD5w6f2xuaO0cwTgkorsmkZq9TEOpNx%2BwHKpv1SnJpQ98hURbeiarp9jwt9v4UcFq0yDbnwnsn3qHUWvmjkaspGdeTocqLo1gMKTX8lrji7ttXbcMCaplZ7%2BQVpKuhkdluRqi1MQgVyjPZRklBvyP5PDwQs6ywnpe3MX3TmfBcef51%2FVxM%2FRnCTPmRHRQANtdh14AesLijzxf%2BMXpzcd80kDCO4pLKBjqkATAw24D30boy%2Ba3RyzB4IKeXUik1ULPVmjgxG3xhkipH2ijD5YffoDXOg%2BB0HmtMmCKU25t8FIXJFPaFGldosURwT2Mm5Uy4tqMPRtBGRCpNIYDBYUB9hO5w9AzAl2%2BfDqAEabYbGcLd4gJsYE9NbiFYUk7ByorOV8t4p6tB9scNI%2F6p8WGaqw%2BLYmKiIvyglRyppkZEWXqlfix8BgpjYc8CaFP%2B&X-Amz-Signature=fa00ae362c272e6002980b8d31122ba3386c5a2622acb569feefe391f85b9a12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGOYQXFN%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2wK%2B0uKQ0jV4fOCIWqpfims15OUI5Q8pNI%2Flp7yHDWwIhAINgTx5rOTluul6ajWLBxtGQrbKE%2F8ZZOjZu9hERktKGKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXNJiEqrD6IfhBqV8q3AMADbNZbkOEK31moRLk6IX58UXRlYS%2FER5JDHu4vvC6nXeFPm%2Fc5r5cg5jBMgkZPaV4cUwJI00vOS3YDIAruoQLRPjWGOnW2T2ml7vWKBTqmoE1QHPUVedEm8Kjn%2BnFHyDy8vu7DppNM4wJhYrnA0aB6lDEQTFD75WZE28%2FhB6Q5inFv%2FKDH%2FjlEcD3xl1%2Bvj6AI4V%2FwjFB%2FyuUIvXow2rep5ncC4Tst5C1v2HZxKxWCB8DbMCL%2Fl1E60QfAYowug12QyARnJWu1oSzC80RXs3BeEnEkbDYmB%2FRtaeS6lDAXHM5HTq5WpycCM%2Fv3TRxyT7zfTN6ItZdVIerC%2BrbZAKYugJx325MNVjn25qMO9V6B2U8z7JIFpWJMzOKVbx4HMLkv2PWWI0zE2gXDVTgmOH7TiIVpEqJad514tkD5w6f2xuaO0cwTgkorsmkZq9TEOpNx%2BwHKpv1SnJpQ98hURbeiarp9jwt9v4UcFq0yDbnwnsn3qHUWvmjkaspGdeTocqLo1gMKTX8lrji7ttXbcMCaplZ7%2BQVpKuhkdluRqi1MQgVyjPZRklBvyP5PDwQs6ywnpe3MX3TmfBcef51%2FVxM%2FRnCTPmRHRQANtdh14AesLijzxf%2BMXpzcd80kDCO4pLKBjqkATAw24D30boy%2Ba3RyzB4IKeXUik1ULPVmjgxG3xhkipH2ijD5YffoDXOg%2BB0HmtMmCKU25t8FIXJFPaFGldosURwT2Mm5Uy4tqMPRtBGRCpNIYDBYUB9hO5w9AzAl2%2BfDqAEabYbGcLd4gJsYE9NbiFYUk7ByorOV8t4p6tB9scNI%2F6p8WGaqw%2BLYmKiIvyglRyppkZEWXqlfix8BgpjYc8CaFP%2B&X-Amz-Signature=9e7d90faa8f44e6b15c37b4f452a21c10a1d711cb670f6abc529b58cd620ad9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


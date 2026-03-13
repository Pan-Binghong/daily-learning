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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTEGQNEY%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCA43GMnDh%2FazeQKSqm0HbnmUYfSFRhGGyogoJEQEtkewIhAIpeui3j36VBFlvVHfYYAG2VIAbNPIvC%2FJY3%2Fk3M%2BejgKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlCtC4kVLpdEGd16kq3ANAlIXJ9pABSi6s1unkPiPOKFV4m4HZ92%2BkMsNOCKyJvRFHXeClxxwAiaUbpsWoArVjUNw9Y3LCEEOz%2BS0G7KyqIhJy%2Fhe6XNxUNltzfUpRgmSPF%2BwvCd8xeVy0JhXZV86zN3f2EeAOijpNwcrtv8afHufT9b%2BsHaF9xmnV3dOnEwoZQm7dUb79d1wtTFK8loFzTpjQ%2FxhXCXOLTYyAoengb388tjPnh3Wk3Ns61%2BYExkaUeKBrWIe0stkBUTmpFXlkxvq7AareOtjzixfzzV9tljjUAkjIfx7gFdLngMxTwCkmo5Jw3FYiQ%2FomcmGctjwkkNyRxVfHF4TAUq%2BlOvYcOh96pvr%2BbKzbz34vxIMj8JnvsnTe2w4JKqYTn26GJNQlvNg5KrnjGoVbQioVszEPQDsB1OSc%2F8BuvXA6F8gyp3r76jQ2%2FAX8U%2F1pH1e3E3LitJjxUm0sff%2FWX1BZsrKiIkiweOR6uNRieAEUKZopvz3lJr3lOh%2FywB9p6pDG%2FhEOzfcuDQgP%2B%2Fod5tPjLzYw4f5C%2FUUaOG3acnmoYQAcoGEi%2Bne0%2F3mcNfuZoHFAlRSeXO3d2W5RAFyYeTrI2OZrH5lxZmeAEALNAXVCAWLSixqTcx8XgYF%2FqZbtKTCXuM3NBjqkAWMzX9rgn5pie6Boe9r6jaohDjle%2BUqC6%2BYrOooePcxF77fmS4R7hvWv%2Bzlyc1B42UbgMNR7thpfRKj5C4ZE2t%2F5oxntP5L9d6Gjx8bQFrOIWZYlde5hznXVEvn6AP4YFXnp5lrLeLpwyPx5Ozc8G5nNidPc8R6bkzoLRCevpMvM0XuXlzZqvooLF46sNgYn1xitYW3ALtWuJJOKaigllQgmrKxv&X-Amz-Signature=32b02eceb7429a2374afe983d10cd4971408c0ad7366a13c10746031d381db61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTEGQNEY%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCA43GMnDh%2FazeQKSqm0HbnmUYfSFRhGGyogoJEQEtkewIhAIpeui3j36VBFlvVHfYYAG2VIAbNPIvC%2FJY3%2Fk3M%2BejgKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlCtC4kVLpdEGd16kq3ANAlIXJ9pABSi6s1unkPiPOKFV4m4HZ92%2BkMsNOCKyJvRFHXeClxxwAiaUbpsWoArVjUNw9Y3LCEEOz%2BS0G7KyqIhJy%2Fhe6XNxUNltzfUpRgmSPF%2BwvCd8xeVy0JhXZV86zN3f2EeAOijpNwcrtv8afHufT9b%2BsHaF9xmnV3dOnEwoZQm7dUb79d1wtTFK8loFzTpjQ%2FxhXCXOLTYyAoengb388tjPnh3Wk3Ns61%2BYExkaUeKBrWIe0stkBUTmpFXlkxvq7AareOtjzixfzzV9tljjUAkjIfx7gFdLngMxTwCkmo5Jw3FYiQ%2FomcmGctjwkkNyRxVfHF4TAUq%2BlOvYcOh96pvr%2BbKzbz34vxIMj8JnvsnTe2w4JKqYTn26GJNQlvNg5KrnjGoVbQioVszEPQDsB1OSc%2F8BuvXA6F8gyp3r76jQ2%2FAX8U%2F1pH1e3E3LitJjxUm0sff%2FWX1BZsrKiIkiweOR6uNRieAEUKZopvz3lJr3lOh%2FywB9p6pDG%2FhEOzfcuDQgP%2B%2Fod5tPjLzYw4f5C%2FUUaOG3acnmoYQAcoGEi%2Bne0%2F3mcNfuZoHFAlRSeXO3d2W5RAFyYeTrI2OZrH5lxZmeAEALNAXVCAWLSixqTcx8XgYF%2FqZbtKTCXuM3NBjqkAWMzX9rgn5pie6Boe9r6jaohDjle%2BUqC6%2BYrOooePcxF77fmS4R7hvWv%2Bzlyc1B42UbgMNR7thpfRKj5C4ZE2t%2F5oxntP5L9d6Gjx8bQFrOIWZYlde5hznXVEvn6AP4YFXnp5lrLeLpwyPx5Ozc8G5nNidPc8R6bkzoLRCevpMvM0XuXlzZqvooLF46sNgYn1xitYW3ALtWuJJOKaigllQgmrKxv&X-Amz-Signature=f68ca8a1ff7534feb947db031bceb3e6fa6a509ea41db90cce2d9492e4049f45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


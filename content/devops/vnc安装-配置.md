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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ5QXFEK%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZNBwpHURZ1eOmZBLhTNA2RSKofepVDOS%2BslOG68O0zQIhAKi%2BU7c2NTgWua%2BB%2B8u2SqVGOWEy%2BPuiAZ5z1dxVfXRMKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVV6pu84EeNbsmZ7cq3ANfaPu%2FObqRpDI9k0d2Q3UBxRjJrRRv8ASTqGIKKvt0qa9Hlar4DrxUVMb%2FIOyYUMSBSu6s%2FXSGrAkBEZ67w9%2BfknKwUaS6DtdFuABl7xA1L3pcbTMua5bj1vB0wR061xrky%2FeiagKiuJhUpTBhGp5rE29Ki774nMpfj%2Bbq04lD0P7zzy4M2vqTLxmomQHVr9t9utKlshXCatovHPIs6wTiZS9YJCr5UFlf%2BKs414T9sgGAiBbbADHIwYs%2FlVgDlnYZuP0jrBe575sPsvMXYfa3SmZfuOJfV0QvKfly%2Fr7yDcmKaBGS5pJc%2BhxgrfSeHzenIE8M8mxCAb1UKTICtGeFk7rjmjwo43ON2XfZmhGCtxrWPQmosHIjOwqf%2FGYe8rgYABDOJEwyQBrj4HKLOYnTC5zRtRL1wGdcDGLfDNT87nre3H2LdezpDMDLdZA0N2a775Cafi7JC6ZqiFiRhXoVWNQ0p5TfiCKT7i%2Fjy5vMSLedxlfGU3ajlFtkGj98pyeFGjDUL9%2F0e0uatBcFYKTDzKTd752HXFMDu%2Buc85oAbmnyTk0RxWXYh35vdaokapOQQWWeUjUiPKTzxDBnPAxTdyOCC7pskb8MHaFqbRemhfKpa72F2tVg8GWsUjCXmO%2FIBjqkARU9O332RonWpkTRUofycDjhRnBbWJuZUW%2FcSlIO1AonZtJTFDB%2BUcOVlLPJ6OeNz8Fc%2BZiKogb2010NuDsZLxLbk5zSS4txy0svY%2BL%2BsnjN%2FsA0tpU1X32Yk6Gynan%2BFke8qNmSUCwy14bRVcQDtUtHl%2FeUv0IRjpkj0UMCyNy8qKW9i5V903Sr9SPGhwjJwyIznFbU9hNZpt2C3pJEWJb9OqB0&X-Amz-Signature=6dd17f45f8566195e35e3bc98c75035b2be524b8642acd897047b96ad09af8cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ5QXFEK%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZNBwpHURZ1eOmZBLhTNA2RSKofepVDOS%2BslOG68O0zQIhAKi%2BU7c2NTgWua%2BB%2B8u2SqVGOWEy%2BPuiAZ5z1dxVfXRMKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVV6pu84EeNbsmZ7cq3ANfaPu%2FObqRpDI9k0d2Q3UBxRjJrRRv8ASTqGIKKvt0qa9Hlar4DrxUVMb%2FIOyYUMSBSu6s%2FXSGrAkBEZ67w9%2BfknKwUaS6DtdFuABl7xA1L3pcbTMua5bj1vB0wR061xrky%2FeiagKiuJhUpTBhGp5rE29Ki774nMpfj%2Bbq04lD0P7zzy4M2vqTLxmomQHVr9t9utKlshXCatovHPIs6wTiZS9YJCr5UFlf%2BKs414T9sgGAiBbbADHIwYs%2FlVgDlnYZuP0jrBe575sPsvMXYfa3SmZfuOJfV0QvKfly%2Fr7yDcmKaBGS5pJc%2BhxgrfSeHzenIE8M8mxCAb1UKTICtGeFk7rjmjwo43ON2XfZmhGCtxrWPQmosHIjOwqf%2FGYe8rgYABDOJEwyQBrj4HKLOYnTC5zRtRL1wGdcDGLfDNT87nre3H2LdezpDMDLdZA0N2a775Cafi7JC6ZqiFiRhXoVWNQ0p5TfiCKT7i%2Fjy5vMSLedxlfGU3ajlFtkGj98pyeFGjDUL9%2F0e0uatBcFYKTDzKTd752HXFMDu%2Buc85oAbmnyTk0RxWXYh35vdaokapOQQWWeUjUiPKTzxDBnPAxTdyOCC7pskb8MHaFqbRemhfKpa72F2tVg8GWsUjCXmO%2FIBjqkARU9O332RonWpkTRUofycDjhRnBbWJuZUW%2FcSlIO1AonZtJTFDB%2BUcOVlLPJ6OeNz8Fc%2BZiKogb2010NuDsZLxLbk5zSS4txy0svY%2BL%2BsnjN%2FsA0tpU1X32Yk6Gynan%2BFke8qNmSUCwy14bRVcQDtUtHl%2FeUv0IRjpkj0UMCyNy8qKW9i5V903Sr9SPGhwjJwyIznFbU9hNZpt2C3pJEWJb9OqB0&X-Amz-Signature=b115a751f1a62b0334f078296d1162c320639d717bd184706eca10ab9ca8f31d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


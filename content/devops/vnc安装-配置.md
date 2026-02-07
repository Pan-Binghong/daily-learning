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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DUZMQ3S%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0JytPUqesaX%2Fzt03n0WfV2ULo4xxYTpOCnKtc4WbDFAiAzpwcnBjkBNSN3tOKvtUK0B3PRC%2BGIE5%2FPKQIpsWQaHir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM72lDPAT8wBntqI7QKtwDLxD7TN1YdSTU6KSWpxpfKricunT%2F2v2vfpj3zJWYgCqHBWmGLuSqGpSMIZDmEyqJbrcIeoRXyQH05eZO1sKICYbFwEkg5%2FwyZDqxzqsZUPjZmLRdKyM9q8jwi057y871kkEvy%2FF9rdT3scDetxcL1uR1IlsNstVdslEtDEBtIIrQZhyu9SpL3wrGOD%2BLSLbuhirWU1SLtJmtiRitQE%2BVc1%2Bhgp8nyKD4eh%2B6FXZHoEKZZSJFCG0KjBknTJXgw%2BgTLw%2F1UWxWlm29TUhN3sIBBKFOCmbNfYZ5V8Jgwk1qZlSlx90dptOx7L4yqdg5BT4HAk3GW7kC9pqL0u%2B%2F8jbv4SV9UqnVg4IqxOkoi4W2hBPOYsR8jYPCQZzZsmky96oVGmYIRYPJwkgRXjNHGKuFJa7r261gR%2B8aLvhonug78OjCVyffkLWmrFkLLvnSgHqVhVqGAfzeqthA8DPGEwMNrM3aujB4Js6CUe6LnE9%2BD9HzuvtVxc%2Fh0AM%2Bk7kJIx3ouMTFNPVEKwmJtdyOay4uBof5mKMdpbRT3QcM0zvgHn2FxqZjCg25i77zAP9R2cOStDC6OaF%2FQkgdMXBwjrLAGf2IgDzzEQSgsanP9ICvjcsOLwxnHoxgHhaOxM8wg8WazAY6pgEAIwKr6rHGGPCSMrtTP4vgk6MNrFTSBoFTMLUsfVhua5jkAhW0TW29U8PtbI74gRqLNr%2Bt7kbsNsKAnUNoEbPi15y7A3BzumiDPIlfJHpK2hT9OKYQm0o5fR4x5xd%2B9mT4jvaXnr%2FpO%2FZzC0CdW4I%2B%2B0Vos3Z4sN2xAXaCKAGAGII5ISzWAaoCsJZGzwbicwQ1cudWEYeCN2sYXcNJHvrcjCAs0pUt&X-Amz-Signature=31da0d0aefddd7856bb18d6dbba3d9b215d4a26673e10e94b9ce19927eaede4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DUZMQ3S%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0JytPUqesaX%2Fzt03n0WfV2ULo4xxYTpOCnKtc4WbDFAiAzpwcnBjkBNSN3tOKvtUK0B3PRC%2BGIE5%2FPKQIpsWQaHir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM72lDPAT8wBntqI7QKtwDLxD7TN1YdSTU6KSWpxpfKricunT%2F2v2vfpj3zJWYgCqHBWmGLuSqGpSMIZDmEyqJbrcIeoRXyQH05eZO1sKICYbFwEkg5%2FwyZDqxzqsZUPjZmLRdKyM9q8jwi057y871kkEvy%2FF9rdT3scDetxcL1uR1IlsNstVdslEtDEBtIIrQZhyu9SpL3wrGOD%2BLSLbuhirWU1SLtJmtiRitQE%2BVc1%2Bhgp8nyKD4eh%2B6FXZHoEKZZSJFCG0KjBknTJXgw%2BgTLw%2F1UWxWlm29TUhN3sIBBKFOCmbNfYZ5V8Jgwk1qZlSlx90dptOx7L4yqdg5BT4HAk3GW7kC9pqL0u%2B%2F8jbv4SV9UqnVg4IqxOkoi4W2hBPOYsR8jYPCQZzZsmky96oVGmYIRYPJwkgRXjNHGKuFJa7r261gR%2B8aLvhonug78OjCVyffkLWmrFkLLvnSgHqVhVqGAfzeqthA8DPGEwMNrM3aujB4Js6CUe6LnE9%2BD9HzuvtVxc%2Fh0AM%2Bk7kJIx3ouMTFNPVEKwmJtdyOay4uBof5mKMdpbRT3QcM0zvgHn2FxqZjCg25i77zAP9R2cOStDC6OaF%2FQkgdMXBwjrLAGf2IgDzzEQSgsanP9ICvjcsOLwxnHoxgHhaOxM8wg8WazAY6pgEAIwKr6rHGGPCSMrtTP4vgk6MNrFTSBoFTMLUsfVhua5jkAhW0TW29U8PtbI74gRqLNr%2Bt7kbsNsKAnUNoEbPi15y7A3BzumiDPIlfJHpK2hT9OKYQm0o5fR4x5xd%2B9mT4jvaXnr%2FpO%2FZzC0CdW4I%2B%2B0Vos3Z4sN2xAXaCKAGAGII5ISzWAaoCsJZGzwbicwQ1cudWEYeCN2sYXcNJHvrcjCAs0pUt&X-Amz-Signature=d716601611f600c16d173fa34ee6c9e1c018c1da3eeac3ba73a4f35a43611713&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


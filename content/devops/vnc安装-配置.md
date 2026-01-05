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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SA2C46R%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCICPR1OSJ2l9P3cwQrHUCRbZnzh6Z8BuUgtEAlneKGnAuAiEAlX2Es0e9DungIfKdKmZr4imJLDcT7QitsMGcP1tN%2BQkq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDCVmDAHw4PW3Xj1uiircA3psVzDs11inrHqZj1ygAvQfTo%2FenaJgbeSbQAgaUEzhn0Xykw5C2DpV32HoRMxBeUkOAIXv1DccixIvJbGhYioYZ4aPcF4uZQycaMuLztCLdZg5ReErpUQKtGG9dntEcvyJFZg%2BN%2BIYBO0ujc01hn3Hq943Wxt%2B7PZGn9o5O1tvStWdcXHSuB5UE7DTnb8aygMJ4t7TzUZPiNAdxzrFLm1tP8T3t2hvwS9MxjWGNSUW9mpGrdAVNshqmQWswRrlRXkHfafawyHC9HFdT96%2FsaAAJJaTvYD43dwpUi4Wpi%2FSZCfyVLppmp6h1QSOQOgosvHSrZw0ZVi69JwxeRdbQHpaERANS1HThRUQ643iyTnIqY%2FSZ53yI%2FQYqwrDrbgqgPSfJO%2BjAcrE0myhitd7VsOe9PgXYAGO4svAkw5m2BxNVAOr7NnpujRhyga6dzTaQTyXWeUZeTQor8pGTsEWbwXy8jt6fTul%2B9M3cQaKIFG3iy%2Fz77nyEVY9B7J%2BZTp5j%2BcYZjQ9I7gaVqH5kJJyLAObYK6Vz0guSllRdqksH3P%2Fwe4NJD5wLq7LLEWK86yBe0imdYeycD6sefWi0skYmveJz087FBovLJTJ42HC9bE0RxizYwitlvF8BGrEMN247MoGOqUB7wU%2FYU1Wng98Nz6OZVv7P%2FftCaRciH%2B8CKlj3WDhIXgLyd1tV2ahT9hvvfGKKRq8pMogL9DQynPZyGJTPnAguIz94WYgGm%2B2srcPHS2YXjJ5UW8%2FPCced8nY3ZtyZr7JYh46mH6aZMnJt7ftIOOX3LRsyUfONa97l%2FVDfoXM%2BGibeFK%2BCZoYHv0AjFvZ%2F%2FAETpJIXao4deVBX%2BsPsAsg0AqGCrGp&X-Amz-Signature=69544b8c8d6d1685ed2744c34853deab9b13de104d53f29f5c5a277f5c042518&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SA2C46R%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCICPR1OSJ2l9P3cwQrHUCRbZnzh6Z8BuUgtEAlneKGnAuAiEAlX2Es0e9DungIfKdKmZr4imJLDcT7QitsMGcP1tN%2BQkq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDCVmDAHw4PW3Xj1uiircA3psVzDs11inrHqZj1ygAvQfTo%2FenaJgbeSbQAgaUEzhn0Xykw5C2DpV32HoRMxBeUkOAIXv1DccixIvJbGhYioYZ4aPcF4uZQycaMuLztCLdZg5ReErpUQKtGG9dntEcvyJFZg%2BN%2BIYBO0ujc01hn3Hq943Wxt%2B7PZGn9o5O1tvStWdcXHSuB5UE7DTnb8aygMJ4t7TzUZPiNAdxzrFLm1tP8T3t2hvwS9MxjWGNSUW9mpGrdAVNshqmQWswRrlRXkHfafawyHC9HFdT96%2FsaAAJJaTvYD43dwpUi4Wpi%2FSZCfyVLppmp6h1QSOQOgosvHSrZw0ZVi69JwxeRdbQHpaERANS1HThRUQ643iyTnIqY%2FSZ53yI%2FQYqwrDrbgqgPSfJO%2BjAcrE0myhitd7VsOe9PgXYAGO4svAkw5m2BxNVAOr7NnpujRhyga6dzTaQTyXWeUZeTQor8pGTsEWbwXy8jt6fTul%2B9M3cQaKIFG3iy%2Fz77nyEVY9B7J%2BZTp5j%2BcYZjQ9I7gaVqH5kJJyLAObYK6Vz0guSllRdqksH3P%2Fwe4NJD5wLq7LLEWK86yBe0imdYeycD6sefWi0skYmveJz087FBovLJTJ42HC9bE0RxizYwitlvF8BGrEMN247MoGOqUB7wU%2FYU1Wng98Nz6OZVv7P%2FftCaRciH%2B8CKlj3WDhIXgLyd1tV2ahT9hvvfGKKRq8pMogL9DQynPZyGJTPnAguIz94WYgGm%2B2srcPHS2YXjJ5UW8%2FPCced8nY3ZtyZr7JYh46mH6aZMnJt7ftIOOX3LRsyUfONa97l%2FVDfoXM%2BGibeFK%2BCZoYHv0AjFvZ%2F%2FAETpJIXao4deVBX%2BsPsAsg0AqGCrGp&X-Amz-Signature=c7f2d0e784bd3f955a1be1923ed0fb03ecdbc1b9bb04ffef7907acc83c2b6276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFSGRNQG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQD2k5H5KV5ko7a91QaF6fqCUW4MGZKxGwPWkuYXwXqn2gIhAJuU34mNtsqkzTeItr2mp1B5h2Bk3cUCMwyWSc69pxdAKv8DCEMQABoMNjM3NDIzMTgzODA1Igz12QsklJ4nYaavIaAq3APhZYqOZtkzj%2BMdSvGegNIRQ4y7UrchIq2He1v7tErD%2BiakFo3Uwz6jjxaU9WIiyH1%2FF%2BBbYhSGbqY%2F7y7%2B6kZmi65e%2BC0HmfIRSEGpfhRUqmG1wkz5pqSjvYaRrPfctGto2pZ8OzL6C%2F1rl8IHXyMfCO1xdFPbeEgtN7qAPE4yhZIpVwxFJXyEG1%2BrzN878eOtVYRWEZf7b86z2WEeF0%2F4ANwThDtLiZJqyCXJ5UwuSFDHGMhvVPjVc1ZOTfAB48g7PBP%2BvxzMkL86Q0429L0YxAU%2Bl8fvKdjvsFkIOchu3lrhrcfP4qLBEUeTu4U0IZmsTwEmlX6An93mAGgmHMbIgnKYQdijV%2FYWvhIdH6sr67NxkkjLM5sQyoOPp4rJRugaYNGaafS3Ikru2I2U2FGtIiHii1SaAd%2BWRi9u5jv3QaUJXqT30WiW3LzmLCA0wsAEqLxebmKcW%2F%2BDfPOI7fjC7GI%2BjwWSAAdkTuXHEswWyyepV94R1vrs7aR0J98cKdifS%2FJ95QRea71ymbr5k20UE0bx9kSAeXKWnlB0XXC6X%2BaYdtIcaE0taBnG97yid%2F9kHLztsCZkPkpNzr6fP4YvBtIVhL9ZxopIlSLB2jsJiga0CXJd4rXJLP%2FUQDDe8dTIBjqkAYeJu9WbYBwQtN2XKdg93aXDjQZtoHBhax%2B6Ei%2B86jqX6VEC%2FmrjqX7h3Oro%2BNvPB%2BnXQIzJepnTXJu7fmuz7yknl%2BpfkiQbOaC7lGYsVI0ZouqeDBgBSAgGLUniiRoIfAbtboFyWjDUJPm8jED%2B6nIEQIygdzgiuNW8cv2GYDxreEMAC9A8mE51DX8EWX%2F3Hgiq9USI4jwba3lhuFZV2Yc403wf&X-Amz-Signature=9d718566b92cc0848251075f8bfe84411258243e3d5508f6f8ddd7293ff195a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFSGRNQG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQD2k5H5KV5ko7a91QaF6fqCUW4MGZKxGwPWkuYXwXqn2gIhAJuU34mNtsqkzTeItr2mp1B5h2Bk3cUCMwyWSc69pxdAKv8DCEMQABoMNjM3NDIzMTgzODA1Igz12QsklJ4nYaavIaAq3APhZYqOZtkzj%2BMdSvGegNIRQ4y7UrchIq2He1v7tErD%2BiakFo3Uwz6jjxaU9WIiyH1%2FF%2BBbYhSGbqY%2F7y7%2B6kZmi65e%2BC0HmfIRSEGpfhRUqmG1wkz5pqSjvYaRrPfctGto2pZ8OzL6C%2F1rl8IHXyMfCO1xdFPbeEgtN7qAPE4yhZIpVwxFJXyEG1%2BrzN878eOtVYRWEZf7b86z2WEeF0%2F4ANwThDtLiZJqyCXJ5UwuSFDHGMhvVPjVc1ZOTfAB48g7PBP%2BvxzMkL86Q0429L0YxAU%2Bl8fvKdjvsFkIOchu3lrhrcfP4qLBEUeTu4U0IZmsTwEmlX6An93mAGgmHMbIgnKYQdijV%2FYWvhIdH6sr67NxkkjLM5sQyoOPp4rJRugaYNGaafS3Ikru2I2U2FGtIiHii1SaAd%2BWRi9u5jv3QaUJXqT30WiW3LzmLCA0wsAEqLxebmKcW%2F%2BDfPOI7fjC7GI%2BjwWSAAdkTuXHEswWyyepV94R1vrs7aR0J98cKdifS%2FJ95QRea71ymbr5k20UE0bx9kSAeXKWnlB0XXC6X%2BaYdtIcaE0taBnG97yid%2F9kHLztsCZkPkpNzr6fP4YvBtIVhL9ZxopIlSLB2jsJiga0CXJd4rXJLP%2FUQDDe8dTIBjqkAYeJu9WbYBwQtN2XKdg93aXDjQZtoHBhax%2B6Ei%2B86jqX6VEC%2FmrjqX7h3Oro%2BNvPB%2BnXQIzJepnTXJu7fmuz7yknl%2BpfkiQbOaC7lGYsVI0ZouqeDBgBSAgGLUniiRoIfAbtboFyWjDUJPm8jED%2B6nIEQIygdzgiuNW8cv2GYDxreEMAC9A8mE51DX8EWX%2F3Hgiq9USI4jwba3lhuFZV2Yc403wf&X-Amz-Signature=b9d531a495ddbdfb4380225f6c05ffce290ba879627a719d4aecd6d52d85f43f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


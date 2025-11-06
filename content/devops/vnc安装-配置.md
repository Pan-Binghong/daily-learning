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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CVBCME3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnHGOjiLenSBMauOj58oIlR0U89r8uXYJVplwCb7b55AiBMQIB3ZadLduB8ZK6iwdsEHv6hOthP1C6Y5pqReuPrRyqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBL2z%2BR1QfrzUmly4KtwDbJoyB6CUOQZXzxn5u7Zxi1ncWAAMbfsEn0Zd%2FV%2B3biuAngZ%2BhAvHeewsoSa8NwaOyDo49QAW901U79MS6O8r85uvJCqltSCLHUGKnrSOzLxiL0J%2FCvlsE%2FlMving%2Bn0EQhdZ5%2Be6pgSvlufFlatuYr7ay7vm13iz1jsuZGUOOGYrab%2FBO%2B3a4ywyStLqrClPMHE8HzBsCDhTnXFLDqGyATMKozESaEue5YlVfJ1%2BoCi2%2BN653EIOtk%2FsQ%2BGIf%2B5sbnarmWXj0yAj5FUoNLoFLn4ass85VKsDOWhL9AjWcCHIiteoFeHcnyXDOnDkeX%2FH3ClZvqEaCNLOrU6HKUJqtBz6OtNl27k9YsZ1BEuriQYtNiz1NCGFjyMEBTcJkd0OMuQZOv7flQ%2FqLiT9xuMpng4uZ3VCCrhwJvqeNOcmTwNFoI5WV77zDXb3UgcIjEoA1%2BNSyoZzrjRvfmPYlEua67M77vICeGhKW9BydFuvFgUH7RpWWIcP75QF7CYssW5XR5fVZJVc4wgCf5xAq3yA%2Bzg3jNs5UfRdOlECBJFowsnGxU2ykl%2FvRr6OoOEwDDW3fBGYwdu9LfTFGP%2FZHvvS840U5JnAQtWenmKrbJ4JDu%2B6X%2BGTzPrSCTNk0YUwkvCvyAY6pgGyxqHQGv6nOKnT8tkMeS2wp1SZp%2BkQyZEA2u774D62g5qTSN2DW7Q4ha1Zw4afGPwzvFbvEFG%2FikAcl9M6%2BjVIrken9qdR8rARVN0UjGbiL%2BYA1Uws6bsDj24KkimjD%2BDgre2SZxlOOWwmitwEZdkUeWPRBSqlEetOTfNvOVvvOWg0g4ao%2Fn4hHXomT93WIBP60hWn05rVY3cVuP0h4r%2B7yZTPVGrW&X-Amz-Signature=3267df51ff93672f4ec2cfb269f1f09fae173e2c1eeeea0b72db0a2dfc2f28b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CVBCME3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnHGOjiLenSBMauOj58oIlR0U89r8uXYJVplwCb7b55AiBMQIB3ZadLduB8ZK6iwdsEHv6hOthP1C6Y5pqReuPrRyqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBL2z%2BR1QfrzUmly4KtwDbJoyB6CUOQZXzxn5u7Zxi1ncWAAMbfsEn0Zd%2FV%2B3biuAngZ%2BhAvHeewsoSa8NwaOyDo49QAW901U79MS6O8r85uvJCqltSCLHUGKnrSOzLxiL0J%2FCvlsE%2FlMving%2Bn0EQhdZ5%2Be6pgSvlufFlatuYr7ay7vm13iz1jsuZGUOOGYrab%2FBO%2B3a4ywyStLqrClPMHE8HzBsCDhTnXFLDqGyATMKozESaEue5YlVfJ1%2BoCi2%2BN653EIOtk%2FsQ%2BGIf%2B5sbnarmWXj0yAj5FUoNLoFLn4ass85VKsDOWhL9AjWcCHIiteoFeHcnyXDOnDkeX%2FH3ClZvqEaCNLOrU6HKUJqtBz6OtNl27k9YsZ1BEuriQYtNiz1NCGFjyMEBTcJkd0OMuQZOv7flQ%2FqLiT9xuMpng4uZ3VCCrhwJvqeNOcmTwNFoI5WV77zDXb3UgcIjEoA1%2BNSyoZzrjRvfmPYlEua67M77vICeGhKW9BydFuvFgUH7RpWWIcP75QF7CYssW5XR5fVZJVc4wgCf5xAq3yA%2Bzg3jNs5UfRdOlECBJFowsnGxU2ykl%2FvRr6OoOEwDDW3fBGYwdu9LfTFGP%2FZHvvS840U5JnAQtWenmKrbJ4JDu%2B6X%2BGTzPrSCTNk0YUwkvCvyAY6pgGyxqHQGv6nOKnT8tkMeS2wp1SZp%2BkQyZEA2u774D62g5qTSN2DW7Q4ha1Zw4afGPwzvFbvEFG%2FikAcl9M6%2BjVIrken9qdR8rARVN0UjGbiL%2BYA1Uws6bsDj24KkimjD%2BDgre2SZxlOOWwmitwEZdkUeWPRBSqlEetOTfNvOVvvOWg0g4ao%2Fn4hHXomT93WIBP60hWn05rVY3cVuP0h4r%2B7yZTPVGrW&X-Amz-Signature=111ebcc943fcaa09179e1b249ebdc785890bce6381c23ccf7469e1ed14e14b3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


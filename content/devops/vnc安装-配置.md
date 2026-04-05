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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFU2MPZ%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBNq5aiBOQYnPo7YhueBoh6WqsgBCRFNpsUxlNx%2ButCBAiEA23JfS1yUk0pGoVz%2BvEPEydFvlomEPXs8lC4g70Rw4kIqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI2XHgMWUxG2NegoircA0SoABzxSwTq1OCAy2jCQU0LsG6Xxf%2Buvgi3EeA8E%2Be2sEpdpUTtIVEoK%2FiqVLIaQ%2Fh4O88fIzv70ylpvY2IEf%2BQV%2F%2B9fDWEIxHPoPGMEPlS0H3MNVRv8O6FBVdUDgjqljE97EMgUpBF%2BGK0D5x562Kg5omqjvv3BhbWv9CuUifIRIabjyg5DZczXAUrQCPJtESrnymRbXB3a6RTdWeALmM%2BREP7rJ%2BKyDOy46WajFgRavztUa7PsIkL4XCuJ84Z624BrJzlxNx6A0Mi6af2SHZVTBJYPb3oWT%2BIRlgTEY4YwR7ZIO%2FarfZLRpcbjzN%2BCRSbwzS8AJFlcyaLz9UxFo4o0f0DHiTeJ0L8FIPC%2BHpnF7ndAd59%2Bwa%2FA9CN1DEZYrokNqQAefWAh4jCORVWzWyMu1Ee4dn%2F89gCq%2Ff6iRSHF6dSv%2FFnEJuUcBcN%2BwDkmF18KBCjCCQ72%2Bvozhjhe4FBWFgrWT7Cg7INXmB0KCfWz7gxtNwuRr%2Bz%2FSr8jf8aQ8RCXdeByxfdmMJ3LBl03NoeMHFiFK1sBhprQqZK20pvx8iaTnBJ63TUKd8DTyPEyj%2F8q0iRo08M4tqQHOYSO7uF785uLGuA4Bs4Afq0%2Ba%2BAmEH3QiO6BfUVe18xMO6dx84GOqUBUhbjyAf2%2Bnds8lUouLKOAemE4wTCcCOQA3KwLE49c3ir6cZnmHzRy4Jw%2BY4jLf79PEE0wwVSvzxVzJaMBT3NL6qjLz7RGI2UTtmAPb5rdZdeG%2BCHmGocZEKmq2dlRmTRXhlz1Hl7X%2B3XwTeWXR7XvCz8r4t1aO61nkqtt4jlfx%2BYqd8bdP8uThar8kOQUili3dzA%2FwbRJOc3PE%2FUCGf%2BEu4P%2FTaA&X-Amz-Signature=32b47f7db3a984cecbeb3e3cc82ae817236cfa5f193475a4f232134f8bc1877a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RFU2MPZ%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBNq5aiBOQYnPo7YhueBoh6WqsgBCRFNpsUxlNx%2ButCBAiEA23JfS1yUk0pGoVz%2BvEPEydFvlomEPXs8lC4g70Rw4kIqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNI2XHgMWUxG2NegoircA0SoABzxSwTq1OCAy2jCQU0LsG6Xxf%2Buvgi3EeA8E%2Be2sEpdpUTtIVEoK%2FiqVLIaQ%2Fh4O88fIzv70ylpvY2IEf%2BQV%2F%2B9fDWEIxHPoPGMEPlS0H3MNVRv8O6FBVdUDgjqljE97EMgUpBF%2BGK0D5x562Kg5omqjvv3BhbWv9CuUifIRIabjyg5DZczXAUrQCPJtESrnymRbXB3a6RTdWeALmM%2BREP7rJ%2BKyDOy46WajFgRavztUa7PsIkL4XCuJ84Z624BrJzlxNx6A0Mi6af2SHZVTBJYPb3oWT%2BIRlgTEY4YwR7ZIO%2FarfZLRpcbjzN%2BCRSbwzS8AJFlcyaLz9UxFo4o0f0DHiTeJ0L8FIPC%2BHpnF7ndAd59%2Bwa%2FA9CN1DEZYrokNqQAefWAh4jCORVWzWyMu1Ee4dn%2F89gCq%2Ff6iRSHF6dSv%2FFnEJuUcBcN%2BwDkmF18KBCjCCQ72%2Bvozhjhe4FBWFgrWT7Cg7INXmB0KCfWz7gxtNwuRr%2Bz%2FSr8jf8aQ8RCXdeByxfdmMJ3LBl03NoeMHFiFK1sBhprQqZK20pvx8iaTnBJ63TUKd8DTyPEyj%2F8q0iRo08M4tqQHOYSO7uF785uLGuA4Bs4Afq0%2Ba%2BAmEH3QiO6BfUVe18xMO6dx84GOqUBUhbjyAf2%2Bnds8lUouLKOAemE4wTCcCOQA3KwLE49c3ir6cZnmHzRy4Jw%2BY4jLf79PEE0wwVSvzxVzJaMBT3NL6qjLz7RGI2UTtmAPb5rdZdeG%2BCHmGocZEKmq2dlRmTRXhlz1Hl7X%2B3XwTeWXR7XvCz8r4t1aO61nkqtt4jlfx%2BYqd8bdP8uThar8kOQUili3dzA%2FwbRJOc3PE%2FUCGf%2BEu4P%2FTaA&X-Amz-Signature=d68b83e600e43bcb03dee779dc34ba916cc8f27e17205266b53eeeae7716360a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HD6YHRU%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIXKmcGvcBmkilavdy2mNUOy%2B62e1cWRatA9%2FzPIt%2BgQIhAL2oSbKdk%2Bj8k9FdxOJewX9FY9wiHqVK00XA2JGTlMroKv8DCEwQABoMNjM3NDIzMTgzODA1Igw22TMbyk2DnB9TqOMq3AOfBDbaaiJmIaLyGY78jmoHOYHk8bOQ2jmfKSMGs1KlkFhhf0ScUB1L7qF8RNgB6T5fqysQ2G%2BzAGhmJQAQ%2F0EIJCossO8kDC%2Bq%2FrDg0%2Fofo1e1yJhIDmzsyK1A6r1u4rSs%2BLqQ6WNXOxYPzbXp4inPHjsPtj7nuxp6%2B3ujn1bXaOwlft34S12Oa4MwftqxDkoudH4UVkPnZSQud2ig4xs%2F5kef2G9Eb7A7lsE539vktUU0KVsY2SoCGOvtEqtuOJCPaU4dNBwJPzk%2BMVN1uuicVa6Z%2B2pFU7nHGTjb3hyb06e9BWaum%2FAED8kqTRm00GKmB3lXUpbGTIfiKJYoaxeyzF69IxUpfAL%2FUovNQX2IXDvCH5WYCyinTnQMe7YEF45yxhJ%2FL7BQHim7tBFa6zABcO6MH9ZcuGEXwg36dzxxAgKUgqxuOYYsskk%2BpOm9MJV6loUjFpl0g0ThRmov%2BSeXi7C0%2B9%2BvVDR54TbZ7VIzQwE1qr6UVRV2o%2B3RVtV2Cv1jHjIovaIAKH6N6KuOByqMK30eKgSJKfPSPB109ASskAT069ZMt0Y9eQilh8ceS9B%2BfJ6ab%2FwFna3E%2BMdkUKISZCa31AS%2BmkDPggHqyeFi5sju7rLIgBz%2FN7hkcjC10uDLBjqkARbuB8876ozovnmwqIhk%2BWIW%2By7Qr4Fnv3L2yEFr4rBmD9H6cZ4YVWtkjs%2BKFu4rzvMovo9xHA%2Bc5y0vKLcvzNA1RaCDnFcdWiT7lQUKAMkV%2FQBxMLoil6fSrV7NYHQs9Nc3%2BIxBq15WcZ4CFOFGjD8Hdnw98RDH%2FYiUKtLxGqjfSxgZupAsQ2siHNFxQmccLJMVtKH8MdWZwYimG1sm6sS8cPV2&X-Amz-Signature=7dfa04aa15c25d8b27764718326c21b622738b73eab24ac69a134d62e04e83b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HD6YHRU%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIXKmcGvcBmkilavdy2mNUOy%2B62e1cWRatA9%2FzPIt%2BgQIhAL2oSbKdk%2Bj8k9FdxOJewX9FY9wiHqVK00XA2JGTlMroKv8DCEwQABoMNjM3NDIzMTgzODA1Igw22TMbyk2DnB9TqOMq3AOfBDbaaiJmIaLyGY78jmoHOYHk8bOQ2jmfKSMGs1KlkFhhf0ScUB1L7qF8RNgB6T5fqysQ2G%2BzAGhmJQAQ%2F0EIJCossO8kDC%2Bq%2FrDg0%2Fofo1e1yJhIDmzsyK1A6r1u4rSs%2BLqQ6WNXOxYPzbXp4inPHjsPtj7nuxp6%2B3ujn1bXaOwlft34S12Oa4MwftqxDkoudH4UVkPnZSQud2ig4xs%2F5kef2G9Eb7A7lsE539vktUU0KVsY2SoCGOvtEqtuOJCPaU4dNBwJPzk%2BMVN1uuicVa6Z%2B2pFU7nHGTjb3hyb06e9BWaum%2FAED8kqTRm00GKmB3lXUpbGTIfiKJYoaxeyzF69IxUpfAL%2FUovNQX2IXDvCH5WYCyinTnQMe7YEF45yxhJ%2FL7BQHim7tBFa6zABcO6MH9ZcuGEXwg36dzxxAgKUgqxuOYYsskk%2BpOm9MJV6loUjFpl0g0ThRmov%2BSeXi7C0%2B9%2BvVDR54TbZ7VIzQwE1qr6UVRV2o%2B3RVtV2Cv1jHjIovaIAKH6N6KuOByqMK30eKgSJKfPSPB109ASskAT069ZMt0Y9eQilh8ceS9B%2BfJ6ab%2FwFna3E%2BMdkUKISZCa31AS%2BmkDPggHqyeFi5sju7rLIgBz%2FN7hkcjC10uDLBjqkARbuB8876ozovnmwqIhk%2BWIW%2By7Qr4Fnv3L2yEFr4rBmD9H6cZ4YVWtkjs%2BKFu4rzvMovo9xHA%2Bc5y0vKLcvzNA1RaCDnFcdWiT7lQUKAMkV%2FQBxMLoil6fSrV7NYHQs9Nc3%2BIxBq15WcZ4CFOFGjD8Hdnw98RDH%2FYiUKtLxGqjfSxgZupAsQ2siHNFxQmccLJMVtKH8MdWZwYimG1sm6sS8cPV2&X-Amz-Signature=efee613ffe1440be5a194bf9dbd66cd155d7107d14fde3e2c8b5c72c8e56d991&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


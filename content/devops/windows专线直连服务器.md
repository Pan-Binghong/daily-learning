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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XHNTSY6%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIHnycqHvdRikCdp4L%2FukqN%2FcUGx1m7VSGBeLOCIJaCbNAiA3jm8N21np0CPQ8dXEI2TRv6a6V548BBAy%2B%2F9dmPAJySr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMYqW6IFyeYVcUkZpuKtwDlGQGbIv3gwj8KAozOq%2Fm%2FBCb8ArqJPWaaFs2%2FUbMNTdcDof7VAbLz%2FgZjC6SJOUkwFtYQctTKqzNRe7s3qmgDxpQOxTpxONizOc8%2B5dMR9LVPtHR3NImp3ciATN7BI%2Fn1sWATq8Lm%2FhmYI8o1vdvziMGcBekRRedGKa%2Bt655Dusi29I5f6W9TIfoQ6%2BL89iI%2F3F0OHArNmUNOg5uiix%2FyeacbiXXczAUUkBiOXY9apEtcV77P5Try47mHPrOUt0nLqrVtOsP2wJbDuAlAqi%2BfVtiSulrINv8Wvh3yFSbdhmR0kvRuvMGtqYm0ZK%2Fx1Kc%2B%2Ffguubvw4wBH0qXY5rFnj8imqHnJKJYS9Of90tSuEcZPCe9vKt06UDSVJV0ImDfgBBa0r4NP4JvoEyJuCeHcf2kFSk7uV7osgWnv84bpp8HXKnTJysir9Pk2%2FUIpsEHucqUyXDNAERXr4ERytZVOK4%2FKqWatvZLyyLmpYFJrqmvo9GEW12%2FP3LB8fCndaOOWx7jlacoW5r5wLOdxNvB9RBeXXN1IvAHJS7GBnlLI1xkIOK0wZL2j8tlNPxjwM7RbiY%2FRhMyQmH4Dplg7gIqU9GDLHtPU076TOpZj8vpdrdoo1KJoQTweYes91kwvL6EyQY6pgEufTod%2F6Z49kay5T3JqUSa%2FKYwKMRO70cwGNsnIlW%2BvebuM9NS7lQcjP%2BbGvcePMsRafTk%2BPiJPvPN5AWO0OI1b8KfsAiXHIAQk3BV%2BCOmGWmrZNkhm319zgIqyLW3oQhHLD22frG1hO6ac8BM%2BonrIbEHCetFlqWN4LerhCs00qTpt6oM%2BU0BTwu%2FKI8Rn6%2FouHE7LfrBf1dZySYHeHMKJwvgj4Mv&X-Amz-Signature=8c029a56567390d663440d65b3203970b2fbd715b9c501df7e588cca3845cdf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


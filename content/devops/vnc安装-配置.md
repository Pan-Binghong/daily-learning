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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XQXWTPC%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCPfwgzmmA%2BuO7y1McE7mXae%2F8e1DuTyp9j0Xs35WH2YQIhAO6X9awP%2FLV9tPST2xgONeCE8iC6YqxMcC3mgJdlycHGKv8DCEQQABoMNjM3NDIzMTgzODA1IgxzhClnehC8cBAeBTEq3ANxqyDQNER8yImCNIDYJEgW6nkPA2n2yPtD5ZupfLAZgF7PF2mZq0eSNPfb%2BAsu87PHHk663OZn3uPv6bMZ4tfMJGxN9%2FjrVPPlqLtzhNp18NddDliEKnfdR1whhwX9vQJd9gUoB7Ip8phi6NlDUWpwAMDpyoYYSEDTPSdeschQsmH0%2FPM29vF026qnCQwhl4Uy2TB%2FrXgAhE8Vu2jsS%2FAKAYf0%2FbAQts80e31%2BtUtOINJiWd1jzaGDAPe3u1w1Q5NyEoRmqFPsZMH%2FIadwgMvr0uKl6cMc3RQ9PYva7UCG3mil8BEKi%2Bpkpr%2FZHhjwiZ5LTzCMmOy91JXgUgJRb6PcDOPxrxTHLSWYIieMCtHoBU8Bk6v9PN0PjwgYNOeXyXsEExk5Qy1FihqKQVeSmLPIHYAcdFXf8ivWIugz7yp9WnsLLkTtSNsucaVRHkDOHOtSkFl9SHNCvv%2Fc8TrtHe0%2BCIM%2FF6ty6XZV65dKrwxqtu5bn1PsKneKvP9t4ia9NDQwMNAWLRzXUki2%2Fevy9yyeTZYF1CSuxyKE%2BpARR0mLKTyzz3EPoX0z1frPsodw2crn4%2Fum3m%2FzByRIH%2FweI9Q0dMG4PpqWgsUnwltaanabIrxQlz6fM%2Bo%2BR0Cd3TCoj%2FjNBjqkAWUEpiy7SclVTxlt32NVeg62I7IZVrsdKLCmTH%2BaByH8xyAr%2Fcnvh6QyvmqKJdYaZupwizjevgwhzQeHCVbG1rh%2Flu1VR2LmaeIMydQnY0oEPlv6gTAHhrilTn6%2BKL1aSOWYCxMyu%2B%2BPuTF7i9KSueToYfeos5AsZGaDpnpJ4thqs1Fns6dWGhTL73CgIFR1FFdKIIe6hySmnp5qiu8lRpvOWShI&X-Amz-Signature=ca096c5b11f85ec4ad56e3b64e5c148db3ed4466c5420fa720c128eed164705d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XQXWTPC%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCPfwgzmmA%2BuO7y1McE7mXae%2F8e1DuTyp9j0Xs35WH2YQIhAO6X9awP%2FLV9tPST2xgONeCE8iC6YqxMcC3mgJdlycHGKv8DCEQQABoMNjM3NDIzMTgzODA1IgxzhClnehC8cBAeBTEq3ANxqyDQNER8yImCNIDYJEgW6nkPA2n2yPtD5ZupfLAZgF7PF2mZq0eSNPfb%2BAsu87PHHk663OZn3uPv6bMZ4tfMJGxN9%2FjrVPPlqLtzhNp18NddDliEKnfdR1whhwX9vQJd9gUoB7Ip8phi6NlDUWpwAMDpyoYYSEDTPSdeschQsmH0%2FPM29vF026qnCQwhl4Uy2TB%2FrXgAhE8Vu2jsS%2FAKAYf0%2FbAQts80e31%2BtUtOINJiWd1jzaGDAPe3u1w1Q5NyEoRmqFPsZMH%2FIadwgMvr0uKl6cMc3RQ9PYva7UCG3mil8BEKi%2Bpkpr%2FZHhjwiZ5LTzCMmOy91JXgUgJRb6PcDOPxrxTHLSWYIieMCtHoBU8Bk6v9PN0PjwgYNOeXyXsEExk5Qy1FihqKQVeSmLPIHYAcdFXf8ivWIugz7yp9WnsLLkTtSNsucaVRHkDOHOtSkFl9SHNCvv%2Fc8TrtHe0%2BCIM%2FF6ty6XZV65dKrwxqtu5bn1PsKneKvP9t4ia9NDQwMNAWLRzXUki2%2Fevy9yyeTZYF1CSuxyKE%2BpARR0mLKTyzz3EPoX0z1frPsodw2crn4%2Fum3m%2FzByRIH%2FweI9Q0dMG4PpqWgsUnwltaanabIrxQlz6fM%2Bo%2BR0Cd3TCoj%2FjNBjqkAWUEpiy7SclVTxlt32NVeg62I7IZVrsdKLCmTH%2BaByH8xyAr%2Fcnvh6QyvmqKJdYaZupwizjevgwhzQeHCVbG1rh%2Flu1VR2LmaeIMydQnY0oEPlv6gTAHhrilTn6%2BKL1aSOWYCxMyu%2B%2BPuTF7i9KSueToYfeos5AsZGaDpnpJ4thqs1Fns6dWGhTL73CgIFR1FFdKIIe6hySmnp5qiu8lRpvOWShI&X-Amz-Signature=9c0d52c6f95f318344145524119645ef7b19d8ca594751a55b6b01243a4174e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


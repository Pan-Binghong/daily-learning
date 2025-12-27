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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NBD5GQW%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCanGNUWZv9X6Z5Uyz3sy2Emmkm8p3ByN4oDajXr8p0DgIgH7Ee1MdlYZhguz80lRJaUXIaH3%2BTBRcWQhABXigNNW0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDB46PRVc%2BFH64X5YNCrcA%2BlEZwkCdV6W7GDzMie%2F%2BnB%2BXYTvD6RQNENYbO8lTGsKuoJ%2F80rflXVjwdHeDIiYij2dKy9gWiZnLMssNp51I0cpIvCZ1VxZkL17eg2SVMnYCIodZ572xFoqDIQT%2FNbtcuqJwgjgdTbmT7R2%2Fg691lJrC1tc3l%2FhthbTBWG48g2iNd4MiWYj2PIBZBhPqGavnXN%2B%2BYcQi5rRbTzAimlgI%2Fy9ETSCtQ8at73JYgOZM3SGmRAHNoEeJEpnD1na%2F0bXMA9hRTkS2M41l9K1zgR66z7N8mar0grau3oMFeVn8a3UE78gtmYLMd23dO61edRye0yvjgumbU7Ni6G1dbtLN6WGnh6Sjjo1vBxzMJntidm5Z3HA1m013Yr%2F2oa6linp1wzkmE0YYnjyiE1F7d6Z9%2F9gsUuxR2ckhIjLaRZodnDy8W4WZt%2BYvQ%2FI7bozIiwCAUA3S2hVQYC8obf%2FDuxLLjFvj%2FAl1xHjA%2Be%2BjLyhsOJwJ9TUy%2F%2F0M08FR761LL1amjVa%2B2DgqirK4fDILAYvjEODRfYXjdWr8UiqxiVrY2W8qmEAa16zqxdmpFizncFNVR3bE2n4Ox%2Fn4JSSH0VPl3G6arumNkXhb%2B%2F7NK3jtvy0ygBHvJdByjNzeB32MOnwvMoGOqUBf1hGkoBbHm5v7f9fxJNDkWbUSD%2B353nsXryMexFrK0GVbrrs3KKTwwMVtjmuqNgyfJnXqB0B5SGHiUDVLMh1LLOt8sqDznlRWGjwF3axf8Nsy5jgJz6L1HRemk6Hp%2FVjPS248pnO%2Bb12yb2qSYGhdkLHfYTgrumpr7E2s6uzbW2HwLcIr0r3RhAr8yUkcQswhO%2BOkU32VatSWPPg50U%2B7gx%2BR2im&X-Amz-Signature=a02546d78d300864918e73cf9b713f42e256732dc02a45206d4a5fc95f107b87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NBD5GQW%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCanGNUWZv9X6Z5Uyz3sy2Emmkm8p3ByN4oDajXr8p0DgIgH7Ee1MdlYZhguz80lRJaUXIaH3%2BTBRcWQhABXigNNW0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDB46PRVc%2BFH64X5YNCrcA%2BlEZwkCdV6W7GDzMie%2F%2BnB%2BXYTvD6RQNENYbO8lTGsKuoJ%2F80rflXVjwdHeDIiYij2dKy9gWiZnLMssNp51I0cpIvCZ1VxZkL17eg2SVMnYCIodZ572xFoqDIQT%2FNbtcuqJwgjgdTbmT7R2%2Fg691lJrC1tc3l%2FhthbTBWG48g2iNd4MiWYj2PIBZBhPqGavnXN%2B%2BYcQi5rRbTzAimlgI%2Fy9ETSCtQ8at73JYgOZM3SGmRAHNoEeJEpnD1na%2F0bXMA9hRTkS2M41l9K1zgR66z7N8mar0grau3oMFeVn8a3UE78gtmYLMd23dO61edRye0yvjgumbU7Ni6G1dbtLN6WGnh6Sjjo1vBxzMJntidm5Z3HA1m013Yr%2F2oa6linp1wzkmE0YYnjyiE1F7d6Z9%2F9gsUuxR2ckhIjLaRZodnDy8W4WZt%2BYvQ%2FI7bozIiwCAUA3S2hVQYC8obf%2FDuxLLjFvj%2FAl1xHjA%2Be%2BjLyhsOJwJ9TUy%2F%2F0M08FR761LL1amjVa%2B2DgqirK4fDILAYvjEODRfYXjdWr8UiqxiVrY2W8qmEAa16zqxdmpFizncFNVR3bE2n4Ox%2Fn4JSSH0VPl3G6arumNkXhb%2B%2F7NK3jtvy0ygBHvJdByjNzeB32MOnwvMoGOqUBf1hGkoBbHm5v7f9fxJNDkWbUSD%2B353nsXryMexFrK0GVbrrs3KKTwwMVtjmuqNgyfJnXqB0B5SGHiUDVLMh1LLOt8sqDznlRWGjwF3axf8Nsy5jgJz6L1HRemk6Hp%2FVjPS248pnO%2Bb12yb2qSYGhdkLHfYTgrumpr7E2s6uzbW2HwLcIr0r3RhAr8yUkcQswhO%2BOkU32VatSWPPg50U%2B7gx%2BR2im&X-Amz-Signature=70ab40e2bf62c12f483c599b7b41fb9aad33dd4801cbcd7a6968b79d2e94af31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


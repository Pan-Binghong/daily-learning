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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7IPCJUN%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDEEb%2F0CpXuxFqK51vJ9wT20EZhT%2Fgh9WHgEwY4W6gmpQIgF8s3kka9wzObce%2BhKzTuLXYzGbtMJZlSap6ydnhMGxwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0IFgtP6L7bgoFc9CrcA62bFHy01YdwX1B%2FG4uYF%2BIBN4elYpwxxBPmEy4i0M226cOEo3VwYayF2U3mJjihy4Ji%2BR%2FdF8Ayq6bF1BOhxRfumjSsPU85snyVizokr61wIOZS2ihzuooGyXWnoCOMbxbgbUO3%2BuFREwcXs6uKqudwfQIRD7VJN31%2BjUBF1ambPfJ5utxgafVR1AMBA4DYJNBb855EGSs8T557B7QwmoFVGtQd9xUCC%2Fe7wlv3C2UDK0TvWn7FetvDnfBWglM1h3cDJY%2Bscme3hOPP1eEQc8vWlvnFp%2Fg1LO603pQT17vQcHWSxmZ2JCyTSkNwN%2BPo1JSFeMgbDbfEd6EQS0%2FrvKsZDnmdC2VzJSSFwXGZHKwI9qnvitM6QTyJFgnSJLEFHPFJ8CVMW%2BK%2BQ2rfIYdi7Lp%2FsMWeBIt0srutBUt3GUjzHcvoghWB2qBFBxh8EyCfrKG0m8gRjjr1eiSovwnFcUEDQqs0ZH6D1W19oR%2FIAImU0wg8irncE%2B%2FgLuOKBQ805pQ%2BVGMffUEH2wHrB8Iyug1vU1U6An0TwiK1WuweSXZsvzjuzZlDSxJW%2F6ZQOIUGn6S4fDoSopHSDOKZZALhmRsdt7C9EC8Er6IrbzY%2BJ6EqH401okY0UmpZpny7MP%2B09MwGOqUBSTBbGhRx0%2BcKCveaP7YHfdU61inHs%2Bvg%2FxTsXjBv0mAFks49ThSq20jZR9DF184r1VkotfM1b7Ix2um689clXnBmAvtBFjSvkD4kN5uSf2W5w23Bj5awr0kOgDrEe5ptT21FEQCp8zkViVQkv93EuKn%2BCCrYmVukRPSAHGp5IOP%2B1QwyrrIesXPK5CvFw%2B%2B8LdHikmA44umMhygv08IlDtbr4cTf&X-Amz-Signature=cacb306345e6828d9d7f29b87617b650779a8ac90b9c99fc55f81c6930fabfbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


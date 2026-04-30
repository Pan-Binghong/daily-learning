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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKIZ7V4Q%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIEuXWyShM2V3xb4rLDCkjECGpni%2FR6G1O1xLVZs2erIDAiALgKzE1Fzf1i%2BpfOAvvWpBgQG%2BE9dpEr7f7hkZw%2BYEgSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMDralkY626fnadB0HKtwDUyOOqvjtScS9G0M6BuqOCdM4SYwF2NBWk5UIZAM6P34%2FK2Mqcf%2FAAHGEEm2tQtms9iJu9lIIR%2F00LkKwO5%2FCWuNL9fSdjO3WfP76mMuupqZR4R%2BN1I7HVHxNMimh7knSvp9wePkH0cJZZtCS9k7IJs3FISdIRkljoOuVzpEDKCBtymHsbRklLJVnMG9hi823ljSz1pTJpIPLYN0hS%2Fjx0DgWjW6q3BQvHiRf8l6G7AUNvg5HAvbWgQB%2BJOYc5%2F%2F0BwjkJja86qVyEu6pP%2BhF7ITORn4RmkbWLw4SwU%2BmyBZ%2FTyVxPKkmxr8pGLViiEw5X5IeCPBXzhuHoNB9WwOSldPN93wsMhyh9W%2BK0Tfdb9CAbgg178J6vkiqGXWuXOp5m0tneOxyTRycYiq%2FipCi752wMAFMgFOrrKvwZ8pYaCf1Uf%2FdqaqIP38J%2FhRnu%2FrySiB%2Fc78ubDBMmO0X4%2BV6Z77HnnDf69z1Goo%2FCSwn1EZef7LEheWlAeu8IcKoSgQ1zed1D09tlKqxbnFJ3dKmBhpFr6T6cyj0%2F%2BJAbIXcrTrvUJs%2FtyRlHNU2LmcUGhpwjBCa2oCwgBKbsUk%2FSIluCQ1wD4XYM9RpUsl0oLcIooZP2XKQK8g9S70rMoow7pvMzwY6pgHuL%2BA54LTK8MiJ6pU2EhNlvRkrmL1KeuZNZu6OGfRNVV77PQS%2FNvCApIWBFP5oL4ShFlKcaXKVomxz9dbjeg2rHG76cNtSUt0KE%2FQm2fo%2FVs2fXVkbClcttKGKIO34FK%2FEzKZ5goVD2P87AcWuhWmOKCjcwhpRHG7%2F5P0stnovYhWi2LehVsOS%2BUeDBJPc1S2Mbs2LCH6VFVetdkn1vrKedi290eEc&X-Amz-Signature=ad3a23f7c9818becde30f0f243dfa758f5554804ed7bbc8ccdefb457155f64d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


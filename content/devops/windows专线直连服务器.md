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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZECRJSII%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCWRGUEv8b%2FlkXJeLyFH%2FDEKliYrUEF3lrlOUDTD%2FXlBwIgY%2BoqxKEA9kuYDbD%2B%2FaNKNmfowY0RD5kxFc%2FjNPiodLYq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDA7GHo0xJyU%2BD0hRuircA1OUu1Gud7WJPmt%2B8W8TT1sNFfXBfb2%2FbTIRla71TjLfmuhDKbJWHQAI26K1QmPp0M1GHDgVhqKW9NH2IN4rpbfMgbz7G9WUtoTrAuUrVveRzTMPItO0I6OB76DHiFMUln2%2Blc7In0XyfD7VbLfrJ%2F7E61AhXTARzKugt5uFqbvD7S4E%2B8LsVNg%2BvP5aFCZahqbY%2BiDSLpCXGwrMWg7Vexqm9VoFJi9rifVjDsCmW1rp0IYLYb0cFCflHbqfapef4%2F4VJZMbIf2a7%2B%2B%2FXZMc1S5lKAvuJdrN6zZg3hIp8Q3PoLCwfSPrYR2piP5GAPvmtcD%2BJlsAGfNoXc%2B6KkP%2Bg2c0GV71qmjDuhqTzdPNpWx%2BlrKGj4Ikhun88v2Q95tQCy91a6wHc%2B24OV41KLkJ1kK2esJi%2BHrV9jzjdJm%2Bo%2FaF%2BPY4mT80Wb55kYYirC85NYZG9ULWWpOMRt06Mz%2F%2Bm8jLv7LhN9kQ5ixlnVy4xp5%2B7x7%2BsfsvcO%2F6Z0KqsLaeq4hnLcMByjAu4bCzfbpBUPXbS2Ba1YqBbCadiVVnuIdleentPilcrGNvCIF%2BZciIEuuUXtYp9AyNoH%2BFTna3VgvLzWKDPE9lbG4f7fCwHHPsdxN8DJLItJ859l%2BhMMiQvs0GOqUBCGHLpSTajXJ1jSlDX4HCewWyD4C5Wo%2F6o40m1%2F3EPlrk0dQq2rDK4AffYh6Qwf0t%2BDjkikmz7BSouUBFS7qpDjzgoBqsjTvhmbadUq0CAx6UxgcuRRXxCz%2FnKPAK4mc9tZKl%2FXNriWq3DRgNisLdXnQrz6AG3xGo63DfJCnejqnRDk0dH1kIDHy3rl41wW82zKqDDRU5ecORXq2Ezf%2BM9hPvTmb3&X-Amz-Signature=386e3473dd39084b0754554cc3e5faf0217dbae6a19379266dbb8bbfa45aabf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


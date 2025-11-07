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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466522TJGKQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGolJE1gFHprT7Kg203sCC3eib1akZzz1Tn%2Fws4n%2BFkAAiEA5FDoXDYhoK0SeesNqdWNvTWe3Hw55B7aKv4skEHrQJQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDElHmeHA59mSzfcYgyrcA5QoRRXNhio%2FhcvQSB176uNodfghfR695hZ87%2FEGto95CUtiLqu%2FWXee8eSNX1%2B%2Fw6Jbf%2FKY1ztHETVCC8HyTpYTt86F1I8NAb4Ir5AeTadGFUN6j4du1ipnGysjSAzOP%2FQkBgZ%2F%2BkabDP7bjmIACswV%2BjkMwA2os19bYbLQn4MKvylf%2F%2FyIVqqD9I8SYpaw3EPevPXicZgTe9h8FsngFG6B5s44hq4LgWdM32HLFCYaE9VdOKxSkANVQSsSQlw83Erebdtk2ubDLdBHpL512UNB9qkIjNgTWMKtRORdvljmSZxezf6zXIV3bF5npuIf2hnK1mtDdf74I5JURp98bpnPmRam%2Ba3yMIR7%2BkJCC7iIGtL%2BHiJaAGgE10RxU%2BH62k3sbmq0elieWCCor2%2FdzjJxMf9NIfH%2B9AyvlK5pt5JdDOtQ%2BWzHmnRVT2aSkh8Qnoqsg60bHVDN%2B4vfXnXk62Dr69h%2BH16CjoJLlY95AazasESl11ht3C6j%2BLZ5gALGb2ANO3HLNWImXiwNL9S1PwPJWrUVCqDa%2FWTVzvQcqCPDx%2B1YC3PzKGuoSyGVTZqVFTHAkZMenhFw4IWJGyqLZcPd2kDuZCp3ZuiKTYMUOiuSFlt0NELcQbhSd4wCMI62tcgGOqUB0LyvUgS%2FlrpX2Hykpnzqz4acMwVDerQiROoZ4jM%2FoD99RZSsCsYflaZ5aZXb0bIa9yI7shh6druMf0hy%2FAyXewrJLXRaHudMsNiaFPgrpvJlorwvJeuOXUuQCwwZUTNLqgpSM09Aeimfdy1J%2B1w29FNSOtDHLwnDlb%2FgicBh6BkeCVED3vJ2gZJBhpnYWuIJK%2F%2BVsehDjsB2sIY4rgkLrPyVxGgh&X-Amz-Signature=a8fa831f3526653cf65fb0f3e45df56212bf9c14d53d7db40164ff8264625c90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


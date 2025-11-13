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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD6AZBHH%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIQCxLzTVgSYvAlwrJ0I%2BBne%2BWSQhLG0qV8DQGheRR6%2B2XQIfQR7YNMdSRAX7v2OLEFlPHiigNRIRCxndutXdFBdj5Sr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMQKCfONX7ZTf1PyDqKtwD0nA9v%2FfKZDnrMALP%2FeI9SqtXLXuq9N7PmV1TYubu8kbAgbT0%2FQ6hlyk%2B5gQQVvLcMfKTJJigg7WLgOF8sSqwZLcmHBwa1W0ESOrivHAsymvzLOC3lpO0u9CSTg64%2BX5x7UKvzE9siEnco3oscLuEbgLuxvEt1mABfDiSDwiFMdPSBDLv72XkttyDqr6v46811NenmGdb2vanKP1cPjHoTykiBJ%2B0kUIA6PeLKMfWQvQ3tPzVa5vKJjIzHPllERoJ2cspVfmDzIIqdLvC3ELeyJbUCuvnm13yKJhmeyISDXXHOgYpBWqcKeLvPDBA3RL0PbH3aZflHBUa29e1gJyLUTdMYr40OfCWHUXwHjVlx9g8IIB1PA39bWSJb0S6iHdFzFGsigJeMmnUYCt75OF%2BFeS4PfIz%2BNjp6KX4t3sR%2FS0i7RQ366p7wNzsFaWI0VofbyH2eTH2KGHOut3xcjHjf%2BBSOTjb9q1K183sPC1b%2FykMu6TY9FtN9uf1MUciKCoA4F6NlOfJrGTL3TMJ8AyxQ5uKfeuGNaGB8k7EeYorGv9lOSjs2mkIc%2F6xHr0An9shLDBrlLe2k99Y6mFcmSCSX7bsEAkqMH%2FCmKbA1383R95EPWE%2BE9TyJ4GQbFYwxvDUyAY6pgF9LcBc0Iu72IlnbVUCi1h%2F7jy0lcQ5siprI4bh5uQdk2Bgi8mNCfSj9LpJQ%2BrosDjx%2BQ3ycwAjNmv1eAar86295B68deawokSMJHzZAGPw4ZPRS%2F9Ho0VSBaWP5BI5e5zs%2BFYe%2BCGicCGd6FHna1aP2CGW1f0xJc95jme1XpJqriR4mcRPrpgKMlxM3xDN%2FxqY4%2FZtQutmnaSZuf5LqL30Tjhlsjc3&X-Amz-Signature=483a887d46c86d756f7583988f7ea7f7b7d7676821c2a539922e0385a60828de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


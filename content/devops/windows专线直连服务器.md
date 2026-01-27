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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627L3J7C6%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAxQWrXV2o%2B9Cpk4R%2B4HgkK4EHSFLkZS1PMpSQFMNZBPAiEAwahnteLZRJcgTJWyuCOKYHLUqzox2WTUT4sGrCpwVuMq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDDOkA%2FuZUrYkhzLdayrcA7vmDJk3Gaw60X9ZtIhL%2Bf6OT61qVU%2B0g2WluMyKFbjQQ%2Bbfx1RNDmWOcarwaG0YES0jLoSSPAK0oaaO95trtE4opaTs11CJK5R7o0cA%2F8%2BRRTwKbbUloqodK3lg6S152NhCZZLhACjffZ0P4Fn3kolBHn0XMGoF%2Fap7y2EvBxsdo4gCeViqdvxkqoo4tKxltmdeb%2B%2FJmnin5EvglZpbwxH86p%2B1tsWA%2FGf5q8XsFTjf%2Bol3sZHJ3oHBS2Lc7WGTp9kehqh6d%2BMngFM3qwezXBi5VohqtearvT9%2BTLeIuAvMl09R%2BcMCoWXPPc0tmrZxLQ9qiJkG3kFKuinHeO4Yr2fr422HERTwQulHQIO7WZGqJHEvn1cpOkhY2GgeIQ%2BENNysCiNIF%2BpcfZlxJim8Nf16iirLMQSrNrpH%2FA5Vsz%2Fe9GpLBvHHfHBNYUDmd2FpRzGtkqobt6F1TzpNdE0%2Bk0QYxhGC5AXD%2BEOLh7fL9Mmnokp5hKPwghZLNXv8Blo2A9GsSfvKd%2FoGOHQtdo8bq6Yzoq9XDAj36NUHskL1%2BZogcddywJyLLWFxGCZFTMkWkC1tEA9r1PdJ2No5Mz6JP2Cqfulw38uOxaCn5xv7SWLYxFomULweQG96Wl8UMMTS4MsGOqUBIYz5X7oNk78hKI7KGPiN45CqXcebzyVpF2gy27gwtjnDA%2FX6sLnklgZJ%2BGfdtxGg2r7mIu3Qev7wpnz9dqOvGiBXHCcX0AliZ7GUZA4OWUx%2FUr6jtn0L5nxSc0OSuL33TUDatwED8zZzP7Tm%2B3OG5hvfxf7TCQXhgPXIZselP95WP%2FQpQEQWfBgH8VQfQ3WMpEERJ80nABwXLL6SiV92iSGx6ICq&X-Amz-Signature=9d591cb088c7f843b5d5c72d16d06858ab087f52d9b2ef32bb4456c383c68bf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


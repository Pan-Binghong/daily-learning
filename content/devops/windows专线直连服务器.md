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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWV6VJHW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD97kRHIYr51c4htC%2BK6L0t9xRcuvS3tJJYCtjsSDJl0wIhANkPAANG5gZXYU8CO9gMhgaKG%2FPsX7OEdVDpXKa8OBHmKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxX%2FfFQc0M%2Fse0Jlekq3ANso62BI4BCs%2BCvE1D5yWlW810mtrZEGAvJfdhSadPcdsiO69gyQy8aqEgqoxrcx539vAdNTadtCKXAs%2FK%2BrjLrI9p%2Fmncaz08L3Dk2r23j2ynaBZPwUNrgVWgjqxhRLecX3jUey04cLfQGjEStlFrX6xLNEa%2FzQ0%2FoUC0YauBrELqp5Sb31flQVnEatdZlmD%2FovPNHq4r55T6Md7MguUH5eVMt%2FcAYT5yIN%2ByY%2FgaSzeqByxryw6pZfZSz%2BKHQVZdzrS6A8VMNCF2btCw1h86s3hhFC1VW4L75bGODpG9h%2FUZ%2Flg4NCVonMYAK%2BslAEMeod6xlrxuWO69KpT91WNr%2BmfozmZ5S7DrrKy8KlcQVxOQKrmVRcmYoSf8mp%2BM3NKLh0yodzZ5zlkVgi09HvQU%2Bd1dp9tlXugu%2Fr7v0MT%2FKkfpwBM32pQdZPALlYmuwa8%2FIYcuGJ84TYUCtQ%2BTqB8zqLjz5vEF4ixCU2vxz1puKeNpB1X%2FZo6CvJx7DiVBabd8O8k76uw2W5gZiacBXJa4Jri5PRFI97T7yBBRcaWVre3sWCbVhfEbL6TjJecGhFGgV%2BeSL9Eu4k72IKe1hPYpPgY%2BAJOZKDhQkiEmzmSKaGlahivBwh6iso5vIOTDKtbvPBjqkAT2cs1%2BJSb6ZVaO8Z1KRnx3S%2FDcobRNTG4sjXTyOEZGbSN6b8GJnvXCi%2FQyJuqejNV%2BT8RjNVp1MtCB8YHJ0icAP2kbalRRrExWKUN4ncLdFgbYiwqK8vAozxg0E45KljARFFeJvNrEO9AkUURSvxieKde2Sf7YTrc63uAP9i4mTduZx2ilWa6kg22W93Uycoce9kJ1%2BLdf91hLN9oKysJFZvFeP&X-Amz-Signature=91b7af8badfb9e6580a0251066de4dc0d09aafbefb46b81fe9818185175b7797&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS2FYF3A%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFRX004LI5fokIyTCTNbJ31w4DeQvjSVhvCo5vT5VjesAiEAl1Md0mcd%2B4jHs5KWt%2BsDE3eYdKFePCeP32ppwCP4CDgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOFDYy4m01K2dSOlyircA%2FniPL1tGiHDkDnhUxAYxUziSqyXyirBWcnIi%2FjO9Tz2JwACUgxweCJjXwxPHvxWQATVgqxqqrC%2FV0uuVUaj8nny3xTwNcjO1DCjLdUvy6M0WoF%2FdAbR0qJf8nATtzZIEp%2FId%2BPiAXJ2ZtOcZkJ%2F3p7MowJY6hN2rzUJCtgvtFKgoXxBfp6E85B%2BrKHLJG9SHFKs79ygltLRBk1NilrLqRviaKCrfKdpXJk%2BOdb%2BXVBdjT97wrIOPoB8EcNDI5y37oNODjquHPdcO2OE2hY6cYBWlCmPqjtdbZWTkf6m7g5IVRVni9Bdw39AUaVyV0zaCa1doQRgny6nOvDjGHxKQPBdkzT5BD40WV0bc%2FGAPwDl7US5WQB4iCIPPG8GisS0%2FIfziJo6Leg417dc5AdwPaoWE%2FSxVVvN48MJIlmx%2BAUH%2B445RmWLGY3AR13aF0Bn20eGVObX%2FDrovr63S24rxQZnmptOxZAwt9GX2hao9TnXKHb%2BOSstlXHoYEaNo4%2F%2Fy%2BtGJLt1kRfIASHPKyX76wa7vuTOkXkoAEE1nvV8hoFAMpyrAK0%2B9SydDjRjdWVXSpiPOPWOAsVgbH9gPqPl2soOZGzHruk%2Fmk%2BpFfD0e8mCvH3lWoDBEjA%2F%2FTMiMM7wr8gGOqUBve%2FAqLam5mvM5IJn28BKMa7ZgJoa3S%2FX%2FrIM0t97oSnVSw%2Fq0T8OS5t9b02KPkR1c%2BZmfWo8LdNleQ%2B%2Bng5j5014E6oygAIy2O1zntwkiCKAv3rM4pXWPVS85TdR35%2F3CbOTbm67wutY%2FXeinxUlXnS028%2FXvAAWfQ9k%2BRdX5K6Nnq3TBjwDLUhgAAmKrdv0WIw0TCtPhrXmUNH1ezEj8j1vhn3L&X-Amz-Signature=17f7fc45cb54882eca30467f8d466f4be56a6c63184aefc592d192f2a149e12d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT2MKWWR%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEOASPSCAIjC4IjEj9Jp5KP75lrZpFfVkljNjExvl3GWAiEA8B%2BaEAh1LERZURuaJjGUMMXPeMoFHMJNffU%2Fh%2FKO0JYqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHZKp5wOR%2F2RZJts7CrcAxgWawQ9cATYB%2BLixBVv31slugsX2qpRXs0jpVJLE77JsPl7o%2Bs1S58g1UNl0OTPqxFDAOVGcrlqKRkJlqO8Oj5%2Ft%2FAhmlGsYsnVUDOe%2FAlbsvVCT8tQOHQPTSj5stLBdwfF9Ot2AhGCC6wDi%2BQ9NVZhd8iJxF3g%2BlH1CbBc1TTssE7PCMe7ohn5YcJcDw%2FhmVdRPAY9PRYz0%2BdvjN5jtRxh0ng%2BIzRTJYYq8Jy%2B7UsusRCuJH%2B%2FFnFLD9clMQ%2B8bEtlav8ckotTxZcCRLGJ1RbJow0%2BEcmtC8jMQhuucqh%2Fr4GVgjpY5cLzEZX9P8CR5gpK4iKu%2F3gBqhyZm37Haopb3BGHg0OW6gYOqDa0z%2Fm888PEK%2FoWDWSx0vreGkUlesxA5fNJIhme5boDIo2Sth8rh62fcU%2Bnp%2FF9Imnw9uXfWumVwCVcB2CVHvane5K2tRWOSLtD3vX5el2UipSQuuk81l4c6Xa7JV0AmJj6lfRPez8aD7WHqO%2FszBFSr2ublr%2FUVccXlyFoN5As4xj9HpD8ZJQ%2FExQIqKpje%2FR4zvLPChiEUc%2B9p2j1YpZRHuHi8gs8pQgrTQvfSjN1N02lD9Un4XpH04JwWVEpfkscMcNsXzdTEiR4%2FrA%2FPQpTMNCY78gGOqUBGVhyOp38LB0cfu8J8lR6RYwOpb2Ba5MH5b2QPAH080Cn0tuhR3k0zC70SEXsagaq0LCN25gzchlPHNN4aiff1uAQY2ea%2FOmTMhI5BdxyJCOb6%2BU3ijWjuP30I3%2FuKwMj4nsPiBCvXD4EQ79L5Zv%2Bn9U27M3JBQx8uNeSeeZpAB4qBPWp06bojpUuEFKz1ZPMUuhjcPRZOO73xsQ685i3ajr2olnt&X-Amz-Signature=83ff1c5d1827786439931f2617e9bec4229cff5dfe24e8152dc6e5e4697b8afc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


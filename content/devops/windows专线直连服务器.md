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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODM2GJY%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQCjwelrdmreBOm6gE65UQLKNSH%2BqgFPK%2FAoVq0XZQIfiwIgTbvxv19envbZ%2BeYr1FYCjWbg4g9aMW3A%2BV6eVi43wrEqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLmpNyrHVeSxIIDa3SrcAz%2B7xuzzAo37%2Fk7T2DqmaEKrreZm23S3QsJQ0KAfD6AYgZNUEza5hMLhkmRo8o6S7V5BgnRb9wIuD%2B8fejNgYxMoUwhO%2FXr0NoAs%2FftCSjFJG2Y3EtXbPNaoGGr5RyO4XtGDKJDbXEJJkiPLkGyQR%2BRH7e%2ByuAryoTZfeID50EDkB4amdg0AaSwK%2F%2FEyChk3gGVPueu5C93323ifxZzEPzGhZ1tA5Hsu%2FGr9YDlTpoXBGSZekx0VOgesM1d6T7G1GJy50meuJSy0IZedhPVcYKH7hmOqt1b6SNtD%2FSkFxCOPCXnZsgp1uTZd70G%2BXKBzaDgLEsmfXEl8dbI51mxCsMBWTMlnXUtP31wlXZds0c3aHHXYNED8sXcY20REf8LEpm8jfuMOaIUjdfOmPOVfcwJyGYaKWrWsbXH0gg4hq1BGq%2FHhUc4SpujOVWXNKHissmMK%2FejWgJib3gSbD78cFjM%2FOg3FROMVMAOV0pZ5LsPLP1PTYcMYeudp3Ey2owj0fYZM%2BXtoH3b%2BC9c0eZfpUvpNy1URstNEk2z%2BCS7FV4KBzSKwUOP4h0TaloAk4u22wIx8jHtereQBe5HVP4cM48u%2B8RZ6ZoTMatbT%2BACb8lG68d%2Fs1uuKrFAFgn5vMIHsxc8GOqUBRExQo75WQytSccrXOpxK7Rt6366OGgyZBkpL6g%2BNKsi0hMxowEunR5dTcN%2B5rvt2Mqjn3YZQFcrBEWxN8kdx%2Fli3%2Bl4yMn%2BKnJZX6F%2BW%2FJsuxJU3dY4544DnV8GvUCANvoAi862o%2BDmkXjs5hLzvjBlDRF6rrH9RnPTFRst%2FYwxwNmzA0HIahOraAxuwrmDp%2F2qFBCWsDav8oBmCw%2F4S%2FJ7Q6720&X-Amz-Signature=9b84b87166ce0381db8c16217d795f276ed0c0032edb4a1721b177c1d67efec4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


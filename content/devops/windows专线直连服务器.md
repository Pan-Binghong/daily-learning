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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZV2EYHB%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOMJK9U%2F7yCFJ0UauyH2Z%2BPswkOdxLMbXKdeCU7%2BosVAIhAM1HK3BvelY8M4VfdVQaQDR1AssZPCcQCUD3ZnDIgp%2FEKv8DCGEQABoMNjM3NDIzMTgzODA1IgzRUbjBKERWed4f7D4q3APxvHWKP6RcVzIu2lCdbJktP5xBZ9jDrFHczfuEZA11J2WxFDO3T4k05cZaVBBb2Xc6If6x1KAAVgX15Bq0W6IdIUrryKTD9hTLFdDPp3d3jJZN0xbDNKe31y1P4MHHJrEd6BCNUFd2LPcPZEay4lgEHKqLeXR1OwDah97%2FmJTWMwBDvFuzw69cKvHDV10DawRuaxcSWlwVe5QUSGHL9Lxx0Jp4RUKA63taIrP9OX7SOjHfniR4DJLdmma64BbJnHyMtf3Uqy1GeevjLEJwYr0I%2F%2B05RQC8%2B6w2DBPJTS2sxIJpxuhwlz22OzEQ5zORQDyKOJFucoXDUi73K2WV79YudlNjpv230qSWyArr5raul6sYAEt2fcp%2BnWcbsXM3Wscueayb4G6yNHACKa7zFgko7LmYbBv45GAiihKWwQFrCLVkmjOQSEan1sp0IMz3TkviObxj3Fy87EMw6%2BRfDilYp%2BY4Bq88gwztDlohAduKuk5jHml%2BCGds9YzsKztwrsAWzhV3m32JHfiSd9rWZXE%2FKDLWHjCeYgp4awWPVyMORJlN%2FMfQliL3OA4tMw4wBBM9OQjrlbHbHR7qyFNMZ2q9LSaBho7%2BnppFByRy0glC6Cb3HrWsl97sdfZcCDDVluXLBjqkAcQscJFWiiH0YeAa16JleTpBOiSpw7krqeBEbHRRRj99C0LI6oxu%2BxnAw%2FBNGfWAe86Y%2FuaHANmuUfA2qmRc60jOLXgYEFsoo9Ec95Kh9LtS1P35%2FpVoB4FpBhjxFwCjrAIAy%2FCInn%2FOOJTBm6MSbgkDROnb7xh4FvjCgOeZYvzF2DTJRZmHJ75v2%2BySFiTJ1%2BwKp41sZYbPfM5L2X3n7vacu7E0&X-Amz-Signature=d5250c2532effe15d9c7cbb925a7c90bb0698dbb0b68a156f9f305acad4e173f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


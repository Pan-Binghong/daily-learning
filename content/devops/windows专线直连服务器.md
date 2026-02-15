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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSZ7YORL%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDBlBIqKcjgssK2LnraNEXTVk4ksV5BXLctqpJ%2Fz9CmgwIgcXImHEbMPOskQc7PKA%2Bn0MpJgbjoKBQmBqLBt2p1HxAq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDK1dz0fUxBNHgm1GircAzOT9nY4isQo5Oa3jGXRzXtc8XMDw5z6TmFUdksNe40fh0GR%2FoiiojKiaIhZtsHWB1FltP0GZpu8ForhY1UGMgWjTCloB3LFZEC%2BPQEu%2FczntxzzLoUSv0nBv6RnertF8W59ze2mQGfmki3r0FAAAfTtTb0MjoxeEQEl1NH6UK05pl9Y628xA3gRqRE8hK0R%2Bq8LeB6ir2PIY3RoaPbGLcbUs%2F1uw1NXCPdO3hwyJC7K979bhZKetP5X%2FCNouCosT3Nrwok%2FUmCkjp2TLMSOB9Ag0y6bFbQXS1XJLWMHHvMGelbHuL3zWDp5%2Fkq%2BWbC%2FkfKl8TbxskIVy6QbDbWdNQLhaol6K88EIgPrJO0X0OvRKCOFbM4OE7iFTf6PC96%2BExzEhY0myFwYf%2Bt8FOGj9CVp2fwcC2U%2FnAVrgShpbL86%2BYi1ha0H0HwbtdkQ95oepXLZn4SHEAe9har7c16k60J0yt%2Bcb%2BpkFMrRbrh7zBmfI6uFRsPoqDNMMmM028fD2%2BUn7LpbpyYePeWtAHWwvLSSFt7azNPkIBmHMMuweW1sEbcjSwPuONMSxso%2BBJpq3eDGvKX67xAcQWn1E80flO5bMeay%2FCt%2FUG2uBlWTo8n%2Bh%2BTYnyDjkDIVRteIMOqexMwGOqUBO1Bdf75LpY49SWGNSL%2Bo4DfgLlq3Ng9U2bPh19w4mhysUWIuODwQzgjoWDXLUS9C8VcPd6vZHMGZjFay2QuhUfgN6FsGlz1N4mB%2FAD1RSp%2B5sngWZgmI70VuBDUU2Zg5PjMqiEX0Ay%2BYUU3t2QfJEF6fPhW5QmcPG2q5CQdVrRKWAHSkQ1YAcZmxYU1V5HfBE6Bfr3cZzpNqDcP3I2%2FxIks0SX6H&X-Amz-Signature=5996099b860e1d3b127c98d29ace3958b0852cdb37bd521a67586f69047a641f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


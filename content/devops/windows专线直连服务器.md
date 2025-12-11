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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF6GFRNL%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGJE38bzPiibxECbFDLdfAzaH%2BQAtdNztInLvmsDIWLxAiEA0vl1d4UJ5oXzYcnGJEHXRXQD7INzbe3S%2Bz%2BqcR7zg2AqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgDuweSVf%2FsvVTDVircA4OE8qPacmV8a4XegDV484fbSACvmEu%2BOPHSHe8O3nJNI7mPivEl%2BOocvWEcNt1adDyM1XXPdKm1%2BHchN3G%2BQFkEGtmo4SnPpLue84hzfDtgB3opviwb4pzr1tTYiNw%2B7RivRKB6mbjgsuSYP4BPJT13WcCqdbPLU045rgw11MZyadxhEGDs1iGtz%2FUrymkkV1pmPInNKiTVLYainUhcst1L6lJXTSHYp2%2FGRetEZURYkuhm35y1tUPUPFagYnuTvgSUQcMEWZMTTAph98vt5P7v8TSsKZEogqn24TCz6EpyvhfIu5GnPADmooqBCGWGVDdmNvDlf8kXuPErb8yUeypRiQRDvc5dcGYddc%2F1dXJ%2BQF95t8vFaLOSS8QxSE9HUkzAGd67GTeAg%2Fk6x2FB1oeaa1877pYoYmz6EzzB6mJbiUSe%2FhF2PDkOcXjDp8L6ua7XQZdP%2F0gIYPL15SJ0IvGXGvZz2od%2FBTmFgzU%2FswOOirjYFKOtEJKjIRgy3cpACxgrAPxOdi%2FajAqTdQGmw051i033weZYcEDnXxIpYh1mAlT7mypZMrvyMSDEd8v%2FDB1eQd1mknoYUzxfu4xrMOQeYDwn3TzRCb907nvhu2ypm%2FmLCr5RgORyXzuwMKy16MkGOqUBGIhRNqcGphoRyTi4KACvBYkQk%2BBbXhFw7ttKv%2FDBh05yVCpusHHM8nDx6mVmWPBSCabciVPio9cO9QvwQ50zEblERMaCrL1AyNAYQ182St9SdDowjiHu%2F4DaTH8nuTSKSLLIdqGvurwOCsEzdyKGr9410Y5fdGyzqdgei7HZKdaYrl7QH58M9rXVkccR9bw18NsvgAsP4DKCzSp8E%2BnmQG6eqwXJ&X-Amz-Signature=d5d5b927fc2774feb33ab47f69ef5559e7991985a2eb7f452a9027990612a391&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


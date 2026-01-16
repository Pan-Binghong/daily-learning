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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTZRTYY%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCNNZEbY5Eyn4S%2BZW2b6GSWBfvVZAsaDB5eMAP34s4J3QIgKzAOENUmDyux5lY7RLH9m%2BMgQtK14%2FpT2TWmcw%2BMHR0q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDFnVrAvV9fol2OiIbircA5HKwB7JTRYkejZZRPiekbLFBqbhJ0OE40QbnmpKOGF6nggnrOuXvYQVjFCl5th4FEM6r1NZwnleR6DhYYNRHAtRxmm3z7p0l7gac3SwYDPBeE66TkjnjzCKgMpPHq2v1%2BwvREFZ%2BIbCP9h3PI6JFM0%2BoNfonjsl9WHlPC0CNdanRGNV6KmrIbhz2%2FqCW9%2FTobPRR4XCm2zdbGQZjzn%2B7rQ73uBY9rQr9Yhw6D%2Bx8OemVfFC8HBBjA68jYdss0KvKw3gmRpTJlDxxZMnNt06cbrAIprXkTz7wyWmhUSYhR6pI%2B6h%2FFOGwfOFnCPpa2G%2BSYYkZ%2F9wE%2Fc1c5bV%2BFKmtPc9X0qdghgpRuXaPadIbjE%2BctWcLuQiqebp02giEAG0Vi2OniYWkHFK9oZOCVnhpW7EbO1AhhTrHt0Aps%2BbuSv0Wna%2BZqbyyjfsA5sMhdxatf922EmFZVmNPsma0OJFHh1H6VsKN7idPVA54z3MV5zCBKbz1Ge61gTM7Ge5Alj%2FBDWj9KTyof%2F40zA%2FfoR5EYiGqCzLZTkYuFvixYoJIBMXKKFBtntrLmPeZacjuRIuWhXmGWXprG61DRGLbEejnG887onRBVCKWO1yOcIsglGZm%2BTKfkao6Y9MJYJKMJXApssGOqUBKHpJD9JeKFWdNWbHvHj65oOM4Y9Ibq11VaEFg%2FMb1q67IV5W4ZJdUMrLBw7GaFCHZkYB54%2F3xba9IIuDnbPgtDQvxnGfgtF9ev1Os6oi4pShyCTdBo%2BacSEznntlBxQpTW6815w%2BiV2YkTYBHgzQcYLD92hW0VRndhrI2ApQyQJRoCO8jE8mbHWkSubkyBb0NZTPDxyGdiSuylp8Da6WLtnQpnj%2F&X-Amz-Signature=1b496d018a6516b32f8a6dd429cad9137255bd39ef6ede427c9ac865095cebe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BSVR3GP%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQD2nwbtdu%2F%2F%2Fg6g6HeUeLCcmu9Sw2J7K4aCgFxNQgIbswIhAOR85S68VJ1paKZpEOJobJ4a3B%2FjIeJSUXBLc%2FiIvRvDKv8DCDQQABoMNjM3NDIzMTgzODA1IgzvlTu136eeev8LI%2BYq3APTsXx9zqQQf%2Fv6aORX583Ud0vTZFXwT0mEjXulJf2asABAODzT3NPud%2B0rXyTazwZ2%2FdcPI7vrgV%2Fos4SagZpCzJkvu%2FeflkDhg9bF8JV1j3V2cu63zVjmY8a3R3FRfLECibtwAeVA%2FBE2HBp0qV%2B%2FFKVe2hjr6bapaxaGlUGeBVKZ8WrCBjSgJwF9LAR6fcGkKZiKoKDuISJacTxmhONHb%2FCNM9TaDQp2cvl7X1jTGXrJXV6nLeG8xb8t5hDo3Y%2F9O6x1j8B97vSZI9JpqqFkFzqrmbUh7QFTfbpUvHVqv4YOHqUGGyWqrODFp431RT3%2BnrJe58NLpff%2Fm0is38KGVyyRJpMnKJw%2Bzemb7d0ZGPSvVEExluSe%2FcWlPQpha%2FbSjVSHzKSIc22MkxVq7Pm%2BfR%2Bud92OqGLUFUh1VMzIE%2FAoo2tDBo%2BiolOr2EIl0dTE1j%2F4BAkPqRDchAcWWBkct3vMGKNNCm1Q8cAI1DHqbg9xhtOhVlscNX2%2FQUpWCoyryyej9o3MNlPuUlX48LSODmASE93o7YfQ86Fld%2BaDxNkqwHV0zBK0uXVOB7TlccV3la27sUsTOqEA%2FdqcmiVevg4cYV27IreZxdB8htAizyROMNFrGRm0pgVv3TD9%2B6zOBjqkAfn%2FmPall0NfNySWqJT3YWIEBeyJiz0gyVmAMaSVHmc%2BCbe1cMQZDNAZuM17ZynWuSVOaopoXAAkXN8fPJ2o0dY0FKfKnLMrTPKmSw%2Fy47cHEjIrq%2FJmsFc1CF70A%2Bl4GM7TbTUTfJQok5RRbW1u1z9yQJiiHLeBhkgBJQZlE9QEcuohFE3ljQ0%2FQlpmufgQbVlyq6dthPUVGiNEMwpnBsuXI6lO&X-Amz-Signature=40a60a20a4156077aeacf78191ce14e232d65a546188943d107fcef84893959e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


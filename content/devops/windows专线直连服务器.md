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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3QZLRI%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKkVleu65hh6%2FES0ZqgGMgaxTJzSBxheePdjMiuXWoNwIgJATS7e%2FdQZCQHivFePNijUze0K4e76%2BlDU0FSMzByTsqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOH0rto7JjHf7Y5LCrcAxnnmG8bssOqyaBhGagBZPG8ySi39FFsGn96dqnOx1ZSLE13ZPtuebGiAK2aBACQnVpFtZEblFbOQ%2FOcBQzbC71hI2cEZQksQymytYVi50Qwc8XyuxcsAKSLU23QdQeIcJGuJAgHudufdDATOTa6pl6T6l2myOg4a0qeiyjYCS6WUa1p5049DOi9WYijNBm7WlQkTroNttANz%2BxeTEkwgeQkaJ5HI%2BQh5OCwdxCOCF0jExjEVcAePajmF%2B%2FFrE1McwIyb107IsMgSg0ZEMzaVe8dH2Fwz0mkwr%2FOrz%2BSuC8r7Yepmui4jdJUQRce6zVu9QFLvVQAweM2Bc3NsUlJj6eN2xnis4XfCEPGJSQ4fSNC3xgCJ1ZelD9ss29FFB8vhWEMIaAj82ACgieoBwri5R9kz91g4KSADStZgMfZHW6lK4wl5WIRW4ZWosRl%2FYnN01PFkMzfScNOSsJVARBto4xGA1pc%2FAucqqaCuazmtV4KifTDmHDt45iCG%2FwuLWM8Imkrtud4%2BN0xlyC6wVlmNmPchQ7zjhgasRhhQEYBSih9zdzI8nlQ7%2BcpUnpqjSSFtbGG7Kn5KYSK5EyLGt%2BsBc83Kml0wHRUz8R9lkpPSAZt6qt2WzacqyAtUCW2MK%2F1h84GOqUBlIRwc83ZtCDVfOJ3TuQpZihNGELxMQbdQWvsIDUXZtTTisWxUe5Fhs%2FyafjgNmDsK1jqloEsg04vWaaCC87F%2BHq9HQIUu3i8O5VNTy9g3jD9NW0JYJIAJARv3U%2BJv6dPawOWODpWtTxQ32Wyker9UoBI0aTsdjH0yE4UH54Mwf7F7Qt6DsJgBSa9T%2BQACoOXOr7pacYLJU2He1xFGsgEoRdKeIJC&X-Amz-Signature=8a29c3c1dd025b49b6443c97285063185f8410c802ca2f7a157102feea56e686&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNTOJVA5%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFEiqzExLCLFglCl6NE2PSIOInfySCGtHLkF1FIZcMUQIhAK0m6vf0a654sDj8exGyRtBp519lfm0CkPO8tBCPtz%2FaKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzL5ThvJ3eUkS44pMoq3ANtsSGklJUqPJzCE0pDYQZ3945tY0%2BURWAzJrjoPVFIngVuacsbr%2FjD22nULtjDY3lIUg0D5hF%2BBPV1ABfAoYvjo%2FUdQkhyX3LjQqooPRYb%2FYcoeIBJFsHMSNFlYbpuyG%2BFRJVPfc9YcYJEqh%2FnSr6BHgrNPB%2B65avFueeVdZTpWent4BNcdpD1M3136hU%2FpMy%2F8OEUUm0aTg3bBioxgKlVMxw%2B9%2FMZsoBxleEl8Crt6AWvfMDULrZCzkDArkqn%2BouyK2coOZCw78kHh8J99DRysCOX2Vj%2FP8BbdEeU%2FF0LmOMhBbc1jVHZN55KgfaGJyK%2F18GFdcZy7%2FRnsAaH%2BUqSDa7tBVDnHveFnB5UjHtk%2FBA%2FiT%2FUdVcMUiRi3Fct7nQ9ThXbFY11d%2FC68IuMxpvY0AtLQ9c9I2OW9gzzPCCsfuqIINcSjwUFd92KyIiQG1iSwtWdCmaJ3yMqBM9R2a0epAW0j5z4KuymP02EtuZskCzQFvH1LqqSPV69uu%2F%2Bdsn5qvQU2feqwGFSm7AmSw8stBmB7cKQh7M9iGo%2FGhVaKe3AItdEQ5SYNkLJ2pgjfO1hbskxVQnIwlZsJdqHy2SPxCBugZfB2i7grtVGDqxA7C2r%2Bjx55iPLj1NmKzCytpjNBjqkAShJE%2BBYs56EzNnxJBuTjqr4TK6S4vw5I1Icy40vOIYT%2F2m8Tpj%2Bzm1B3w6wPVyPmZoTDUrk%2BWtez41jOWdAT2kORM8MB6RvhVmFVIDfJxjaqyGqjUa%2Bmgg0i2wmP5FWlWKDlR4UZm%2F6MiqqXqZgY0sd7cigbQdn5BlxqCVtgCKdOi71%2B%2Fl3cRnmC9szJh921tDV%2B55WWgO%2F0tVuNM%2Fztl30Wgld&X-Amz-Signature=a016099282a0c5fb852cfa2d0b090f23990b1d2231802298d25670185806b1a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUFDT4SL%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQCFu%2FNadfBYODFB5y3L%2Fikvv8rk5CZec%2FswHWlTh1%2Bc%2FgIhANUMRe7cQG4t6JeP11HUMfd5AccYMOXVTwzvaq6N8iv2Kv8DCAMQABoMNjM3NDIzMTgzODA1IgyAQ6qR3VFHU7C1bjcq3AORLUhSA5oTy9mNbEd1PkOrir0yYfZ5YpVSD2KHCZ9583RLRppnan4R4KRkp78zxbnq%2B0ztZje4H%2FwfcBwth2npazqWmIzUa2EK4IfilxY8IuN%2FpFVAmbUXqmxXIykiR6PJei077u7TYZaXhjSq9MvpP7TEeb47dyAYhE3eMVySSEe9uDvs3kbcjQo0VpIxtFq1Q77%2F5gBiDzd6GP0S6sF9Vy9AofhiTPNC8G15xKrDqgi2IIe0ebsqKHNBSCDTsk%2B1%2BAvwT7anu9eaAPbaZODb5QaaYFkQxoexyJlWJ7uX6oIat2bFvfHXd7fF0VBc4yG0KJ3nHZ5mijCDuMXDVLizpff0LniMnFOARC5mzSvbtX5IircKFDdpPNtqz2c65EX32zy4YSE7KT49Jfxw2ZqaNaE%2FGKgMLhCmzMHQRzf8xjY2z2MHo78ai4wj3yaNnztVJvmGUZcAIpzh0ad43hvGoQXoj3JgVu53zcn30WFnEF9Scl3JR1Uq%2FxwARLkMi6ynuJ95bohT3nLnquyRlAfRVRvRXTNXAxh4KvAaoEEG7bBKBEYuwmkClwRnB4lk%2BscXDsNleDeH94DtRKzOGzjxr6%2B2wP8Hbgr9pR9l2uqpAnj0Gj8I%2FAwJRBzR0zDQztDLBjqkAQn%2FZuwG5T2owbCGuQhSXHeehrzu5BhOFaBknoaSoLVfi1i%2BOeXhedIWYALO%2BHPPLkf%2Fcf5fq7de%2BtTV03%2Fp09%2F%2BKqAjLXITNqYP0YLF89lbARio6oGtQeDhpgqWC9X1BCWs7QVVQrOcTusX2%2BSSU%2FiTe5KV0cXqOFsUaWRiQ4whliicQKlUtFMz6ROCP%2BpKbTJGCbL34ZKiODTy3gcuRVrqUi3e&X-Amz-Signature=9211f9541f37ae6dafec1218cc8519b8fb140c906e114a826457ebae070d2e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


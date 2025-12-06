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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655ILFNEP%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCBhsmUn4hSJATu7NP9FPqe0jIeXAAlWOd4tlYeOljRQIhANbc9SIM3lOTOe%2B95yYXCqTfNg75QD9fQsHTroZ%2BV31JKv8DCGsQABoMNjM3NDIzMTgzODA1IgzQYSAvtWHbMnde4Voq3APvkQR1VMRprZAalY5BOXuMgS4X0ycGLXFxvPtWny2qAa2Tn2Ihw2qqoe6fz4Y7%2BnJCSp9gVdIKDlnb1c%2BSVjsSvzg02%2BKZlTzlScBr%2BSTpmexstMJ%2BOsTYN7lUggxco0oas4s8vVrxbHTK7CLU22Ilkm8MEaii4vI2iWdCy1R%2FdJj45UndbZnuLSXMTM5QTHhWJNPG%2Bl%2BCknMtzERO1AxoLfvbE6SZXEK4spFCEkCGUPyD7UELdMmXW8LY%2B6RpTc54xDgKFwTfRBP3QfijNAUL2zOhCYma1FCxggA6UcShkVLSfsdQPCx9MwEowvlkEvzLmg%2FPgdRSbRxb8uot02Z8CAmWOq61F2fCAXBBecEIGkkbumCR%2Bqnr6IHqV71ULCqKs6YSamdRlmXn2yqKbrsEai9rXNdrZ3lxg3uBdU1QzxeVoxLbQhsoIxpjEV87zJsQzKb6r2Y1XTzVIlU6IK1jB5JZmlTMAigwzrg0CnYrvKUz6g1zy0rYhgJhK6FqjrLEHTnfMuHRgHWE8wAp1Y2IzLtxDDNcnnSyKCMc2OqExxKb%2BFcKSnMPsCFbulbe9t9%2BT2iVfc3bLhgMBidgUiUl2cELii9ajgT6QsIogJcSecMCedFlA2j3VURNJjCNp87JBjqkAcFum4lH61Hikw9d%2FtdL%2BL1qvDuzZ9BZyG9Lakh5ohCEy6XQgP5ktL%2BEL9Y94tm7Q2mZdETXyw2k8zAFIAzindhpP2uUnRIEzqc7V3FseIxl%2B99nUiNNCjbyl9XGnAhiKMVWivEQiQ9Y3E7X8O2qrU5rqx%2BU7HM8%2FVM%2BPyi5Zv%2FEKrZrR3Sfg7eismwpNdOfuo%2BzLFhlznNRYdTQlscj5MHYgs%2BI&X-Amz-Signature=51c03bf0d458679ed29d8e96ba8e7f23e07c8251267d2a17871d02df73de2eb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


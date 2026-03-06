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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URDDTLCH%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIBRDsxZJeIVGE6ih3E3JY3C25V3nAeX2ad9YWUGBsgvmAiEAjSNwuRzsAGcnxDhHg5%2FSXUo54bhDIPWgmporOFr2SIwqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNO1krMQSwa98VbQjSrcA%2B2fAi%2B7Nf5%2BfsudyUBtbDeSRLgOISNaYpH8nvemFxEOomY16vOZnDN3dRAc1c19%2FtaJ6eUbsnKK%2BUvXOKVGeEDdGm6H0DTOwk3qo9aH8UI0g%2FyF%2BIpOzogaDPUqh1U%2FenernqWzAPdKqnn6gcXrG6T6tJf41jbVHczUrfSXSP3rfSVVYZ6oe9rrSXgT6oLz9e%2FBkB%2FxpIL8OBJgeL4DDjd18Tr0n6orbRUTrmgjpnbtDOr8DPFBHesaC13kOSSuuHRu3sh2X8rcvk2DHaMaXxdJqVrnpbWhf1cn%2BD8iWLcToXaukX3JEbkaj9cqti904e0HVSwXQtB3zru1dGKbRK0NLuFgYKeK6yLdhPVuUdp%2F%2FeQ04iP%2Bhc0%2FxeZCYqfsN0iwP7AtFu3O%2BsStTBgFcEO9B6HHD4j9rMtey%2BxyUx4FJDy9Jj4GX5T8RcwpKEWL6qFiYtF2YO3IJ0I3Z2i%2FaMWp5gXPgD%2FuDMGScHKQYwC5RCudek7ehKgbiiWyzvTw9W9EEPwj6ITJIdcfY6bnsdoaj%2BY4U9olQF4w2hRDxwsyUaUikUGSpe0Q14UuS6fWIlX%2Fpxm%2BHZo7VrwIzzboVSTIwH4%2BGzMK3A2A3cP9OErMR9OVz97B%2BScm%2BZSKMILQqM0GOqUBy9y6YB0oWuN3f%2Fx0iWHdEZkgBRcPBD75jydwvqrYiABPiEGg3V1gZXJ%2BiyFRgS8fwgC88jFtWjvgQLvaPksOAmQqA5xsodee8PNJYzctnx5t6%2B6isd5ZKMPgoNBNxcQQlEgFGsLMPfRmVBivI2kVh1xSAmMoW1EFhck%2BDu%2FaRfKHczypFL3cQ6r7quPXdFqkL0HD3h51ld5vLGOmCE3RRDAMEzDI&X-Amz-Signature=a89da070773ff46ea6a6c1a6d99347e86665ac8315be4d68f8f1a329b4390788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


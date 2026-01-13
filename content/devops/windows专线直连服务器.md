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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZLH6AGX%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIFqZ2Zv0NleeUyMPCgmwrO5yINp0%2FCzjW91znIg93A1cAiEAxWGJnQ5Nk8ynVB8sNrBcqYzmwdtIx8F6lHG6opkfDfYqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEscuBdmVrUVN1R%2FGSrcA3fPTgPEPGJk8UuqPcLH3TprEmeX5Foh6t2DZLGItkOpMe2DSyLL83X7cYLMl1hLalo9r4h1VMi0TSHx0JGIkfzoPQ2ZOWPoXFfu7GkJ2CXDCO%2Blw9ktBS%2Bzb7jE9v%2B%2FUi0F5RXz9fIIR%2Fyvh3%2FMNy1LPUp5wBlc3DgpGZ1ogC3he9lW%2FkH6FrP3HsFE38OF%2BsmNgNblGp%2BLZHLpv64zhnF01AgVh1otiYegNSF4SX45%2F1wye6CFpMdjqpoTFJNZ5kQSp%2B94sH7B7XgQSnZNsu9PeLvQSC7%2FtADTwIqh96fVFIrJYk41baTryRIJtR%2BxAit878V%2BBsUNeobxX59XLq6dbrj97b38NHMFaiAjB%2BhhVkVWCsw76Bn0eZNXUgGJo2vmFrI8fgYtq1a5xRcFOfQKcCdzTibbr%2FRoVOBVOs63QowS5RDJiXbBoEMOenrAzGT7l8qwZ%2Bc6LFr74Hjwgm6r7j7Gngaxm4DqhVBMs%2BwzpE%2BlZLSiCPOhOVfMbPWFkVxtaBC0CiaJyPHvVtKPYxBqFX12TGZfkVXkDxOT198pdJXzQfnHzaClkm%2BHGAZIYuQabQAtAKx0%2BWUEOo9fT0KbqPibSYjtq38QDbH7Q3sYY9SQ3EZCKlAf8cvOMMfllssGOqUB95%2BPHA6kKQ283HSy7%2BWWUK8%2BfVv0Q0CMc13kP9VY%2FmS%2BWpt%2FlUxiC2OuTSnvP8VXNxAYcbZF2bXN1rEU7trESEqvs0xqAdOPjalGzPS75Y2bRqqVCUKriRUSHzYiAvMvnjit7HH7Bp53bhzqx02iGGuy03SVHg0Hljcj6CejldHOHWL7xsZgRR5GAhn6KFG7cjdOrRXhidqwvjXA5GC25Wc6nX%2Bc&X-Amz-Signature=953e6f2e08c69b26c9993ab599833615da66fa4e48a2eddc001fbb950c95317a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


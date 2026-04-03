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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DCCUOVW%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF44mEmOBr2htFyVcVNcGCOQtoL6Y1sBtsXWVpVV6PetAiAOoa9q9YXGV7CkkZioCi7sF6hQ4Wtqzx0eT7Mpc7IxEir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMRQJ07%2FctwzfMus23KtwDDcXUvAEOeT%2Bg2%2F3jgAM2gtBcMvIgj4yIoASbqYBH0VtA%2FSHC44PlfcYAPxDFFh0wqx0qbc4srU0xxT1ilwSap2Q7Ezjvf2EGv1cAC9cgdvXe9qJzZ36S1QiZQI%2Fe%2FctId1MZa4IHfdRK7VXg2HENMCE3oXbxMJqkJP2bYtMYnAamhX83BI6A3hI3F3K9InFd%2B2JChzimObTiVNqkhhhFtLmg1gRy3vMNuUNwOS0jUIZhHkIq2yZswk7ObTpK86M6XAhdzkSBi45buAAORUHzLeN1uHRAYenUv%2FHEjNM9nIeiImB8eIHcE0SJhQezqzq2nQZrisizBTxyauudS30b1YSJAfh0%2B9zosn7WxxtTflz%2Bkxf5z7ttehxvEHQM9k6erhCU91MCfCQlnPlCSTvcqgGqxKRAbYGkTisWUeQRxfksBf5j6YoO%2Fmf%2Ba%2B3YfB6r8WMqVL%2B9yet7rgbe6j4syoYwQ4R3m1LrMHraGavppz39LuzZXFdEKj4qN8n37nbEd%2F1Tn7tD1nGd4mZ9TDZJV%2BU8D9IOrT95nUkZ7ectCVQV4R3fe2xtoq38ZPP2uCPJnqab0mL7XcyUrVLNTYnqWmGMnOKFB3b02Nl5S1lxwRBy7Q0vSTkh3MfNI2kw%2F6y9zgY6pgGmhGNjbLd2DWWL986caeAsSnYkhtygOobnKSedTOrWzdhQyOA6EV6KblUB%2FaEaaEGtXwhHW1rEoDitoP%2FH%2FwbVgrB1sM2o3KHkcl2ejU05D1aLJ%2FcvpaPJTLVXWvLVwQo1bf%2BLxaJaZz4RDAckWka47LEGo6mjbC9v821C6HwbFdFDLHfRejkRrPbemViFnEgV2XUaBFqaUXJ7GAMbppI9d1SeYPL5&X-Amz-Signature=13032fdb7b9c108ea8cd8de4ac947089c081704b5328fa7b5507bfe3ad31ccc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


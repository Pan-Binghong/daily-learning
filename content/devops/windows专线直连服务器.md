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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUR7SBE%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIDdj3EYmiX1KRQH4QzS6%2Fw5doPDISDW7yaKFpodgQ5SoAiA08lNcKtfuKDxKEzG9gYuTpWkcSkWvFgtOxkl3CvSb%2Fyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMPUBnouLLqwIsbO9JKtwD7PugnJz5SB02Y8c%2FvCfkWgtUVsPsnb9y8jaslLiugUa6AxOjl3QVLND%2FqUSPfNuOOf4U1p%2FxYj4018KMZJccOIGcsLY%2FlUWP2u%2FzaZwpv3GayonoBvHE%2BDEOGq5J6Ei7fXtzG8093wnHA6eDU3Ct1e%2BrhqvRTLsnhl33h0j3s3o4MqDsJdMyx7ZvM87NNs5OPtxRD89acDkWnwaeJyoNc3GPXbkmJDqIJt7ly9Z7r8UQDUY8BW6KC5DlXLsGQyfL2eRXF2kxibSHCSRjZKPPw9OxklilJcHljhDZ%2BUwWNQRKne4MbIgedEpVBvBD0Rs80pVRLfjzsRySJzvPVEBYicf3v1ZWdxFvTMc0j5aVyNx1qhgTPC4j7oenaHQ0YrbzNcjcyXkA0JQnD9ZUqSj3qc4Bc%2BFp%2Fs0TgwNVaMeJYqWftBr2OOWeVPrHOPpU7jphG0nUaUcmVcZUJ8SkG%2BYlNKVC8XQG4qJKjRV8V4B7apbntPYpDRlzdBNaFCXkzAN1XXILq7y72S%2BGUmOq3VTXflaqK5lz%2Bte%2B1V9EM21PlRtFiFTaE7J8BGaP14fgLmtKHovVXkygdCoW9fAoaTnZdLdLIn0t2zdgZuTNNBqpwu8Pbpz8XXhiwOk4RfYwl%2BPPyAY6pgF2HopyLfclwuskMqSiYG35KVvsIVgCQnSpGrS01kkDAVT%2B%2F05ma8JUaX2nJSp6BO4X6HnqdEjnYqpoZfH0T0J837t87fWSAX7UK9JT%2F0sGHR3S01Skz%2BGvb0LBf5gVtyTj2TmRqo3VBe1%2FO325bCLwZMd2ywHN2NzGl0123Px8XSwPjHFOheG9O9XcoIMdgvc0kzFTxPijmdq4sVhKD0VoANYgCD22&X-Amz-Signature=6d0973ea3fb4a3212cb026479cd23bf48685770260c3ba122f69d4565bab4620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


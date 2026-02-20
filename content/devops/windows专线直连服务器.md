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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N4ZGSQO%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDoThY53%2FjrqKWLmjQJxVaOoSAmyL36bUSXTLn1r%2BYIJAiEAlKZQC1PccherBnQc1YE%2FtHYuJ64vJYpbxRg%2BeBFoPTwqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2QrRHLEBfXgcojvircA%2BnmPtYLlxuFxd%2B0BitEwezs0tJpLPNJxxH6ntdsbfXj6%2Ft6RHzSLxw9a2pYIecBDKAO3OGeVNMXFzzMOTAMYG0qSsSwdEhmN8v4jDjDGd0VhUSFVQ08VF9fVHFURK8cEGxCCjaJUMpp5kCAWExVL%2FqXaampDk3Vbp06uGYn7KDu6xn9yLbDpuJK3WCFw7YhV4FLPYFDZa1l%2ByiNHNydck50irWlasEtV8BGtJaeE3P6tdPqY9wKUAir7vBhbODKVi%2BlqqGQnlsKIH4LZ4v1K%2BnGVA4vTNw0XTkjQMzOdK2UnKZ1Zfhq8PuKRdFrcFD3Kps%2Bq%2BVnYplLvQoHJGoUKUPZfmSyxEd1zv8de8SlYI4KcK%2FpqR7HMac%2BSd2yIFmEYB95I1mpdKF78JXNAVEhn4i7iSiAvQPk%2BQBkdhluoZp9wp9c2OBl1HikgeweTPaDrqyIQGQ3ABcSQR8tDrKTvvuE7PGfGEbeSDjqg6rdlM%2F8ckfn6GmQGuD9VJpTg7jDlREKwJSsJ%2FqZ0AW5Ia5msJPi9O1tA97ApT7jw2cpRHoiOIAiR7eF30GgFZODbTXftvyffGIWqNN10h7Akjpmo5WV4TRA34jYUc2H4Kbt21D3VocjxWzleQLlluWYMKaR38wGOqUBrPQ0SFAaXzgxS4q4VekTFrGqnXz%2B3bybafhz%2FKM2ZOZ7j8wSZo2wodnyDKlecOTdb9HZoMHPEpsgqVE0agRNeM5ARf6mVA89zMGTIFGtaHZSU6g4wGR9y89xE1R0Xp4lwk%2FGd7caGfuAOQKQiaRyoNM6ASpMsWUvulp0AdhoomjEzeuAGrNe38mAw4QOeAEP%2BobOIxFIlFyyxhNHi%2BJ0H2pY77ra&X-Amz-Signature=59e3ef4968d741c65b407138ca7fec5aae0c3f5d340e32d3bfa979be172e8ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


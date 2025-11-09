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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC6TGSID%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIE281Jj0lpBVckhtSaPOcjfYyDl%2FipUVtUG1VMjAE0loAiEAwwfBe05SOCaQ5Ca4Pn2dl0I5gCN5fX%2By4wxG3m8js68qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJN7MmY9czi5FtOs7ircAzLE6yrdBMpStsw3IJuV1uklGeGP1vQWz1pZ77vDEXWrOe5KtujkOXM3R3xgP4MDkfua6XuW2cJdeVhOLWNQiBkNdjlncS%2FGf%2BEPuVjIzm5uRfSZopembIUxoO0KVs09SOoNcYgKiaA%2Bzxu87P1Gpi1ukexKNzfgvBF%2Fx79EaQaoLwD6DwP6wivUdvbs1IwtWyLQ4Uz3fAtwNLHtHlDw9K6lzXPA3n3yqiZqX3H09AbAp%2Bt%2BI%2BDnGunSmf6GAh4STZq%2BpHeuRDsrq5xDR2%2B7bNjVKsVV53hl4UDkRBbZffMNAsiKER3RCA5TxlxHM63XTzAe9%2BYGfUgGB%2BnKeEb1vBIR7D5PzSK87BLbGW3zYy0Aw%2FrIMdDlqipOGgR4FCIIya%2BFbanGe9sOSDBDWBTW40omS9Zo8YtQYMZ8GXpUy8Mic90EN%2B4tUgLnG3us7kaY8Uy6BS1ZdYA8V0pFPgXAXOaumu%2FzoOhsESqCo0ST8oCrJaCtgK7mGYdP3VKSJ9gIkytWRTz9XbJn4ezBoOLaXmUhD%2FAInHplI99Rw%2FYfe2KSBxtUi%2BxEQ%2BMpHFImu6jL3kFxPJn8GdIkDVbNFNyYTSDZ1bSOPVpKSpsM9xArIQ6jREEq5d%2Bh%2B%2BtTnBd8MJa3v8gGOqUBjHG3hLril6Xq2Mh1ypH50glfX0sgs4xWUyCGg%2BBH03%2BSk7Glwyn5ZudDxawSjF0Dr%2FuLcpQMYxqfh560f4V%2Bzb0CVMAcoUUx1GfEq7NSbj8OLpSChDP6eLfmpNrAe3gGUfEJz7yOeh5p8NUVy%2FSsQuTWi4mIzC63HJXW0%2Bl1K5KD4fpoWJC5Pw6meVLBpBwYb48mLqXjMT2lTnT5GJYzqTPBDTn0&X-Amz-Signature=18ce1f3d37d5f3eb58fe2efe93f8b8b89d409df0cdbe890a8009feb567cfb76f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


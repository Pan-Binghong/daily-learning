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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MV35TIG%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDyr4VJ1%2BngxEjjuvgflOBZPHK2NhkKwrm81A20FPgp1QIhAIx7ab4PUCqUCX%2BeOxLGfa2MH9CQiM9zlH1za1GPOGjHKv8DCBwQABoMNjM3NDIzMTgzODA1IgzC%2FT131jQ5k%2FkUa%2B4q3ANytHb6YBlPx4I1v186hvJeDYpseRsfPjihrFsaU3xBRJBidjd0oD6Rth6umFpwvgeu38hGxpRQeAcqxij2TnSYxzFaH9l6WoqcHWDnRmXJHsIwZ8f4jDa9xbQVMhz4t6d29OKCy7RWZbOyp4jwtfSoEXXKEnGWOC8hU4aBpo9izsz0pz3r3w%2BYVpXJgrE5E5simD4XkkSKh3%2FMkidDVTE9zCjK6REgRJgMcj4Y%2F9yKEvTzzrjGk8I1zYIjWZzFFpLZXPAvfzG4Oi5UZbeGGIN0C8YyucseA7cszTi%2BAvk1pXGc0frgFfkufVIvfj2xrOGjftQOb9Y%2BbdDLWUEnrNdl2X6x4S%2FbYhhRJeJlNgf2zs8pPRD4g1WeOw87YDSeggkdDxq%2FRIJ3iDGxgpH0sbyD5H8Ir0nv44HXSi%2BqqiSJnEl9MsYLlL%2FAjdoa18qPLAW9vqyRlsn%2BzxZf2zkhek8ZPreoWExQigOiYWT61AU9%2BMQXr54rB38Vk6N%2FbMoEurEryN6WTDwesUCMTlBYMj45IBrABYGo%2FrNuth2Ew%2FlODvEs%2FwQPQlkLEa%2Bj%2FQwYyIwtE6ws6gVPpLX%2BCPSlm6UAi0FI8lQ1UUz7Rs1iARuqaE7q7JYMs%2FTIwK10GzCO9v7MBjqkAQ2b4%2BWcVaMS8yt%2Bj6bH0XHIWUJ%2BtLq20Y5dDdDoPXxv3skJoaMvNOGFGTd%2BcHSbot8wKqcFFq1YAqXfcR4PgFsldJ%2BxxDGrnC5kWR%2BeR72R3nO93q4uPamG%2FrC12pHKMOAuSda6Gk%2BqZoqS2cYHPh6R88gwglYa%2FUwZAs9Z53dmwl2zQvP1iH6F9t91149KIn7Zvona38iEKeu5It41I4PWz3rL&X-Amz-Signature=98b20552727159ed23e0829e69095febf87505fb9c2f7a67ef7ecb554e238f32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


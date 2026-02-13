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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664X4BN4WV%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDJihwGV2AIJvnGr9KJdLt68%2B9coN9cFFQr89Zg23CqbgIhAOAou6jaiTQQuXkheHHF4wP7R4mcAnPkwxDbEnFUQ%2BHjKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdiOfSms6nqv7VI5sq3AMPeuRJjmbuNATCMRX7qrAZvq1LOePfDlvKLRXlYm3tODU0Z9Fg92ORImUlAPOIQSt7UY%2Fuc5aXqEVA%2Fbv0JTUeN9wOoW3T%2BVsNZklUg15v6Xcdrfmcw4E7BA4MZYGuc2b7TSwz3HC75N2Bs0SOssfvBi8%2BtIUI5N3ai2dyWtI%2B8yYlQAn11qiJmMrIhjYz%2BmixhkyosPbAHMxtsUOo%2F2%2B1SCWTzqbDiDD9IJp5829Kbmspg0jKcM3mGuw67Vbsf5X7uA8Tw%2BPe4vuNJ%2FFIIwMVZvq%2FCQP8bLryKyizvCuP76oLg3%2FxYNNH%2B7MDf27qIAjIkbO%2FnJkAqu0u8meuI39xDxFkzGezZmCvaR%2B4%2BrveoqVjgIEZltAF3BStb9hoHcnLZxNb0jK12aOaI2mWkrTkuiz%2F0MDEcso8RuPzUK%2FtyoZmULlH%2Fy1ng1cfIJeMnR0dizoyyCmBkL%2FmJ0MAkpvT4YJDm%2FVRY53Zbc3GgNgv6eXpxjYY%2B2j2QRQJlJttAIP6zz238MKNELCp%2FONi1p5b3X5nWdEXN5aDLZgWyh3%2Bv8Abiu%2BsBex0nKhBhEW4kd2CeIQDlghOqFaqqWkoXsGBAVBU41wJivA5SJ6jfFPAP9OtQeLEroLllSJiCjDOurrMBjqkAasEE0PlO%2Bpgwn55Hv0bXmjHElV27C8EvD5g9M%2B%2Fu1HmT136epXxFWgrLpaIKs2GvusWkmEWKXWvZBYiWVmiMKxoH%2BULG9qhQ3phLbBSmkD%2BWnOucr0VYZoEAx8EADG5D9Uw8D%2BLisTBbKyGX%2FUl8exVlJV4ZlBFvZQo7tIsYGP8SQnAxnTIme5uUFtNByOieb5JgvPk6UIW8BW2AasOuWLIzhoM&X-Amz-Signature=2888bd6a46fbb928393547db5620ea0badb7dcbd1cdf232ad5e604b3832b06bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


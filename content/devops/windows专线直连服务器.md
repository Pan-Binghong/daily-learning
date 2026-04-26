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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BXVHCIY%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY1eaTCgILvhxE88a3emtG0%2FXaDXu6gnpu1wi8IiAGNAiAzcwGGHbmjDZrX9nefvkvjNpEw%2FNHll3a42XrpIaVwBiqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqZs1oL2uKJFh%2BEkOKtwDMNo2zY6lC6p%2Bf%2FZgIdolUuRZdrS5lSyHH8ko0e03YFwEwGDDFXHJZS6b5VTo%2FlnUcrpG4yVKhgKjuCbfQKy6qLb27SY7u%2BS8f2%2FflDTjnyJzGvvzlYcepT%2BBLIIiJO%2BkLqtDEb%2BSVnDmLceuVrqzyD2DVjeIZdjdyES4Ghh4x91mqulOoFb05OJM%2Fhwny%2B4P4d%2BHyFQMbr5IIp%2FTS%2FJAzS38JdyAq4BCHDRJgeMcd77X3pPmBDdonuoOeyrfJfqtieXdf%2BQI2F7Bvc%2FrVSU3URM%2FpQoKKReJs5qt%2F1ljzWkoUo36p0hurILSqV1j197Z4zY7YXs1D2QsGsqwWWSavmeUkaSN2m4fjIZK0uLYZXXseWYFO8dW33fEgNQjrzWCZ6a2t89xfs9wSG5v3RVg6AJW%2FBn4iCaTXKAyINHOP8TNLMTd41Kbg%2BP0%2FA6PW89njDza2WP9qAOs3GvqtWdO9Ng1bXily9FrW7KVqdmLCe%2BnL8wWKAngkqZAQZcHbWPu9jQBVhuqogvct6wEaV9TMqJyXkensPeRd5jmdKp82VZbuNmfaPadRnjwsFIQFxWVOx3ETg%2FWlTFv5dBjBSMFZoUcQXg6bHW9LmfsuSStKZ5cWiThf17AMtDaK84w4I62zwY6pgEOdXOclIotAG9Tvo0OYS6x1mnYs1Ep%2BvMk%2BmpvQhOIvm0nduifYsAhejjaLpGJeJA8PPMAeYUHZ6JO2TLYZcCQPdoKgO5eDaAXPSd0fv7byOrAcNsBasfMHUMC4X%2BkSSxVcTRI4kNEQ9U6%2B9oo7fvF8p9awOSBKyJ9IeBJW0DomE8uz%2BJx1pXmeT9EuwpID8rVu0LqbnVyr656o2fiaSkefwrWtelR&X-Amz-Signature=a591971adfd072cd5a539357cd3b20836e50147b162333e5c213aa15e7f91588&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


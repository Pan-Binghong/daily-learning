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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4PIYVDI%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCUtz5rm0zBh9lK82YOlyTswcCauWdv8fPb6sKhLxV2ZwIhAP%2BTwSP%2Bbe%2BzA0rRHyzzrJfUxJpldip2m0zN1wpSizA2Kv8DCDIQABoMNjM3NDIzMTgzODA1Igwgx4oHMRg0RUfkYiYq3AP%2Bg2WGaCqOtiQrwRlZhYio2Zq5Wao1%2By7kbGNQDO6cS3zA2272rRkL6fH8WE3%2FNw1sTauET8zBl2RNSONAFj1xlCxmKRXkQGGyrlgLjzfZtldjO032VaFMdlqqyjNsfwdVKWW4%2FL%2BLBTmJnfPkzfhrYG0uZHmUC%2B4dgMpFKVOBb%2F6tTHfUMLCu9TGUNshTogfutntaJwyRkLVtwYsoO8omAXVzlyG80wmQ8wuOqhACT3%2FMKQ5Fba%2FurxoNWEv2m%2FRYrCP8IMOhWFAR7xYthETIUXiQsdNWseE78Fkqw0nvDK0y5Z3zSIzfuN7aODTLwv9KMLd4GBZdScns6DiICg0LwM1jtJBeghmMcK9pi6NI42zztbkUazGu%2BF%2F3cJ61ChrUfmnUgMqrk%2FiQyidh1PPEO52eT1FdE%2FERbb9MNBs59z9zl3v9sOeJnGlL72B78voURqAZcTX6lXQvUK955DHT%2BYrhsKa5QxEfxxKrEEjjFhP6eDYU3Yixq5hRvr6WhMKfA%2BUc8fEuXf73TLNi7FOWf4cc80JYUCDRJvAWAphWnXF8BGhitovDZIEW%2Fclvh1GZL7LQ7caQ4OCvEk55Zfrv%2BahoLQuDhEbN7cEhq2OhtOSaleWXIBEYvPRKfjCqorLKBjqkAUp3er7DYAmQhCbr4ZvimPiX8BNGrOERX5e9g0QeApo38zNCb9bzrJHVk8erVoQtj9UP5NNoDJ8hxMGyzVIHcbSjeB6qU4OfOmiXDF1axo%2FpA%2BwCdsVu8InqiXSwaR6YbY9%2F3bpXmEzsMZn3T9bZ%2BWOxu29a4h79NdvYTcnHQFu8dL5neOzlsjmFjDvTyP9GWOQdptFxg3j1MM2FWHOK11SJr1ee&X-Amz-Signature=f079d4eded3408f0a95abf72d693d3ff92c043d5f2c1f3ab40b1fa3639fcd01c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


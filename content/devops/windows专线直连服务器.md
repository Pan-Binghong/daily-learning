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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IG6LMIU%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyaU9wYluqoYJHIZXogqHgbiFU23cubPb%2FHVqQ65h2mAIhALK5gJSTDkq0U%2FRWsqMfpfzqeY1ovGpohU7JECCHmUKBKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Bs83BmV0XKCwfnPwq3AN%2BIcTyIX3I57vCScMQRk2jZt2UMNCuksuQQ%2FEARCOcyFrIuVYuD4W%2BTzuxZS%2BOKKfj2mm1S2fGnYl%2Bzw5RWGBVTR0e8huwbPrAh0seOXTdy38c8qwfACM07OBFdphaRDBVxFr3bigMG9Sid02o1zzMBtDij0vIm%2FSo1%2BUEA4Bip0vlzk8nr9PUNU6uZa30%2FSshXiQ608XO96x%2FgZ8FsPsHUBymn%2FHpzbNO9hkRZwQSJXapHPgxE47gbPOMdaqj8hKIHQ5DfVr4%2FKQi768NTvK1ji2RXP6HzqmirmdfMc2XUSulbE1crmyKIFOuw5%2B%2BwMdOhXdy7FmFbPZRlIRwZTp7g6nbvmqkM8AyHwRc3DijT3Gc4kYuT5%2FvEOvlE88%2BhJ7a%2BZbvPovO8kPVcASWR%2FCP5FlbXcQ6nUcgNgAIgjMWe6IWITfYmBUB81VYyAEQv8M2vxO3EV9%2FtZgaU9fyoeL7QG5ChDZUrv%2Fpi9hq2RIE%2FQ9FCXZzZvg05gYGK0d%2FqmWKjlo9g%2BISy5ls1mItQ5vWYB9IiVCRso%2F%2BwHnMoJxPLyK0Xkhr6DQ5O1ANJZUkMIow6r5z4dMhu242IGNvu1hnxjibRmTmwdgRolpAQAq6nmXF25TdBwb9Y%2BXP2jCo3bXLBjqkAZYhkMn%2BKm1cJ%2Fzcm%2BPdU35Hvo6O%2Fr3Eji1vzEPSWNtuIrVHapHenBA9u9rihVQnZZkvF7wZifnvFY37Pqw2%2F6Bz3e02szWnvhXDhtp0uslLX2JJk%2Fj4deLKByllm%2FBmV%2F2wWhuPNGeSDYWI7B87R%2BhRjJSZG8j8i80a8o7Iy7um7nFguD0QBx7WXgsqgejtk1W3sRF5CXcR0laE0rss7GlrKCj1&X-Amz-Signature=e2f509b998f62fc60863faa410d047a5374dfe7f13bbcff0cdcaff47126ea043&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


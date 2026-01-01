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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBN6C7GQ%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCMRvzxJZLKD13kvi9R5rmDwRqT%2BZ76b%2FAdrsz%2FBPspYQIgX%2FCMJTi0TVmLuLLlEyb3rTia%2FUYKaFBgKtOshZOR5IAqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLL%2BQ%2FUX47Rtt0X%2F%2FCrcA%2B5Fs06vXxnMz9v1DTl9mNu5L8ALFJ7eJbLLYWpRhKE4jiV%2FS2qrZsdtecp1QcbkQePCzlt9%2B1fcHxEfOnJm5lg5GGAm4SrsAez8wXlQUMHLr4lPk1B%2BeLtPMoGhgq8ztr2oNUlhX%2FG8cc36VqmJG8Y2%2FV9%2FZMy5AILT992x119TIHcftOxyHCCMznRESxdbkfaQtFlHpV4whkzMJt9veUMe8%2BvdMztVT2aK80Gk9bonfuHXBqPM4scM%2FFM4sPhGuQGcc9KsdOG1LWWLvDPBHeIBetFLNsgzlQ40sxgkDZzF7jfmRtpdcmpT2xIfVEspPT%2Bbx8HF5eS7U2xC8v06RUkUvwE%2FbX8%2Fppx8T5sr0qmH9gdrtvfHOuBUJR%2BUeSxs369Qstw3EqmH%2F6iNnxEvVv4Wo6xA9nT315puZq1a0Fa4jxlr%2FMqk7136XpLApCZ07DoJ0%2B6hsA3A2prsOhdfRy3oTcZCE7JX1SZnf1SDA4tdugRlH9%2F1iJvyEgC9zaJpCxt3TO%2F22DM495txSb%2FcjnkBZIUEB6h9jYQWhHWcopFFamNe%2Fs%2F%2FYQrHMKVgtDBDRlqdyuo0kmtv3UFibfR0HSXJIyd18ydnIXplZnm4fMQZ44BlEthj4VY4zwfOMMWj18oGOqUBFvbpcpv3mamuuxOp%2FiLBGC2YuqsJyGAmrt8cGI%2B8z2NkqWt%2Fqyt9H5M9hvxH8W3fcuYIqj8linZQo4RoQ8dxHZyISzmY6s9GPS4y3QMk63Gi3Xrk6GUexI%2BqLMXhzTdru%2BrzBdPLMMMkQitqtiQL%2Bh6eWdiVBOTKd015vB1cgdDHOYhLf0MxSFPDG9Azj6y6BSelQBRnN8u2XmEw%2FCfjn8k5n37f&X-Amz-Signature=4ede7d37221f94c0d987bfce59cfa443fef2da422810c83b4d3482b2f955812d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


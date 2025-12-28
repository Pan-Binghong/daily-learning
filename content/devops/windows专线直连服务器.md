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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOT5X7W6%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHk3rMUGhOI94q2mmGhZxgA6yMCHdKA8iYUdg3m%2BvqOPAiBZBUAnH2Qwi%2Fy0NhYVj80z2W5CvdkZYwBfEmMKudRefyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMTp8%2BRtOQbF%2Bqi7VxKtwDVsquoL5bw6rktr7Tbiw6maBpb9MqHrfck9Yoa3qAsrB5KfygKN9xPKp7D74mRF3C1M4woGmjqSXANAcG%2BCQY8CQ04WBCOA89ri3HDX06gUyzOWXmyqWArPtCSAQAboR5SPDidN%2FixjjkDAuVikgToVPi2fA7OnifZ%2BE0rcw3ZhbJ0%2FQGqLSSNioXMQQPxdNWGewGjg6EPPdXMdmGebVl4MfmqysKzqEIwObJRz9P%2BoKDotBbnHn8sqS1346mNLxhDrXgl6vJVf7A6%2FcsznUkBWHAvF8Iq265yhIOZzl7%2FrRXWqFAlX7jDs7%2Bbumt%2FrVSGfFN94gzBuf7YBCV3JDMi5sABVGeuuc%2FD1GLMKOcIE0ezV%2B7rC5kAYKm4SO1p9xxvW3ZrwbOnAouLQmbIdhhmVlob9OfWgoZpV%2BkZBovKwymwWCh6LDk3dZgIDDHK3lDbqnh%2Fnq1mj7O16KcEiS873hR4iTRlWYxCUp16JjTXvlqyuet%2FQLkh9CqTCVbSCzLyGjDtRRaX5cdTXF1VnOrCtdgflKMnoTZUGr%2FFn6e6QEmyBmGN9wZ285efQT1Q35wqPTq5sviSBV8WXxA2PdFNbBkO36cz0Y69Z9KShty3C%2BTeYaH4zUXfXTIJbcw8vTBygY6pgFLAu5jNlIs9DAcuMUK2ctT8kvZ6sdQWU%2FEZpAZeLYZDKe73EhJiJPDemL4cgrhtJBPjxtLitMyyjyq2mfs7yvjCy%2FIB8fKF%2FbEs3W8UxapvGEAUzfLF6U8U%2B9Rrm9mnR2oAawb%2BqCBYP5Ue%2FeUYXJfHHi7ZRp2NlWRileSKu3j%2B6XOpwh57d0CgqOk9JLFazGqO9k1YtmbfqJswiiTcdwJdsaKlmr9&X-Amz-Signature=6c2fc94f789bc710ce9bb97b5cd944ae89ff0aed06216b65fb87f5e2b312d65a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


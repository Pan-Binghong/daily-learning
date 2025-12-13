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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PROHJCK%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQD7xbCoM4YF4WRV%2Beqr9ovZ2PNNmBObeOrvNH9CbaII%2BAIhAJGJflvrBTznpjTA4aB1zXPSC%2BnF%2FBOn2GjQ1xYZcRcpKv8DCBMQABoMNjM3NDIzMTgzODA1IgypkRhhGg%2Fo1c62Ovwq3AOxS8%2FCw6RpUXyu7eziQhWzXO8lVzF2XuyLy1Ty1Y%2FbJtP5JS5Fi5qVlJ5THCWq9DPiwlWtwSGo8L2OzM%2Fyep7bwqSd9qoDdyPPGkF830b7quC%2FFqgz48oaOxa3iEi15xW5NlL7dwKW%2FjD9REZI7dZPF7aA27p8gz8YvSRVvW%2FX2pmn9YS6kuaNj2HfYQvOJBa9IksDX9LbAf%2BzLP9Asx3nHKkjsoy5RsCe4ROINBLcTa2i7lZ2l43VMoHubiJT7%2FlsxabZBfvc0Dc8%2FixnnV5ZuatUilG6xuleTOPtH07eYCf0O7bTrz3EXkQtTOX2St7pYADcWmz0VGrY4zbLv2q0lR9zDt3zhwLtJnSnSH8fFtFdrGf%2B%2Bnw0D0TGX3Lu50aTseU52y1fZPfvcqomRXGfmJu87EntdVkakCFFfRgKkw%2F2upwCpoGJlZGvhOpuxhYfLEKn560ibFOyqLR9kdd5TzBncedcOlFPF%2Byo5Buju70uddYS39PDCiVyPr8hyTxJtQHQLTVFnv%2FoBQk5P6TiN%2BPNWb3B9bWNBNjqLyL5tN2dBz9hvV1BD3L9Uze%2Be5mm4QGs4gub96Wh2szSgOG4iapuM7q14z9xwkG%2BjgNt5uEDyQZTDlUEw3vFzzDNjPPJBjqkAafZuL1%2FlYGIRskhN8RBbQW1h%2BlEFtSSogisIQz5EOab%2Bx%2FwpX8sKRjJrTLpUtWKUMO4XY1aJcYkCbjDZIk105wsVz6Vd%2FZKwWTkqPZY7HNHniXgOxrVxjTaGJaOKghIs0A40qgFFk1lRfkYedO2Frr2stX%2F2o0j9kvSDXMRa1jyWM%2Ffjb0ZNTP4XHIPhLoqzP7mSNwNyS8rnSJEE4ZnkfeExsUE&X-Amz-Signature=d6d91de009a046633fce2a801ad2e1708fbcd6be37e97464bc973113ba1be3e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


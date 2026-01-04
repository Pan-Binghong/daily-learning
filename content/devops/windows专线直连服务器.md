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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QR4S3N5%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIES2S%2B6NKC%2BBuSqLLn3moZRupTW8UQE5ORvE6hIcF33rAiAvxcVkXbe6BbY2%2FbqOQbtWW%2BIduCJhm%2F6kzYG9vvwx%2BCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIM9a8uVtIGZqxyxwjIKtwDDTHpWKfcdWSHVkPpEyDM1CIfHuwAbwiNmXsut%2FUquxu4yjb7QqcDtdSgkpYVBz8ES3tYPwiSjsQwridnoTOUTbl40gz8iqNMfvq49o8mpV7v53aK6g0i6oYl%2BSMw8oSw9uVXBeykFwv9yRcio5vfFA6rpmmahnQof25TC8x1RZu8e4%2F2ccl2PR786W5ya58bG0sYfRt7yA8fnDM3uKDL4dW%2Bs6JEGF2jVRC4Bbm%2Fo34DjP1n0%2BVibn0T62VYWgy88hH13E73VKl4NVzu4SRGuk68OtZXWBnxriPDAoZwprxjOJ1bmbjxEulP5PJLgo0WSPh6tNiQdjq29GlQU5DlqCtv335u4cOj28fRF0lRmPAc9E7sPxU%2B%2B7GDGv4npMCqWQFM%2BXS8oDA7Z5nUl3a6IcnkVDKaiMOXyVOztQr3oS%2BLIfk9CtqswPYAoTBBAyRv1A34y5v8uBz0Rg4%2FZ0RPu8aVzSDcyTHRsgce3DQsvwjCdXUKXHxH%2F7zT3HmqRtKAfDNO7r2gXIUaNBwNgTThDzfF6ATQXwhesOzeNJU1JCYeG1dTdRJJWJPxVUFQCUV6ZjgNnPYBTNIvbU%2BqNj%2FdqiYhUq8x9S9%2Br62fLdVOp8%2FnXa0NbPUSggQHalsw%2FaLmygY6pgGqUn9JGyr61kF41PA3bSHKWGPW1YSxXjT5xzVH0zLlMYLQmYv2FTPi7QGRXffKbOkBBsaVetpEPhiyS6lRS1eDjULNelF6P%2Brsnv5nJP6uspFDbVE0tb9YkHGFpntb7wz5G3Kl8HjC1B3kXOd63CD9q0LzrodHC%2F%2BQF2iSsv6S2wAI4xIZZGfKo4qQ2Qe9TaWwV9Zey5PlT38m5n5Sy2uhQtsyIu3m&X-Amz-Signature=3e3a8343ce7e9b103f0f7b44e7045c9ebaadc4b2f69c0edb79a54982d61bceaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


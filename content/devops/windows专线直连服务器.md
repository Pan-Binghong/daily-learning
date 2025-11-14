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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NAQJXSW%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDugkxMZTGiHoN0%2FDKATGI9TD1Q9hOyjaKTGOityRJDXQIhAPLkoX1JJEnvUgLxu0pgI%2BRxmCVQGV7HN5rlaKBbAvczKv8DCFsQABoMNjM3NDIzMTgzODA1IgwttZnnf8%2BIUfjhSdIq3APNTFHVnNTUIF8XeOgXqRoE5mDMunrwYXVrC1tflR%2FyGb93s4xUsr7ofLDkpOyNy1etKUFFmieTnrpQ6RZnoabAP3fUjlxi50iOsKD%2FMKcbj4CZxwlD8X8Hdw4Q5lvMR%2FfVFGy1NiN6WiV%2FVq12vzSu17ZzC%2Bl%2FZIZadeBpDd46Wgcgew9spoIOz36p8u7o8zEya2mocaT2NFVgroCmt7T6T9FWca0GsclKdRBmYxkxq2Cf%2F9PdxEKUKVXXbVNufiWPmPCusVQi5vLqEMM76tCOle9TWCP7%2B%2FJbeuSZ%2Fnu%2FtTvhP1siseHWOdiDWgS2o7r6G8UUX%2F7yhbE1xfSuajMGlMMIEeBCxFjTqqtzLKoSJf%2BkQZ3oFW5Nlu8VNiRy2cWJqlQRhsI%2FK4c93obBpLmTHhuWbfOaGsjpZwQKIQLoiczZ81GicJEtuErC0QhgqbPtc8NjydgTWxFrmtS4myJm8Y19LNVwubRqCa5WrdOrH2z81cW2ge7zIUaFJjSkHNEaQv6jC3GHhfNhjIdCu%2FvJ0vZHu%2FMsYQhDnchc8BIlovM%2Fc3p3wOLdyJISfgwHbk%2FfSIz%2BPkXg9OHmbslque%2BZqt%2ByYmsEB98t09PZcjY2snc03FjzGRS%2FNYEkmTDfidrIBjqkAXXYObPc15iqTrvsj3C8NiyldDgEBO52Br1Upm9t1Sd1IRg3N%2BwIbtoacJ%2B921TqgpIlO9aoFAfHS2r%2F6pmQTY%2B3piug0PrpuY76gRrvWHb3p9NAKwjXNTyW4XXs3PLF1DlAVQ8WEJWMC6rvc2J%2FxTWvHZ2j%2FIF6F0RzaiN4oHsG8dl9rt68N73EKxC0J6Pemqhk3gmK6EftDw2NnAz69RsJuyM8&X-Amz-Signature=f7a62e02172c75f8adb77f9dccf217f5959bf2ad75f42f9a0e4d9aaf3bbbf492&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


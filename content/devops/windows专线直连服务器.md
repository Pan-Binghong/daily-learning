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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KJQ2WXA%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDguxHA%2FYIZLkCwrjJDaU%2FI9vrwirLkvtI2XKAtGhvy5QIhALuPyVlSxRyUu7bCdJmSWihMkgs3vI%2FSAU%2Bmf8N2gE6pKv8DCHQQABoMNjM3NDIzMTgzODA1Igz25E4RTA3PpbHvrtQq3AOmU5OPXtyXM3tLkFdiiNt0L%2FmuUy8tg%2FD%2FbmkoljCGu9mu%2BCbL9Nj7APGEC%2FxsI5Ei4FlAUyVPLqZKUjx5U97VkhfcYET3EUapIIC9NutZuke%2B%2FxOvjKXLWp5SonZK9Wdx6qQcvXVzdO%2BObiGe%2BAUBWfzfvP5S8PSrX1dtBHfkm4YVZTk2W1fqlcMeDRW8jJcIxWQlR855RdUf%2FxNoh8xrgVBo7F1vpC%2FbbuDYFY3O0rpXv1oDgmbyQm3ooOZf5Iq2dloVtxHNOqXTyvwBNz%2B3zRRPrxjmj%2FRj2Uzrycax9QwjFhgm7qOTt2UHXhBqY0VXPIsSA56XJOiSDhxUGN3LynsyMvpYCdYAaZaDRgeFtf5H4nsHOJP8AtC4Xyc5vaRAeEmZIXZEP3eGqG09wFMMHWL7X9Qt10oDXFxtDBGyEZ7EyXPc3uZWMQ%2B1Yu8y8ztYI%2FJmseCSNSixn0m7Nz3tAjzrmpTdUXXOvez1xJ9h3IeKtVaCUQ9WTEqzp4D0B3Di9jdAtwU0nW6BRSNAvdQegO9sQOlHrgzdhu%2FuJZloKZjNYXl6FMnKCJlD85ZRBfdbgY9GU4zWOkNDs%2BIcy43ewyRyf7Y7eD1znwSp6B5iIJpYXL44k2H8Mf9fJjC8sYjKBjqkAYmX54wJyuzsbIUgB%2F%2F8%2B55MY1mk79RxTA3L9ZueM17K3uvvwYEbwxw8Cnr0XBgaXXaOa31XVOnCOmnp%2BV70SuIYmBOGn4VkksuOzhVqIQRoZflRCyCpFBDDTSOyfMkcObBV05bimqFS9C82f6RuOcNEIqTEPSvcRP5KMFA%2B6aYIGmjK%2Bgao1VgUaiOpj0J46sdsXGrW56QQCPfpy2%2BS3plvobF5&X-Amz-Signature=a282a2ec9207fbee217fd46411c50f2317cb62000e76ead2f4ed33ea1464eaf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


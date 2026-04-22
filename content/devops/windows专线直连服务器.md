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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YNBACCE%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDdIFgBhUjjuw8O6chAOz2fYNY77WjKzqhAF7byA9ix%2FQIgUN3VPssau%2BGZpUuig%2BghEJiwFgBSZ7vo%2Fy9FJIKonL0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDIG6lOLTHaM%2BiGqZ6CrcA4gS6%2B8Bkmtqr%2FCClUgV7fT1lnhbhmBbWI6sB0o%2BWKpQZawuLnjSoRbK9gqoUcCX0BRYy%2B7y31X%2B1cJJ%2FZSTflNB3BaeHFMg8AasWVEre0I2Twc1RBXW5TWaDgsWs%2Fqvv4xJWMvnmuY2ugM9OZCmVw65L92iHmKxyfE1wPr1pUd5HcPQ%2F742zuAyKoEwoPqLGxIlhMQHMkGY%2F43obnLak6yu9SKLLbj6EoJn1BISg7LgIDDvfNt8l%2BgK6%2BnRqlCW02qqw89fnqBVnIMOzAoq0zNdUHIRP%2F6AOFpjSUOtJulftxlH75JU75eRjWb0SgSVW9n5cPbDXU4aXW2rmU8LgW4N5gO1upbLX6VdoQ3oAR3apPa%2BPqzHzQcE9Uvil537ekNTgCxdWQFB4Wi3vdduO2udsGKiNFBDorQjb4NM5gYHsrHRi2VijTQFSU%2Fh7Xbe5954zfYahiI7ECQtW4l%2FIwzEEhQksvrW3hBipc2rJCf4m%2BXcu%2BRjGth6GZA8dC7OBo0ZsSdNAkdiylU0VYkPEvP1Vgugwdq7ijkcqONSWmG4esfPiujfGsSeAcbx2qdCU3dXoxuEQ27R5GJmLgGUffZFgfIwSHenjCACnR638lufuvXUj2cy2JkXdaBGMMD5oM8GOqUBinSp689WASTezcTDk%2B2QsIYqXAyWCc39qs8%2FMizh%2BuQTbSqBQwlfcbiFnEKKTOnggRA5NWRjU4dtY9b0X9npIR0fnZeuEE1lyzg7i08DjaY9hcKGch%2F%2FmbaRupvHHeAQXdXp4zy10F9m0%2FqgYYJJ3dxraBLFKxWmiRymquzXfOozWceMhmsdSCqzaKsvkl74ynOXbXhiM%2FFgRdKGsP7vnzhiz1uZ&X-Amz-Signature=b58b40cc4567876f03850898beeaf6762726363e584b38b050bab208384a39f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


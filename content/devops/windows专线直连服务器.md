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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZU2WDWDQ%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCBH3JPkWoSBPyVBWTqf5YACVJjIA0yYRiJyoVXMYBvOwIhAPLv8Ct2lL1jPimYWpX3DkACE3YOGLsvATdsPA8HxRwyKv8DCDwQABoMNjM3NDIzMTgzODA1IgyNPshUtWxoXdSrMPoq3AMnhWzNg4V8vEfXCs4JmjzW89FQgej4hJaNDO0U9CgQb7RQHRsyoby%2Br8T41Bq0WzfSKlcEDzux2Lt851wgW5ZqkBDfjCFeYwBTCWMsky86zeIwK%2BQGDoztWR3JG2xiKnyJvvDUksBDpW2b8DtNi82Sa6Qy4Srabn%2BhpeXUq5wVG%2BCSeFn3O%2FI3wg%2BGB7hGmZdmAscC0%2FuDiH31ceKMHl2DfxXETEPTPddo9U0Z%2B8UC1cv9qiCmvFWJ%2Bro73MR8fvIYV2qaKQYisItxq8AorYZg5vwm5%2F85KZ5dVJnPn1KjQUkMisbb%2B9TcvtnyCNzPhPVFFqKODsG26DGTfLWfYABqFMs%2B%2Biz2Cb59WK8NxlR4Cg5rCq46vYSlegYWVhtbCqil7HLom6EuqBD56vWFYwQAxAaUMXpUmUPScbIJQb8CVP4ehqJjiDzniQBJMjg2JoSF4mSGHJB%2Fr3bAJs2w7TesZcmfae2dE6gU6U89Qi3QkQ4J8Y4gjI0X%2FLuqFBD1Ds9ixR2hT1lOpbocTU7kCD5q0e6M9lDCZRgCKM3QoMiaYdolNeWbXnuptPLe7R8d2JUv2QbkRgpHLY3LuRdNF4TY4fBqv0%2BlL6P6Ei%2B3afG9Ad0EkRG60%2BG7cQRskzCT6ebOBjqkAavQEySprrWLEe1x%2B8vPmBEg3m54AaXXseOS1b%2FwevxIYCQ2zHXwrY9on3SJDb5Hh4a5kPeuV3075gSCqr3GOZ89%2FJqLC%2BqP4z7hQJjxn8ITV%2B7m9PLf%2BkYBpYMtisvdZG03T5jflVsl0lYGhB9UCtr%2BJTDj%2FC2oi7Nu%2FfuQzvZKzwgiqG07XoAzyIyd0bVi%2BhJT7QqXuWBxc8IWqH0gbotuiNAO&X-Amz-Signature=dd209a04cab23d99d84724b19e4a6dcc7074377f575edbb5e9e5cc00d023a267&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


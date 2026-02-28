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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YAV2Y2X%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCVgQ1%2FS9CyV%2B7JwuxJBHpsaxBuypAChF6MhMdFIxJ5AiB%2FKQ4z%2Bv9RJNDcjrcHtN6gPh5zthwK9vzeuMWIUB1N7ir%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMZwPV7k9NcW5rPTjBKtwDYf8RnZC5oR5atdfPpKeOLcWwn6J6kAQ9tyZSMxSmUgiDSfRMa267lRTDhHHJqSbUR2Gl14VuwSBPqro7YclOJMOH23kkyWPDWLlGmKT59gmbqWknoUWL2NeqwR%2BRVi4eHlazejv2N%2F%2B%2FJneMkoyXQWB6S2C5CoyJdaX0sDMWDPV5fmEvlBF8VvBcxmtpeL97oCkqqDzast963LaO9%2FjOJmc59s0PNWCeg0rXzxGLnBCim7XYws%2BtvDXNtTfjwXigKgrvfRaS8Vi56B0CJ0882meeJ8X1jW0OklsO4Q0fqR3yJ2%2B0DWzmxMU3pTvbY0tybo4wP33l9uZosWQHIMG0vphDg5TOjEV1%2FMOhICMDGO9ZTksq8wd7P13WtAxqx2n6vRV9iQJBc3JPdgcd8eG0ENIe%2FT8UqlWqMsxlAPSXaGKXEDN0oZtrmmQi5AizKPhdbXFaVoIF4tfNXtBQJZHUBd9wA4mnsXTKaiMijeGCGh0OZnKdqmp3%2FMkzOyYpExOrvbySFKaZVQDto2aFFJVFHKmwv2va%2Bv%2FJi4YfLqASYCVbtUwM9rFdj8IXdsLQPkJrla%2B8oSpcLduzABgMtGWOybnPNWPyITQ0rXC7E2qa6y8Gxm2oNOuUeuVXV8swtZaJzQY6pgGDloCExkhbi6cY481szgIRZFUyyDvw5ud5m4sfFz3whxXhXastmlWXJz1UBdSrzckbD8dNSvnTgmuiyhAsTKzXCuZv5FVlm7pBjFA%2Bdok10c2kKDCNmQnKH6E%2FsIqaDl8rCKa%2Bc%2F3twjWF6T5n7%2B2ZVoYiLTYoUOhaqnSc%2Fprf1Z%2BNFFLhmnYqWMMFenYNS1wbtr9HoRWh0Fh5FFsrQiIUr8u9E%2BuN&X-Amz-Signature=63b1afc5e7600df98231a5de60f89bc501773e8eef56441a058d56b55aa9f698&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


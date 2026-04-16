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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFAOHUS3%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqpC%2FIgpHTGR3ak5EL5INrdItWNnwpvQ9LHIyPQCbN7AiAWTVscoCsgXIUKsmTxzFiKNtexx2DIs3eOKtsAKBtHKyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2Rvcoi6SKhun0j4bKtwDXoAt0abTysFuZtZUwaVB%2BFFGqkMOPnplZz4J5OeRmjnjNhMHRXSUmznSHrk3XcLxj%2BIl0tA2eTK2NkixxVPnMwSLVsVc3rmoShakGQUd9un624N8CO9tlmKaFdWwk6Gzxa9q5K6MMLCIgnwv40WjebA4aFH%2F%2F94BGHC4crDORrWzlnSQ4G6LI%2BJaVpOWuG9j%2Fjx8xolLNNA7dLTvUvrx6xqu5JqGgQ%2BtGJvjCsmel%2BIPujkzgBgWGLU4kxc5RocOcpyk4hTcEJfM8Tw8vMlNReGMEvzB8qu%2B%2BQPeWL1Q%2BQBI5N2Ieu8okoBJC8JTMNeGO4LMx6dSmPxpFwJe1X7q6Ktzw5U%2BBxPdbRxPHRjpvyf2R%2FtWLh8aiuPf7smlOsZxS9wsudgjXT9DjLgI2E9xbJf7VaDYjt3D8%2FpNXmW5DWdO0ZvqsGQJwidOytCfQXAHpsWgUL%2F7jPEJb%2BSKmTlIhmoR2FmK6oW60dM5oDWTB6r8JaGX8GXLStjmfdA4paJEOX8BPZ2dFvw97l9y%2B95EIpvjjZ%2BEicHFHjjc3LL6zQCD%2BCEG2Zlp4rojdELaVj8mKxGye9U6P%2FOjbdAHQa6ogCZphO%2FLap9gVMwStGrztmbeX%2F%2BV5TnyegdkkHwwkbSBzwY6pgH0%2B8xv71fNdnTKr1k8L2guLuvhJV0ps%2BAdighxyoI2YC0dOy2XhjAjd%2BHL4RJuskLqb2LRLBN80KWahM1%2BI6Go5XZioJxKsCUnKgxxrS2y53i62Zpah6K3PXtXsbH07eZtZjIpla1csq%2F43kO4hNbxxx3Pnnm9%2B6lC7aqArqJV5lfbwLENvntcHOCgdn1gUh3B3EH4eKGoa7lwcDnMh9YxIElDKlpy&X-Amz-Signature=c2f7cfdaa90c78436937ceca41553a0293e013eb1f7c586fc6f1a8f232af025a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


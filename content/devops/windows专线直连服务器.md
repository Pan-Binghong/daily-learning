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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT2SZWIA%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIBxIu15shxJSF9oqCof%2BatbYlJDAcDpuzGxqrsCLv4IKAiA7ARRbk2L6G%2FP3ZHs40%2BOhIKN%2BQfEFicrpON%2B5qyJeYCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6sItd%2FpTEEdbpRuoKtwDrmbcxEiI8lrNDcEW3OR66e6SxOFb6e36zYzYgvUM%2FLt4cHvLM8W0Icv1qKlKlLIvZiP7H%2BzCIiSghB%2BkCuMTmR9HR2CmhowOFSAOw0EYqoUX3z%2BAsxHaiI5xcDUIcas%2Bt%2BTz3fvACef15sa1fCcHkewHeo9B0JjpXT8CezJaMrzNxRjA1SE09stQqPXS3hhYxhK%2FG3IvdmWNrxab%2FN0c4sa5%2B6ylRwYwvhjREBius9mlkqUfgcFdlBbepngOqf7IzGI2juDvQrXIaO7mxfbqGURbByd5wLRbAySKoyvWZskKvCWlmTPQ4Z9tzXc%2FYSj0n0Vde0bGVZKUMMaZl9yKj%2BCoi4AMfRsGWa%2B0tpfp3Y7qbjCHEtvPQekY4IL5Zo1NpyH9YN0nHcrJt9kM2nCI6d6otA54HzrIW4wRosci1R9Hxdqn%2B9JuzQS%2B4u%2FMQY%2FiKPZKN%2FWcM0F%2F6ltlFoNvUC46%2FSOT%2BM1j%2BewUb6%2BIaN6aS3ijSNFkldnZEEnAP0%2Fw81L5QD9v7T6IYUTjeKFlLbsS7K2HrA4hbK%2FuWwN1tY0b1BbcbBmJDu8QnB%2BwzPvnvysZKx5YcGd0VcbEhDNFsMNiwGdZJwWhaxM7Jz73yAlD9GXDLxr5HLk%2Bc4Qw3NfFywY6pgGOa2W%2B2BuIYejlb3ulu11ZIwEhaOzonLViwhVdFrL3EhSTxkuBWssdXqYFf9n4xKaZDO42TQu1J1zpo1QKYn%2Bkr6Y05ShVpPC%2FJooWAKxvYt6RzRv4iFPkeAl%2F%2BXCvcjbqZTOSgwrM%2BgApOICsrRwYoyHArvb2Lo5LIYBVh8d9bRt3tyqDEbJWsEU45qFebSNCItiIMdH%2BAgnvZfo4gYiGlvPkl%2BH7&X-Amz-Signature=f0463d0015cc5c690465286034efcaedb4f278e4cc2d4cb6f2e87902c933a636&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


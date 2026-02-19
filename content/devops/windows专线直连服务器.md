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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNF5UE3C%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3VC8DgFg6UQwDbB%2FTFgPNXiokyBe7HNqBUtAS8wq7GgIgXSeUk3CMCv%2Bg7iB9WqweZKybALZuwHBW9zGB2LdUJ94q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNn3ZDm%2B9qj7XsIdTSrcA10ED01P3r2K25TSm6M0I4TRPMnA40KjO07n%2BS8Oc4ZcabshtMzQwR2DoVpBVHIYbe80ARjQMOAIOq%2FrsxWZKsGvdtXoYX6jcUyG3QAQobHRyUwma5%2B%2FAQY6O3PyEgXyTJ9z837c9XnkDSF9B7X8oA73bjIg82UVqbnBYR7A9ljFLpNRPz7Jdtdx0bdLmmZp0M2ZLdtt70MOiXkF7ldWpqrzPkL3KQPydE5vnFgdfd0Tfn2hEJw13t%2B69UtHRjBih1NguWwDCSq971hdJNvjFd%2FOOVtsBomUIXsSeYZev1XVVcV9w0J2JTpmsJ%2FkrDs7lf1GxKz9ZvBM1tGwpanvHQieaKfsfB0aHKYM9gUnIWvW2FPjUg7lUKi86ts7x9KJ%2Fbrl2oZ5MHv0Dixy5D%2Bdzl3eTDh7ujSSavnuqfiP0SHMubzKLGf1wC4xWO8fakLyEo8KuOMxjl6S4RNvUaJIs8j78gDKIIB7vwiOUgj1PXK8cMTutRGUrq7uBVdtuz69c5URsgvQ4lprce22dW1L%2BbJHRQWXuIYiBzjwK3pfL2StVRdBYQ4jhEECWVvzTIy8Xt%2Bevm5EAyDIt2cot1fw7ALs7myohbFFxQ2B%2F91Es3VMgEzAFGP1ESBafRNNMPvy2cwGOqUBoFm%2BTLmuXbkmSSdciVSzhbavgRXbgpq00vgXijPxNaet9KXX0ONvCzUjAKPpjOWun7BKc4LVye%2B8gmRfrLiztfSE0bhxEs7iw3anKXpkIX4tI061QA7yDM3TUYW4fMaGA5MJFkge56TmASs0vpbSI1WrYMYGfJwBGCno0YK2VIwAA9tYRn0HMUGJsqC4yz6%2F8bRsJMM4C3LD02pROGFDEjGwXVit&X-Amz-Signature=5774576a9a7bb753643ea0a7116d1afff9f5b9a60508c09a827df16f4bb85c34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


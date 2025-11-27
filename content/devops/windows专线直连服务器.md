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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJPQNUFE%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFfXplxcIyoXd6Lyk4ssPjXzDx0anpnbUriuStbUAmbuAiAseRVrwMpR5UxPdnLjigbLVltktqYLCCisyk%2BxR0cPHiqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTTTMR8vIqMfkzY%2F1KtwDzJTZvsma02qPY5tDxSfrol3iT%2BWV49iYFxhL1Oyp5BvjOoG1Tn3KQOL5XFIfDraitG7Ddd6odV2NYXRD%2BPHU591JoGVX%2FgrQe5CoBY3PG%2BzQKyW5BWuseFHOVVbq%2FtZ5e42PUiwBy2L1j5hFAd5azpZpwf6yB%2Fy1hzM6WUzxEZuXPtKpPU2RRUkpcnrRO1aNLb4KKBFAAl2mD4%2FsCFaIRLMAtrchc5p9KN9gAvimmyVfFF6nmnKRWRTRdt3XnfWCc7gsmWwdcCL1eiLNilKnxsBhxsyVbhYGTMDeAKd9mXa3LBjdmDCrLw4pE4xT21A6r7D55KxjoLStcyBH%2B0ePOrc1adO%2Ftmbikz%2FaZR%2FTas%2FzwF50IjDIeYYXiSCu%2BlTi9OKKDwPLKsQhY5%2B7Sup0KQdXslkVpa0vNb%2B4g866gxezZtXJH07KgRb5Gs3naeB1c26sUc1jGZjim9eIyvRHv7XHJGvDwfYAAtjtOTZyedn2S6FSPSkPdz2ByyazKwBiL7GikqaleixKkoCr8L6QaZlkAAGS0yJUvTmSueLDNiJFbgDhBIqMQuwqNuq3TxmQUEW85bHB6Jf2YYcHqhtvfP%2FdLp2oFPQ0nKZQ3JSyvOUV4BD5EFFWBnKHmQYwrMyeyQY6pgHr5CePkE1YNctwDH5I%2Bp1onAeljcoonAsg4f0c8uR4y2UmO6cH91jU0xH4tGyMqMsm6MoWT6Xi7iD5VfqbTMy3kuV2LZGZn7WK0cy493HOTn7QYSi7teTRxFaEMwCQD7JIhw%2FbJTKR0fB9eQCwEs4nMGhSPcTUa4CWzOslgU%2FWjCMqv6X5%2BBhKVyn47AuRcyvm7NOAX2XmdyWZWvMNiGANM6bbRES6&X-Amz-Signature=4fa2aefb3beb09f886b9cb896d6d08eab5b117e8c85f3b42437bb4563e1cbc2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


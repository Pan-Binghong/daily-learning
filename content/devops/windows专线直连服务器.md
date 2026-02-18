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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KOYCERR%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSuOLI1dZ7S1LYBgBmGFgpIP9V2FGZ%2F5avxmp%2BBMsjawIgCWKza14GNRhuaYdVx%2BYdgwSkJnbEM4ULXg%2FfhfNxVMoq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDLyav6XnVq3T8kQCBCrcA8bUc5wXK8B6DaPbCgd5bY46irLEauwfAiB0JN6nvdrny4H0SLAQhUFStDDyw7mduqSXBTRdFvNn4zHeqdP68cFfPDKgg%2FpEJPhGXhPI405Wa4qi9oLKWtG7DD8l9L8TXurwlFlkgE47zv335aaYS%2FVuoB0k8D0UV9ftfwJSAq4ix6hY6SmOjQFUsFZUL1KVfmql3r57ldgROIAeGzZRVKLUqQqlranGY5zlYWktwbzKBsWfRC9l6GkQvCnvIp4s9qsMedc3K2S4FImaxZfDVe0%2By%2B07Fchq0Fr%2B4JUuraNIxEyERKGtjEskEHzAfJXAFVDFh6AlnD4NJQWObmnzHllXyN2Knd3MIq593UwaEIx0xNPoYvYmi0T5AJ1u%2B543ODPMs7EpNoJXpRbYAzCDJ1vEZGQSU1duVX4zYbQcXku6Vh47enVlm7KEe8%2Ff%2BIkK85D0aEsaE0DJGwQ%2BrtydD92pzclsy8nIv9IFvTzmceRRdICf3YDVEtWCDKEV6aRhCcbSu5iWAyX2WlFsPdziNwlf%2FbT2t1qhRs7%2BDK9FlwiC%2BfR9LWEUdBehEdBpfKeeuypx96DtzxrHWKWa4hRF1Rq9Ltymwu5ASiFAvFFc3R4aw9XG%2FzjbORsxNhxSMPqe1MwGOqUBS93Rn0ZQGMDEug4NjbzJtP2wQtrqv%2FO9V7%2F3uNspZKFz19ZCOInIK5I%2B%2FVv5PDRMbWzvG0tdTBmwLDS9u4i9BoQr3Wqie9Q9PkUWg2GF%2FYxDheKTXawkKvjwjSbqR68RCDXuwGd0tKwX54w6ExRvLeziIPSOkLc9WDbKX0Be2HhfSKMfW6rZ%2B%2BfI9vfA%2Bqm7XrPOMB5D47B0wZa2x2bbuXjGrxQP&X-Amz-Signature=db0baf547d19a0dd40545fab3bdce34e770665a823aab44f2cde8f09cf1c72bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


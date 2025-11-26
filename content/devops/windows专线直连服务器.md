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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNCEHT2M%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFQcOOupPP2wpae74xVUcDOhb4Mp1Rdh3a7LDnpvd31gAiEAmOcAzpq0XRZxkL9pM%2F5AQLjHaN%2BKvzzvTjP9bRyDhGwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDE7dD284YIsuVZtWWircA9OfbLCi7lGUXJVHt9YJcftEQFN%2BFvBTgD9cxDn7L8olHD1N9WDeFq%2BGR%2B8whiEv287rCDpgkneStmpFw1lTCvl9Rh2aiG8AYo%2B7ZlCl%2Fm7z8o9RsXs1kbvXmZT8hoFkLmM%2F7NrctRvQA253IhCXDvLtA6HVa%2FUUApHHUG3xglL%2BuHhCBNv8ZWpG9sD8FRtwLmo4i87hufWvj0SWz2oMKE1N1HYjurFJ5NNAjVh5TXUR8tZUvpGe1S7e%2Bcg4cP8VKVqWb2syUiEZv%2B7O94R9tyh%2FGFEyXNKyTDLJVPTiny34DTuJNMcVp32P54kPkiNupW3YvDv0x0IY%2Bi34psOdq0u2J6N7OFAZoqSLKIIL9qrvt3tLH6%2B0ktIK%2BJCjmoHkxYx1ovTLRkMXQiiU%2FhNDXswn8RaSlYHPc9KF7sxAjGyiXxZ1SUOZ%2BbhgZigU2dGnt%2FtcfcEq%2BjwyUWTpmtlCaCejewolS6BdLEh%2FKaTnG2IflzREbyHgWQqNTjhh%2BykkPSbwz5mwutAKFpmoObW033alZ30gkcfyxMBLJmJSHqJCvQojWi6NbW4gcBBX%2FzoBEyJNU8Uh9ru5%2Bt5lfWU6q%2FJ%2BGwCEZtRhRFen6ScaM%2BRSlKiq4XTb2BcmrjWFMIKxmckGOqUBOque3S%2FBxasUP3QdjjfngFn7EQCVSHzf9pdjtNmwZ3nBirfgSG24u7ZF25Qanx%2FnczQeZLkIwYOyX%2FBOqPVyk2egwbZJeJRNtxAunjBxQW4Ci1tCRM28GlxC0wqDdpCo8eWYFMOeBtZQ8sLyMB1M3oMW%2Fyo8AH%2F6eltNwNHPA00q7oiZKTgXXS20%2B2q1s8klV8QvbZviVp9mQkwCtnqk4HaEoxso&X-Amz-Signature=e4d1c7a7c7b5968ae64d10311fedf8c4450f64673d4a8128c1e5b13c1bf8f140&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


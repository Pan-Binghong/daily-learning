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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3V7ZDRS%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC011jBdP4vE7BgOkz%2FulPpgaIlJDYC%2BKMOljS7RVWHlgIgKSiYwZG7kiqG8RGcWW0KVMgX%2Byl1N%2BO9NMlnyZM3wHIqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI1gzqhCwlbzgSkzECrcA9hfbaj%2BOeoE9DzMXJA0KIRwAzg8qtzlw8QDRwyJ91S%2FKKyWcddS4vbpLbCDcFvPTVMYGPbTDO9UiYcrCX2I%2B8%2FTV1jklzpyS0NTATyek%2F%2F4IsmGkHKUIXab4OeWkgJBY5gK6jdNV1tI6A%2F6r%2BRXSmaguvauW66q1GEXQBrZZ8CFy%2BBYmDXAu2A7prh5XxOsDTnaPj87CcD2v0bz2Dh0RPpdDtarZeOVoeP16DmMa4SQT%2FejoAYklMUcyduT8vXhyRZBTk%2BM%2Bu334UTRUyRKkfAzbQpogX0Ks6ygactCj3hFBmAgCCBnyM3OVWRWJnlrBXkPjChCwbZa3KHlnUtPex5fIdgTOY9SRnFTm1Lw6dcbHGutv8ynMXjWgw%2ByVO7hU1%2FPeGiZJ6V3bh88DqRK7AnsrbWle%2BVzpmOvYO%2BkQ%2FX8YZwtosluR3AryeWYo7H8MQt%2BcDPvUUQGW9BIkIVLjz6q7BDyMDholeGPw6vIiH4RHl%2F65wbtpILTDsgbf6qNZJVwuHs93czUvhMcGKLM1K9gwdWkRvYGeBszCNVJjdzogz0xlVvIgfOS3eIwLmKAlSUQklJZ8hFc1MPFjAqcRdRk2F0cMcUht4TLSzSaA8lzJ2k%2Bcw%2BQI4boFuEtMKX5hssGOqUB8jGkktmAqf7h41XbUFtBzYGKVqe4Nc7G3g%2FYCa90LoMwPzPMVBVcw6nkQgb6ttmAK%2BTlYyey6y3prlVGWJo6Pdidvp2%2BnMD%2Fr7lA3TUUTOTuYXnYJCiKJ7Wht0VCPYVqfTBwi2xRHFadrzi2eGGbgu4hqLwWzKeKYcP8BVeIQC%2F5Ya4g3J1YVYCbC0F89pCJ6XTIou7OM1lzjPI4%2FcVPo81O8rcl&X-Amz-Signature=6e8cfc9d96e956b9bfb95dcaf8e544facfcbed0de7bb4acdb6911e8aa50adb19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


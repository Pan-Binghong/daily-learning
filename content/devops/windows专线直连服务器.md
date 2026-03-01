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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q3CKX7D%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHVs8wqkHyjrwuFVJrmHmYCGlkALPVjwlAeiXwCvVHZZAiEAr8Q1rB8VU0odIZ94hp6ItCNanU6yPRTfCRYx%2BlbLAOEq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDAjK7K%2BqV2YUoMGFFSrcAyWc1bidUCQVHmeq2fH4VWJoUOuFJgpA2k%2F%2BIaRhdrrpmFvTewnCYt%2FVeqczpZyCtQ48LPvTWdV9fsy%2Bp%2FG2NfFSWEDkyeEVkdN1o1%2FM0SKHkV635JoTaKklQBfSANMRd%2BmcjEld75kPeC3bDj5kTWps%2B%2BNOFgzWUWWD37Lf0NQPeHI%2B4TptIk8KRKKpmjyUMsAVIjV7Y7w%2Flt5nXWqxGv78KGtTPCSG%2FkMIm0wTCOK4gcShfLoQuimF%2BWM%2Bj2%2F%2FS3SmJX9S29zvoAwGs9VTVm5pLNnQAFlMKVh64hncQhVBW9sYB%2BnumxAeO%2FfcgLWYCqszCBGU94HTJdXCXZT6AMi%2BPCLHBUEuxw83fkOI2o3psJeD9nFBAhzbB4WvFgXsgR2d48T80TjseAquR4KfP2fksHdipgluRlnT5yuuEb8xE4b9%2BAan6h7FQtkaGsikMDRFV7izh0tpsWKR%2FFKPrd4dJS7BMsz6fiXG7%2FcVNXb4gKqBeN%2F2aJwz%2BQQ4pBGmMEQOKp7%2FJvRsfy569HwnemKbBVeXFEhRWAslyRAKqUSJUX7KUbsITAaA71u2g%2FjbLBGxzsLCkVsq4MIjR7d5b6Me7dkBo%2Bda%2FjOy%2F3LOIgiM9qNi9HP%2FHcud%2FmBrMKbNjs0GOqUBEG1K4%2BPlr20OJ4N4NKV8IQVUkJOdClV%2B3of6fkyP8CHD38Z429H%2BtX1DBTzp9lqt1dt1Vffuysz5lIJBYGfkFNOtJqyyLmzlpQrOvICci25CIyQWyXxi5y%2FAiAHy2XyEvlVqWVL%2FvippecvoZx%2F9DnV%2BWLZcpdIkHTdnL042g7Jp9y7lux770zNo5H%2FmaaSI2TmfyyfGPQh%2Bw1o72DFMJ6VWO4Hl&X-Amz-Signature=18f5c0d0820a879dee81cfabafb808cef134f130a12f16c0eecf2b0e80e28dcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


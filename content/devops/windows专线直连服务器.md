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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4FSYL5%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENcpuQcvCwIYugKthEYlSf4DxwAk7gkNJmorxVzg1ypAiBfTsBIdpABkftluSHtnSqni7PQBMY66R485o8HpgrwdCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMBc917qhtIDrhz3AlKtwDuanGS4QPbnnAE6Perfsao5tKFipeDOPqKDFKX3a3CViOXDlsCDjacjWDWdR1t5KDhQKCivPNjaWf4LsQyswGzv1rYzVqnRK7fZLQoSs%2BYNvUT47g0Bo7M1mLbl8x739TshkOeONRC1H7zhxT2fU0OOzn%2BkOT%2BqcJSUf%2BV4xQpCdygYVUYR2xuf%2FnRijUcttXlwItJUoL9636jkaazPnBcickyhmXySlAlKqhuHiE1VS3jeJ7MfHSkObmBnBl8%2Bj48ave0YtnzidpPfmYN%2F5OCl5LfsEkmrRFdjtdAX0cJeHrrONmefnva2%2BaLR%2BkKQ2l22jy8umGXjyiW9Lk1Eyy%2BzLVp3mfeBOXCbZbaSM7y4seoluG4t93StHFsRMaTWsjVyqlflI%2FfpE8vUjtluJErf6EMCO4tGvEDRv9nybrvDoOp%2B2K9wv5E2svsLypCoacHOyfs5FcTc5dumbkloAyQe7mKWd1eZLVmvcmZfT3otXjBScNtjgjohF5eyxAh8gnmxtqLRDH7PR5STrb%2FWIhopRcMdFegNrMG3isbxKNhKvUA4UIihrphI0aK1rumNH57DuYaGsm8wMmUlvgsZLKHj3EK5t43Pkzy9zsV3aI7CpyvDETqkbn%2FuGSv8kwv66UyQY6pgHwFBnmgPLNctXEcu%2BhoaDrNlvMi2fsjBg4maPWvDjJtGIblCh7CEggwaL1xK3C11IlIiUztfT6KKPYZko9ci1%2FIpHlqOuRCLSjjCUxsw19ptEnSjuPJ%2FoaDgTRJQdTlRpj%2FJAylJVyduXsXZXm4duux90hwluN7C6d0zRI4%2BFN6Pl2SxNMrKf2WrcBZFeXKB%2B%2FiLjQAFp0HaBA2mjH64SdPh1Pekg6&X-Amz-Signature=ad000751d270b930a5e0848a5174bcb1f917457a57d923f8ba8a863cbf602001&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCBXYWPT%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9x52FBtxqRbVHIo6ahk0EDEMnmtGHYMbM41l0cl%2BzhAIgP0RrbXbt7%2FLwSsDG6fJOICNaMHR2%2BUplbJrEZGmzpXYqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeF%2FAJtXxcKPv4dVCrcA6PZXavp%2BGA818gkrGBXcEyXL4cKgH9uBBpfGrXLO4IKnEUHvbCckpUBhDFtx0El%2FT8ORUGr8TAvnV0VbZ9pEBARyvjZY4te%2FXf1RdyRH4qofXcm8dAg0R78gfIXGG5wUrvTebIy%2Bt2RWfXhDndmsVb7%2FFb4joKPrkcfiY2HGOEtcjPYmVN%2BRahqp%2BX1CsjCAvynKibhRmNc7gM4PQ6yAyRjQxwSWKjD6y6KrW7pIMkDvf4LXRffaT7C5%2FlNtV%2BewhQ42h58p5pKCb%2BMtjTrDB0B5MvhSzNVjhsexlTU2YyiiuCEkiG3E1HN%2Fofz9gNGR3cMzr3DdtuJjgCmA1qu9Bq2sypwNT9qyJvGeNUcTM2vRt1R8E8GDf3w1BCD%2FRfUmF7ZIzfrilqe%2FS17L7PoA18GEV2mA0bLau6M3RE%2FABF3HZLsJCfd2T70YG4m0J240a4Ic0Q%2BSO%2F31DlGyi%2FgVGDhKXboEu4ykCy6X8B%2FBluDwojfuv%2FzbzN3CUBcHSR1aPWCfxs03q5vAKHDfCLQK5hbm75rpZsa%2Bxhui37Jy4%2BZQ4ZVlyXtQwMf3L4fZPPaq60sE%2BhFG25SSsGTtBlZ0f%2FAICXiYwaBug5jLQYksSwrpIg4xqjnTwnZDahoMI%2Bax8oGOqUBFDFvfa0ZIc29CJIE%2By35Aor37lE%2BuDXUAHAz1rYic63A755%2FacV0lxaBo%2FzBNyvH%2BOauyXNqb5gT9j2QFu7H8xBNYADPGrcgocoomAaHblgfrrNlRqiEqNOmVJjkRU1jVewbUonkvuEiEx%2FRTgrjeK67zCYoCH%2FhEUS1o6dFFzqwV%2F3yCY%2Fv92p41NIU914IDXlUkG6617Qr0sTugNppRRhuk7pr&X-Amz-Signature=723c8acff5041cd6701d10c4f3eac24ddc8afda0c0a09892bb5e7ab42a8d8b41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCBXYWPT%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9x52FBtxqRbVHIo6ahk0EDEMnmtGHYMbM41l0cl%2BzhAIgP0RrbXbt7%2FLwSsDG6fJOICNaMHR2%2BUplbJrEZGmzpXYqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeF%2FAJtXxcKPv4dVCrcA6PZXavp%2BGA818gkrGBXcEyXL4cKgH9uBBpfGrXLO4IKnEUHvbCckpUBhDFtx0El%2FT8ORUGr8TAvnV0VbZ9pEBARyvjZY4te%2FXf1RdyRH4qofXcm8dAg0R78gfIXGG5wUrvTebIy%2Bt2RWfXhDndmsVb7%2FFb4joKPrkcfiY2HGOEtcjPYmVN%2BRahqp%2BX1CsjCAvynKibhRmNc7gM4PQ6yAyRjQxwSWKjD6y6KrW7pIMkDvf4LXRffaT7C5%2FlNtV%2BewhQ42h58p5pKCb%2BMtjTrDB0B5MvhSzNVjhsexlTU2YyiiuCEkiG3E1HN%2Fofz9gNGR3cMzr3DdtuJjgCmA1qu9Bq2sypwNT9qyJvGeNUcTM2vRt1R8E8GDf3w1BCD%2FRfUmF7ZIzfrilqe%2FS17L7PoA18GEV2mA0bLau6M3RE%2FABF3HZLsJCfd2T70YG4m0J240a4Ic0Q%2BSO%2F31DlGyi%2FgVGDhKXboEu4ykCy6X8B%2FBluDwojfuv%2FzbzN3CUBcHSR1aPWCfxs03q5vAKHDfCLQK5hbm75rpZsa%2Bxhui37Jy4%2BZQ4ZVlyXtQwMf3L4fZPPaq60sE%2BhFG25SSsGTtBlZ0f%2FAICXiYwaBug5jLQYksSwrpIg4xqjnTwnZDahoMI%2Bax8oGOqUBFDFvfa0ZIc29CJIE%2By35Aor37lE%2BuDXUAHAz1rYic63A755%2FacV0lxaBo%2FzBNyvH%2BOauyXNqb5gT9j2QFu7H8xBNYADPGrcgocoomAaHblgfrrNlRqiEqNOmVJjkRU1jVewbUonkvuEiEx%2FRTgrjeK67zCYoCH%2FhEUS1o6dFFzqwV%2F3yCY%2Fv92p41NIU914IDXlUkG6617Qr0sTugNppRRhuk7pr&X-Amz-Signature=8bedcc7c0425b3fce1d754686393e5c09f0bdc183eae276cae85d40db041bfe9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



